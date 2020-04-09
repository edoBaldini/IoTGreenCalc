<template>
    <vue-form-generator :model="model"
                           :schema="maintenanceTabSchema"
                           :options="formOptions"
                           ref="maintenanceTabForm"
                           >
    </vue-form-generator>
</template>

<script>
import 'vue-form-generator/dist/vfg.css';
import VueFormGenerator from 'vue-form-generator';
import prettyJSON from '../../prettyJson';

export default {
  components: {
    'vue-form-generator': VueFormGenerator.component,
  },
  data() {
    return {
      // model: {
      //   avg_distance: 0,
      //   avg_fuel_cons: 0,
      //   conv_factor: 0,
      //   n_devices: 0,
      //   lifetime: 0,
      //   device: null,
      //   battery: null,
      //   solar_panel: null,
      //   tot_e_intervention: null,
      //   n_interventions: null,
      // },
      model: {
        avg_distance: 3.505,
        avg_fuel_cons: 6.0,
        conv_factor: 8.9,
        n_devices: 10.0,
        lifetime: 30.0,
        device: null,
        battery: null,
        solar_panel: null,
        tot_e_intervention: null,
        n_interventions: null,
      },
      formOptions: {
        validationErrorClass: 'has-error',
        validationSuccessClass: 'has-success',
        validateAfterChanged: true,
      },
      maintenanceTabSchema: {
        fields: [{
          type: 'input',
          inputType: 'number',
          label: 'Average distance (km)',
          model: 'avg_distance',
          required: true,
          min: Number.MIN_VALUE,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-general',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Fuel consumption (l/100km)',
          model: 'avg_fuel_cons',
          required: false,
          min: Number.MIN_VALUE,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-general',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Conversion factor l to kWh',
          model: 'conv_factor',
          required: false,
          min: Number.MIN_VALUE,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-general',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Number of devices',
          model: 'n_devices',
          required: true,
          min: 1,
          step: 1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-general',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Application lifetime',
          model: 'lifetime',
          required: true,
          min: 1,
          step: 1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-general',
        },
        // {
        //   type: 'input',
        //   inputType: 'number',
        //   label: 'Total energy intervention',
        //   model: 'tot_e_intervention',
        //   required: false,
        //   readonly: true,
        //   disabled: true,
        //   // eslint-disable-next-line no-undef
        //   validator: VueFormGenerator.validators.number,
        //   styleClasses: 'display-general',
        // },
        // {
        //   type: 'input',
        //   inputType: 'number',
        //   label: 'Number of interventions',
        //   model: 'n_interventions',
        //   required: false,
        //   readonly: true,
        //   disabled: true,
        //   // eslint-disable-next-line no-undef
        //   validator: VueFormGenerator.validators.number,
        //   styleClasses: 'display-general',
        // },
        ],
      },
    };
  },
  methods: {
    onComplete() {
      // eslint-disable-next-line no-alert
      alert('Yay. Done!');
    },
    validate() {
      return this.$refs.maintenanceTabForm.validate();
    },
    reset() {
      this.model.avg_distance = 0;
      this.model.avg_fuel_cons = 0;
      this.model.conv_factor = 0;
      this.model.n_devices = 0;
      this.model.lifetime = 0;
      this.model.device = null;
      this.model.battery = null;
      this.model.solar_panel = null;
      this.model.tot_e_intervention = null;
      this.model.n_interventions = null;
    },
  },
  computed: {
    prettyJSON() {
      return prettyJSON(this.model);
    },
  },
};
</script>
