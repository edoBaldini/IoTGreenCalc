from mip import Model, xsum, BINARY, CBC, OptimizationStatus
from flask import Flask, render_template

app = Flask(__name__)


def min_replacement_sched(mttf, repl_c, disp_c, main_c, life):
    n_elements = len(mttf)
    m = Model(solver_name=CBC)

    x = [[m.add_var(var_type=BINARY) for i in range(n_elements)]
         for j in range(life)]
    c = [[elem for elem in repl_c] for i in range(life)]
    p = [[elem for elem in disp_c] for i in range(life)]

    w = [m.add_var(var_type=BINARY) for i in range(life)]
    d = [main_c for i in range(life)]

#  Minimize the sum of the disposal costs
    m.objective = (xsum(xsum(p[i][j] * x[i][j] for j in range(n_elements))
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

    status = m.optimize()
    if (status == OptimizationStatus.NO_SOLUTION_FOUND):
        print("no solution")
    else:
        r_times = [[j for j in range(life) if x[j][i].x >= 0.99]
                   for i in range(n_elements)]
        print(r_times)
        n_main = [j for j in range(life) if w[j].x >= 0.99]
        #TODO COMPLETE THE CHECK BETWEEN MAINTENANCES TIME AND REPLEACEMENT TIMES
        
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
