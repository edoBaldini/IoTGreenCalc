<template>
    <bar-chart ref="bar" :chartData="chartData" :options="options"/>
</template>

<script>
import BarChart from '../assets/js/bar-chart';

export default {
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
  components: {
    'bar-chart': BarChart,
  },

  data() {
    return {
      options: {
        responsive: true,
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
          duration: 1000000,
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
        responsiveAnimationDuration: 1000, // animation duration after a resize
      },
      easterEgg: {
        update() {
          this.chart.update();
        },
      },
      chartData: {
        labels: ['Device', 'SolarPanel', 'Battery', 'Maintenance'],
        datasets: [
          {
            label: 'Your solution',
            data: this.values,
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
          },
          {
            label: 'Green solution',
            data: this.greenValues,
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
          },
        ],
      },
    };
  },
};

</script>
