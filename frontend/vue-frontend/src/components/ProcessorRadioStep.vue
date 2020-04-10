
<template>
  <b-container style="margin:0; padding:0; max-width:inherit">
    <b-row align-self="start">
      <b-col class="table-width">
        <b-button type="button" class="btn btn-success btn-sm" v-b-modal.processor-modal>
            Add Processor </b-button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Manufacturing energy (Mj)</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ processor.e_manufacturing }}</td>
              <td>
                <div v-if="processor.e_manufacturing" class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.processor-update-modal
                          @click="editProcessor(processor)">
                      Update
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </b-col>
      <b-col cols="12" md="4" ></b-col>
      <b-col class="table-width">
         <b-button type="button" class="btn btn-success btn-sm" v-b-modal.radio-modal>
            Add Radio</b-button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Manufacturing energy (Mj)</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ radio.e_manufacturing }}</td>
              <td>
                <div v-if="radio.e_manufacturing" class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.radio-update-modal
                          @click="editRadio(radio)">
                      Update
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </b-col>
    </b-row>
    <b-modal ref="addProcessorModal"
            id="processor-modal"
            title="Add a processor"
            hide-footer>
        <b-form @submit=onSubmit class="w-100" ref="processor-form">
            <vue-form-generator :model="model"
                                :schema="elementTabSchema"
                                :options="formOptions"
                                ref="elementTabSchema"
                                style="color: #343a40; flex: 0 0 0;"
                                >
            </vue-form-generator>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="updateProcessorModal"
            id="processor-update-modal"
            title="Update the processor"
            hide-footer>
        <b-form @submit=onSubmitUpdate class="w-100">
            <vue-form-generator :model="editModel"
                                :schema="elementTabSchema"
                                :options="formOptions"
                                ref="elementEditTabSchema"
                                style="color: #343a40; flex: 0 0 0;"
                                >
            </vue-form-generator>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="addRadioModal"
            id="radio-modal"
            title="Add a new radio"
            hide-footer>
        <b-form @submit=onSubmitRadio class="w-100" ref="radio-form">
            <vue-form-generator :model="model"
                                :schema="elementTabSchema"
                                :options="formOptions"
                                ref="elementTabSchema"
                                style="color: #343a40; flex: 0 0 0;"
                                >
            </vue-form-generator>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="updateRadioModal"
            id="radio-update-modal"
            title="Update the radio"
            hide-footer>
        <b-form @submit=onSubmitUpdateRadio class="w-100">
            <vue-form-generator :model="editModel"
                                :schema="elementTabSchema"
                                :options="formOptions"
                                ref="elementEditTabSchema"
                                style="color: #343a40; flex: 0 0 0;"
                                >
            </vue-form-generator>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </b-container>
</template>
<script>
import 'vue-form-generator/dist/vfg.css';
import VueFormGenerator from 'vue-form-generator';
import axios from 'axios';
import prettyJSON from '../../prettyJson';


const apiEnpoints = {
  'element-form': 'element/',
};
const path = 'http://127.0.0.1:8888/api/';

export default {
  data() {
    return {
      // processor: {},
      // radio: {},
      processor: { area: 2.641,
        lifetime: 1000000.0,
        active_mode: 9.0,
        sleep_mode: 0.062,
        e_manufacturing: 14.641703999999999 },
      radio: { area: 6.731,
        lifetime: 1000000.0,
        active_mode: 0.303030303,
        sleep_mode: 0.0,
        e_manufacturing: 37.316663999999996 },
      model: {
        lifetime: 0,
        area: 0,
        active_mode: 0,
        sleep_mode: 0,
        e_manufacturing: null,
      },
      editModel: {
        lifetime: 0,
        area: 0,
        active_mode: 0,
        sleep_mode: 0,
        e_manufacturing: null,
      },
      formOptions: {
        validationErrorClass: 'has-error',
        validationSuccessClass: 'has-success',
        validateAfterChanged: true,
      },
      elementTabSchema: {
        fields: [{
          type: 'input',
          inputType: 'number',
          label: 'Lifetime (years)',
          model: 'lifetime',
          required: true,
          min: Number.MIN_VALUE,
          step: 1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-modal',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Surface (cm2)',
          model: 'area',
          required: true,
          min: Number.MIN_VALUE,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-modal',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Active mode (mA)',
          model: 'active_mode',
          required: true,
          min: Number.MIN_VALUE,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-modal',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Sleep mode (mA)',
          model: 'sleep_mode',
          required: true,
          min: 0,
          step: 1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-modal',
        },
        ],
      },
    };
  },

  components: {
    'vue-form-generator': VueFormGenerator.component,
  },
  methods: {
    onComplete() {
      // eslint-disable-next-line no-alert
      alert('Yay. Done!');
    },
    validate() {
      return this.$refs.elementTabSchema.validate();
    },
    addProcessor() {
      return new Promise((resolve, reject) => {
        if (this.validate()) {
          axios.post(path + apiEnpoints['element-form'], this.model).then((res) => {
            this.processor = res.data;
            // console.log(res.data);
            this.initForm();
            resolve(true);
          })
            .catch((error) => {
              // eslint-disable-next-line
              // alert(prettyJSON(this.$refs[ref].model));
              console.log(error.response);
              reject('the data provided are not admitted');
            });
        } else {
          reject('form not properly compiled');
        }
      });
    },
    updateProcessor() {
      return new Promise((resolve, reject) => {
        axios.post(path + apiEnpoints['element-form'], this.editModel).then((res) => {
          this.processor = res.data;
          resolve(true);
        })
          .catch((error) => {
            // eslint-disable-next-line
            // alert(prettyJSON(this.$refs[ref].model));
            console.log(error.response);
            reject('the data provided are not admitted');
          });
      });
    },
    editProcessor(processor) {
      this.editModel = processor;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addProcessorModal.hide();
      this.addProcessor();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.updateProcessorModal.hide();
      this.updateProcessor();
    },
    addRadio() {
      return new Promise((resolve, reject) => {
        if (this.validate()) {
          axios.post(path + apiEnpoints['element-form'], this.model).then((res) => {
            this.radio = res.data;
            // console.log(res.data);
            this.initForm();
            resolve(true);
          })
            .catch((error) => {
              // eslint-disable-next-line
              // alert(prettyJSON(this.$refs[ref].model));
              console.log(error.response);
              reject('the data provided are not admitted');
            });
        } else {
          reject('form not properly compiled');
        }
      });
    },
    updateRadio() {
      return new Promise((resolve, reject) => {
        axios.post(path + apiEnpoints['element-form'], this.editModel).then((res) => {
          this.radio = res.data;
          resolve(true);
        })
          .catch((error) => {
            // eslint-disable-next-line
            // alert(prettyJSON(this.$refs[ref].model));
            console.log(error.response);
            reject('the data provided are not admitted');
          });
      });
    },
    editRadio(radio) {
      this.editMode = radio;
    },
    onSubmitRadio(evt) {
      evt.preventDefault();
      this.$refs.addRadioModal.hide();
      this.addRadio();
    },
    onSubmitUpdateRadio(evt) {
      evt.preventDefault();
      this.$refs.updateRadioModal.hide();
      this.updateRadio();
    },
    initForm() {
      this.model.lifetime = 0;
      this.model.area = 0;
      this.model.active_mode = 0;
      this.model.sleep_mode = 0;
      this.model.e_manufacturing = null;
    },
  },
  computed: {
    prettyJSON() {
      return prettyJSON(this.model);
    },
  },
  created() {
  },
};
</script>
