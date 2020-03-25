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

export default {
  components: {
    'vue-form-generator': VueFormGenerator.component,
  },
  data() {
    return {
      model: {
      },
      formOptions: {
        validationErrorClass: 'has-error',
        validationSuccessClass: 'has-success',
        validateAfterChanged: true,
      },
      deviceTabSchema: {
        fields: [
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
