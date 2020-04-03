<template>
  <section>
    <video-bg> </video-bg>
    <b-container fluid style="padding-left:5%; padding-right:5%; padding-top:3%">
      <b-card class="b-card-header-color">
        <b-card-text class="font-set">IOT IMPACT CALCULATOR</b-card-text>
      </b-card>
      <b-card style="background-color:transparent">
        <b-card-text>
        <form-wizard @on-complete="onComplete"
                     @on-error="errorHandler"
                     title=""
                     subtitle=""
                     color="rgba(126, 211, 134, 1)"
                     error-color="#a94442"
                     back-button-text="back"
                     next-button-text="next"
                     ref="wizard"
                     >
            <tab-content title="Start" color="red"></tab-content>
            <tab-content title="Solar Panel"
                         icon="" :before-change="() => postData('solar-panel-form')"
                         >
              <solar-panel-form ref="solar-panel-form"></solar-panel-form>
  <!-- IN ROUTE CASE route="/solar_panel"> is it possible to validate the form of another page? -->

            </tab-content>
            <tab-content title="Battery"
                         icon="" :before-change="() => postData('battery-form')">
              <battery-form ref="battery-form"></battery-form>
            </tab-content>
            <tab-content title="Device"
                         icon="" :before-change="() => postData('device-form')">
              <device-form ref="device-form"></device-form>
              <elements-form ref="elements-form"></elements-form>
              <processor-radio-form ref="processor-radio-form"></processor-radio-form>
            </tab-content>
            <tab-content title="Maintenance"
                         icon="" :before-change="() => postData('maintenance-form')">
              <maintenance-form ref="maintenance-form"></maintenance-form>
            </tab-content>
            <tab-content title="comparison"
                         icon="">
                <b-row>
                  <b-col>
                    <canvas style="background-color:transparent" id="waste-impact"></canvas>
                  </b-col>
                  <b-col>
                  </b-col>
                  <b-col>
                    <canvas style="background-color:transparent" id="energt-impact"></canvas>
                  </b-col>
                </b-row>
              <!-- <div class="panel-body">
                <pre v-if="model" v-html="model"></pre>
              </div> -->
            </tab-content>
            <div v-if="errorMsg"> <!-- TODO CSS CLASS FOR THE ERROR -->
              <span class="error">{{errorMsg}}</span>
            </div>
        </form-wizard>
        </b-card-text>
      </b-card>
    </b-container>
  </section>
</template>

<script>
// eslint-disable-next-line no-new
import 'vue-form-generator/dist/vfg.css';
import VueFormGenerator from 'vue-form-generator';
import Chart from 'chart.js';
import axios from 'axios';
import VideoBG from './components/VideoBG';
import SolarPanelStep from './components/SolarPanelStep';
import BatteryPanelStep from './components/BatteryStep';
import DeviceStep from './components/DeviceStep';
import ElementsStep from './components/ElementsStep';
import ProcessorRadioStep from './components/ProcessorRadioStep';
import MaintenanceStep from './components/MaintenanceStep';
import { wasteChartData } from './assets/js/chart-data';


// import prettyJSON from '../prettyJson';

const apiEnpoints = {
  'solar-panel-form': 'solar_panel/',
  'battery-form': 'battery/',
  'device-form': 'device/',
  'maintenance-form': 'maintenance/',
};

const path = 'http://127.0.0.1:8888/api/';

export default {
  components: {
    'video-bg': VideoBG,
    'vue-form-generator': VueFormGenerator.component,
    'solar-panel-form': SolarPanelStep,
    'battery-form': BatteryPanelStep,
    'device-form': DeviceStep,
    'elements-form': ElementsStep,
    'processor-radio-form': ProcessorRadioStep,
    'maintenance-form': MaintenanceStep,
  },
  data() {
    return {
      wasteChartData,
      errorMsg: null,
      model: {
        maintenance: null,
        results: null,
        green_maintenance: null,
        green_results: null,
      },
      formOptions: {
        validationErrorClass: 'has-error',
        validationSuccessClass: 'has-success',
        validateAfterChanged: true,
      },
    };
  },
  methods: {
    onComplete() {
      // eslint-disable-next-line no-alert
    },
    showModalComparison() {
      this.$refs['green-comparison'].show();
    },
    getData(ref) {
      axios.get(path + apiEnpoints[ref]).then((res) => {
        this.$refs[ref].model = res.data;
      });
    },
    arrayToDict(l) {
      const d = {};
      for (let i = 0; i < l.length; i += 1) {
        d[i] = l[i];
      }
      return d;
    },
    completeDevice() {
      this.$refs['device-form'].model.sensors = this.$refs['elements-form'].sensors;
      this.$refs['device-form'].model.boards = this.$refs['elements-form'].boards;
      this.$refs['device-form'].model.processor = this.$refs['processor-radio-form'].processor;
      this.$refs['device-form'].model.radio = this.$refs['processor-radio-form'].radio;
    },
    completeMaintenance() {
      this.$refs['maintenance-form'].model.device = this.$refs['device-form'].model;
      this.$refs['maintenance-form'].model.battery = this.$refs['battery-form'].model;
      this.$refs['maintenance-form'].model.solar_panel = this.$refs['solar-panel-form'].model;
    },
    postData(ref) {
      return new Promise((resolve, reject) => {
        if (ref === 'device-form') {
          this.completeDevice();
        }
        if (ref === 'maintenance-form') {
          this.completeMaintenance();
        }
        if (this.$refs[ref].validate()) {
          axios.post(path + apiEnpoints[ref], this.$refs[ref].model).then((res) => {
            this.$refs[ref].model = res.data;

            if (ref === 'maintenance-form') {
              this.$refs[ref].model = res.data.maintenance;
              this.model = res.data;
            }

            resolve(true);
          })
            .catch((error) => {
              // eslint-disable-next-line
              // alert(prettyJSON(this.$refs[ref].model));
              console.log('error data provided ', error.response);
              reject('the data provided are not admitted');
            });
        } else {
          reject('form not properly compiled');
        }
      });
    },
    errorHandler(msg) {
      this.errorMsg = msg;
    },
    createChart(chartId, chartData) {
      const ctx = document.getElementById(chartId);
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options,
      });
    },
  },
  computed: {
    prettyJSON() {
      return this.model;
    },
  },
  mounted() {
    this.createChart('waste-impact', this.wasteChartData);
    this.createChart('energt-impact', this.wasteChartData);
  },
};
</script>


<style>
 @import './assets/css/style.css';

body {
  background-color: #163766;
}

 /* allows to change the color of each tab title */
.stepTitle{
    color:#eaffef;
  }

.vue-form-generator {
    color:#eaffef;
}

.errors {
  color: #a94442;
  font-weight: bold;
}

</style>
