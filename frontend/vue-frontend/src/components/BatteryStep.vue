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
      model: {
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
      batteryTabSchema: {
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
