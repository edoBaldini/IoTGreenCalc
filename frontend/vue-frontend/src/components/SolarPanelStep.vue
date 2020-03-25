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
        firstName: '',
        lastName: '',
        email: '',
      },
      formOptions: {
        validationErrorClass: 'has-error',
        validationSuccessClass: 'has-success',
        validateAfterChanged: true,
      },
      solarPanelTabSchema: {
        fields: [{
          type: 'input',
          inputType: 'text',
          label: 'First name',
          model: 'firstName',
          required: true,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.string,
          styleClasses: 'col-xs-6',
        },
        {
          type: 'input',
          inputType: 'text',
          label: 'Last name',
          model: 'lastName',
          required: true,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.string,
          styleClasses: 'col-xs-6',
        },
        {
          type: 'input',
          inputType: 'text',
          label: 'Email',
          model: 'email',
          required: true,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.email,
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
