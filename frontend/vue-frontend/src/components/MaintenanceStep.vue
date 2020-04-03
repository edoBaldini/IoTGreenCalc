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
      model: {
        avg_distance: 0,
        avg_fuel_cons: 0,
        conv_factor: 0,
        n_devices: 0,
        lifetime: 0,
        device: null,
        battery: null,
        solar_panel: null,
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
          styleClasses: 'col-xs-6',
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
          styleClasses: 'col-xs-6',
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
          styleClasses: 'col-xs-12',
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
          styleClasses: 'col-xs-6',
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
    validate() {
      return this.$refs.maintenanceTabForm.validate();
    },
  },
  computed: {
    prettyJSON() {
      return prettyJSON(this.model);
    },
  },
};
</script>
