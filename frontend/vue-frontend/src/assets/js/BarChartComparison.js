import { Bar, mixins } from 'vue-chartjs';

const { reactiveData } = mixins;

export default {
  extends: Bar,
  mixins: [reactiveData],
  props: {
    values: {
      type: Array,
    },
    greenValues: {
      type: Array,
    },
    title: {
      type: String,
    },
  },
  data() {
    return {
      chartData: null,
      gradient: null,
      options: {
        responsive: false,
        title: {
          display: true,
          text: [this.title, ''],
          fontFamily: 'Aileron',
          fontSize: 20,
          fontColor: 'rgba(255, 255, 255, 0.85)',
        },
        tooltips: {
          enabled: true,
        },
        hover: {
          animationDuration: 0,
        },
        scales: {
          yAxes: [{
            display: false,
            gridLines: {
              drawBorder: false,
            },
          }],
          xAxes: [{
            // display: false, // this will hide vertical lines
            ticks: {
              fontFamily: 'Aileron',
              fontSize: 16,
              fontColor: 'rgba(255, 255, 255, 0.85)',
            },
            gridLines: {
              display: false,
              drawBorder: false,
            },
          }],
        },
        animation: {
          duration: 10,
          onComplete() {
            // eslint-disable-next-line one-var
            const chartInstance = this.chart,
              ctx = chartInstance.ctx;
            ctx.textAlign = 'center';
            ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
            ctx.textBaseline = 'bottom';
            // ctx.font = Chart.helpers.fontString('Lora', 'small', 'Lora');
            ctx.font = '16px Aileron';
            this.data.datasets.forEach((dataset, i) => {
              const meta = chartInstance.controller.getDatasetMeta(i);
              meta.data.forEach((bar, index) => {
                const data = dataset.data[index].toFixed(2);
                // eslint-disable-next-line no-underscore-dangle
                ctx.fillText(data, bar._model.x, bar._model.y - 5);
              });
            });
          },
        },
        legend: {
          display: false,
        },
        // responsiveAnimationDuration: 1000, // animation duration after a resize
      },
    };
  },
  created() {
    this.fillData();
  },

  mounted() {
    this.renderChart(this.chartData, { responsive: true, maintainAspectRatio: false });

    setInterval(() => {
      this.fillData();
    }, 1000);
  },

  methods: {
    fillData() {
      this.chartData = {
        labels: ['Device', 'Solar Panel', 'Battery', 'Maintenance'],
        datasets: [
          {
            label: 'Your solution',
            backgroundColor: [
              '#e24b49',
              '#e24b49',
              '#e24b49',
              '#e24b49',
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(255, 99, 132, 1)',
              'rgba(255, 99, 132, 1)',
              'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1,
            data: this.values,
          },
          {
            label: 'Green solution',
            backgroundColor: [
              '#00b894',
              '#00b894',
              '#00b894',
              '#00b894',
            ],
            borderColor: [
              'rgba(126, 211, 134, 1)',
              'rgba(126, 211, 134, 1)',
              'rgba(126, 211, 134, 1)',
              'rgba(126, 211, 134, 1)',
            ],
            borderWidth: 1,
            data: this.greenValues,
          },
        ],
      };
    },
  },
};
