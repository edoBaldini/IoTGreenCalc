from mip import Model, xsum, BINARY, CBC, OptimizationStatus
from flask import Flask, render_template

app = Flask(__name__)


def check_maintenance_times(x, y):
    z = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            z.append(x[i][j]) if not x[i][j] in z else ""
    z.sort()
    y.sort()
    return z == y


def min_replacement_sched(mttf, repl_c, disp_c, main_c, life):
    n_elements = len(mttf)
    m = Model(solver_name=CBC)

    x = [[m.add_var(var_type=BINARY) for i in range(n_elements)]
         for j in range(life)]
    c = [[elem for elem in repl_c] for i in range(life)]

    y = [[m.add_var(var_type=BINARY) for i in range(n_elements)]
         for j in range(life)]
    p = [[elem for elem in disp_c] for i in range(life)]

    w = [m.add_var(var_type=BINARY) for i in range(life)]
    d = [main_c for i in range(life)]

#  Minimize the sum of the disposal costs
    m.objective = (xsum(xsum(p[i][j] * y[i][j] for j in range(n_elements))
                        for i in range(life)))

#  Minimize the sum of the energy costs for the elements and the maintenantce
    m.objective = (xsum(xsum(c[i][j] * x[i][j] for j in range(n_elements)) +
                        (d[i] * w[i]) for i in range(life)))

#  Constraints
    for i in range(n_elements):
        for k in range(life - mttf[i]):
            m += xsum(x[j][i] for j in range(k, k + mttf[i])) >= 1

        for j in range(life):
            m += x[j][i] <= w[j]
            m += x[j][i] == y[j][i]

    status = m.optimize()
    if (status == OptimizationStatus.NO_SOLUTION_FOUND):
        raise ValueError('No solution found')
    else:
        r_times = [[j for j in range(life) if x[j][i].x >= 0.99]
                   for i in range(n_elements)]

        n_main = [j for j in range(life) if w[j].x >= 0.99]

        if not check_maintenance_times(r_times, n_main):
            raise ValueError('Mismatch')
        return (r_times, n_main)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    min_replacement_sched([15, 40, 3652], [5.24, 13.82, 15.36],
                          [0.028027397, 0.002022899, 0.006726], 130.4207942,
                          75)
    app.run(debug=True, host='0.0.0.0')
