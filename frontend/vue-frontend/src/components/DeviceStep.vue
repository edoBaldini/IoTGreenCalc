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
import ElementsStep from './ElementsStep';
import ProcessorRadioStep from './ProcessorRadioStep';


export default {
  components: {
    'vue-form-generator': VueFormGenerator.component,
    'elements-form': ElementsStep,
    'processor-radio-form': ProcessorRadioStep,

  },
  data() {
    return {
      // model: {
      //   boards: null,
      //   sensors: null,
      //   processor: null,
      //   radio: null,
      //   active_mode: null,
      //   sleep_mode: null,
      //   duty_cycle: '',
      //   voltage: '',
      //   output_regulator: '',
      //   e_manufacturing: null,
      //   disposal: null,
      //   daily_e_required: null,
      // },
      model: {
        boards: null,
        sensors: null,
        processor: null,
        radio: null,
        active_mode: 84.189030303,
        sleep_mode: 0.062,
        duty_cycle: 5,
        voltage: 3.3,
        output_regulator: 90,
        e_manufacturing: 144.14399999999998,
        disposal: 3.42,
        daily_e_required: 0.031477248,
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
            label: 'Duty cycle',
            model: 'duty_cycle',
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
            label: 'Voltage (V)',
            model: 'voltage',
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
            label: 'Output regulator eff.',
            model: 'output_regulator',
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
          //   label: 'Daily device energy (Mj)',
          //   model: 'daily_e_required',
          //   readonly: true,
          //   disabled: true,
          //   // eslint-disable-next-line no-undef
          //   styleClasses: 'display-general',
          // },
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
    validate() {
      const processorValidate = this.model.processor.e_manufacturing > 0;
      const radioValidate = this.model.radio.e_manufacturing > 0;
      const boardsValidate = this.model.boards.length > 0;
      const sensorsValidate = this.model.sensors.length > 0;
      return (this.$refs.deviceTabForm.validate() && processorValidate &&
      radioValidate && boardsValidate && sensorsValidate);
    },
    reset() {
      this.model.boards = null;
      this.model.sensors = null;
      this.model.processor = null;
      this.model.radio = null;
      this.model.active_mode = 0;
      this.model.sleep_mode = 0;
      this.model.duty_cycle = 0;
      this.model.voltage = 0;
      this.model.output_regulator = 0;
      this.model.e_manufacturing = 0;
      this.model.disposal = 0;
      this.model.daily_e_required = 0;
    },
  },
  computed: {
    prettyJSON() {
      return prettyJSON(this.model);
    },
  },
};

</script>
