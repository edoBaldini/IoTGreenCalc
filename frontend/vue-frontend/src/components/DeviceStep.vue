<template>
    <vue-form-generator :model="model"
                           :schema="deviceTabSchema"
                           :options="formOptions"
                           ref="deviceTabForm"
                           >
    </vue-form-generator>
</template>

<script>
import 'vue-form-generator/dist/vfg.css';
import VueFormGenerator from 'vue-form-generator';
import prettyJSON from '../../prettyJson';
import SensorsStep from './SensorsStep';


export default {
  components: {
    'vue-form-generator': VueFormGenerator.component,
    'sensors-form': SensorsStep,

  },
  data() {
    return {
      model: {
        boards: {},
        sensors: SensorsStep.model,
        processor: null,
        radio: null,
        active_mode: '',
        sleep_mode: '',
        duty_cycle: '',
        voltage: '',
        output_regulator: '',
        daily_e_required: null,
        e_manufactoring: null,
        disposal: null,
      },
      formOptions: {
        validationErrorClass: 'has-error',
        validationSuccessClass: 'has-success',
        validateAfterChanged: true,
      },
      deviceTabSchema: {
        fields: [
          {
            type: 'input',
            inputType: 'number',
            label: 'Active mode (mA)',
            model: 'active_mode',
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
            label: 'Sleep mode (mA)',
            model: 'sleep_mode',
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
            label: 'Duty cycle',
            model: 'duty_cycle',
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
            label: 'Voltage (V)',
            model: 'voltage',
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
            label: 'Output regulator eff.',
            model: 'output_regulator',
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
            label: 'Daily device energy (Mj)',
            model: 'daily_e_required',
            readonly: true,
            disabled: true,
            // eslint-disable-next-line no-undef
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
      return this.$refs.deviceTabForm.validate();
    },
  },
  computed: {
    prettyJSON() {
      return prettyJSON(this.model);
    },
  },
};
</script>
