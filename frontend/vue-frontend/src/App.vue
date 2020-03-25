/* eslint-disable */
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
                     title=""
                     subtitle=""
                     color="rgba(126, 211, 134, 1)"
                     error-color="#a94442"
                     back-button-text="back"
                     next-button-text="next"
                     >
            <tab-content title="Start" color="red"></tab-content>
            <tab-content title="Solar Panel"
                         icon="" :before-change="validateFirstTab">
               <vue-form-generator :model="model"
                                   :schema="firstTabSchema"
                                   :options="formOptions"
                                   ref="firstTabForm"
                                   class="stepTitle"
                                   >
               </vue-form-generator>
            </tab-content>
            <tab-content title="Battery"
                         icon="" :before-change="validateSecondTab">
             <vue-form-generator :model="model"
                                   :schema="secondTabSchema"
                                   :options="formOptions"
                                   ref="secondTabForm"
                                   >
               </vue-form-generator>
            </tab-content>
            <tab-content title="Device"
                         icon="" :before-change="validateSecondTab">
             <vue-form-generator :model="model"
                                   :schema="secondTabSchema"
                                   :options="formOptions"
                                   ref="secondTabForm"
                                   >
               </vue-form-generator>
            </tab-content>
            <tab-content title="Maintenance"
                         icon="ti-check">
              <h4>Your json is ready!</h4>
              <div class="panel-body">
                <pre v-if="model" v-html="prettyJSON"></pre>
              </div>
            </tab-content>
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
import VideoBG from './components/VideoBG';
// eslint-disable-next-line import/extensions
import prettyJSON from '../prettyJson.js';

export default {
  components: {
    'video-bg': VideoBG,
    'vue-form-generator': VueFormGenerator.component,
  },
  data() {
    return {
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
      firstTabSchema: {
        fields: [{
          type: 'input',
          inputType: 'text',
          label: 'First name',
          model: 'firstName',
          required: true,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.string,
          styleClasses: 'col-xs-6',
        },
        {
          type: 'input',
          inputType: 'text',
          label: 'Last name',
          model: 'lastName',
          required: true,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.string,
          styleClasses: 'col-xs-6',
        },
        {
          type: 'input',
          inputType: 'text',
          label: 'Email',
          model: 'email',
          required: true,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.email,
          styleClasses: 'col-xs-12',
        },
        ],
      },
      secondTabSchema: {
        fields: [
          {
            type: 'input',
            inputType: 'text',
            label: 'Street name',
            model: 'streetName',
            required: true,
            // eslint-disable-next-line no-undef
            validator: VueFormGenerator.validators.string,
            styleClasses: 'col-xs-9',
          },
          {
            type: 'input',
            inputType: 'text',
            label: 'Street number',
            model: 'streetNumber',
            required: true,
            // eslint-disable-next-line no-undef
            validator: VueFormGenerator.validators.string,
            styleClasses: 'col-xs-3',
          },
          {
            type: 'input',
            inputType: 'text',
            label: 'City',
            model: 'city',
            required: true,
            // eslint-disable-next-line no-undef
            validator: VueFormGenerator.validators.string,
            styleClasses: 'col-xs-6',
          },
          {
            type: 'select',
            label: 'Country',
            model: 'country',
            required: true,
            // eslint-disable-next-line no-undef
            validator: VueFormGenerator.validators.string,
            values: ['United Kingdom', 'Romania', 'Germany'],
            styleClasses: 'col-xs-6',
          },
        ],
      },
    };
  },
  methods: {
    onComplete() {
      // eslint-disable-next-line no-alert
      alert('Yay. Done!');
    },
    validateFirstTab() {
      return this.$refs.firstTabForm.validate();
    },
    validateSecondTab() {
      return this.$refs.secondTabForm.validate();
    },
  },
  computed: {
    prettyJSON() {
      return prettyJSON(this.model);
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
