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
                     finish-button-text="Reset"
                     ref="wizard"
                     >
            <tab-content title="Start" color="red">
                <b-row style="text-align: center;">
                  <b-col class="chart-color" style="margin-bottom:0px">
                    <h2 style="text-align:justify; font-family:Lato; font-size:20px; padding:15px;">
                      The Internet of things (IoT) has the potential to change
                      the world just as Internet did. It will allow us to optimize
                      the use of resources and avoid waste, but we must intelligently
                      develop this technology in order to limit its impact on the
                      environment and maximize the reduction of greenhouse
                      gas emissions (GHGE).</h2>
                  </b-col>
                  <b-col cols="12" md="2" ></b-col>
                  <b-col>
                  </b-col>
                </b-row>
                <b-row style="text-align: center;margin-top:30px">
                  <b-col class="chart-color">
                    <h2 style="text-align:justify; font-family:Lato; font-size:20px; padding:15px;">
                      The following webservice allows you to evaluate the energy and waste impact of
                      your IoT solution. The webservice returns the impacts in Mj and Kg and the
                      ratio with a green solution. This green solution is calculated by
                      resizing the components of the energy harvesting system ensuring the energy
                      independence of the IoT solution.</h2>
                  </b-col>
                  <b-col cols="12" md="2" ></b-col>
                  <b-col>
                  </b-col>
                </b-row>

            </tab-content>
            <tab-content title="Solar Panel"
                         icon="" :before-change="() => postData('solar-panel-form')"
                         >
              <solar-panel-form ref="solar-panel-form"></solar-panel-form>

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
                <b-row style="text-align: center">
                  <b-col class="chart-color" style="text-align:-webkit-center">
                    <chart-comparison v-bind:title="'Energy impact (Mj)'"
                      v-bind:values="this.energyV"
                      v-bind:greenValues="this.greenEnergyV"></chart-comparison>
                    <h1 style="color:rgba(255, 255, 255, 0.85); text-align:center">
                      <span style="font-size:60px;">{{energyRatio}}</span>x
                    </h1>
                    <h2> than green solution </h2>
                  </b-col>
                  <b-col cols="12" md="2" ></b-col>
                  <b-col class="chart-color" style="text-align:-webkit-center">
                    <chart-comparison v-bind:title="'Waste impact (g)'"
                      v-bind:values="this.disposalV"
                      v-bind:greenValues="this.greenDisposalV"></chart-comparison>
                    <h1 style="color:rgba(255, 255, 255, 0.85); text-align:center">
                      <span style="font-size:60px;">{{wasteRatio}}</span>x
                    </h1>
                    <h2> than green solution </h2>
                  </b-col>
                </b-row>
            </tab-content>
            <div v-if="errorMsg">
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
import axios from 'axios';
import VideoBG from './components/VideoBG';
import SolarPanelStep from './components/SolarPanelStep';
import BatteryPanelStep from './components/BatteryStep';
import DeviceStep from './components/DeviceStep';
import ElementsStep from './components/ElementsStep';
import ProcessorRadioStep from './components/ProcessorRadioStep';
import MaintenanceStep from './components/MaintenanceStep';
import BarChartComparison from './assets/js/BarChartComparison';

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
    'chart-comparison': BarChartComparison,
  },
  data() {
    return {
      energyRatio: 0,
      wasteRatio: 0,
      ready: false,
      energyV: null,
      greenEnergyV: null,
      disposalV: null,
      greenDisposalV: null,
      errorMsg: null,
      model: {
        real: {
          solar_panel: null,
          battery: null,
          device: null,
          maintenance: null,
          tot: null,
        },
        green: {
          solar_panel: null,
          battery: null,
          device: null,
          maintenance: null,
          tot: null,
        },
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
      this.reset();
    },
    reset() {
      this.$refs['device-form'].reset();
      this.$refs['solar-panel-form'].reset();
      this.$refs['battery-form'].reset();
      this.$refs['maintenance-form'].reset();
      this.energyRatio = 0;
      this.wasteRatio = 0;
      this.ready = false;
      this.energyV = null;
      this.greenEnergyV = null;
      this.disposalV = null;
      this.greenDisposalV = null;
      this.errorMsg = null;
      this.$refs.wizard.changeTab(6, 0);
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
    computeRatio(solutionRsult, greenResult) {
      let sumSolution = 0;
      let sumGreen = 0;
      for (let i = 0; i < solutionRsult.length; i += 1) {
        sumSolution += solutionRsult[i];
        sumGreen += greenResult[i];
      }
      return sumSolution / sumGreen;
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
              this.energyV = [this.model.real.device.energy,
                this.model.real.solar_panel.energy,
                this.model.real.battery.energy, this.model.real.maintenance.energy];

              this.greenEnergyV = [this.model.green.device.energy,
                this.model.green.solar_panel.energy,
                this.model.green.battery.energy, this.model.green.maintenance.energy];

              this.disposalV = [this.model.real.device.disposal * 1000,
                this.model.real.solar_panel.disposal * 1000,
                this.model.real.battery.disposal * 1000,
                this.model.real.maintenance.disposal * 1000];

              this.greenDisposalV = [this.model.green.device.disposal * 1000,
                this.model.green.solar_panel.disposal * 1000,
                this.model.green.battery.disposal * 1000,
                this.model.green.maintenance.disposal * 1000];
              this.ready = true;
              this.energyRatio = Math.round(this.computeRatio(this.energyV, this.greenEnergyV));
              this.wasteRatio = Math.round(this.computeRatio(this.disposalV, this.greenDisposalV));
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
  },
  computed: {
    prettyJSON() {
      return this.model;
    },
  },
};
</script>


<style>
 @import './assets/css/style.css';
 @import './assets/css/form-wizard-style.css';

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
