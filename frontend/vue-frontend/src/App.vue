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
            </tab-content>
           <tab-content title="Maintenance"
                         icon="ti-check">
              <h4>Example of prettyJSON!</h4>
              <div class="panel-body">
                <pre v-if="model" v-html="prettyJSON"></pre>
              </div>
            </tab-content>
            <div v-if="errorMsg"> <!-- TODO CSS CLASS FOR THE ERROR -->
              <span class="error">{{errorMsg}}</span>
            </div>
            <!-- <transition name="fade" mode="out-in">
               <router-view></router-view>
            </transition> -->
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
import MaintenanceStep from './components/MaintenanceStep';
import prettyJSON from '../prettyJson';

const apiEnpoints = {
  'solar-panel-form': 'solar_panel',
  'battery-form': 'battery',
  'device-form': 'device',
  'maintenance-form': 'maintenance',
};

const path = 'http://127.0.0.1:5000/';

export default {
  components: {
    'video-bg': VideoBG,
    'vue-form-generator': VueFormGenerator.component,
    'solar-panel-form': SolarPanelStep,
    'battery-form': BatteryPanelStep,
    'device-form': DeviceStep,
    'maintenance-form': MaintenanceStep,
  },
  data() {
    return {
      errorMsg: null,
      model: {
        firstName: '',
        lastName: '',
        email: '',
        streetName: '',
        streetNumber: '',
        city: '',
        country: '',
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
      alert('Yay. Done!');
    },
    postData(ref) {
      return new Promise((resolve, reject) => {
        if (this.$refs[ref].validate()) {
          axios.get((path + apiEnpoints[ref])).then((res) => {
            alert('right request', res);
          // this.getResource(ref);
          })
            .catch((error) => {
              // eslint-disable-next-line
              prettyJSON(this.$refs[ref].model);
              console.log(error);
              reject('something does not work in communication with the server, try again');
            });
        } else {
          reject('form not properly compiled');
        }
      });
    },
    //   if (this.$refs[ref].validate()) {
    //     alert('sei valido per questo form ', prettyJSON(this.$refs[ref].model));
    //     axios.post(path + apiEnpoints[ref], prettyJSON(this.$refs[ref].model));
    //   } else {
    //     this.errorHandler('form not properly compiled');
    //   }
    // },
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
