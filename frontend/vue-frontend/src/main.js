// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import VideoBg from 'vue-videobg';
import Vue from 'vue';
import App from './App';
import router from './router';

Vue.use(BootstrapVue);
Vue.component('video-bg', VideoBg);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
