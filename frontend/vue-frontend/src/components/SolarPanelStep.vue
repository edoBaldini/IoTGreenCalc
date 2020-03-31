<template>
    <vue-form-generator :model="model"
                        :schema="solarPanelTabSchema"
                        :options="formOptions"
                        ref="solarPanelTabSchema"
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
        technology: 'mono-Si',
        surface: '',
        irradiance: '',
        s_hours: '',
        lifetime: 0,
        efficiency: 0,
        kwp: 0,
        efficiency_w: 0,
        weight: '',
        e_manufactoring: '',
        disposal: '',
        e_produced: '',
      },
      formOptions: {
        validationErrorClass: 'has-error',
        validationSuccessClass: 'has-success',
        validateAfterChanged: true,
      },
      solarPanelTabSchema: {
        fields: [{
          type: 'select',
          label: 'Technology',
          model: 'technology',
          values: ['mono-Si', 'multi-Si'],
          required: true,
          // eslint-disable-next-line no-undef
          styleClasses: 'col-xs-6',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Surface (m2)',
          model: 'surface',
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
          label: 'Daily irradiance (kWh)',
          model: 'irradiance',
          required: true,
          min: Number.MIN_VALUE,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'col-xs-12',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Hours of light',
          model: 's_hours',
          required: true,
          min: Number.MIN_VALUE,
          step: 1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'col-xs-6',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Lifetime (years)',
          model: 'lifetime',
          required: false,
          min: 0,
          step: 1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'col-xs-6',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Efficiency',
          model: 'efficiency',
          required: false,
          min: 0,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'col-xs-12',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Kwp',
          model: 'kwp',
          required: false,
          min: 0,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'col-xs-12',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Efficiency wear out',
          model: 'efficiency_w',
          required: false,
          min: 0,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'col-xs-12',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Weight (kg)',
          model: 'weight',
          required: true,
          min: Number.MIN_VALUE,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'col-xs-12',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Manufacturing energy (Mj)',
          model: 'e_manufactoring',
          readonly: true,
          disabled: true,
          // eslint-disable-next-line no-undef
          styleClasses: 'col-xs-12',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Disposal (kg)',
          model: 'disposal',
          readonly: true,
          disabled: true,
          // eslint-disable-next-line no-undef
          styleClasses: 'col-xs-12',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Daily energy produced (Mj)',
          model: 'e_produced',
          readonly: true,
          disabled: true,
          // eslint-disable-next-line no-undef
          styleClasses: 'col-xs-12',
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
      return this.$refs.solarPanelTabSchema.validate();
    },
  },
  computed: {
    prettyJSON() {
      return prettyJSON(this.model);
    },
  },
};
</script>
