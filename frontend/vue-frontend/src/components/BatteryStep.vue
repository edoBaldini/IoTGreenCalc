<template>
    <vue-form-generator :model="model"
                          :schema="batteryTabSchema"
                          a:options="formOptions"
                          ref="batteryTabForm"
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
      //   technology: 'Li-Ion',
      //   lifetime: 0,
      //   efficiency: 0,
      //   density: 0,
      //   capacity: 0,
      //   weight: '',
      //   e_manufacturing: '',
      //   disposal: '',
      // },
      model: {
        technology: 'Li-Ion',
        lifetime: 9.0,
        efficiency: 90.0,
        density: 140.516129,
        capacity: 6600.0,
        weight: 0.155,
        e_manufacturing: 25.544,
        disposal: 0.08556000000000001,
      },
      formOptions: {
        validationErrorClass: 'has-error',
        validationSuccessClass: 'has-success',
        validateAfterChanged: true,
      },
      batteryTabSchema: {
        fields: [{
          type: 'select',
          label: 'Technology',
          model: 'technology',
          values: ['Li-Ion', 'PbA', 'NiMh'],
          required: true,
          // eslint-disable-next-line no-undef
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
          label: 'Density (Wh)',
          model: 'density',
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
          label: 'Capacity (mAh)',
          model: 'capacity',
          required: true,
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
        //   styleClasses: 'display-general',
        // },
        // {
        //   type: 'input',
        //   inputType: 'number',
        //   label: 'Disposal (kg)',
        //   model: 'disposal',
        //   readonly: true,
        //   disabled: true,
        //   // eslint-disable-next-line no-undef
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
    reset() {
      this.model.technology = 'Li-Ion';
      this.model.lifetime = 0;
      this.model.efficiency = 0;
      this.model.density = 0;
      this.model.capacity = 0;
      this.model.weight = 0;
      this.model.e_manufacturing = 0;
      this.model.disposal = 0;
    },
    validate() {
      return this.$refs.batteryTabForm.validate();
    },
  },
  computed: {
    prettyJSON() {
      return prettyJSON(this.model);
    },
  },
};
</script>
