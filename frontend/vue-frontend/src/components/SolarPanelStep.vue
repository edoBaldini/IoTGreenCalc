<template>
    <vue-form-generator :model="model"
                        :schema="solarPanelTabSchema"
                        :options="formOptions"
                        ref="solarPanelTabSchema" cols="12" md="8" >
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
      //   technology: 'mono-Si',
      //   surface: '',
      //   irradiance: '',
      //   s_hours: '',
      //   lifetime: 0,
      //   efficiency: 0,
      //   kwp: 0,
      //   efficiency_w: 0,
      //   weight: '',
      //   e_manufacturing: '',
      //   disposal: '',
      //   e_produced: '',
      // },
      model: { technology: 'mono-Si',
        surface: 0.03744,
        irradiance: 1.127419355,
        s_hours: 9.0,
        lifetime: 20.0,
        efficiency: 17.0,
        kwp: 0,
        efficiency_w: 80.0,
        weight: 0.54,
        e_manufacturing: 205.02518400000002,
        disposal: 0.08650800000000002,
        e_produced: 0.025832875358534402 },
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
          styleClasses: 'display-general',
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
          styleClasses: 'display-general',
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
          styleClasses: 'display-general',
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
          styleClasses: 'display-general',
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
          styleClasses: 'display-general',
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
          styleClasses: 'display-general',
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
          styleClasses: 'display-general',
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
          styleClasses: 'display-general',
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
          styleClasses: 'display-general',
        },
        // {
        //   type: 'input',
        //   inputType: 'number',
        //   label: 'Manufacturing energy (Mj)',
        //   model: 'e_manufacturing',
        //   readonly: true,
        //   disabled: true,
        //   // eslint-disable-next-line no-undef
        //   styleClasses: 'col-xs-12',
        // },
        // {
        //   type: 'input',
        //   inputType: 'number',
        //   label: 'Disposal (kg)',
        //   model: 'disposal',
        //   readonly: true,
        //   disabled: true,
        //   // eslint-disable-next-line no-undef
        //   styleClasses: 'col-xs-12',
        // },
        // {
        //   type: 'input',
        //   inputType: 'number',
        //   label: 'Daily energy produced (Mj)',
        //   model: 'e_produced',
        //   readonly: true,
        //   disabled: true,
        //   // eslint-disable-next-line no-undef
        //   styleClasses: 'col-xs-12',
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
      return this.$refs.solarPanelTabSchema.validate();
    },
    reset() {
      this.model.technology = 'mono-Si';
      this.model.surface = 0;
      this.model.irradiance = 0;
      this.model.s_hours = 0;
      this.model.lifetime = 0;
      this.model.efficiency = 0;
      this.model.kwp = 0;
      this.model.efficiency_w = 0;
      this.model.weight = 0;
      this.model.e_manufacturing = 0;
      this.model.disposal = 0;
      this.model.e_produced = 0;
    },
  },
  computed: {
    prettyJSON() {
      return prettyJSON(this.model);
    },
  },
};
</script>

<style scoped>
@import '../assets/css/style.css';
 @import '../assets/css/form-wizard-style.css';

</style>
