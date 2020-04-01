
<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <b-button type="button" class="btn btn-success btn-sm" v-b-modal.sensor-modal>
            Add Sensor</b-button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Manufacturing energy (Mj)</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sensor, index) in sensors" :key="index">
              <td>{{ index }}</td>
              <td>{{ sensor.e_manufacturing }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.sensor-update-modal
                          @click="editSensor(sensor)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteSensor(sensor)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addSensorModal"
            id="sensor-modal"
            title="Add a new sensor"
            hide-footer>
        <b-form @submit=onSubmit @reset="onReset" class="w-100" ref="element-form">
            <vue-form-generator :model="model"
                                :schema="sensorTabSchema"
                                :options="formOptions"
                                ref="sensorTabSchema"
                                >
            </vue-form-generator>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
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
      sensors: {},
      counter_sensors: 0,
      message: '',
      model: {
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
      sensorTabSchema: {
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
          styleClasses: 'col-xs-6',
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
          styleClasses: 'col-xs-6',
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
          styleClasses: 'col-xs-12',
        },
        {
          type: 'input',
          inputType: 'number',
          label: 'Sleep mode (mA)',
          model: 'sleep_mode',
          required: true,
          min: Number.MIN_VALUE,
          step: 1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'col-xs-6',
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
      return this.$refs.sensorTabSchema.validate();
    },
    initForm() {
      this.model.lifetime = '';
      this.model.area = '';
      this.model.active_mode = '';
      this.model.sleep_mode = '';
      this.model.e_manufacturing = null;
    },
    addSensor() {
      return new Promise((resolve, reject) => {
        if (this.validate()) {
          axios.post(path + apiEnpoints['element-form'], this.model).then((res) => {
            this.sensors[this.counter_sensors] = res.data;
            this.counter_sensors += 1;
            this.initForm();
            // console.log(res.data);
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
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSensorModal.hide();
      this.addSensor();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addSensorModal.hide();
      this.initForm();
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
