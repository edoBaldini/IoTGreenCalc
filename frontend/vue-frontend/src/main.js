// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';
import 'vue-form-wizard/dist/vue-form-wizard.min.css';
import BootstrapVue from 'bootstrap-vue';
import FormWizard from 'vue-form-wizard';
import VideoBg from 'vue-videobg';
import Chart from 'chart.js';
import Vue from 'vue';
import App from './App';
import router from './router';


Vue.use(BootstrapVue);
Vue.component('chart-js', Chart);
Vue.component('video-bg', VideoBg);
Vue.use(FormWizard);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  // data: {
  //   errorMsg: null,
  // },
  // methods: {
  //   onComplete() {
  //     // eslint-disable-next-line no-alert
  //     alert('Yay. Done!');
  //   },
  // },
  template: '<App/>',
});
