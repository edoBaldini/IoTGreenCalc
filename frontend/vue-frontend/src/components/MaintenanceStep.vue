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
      },
      formOptions: {
        validationErrorClass: 'has-error',
        validationSuccessClass: 'has-success',
        validateAfterChanged: true,
      },
      maintenanceTabSchema: {
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
