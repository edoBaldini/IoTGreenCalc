import { Bar, mixins } from 'vue-chartjs';

const { reactiveProp } = mixins;

export default {
  extends: Bar,
  mixins: [reactiveProp],
  props: {
    chartData: {
      type: Object,
      default: null,
    },
    options: {
      type: Object,
    },
  },
  options: {
    responsive: true,
    title: {
      display: true,
      text: ['Waste impact (g)', ''],
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
  },

  mounted() {
    this.renderChart(this.chartData, this.options);
  },
};
