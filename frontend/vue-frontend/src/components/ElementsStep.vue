
<template>
  <b-container style="margin:0; padding:0; max-width:inherit">
    <b-row align-self="start">
      <b-col class="table-width">
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
                          @click="editSensor(sensor, index)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteSensor(sensor, index)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </b-col>
      <b-col cols="12" md="4" ></b-col>
      <b-col class="table-width">
        <b-button type="button" class="btn btn-success btn-sm" v-b-modal.board-modal>
            Add Board</b-button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Disposal (kg)</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(board, index_b) in boards" :key="index_b">
              <td>{{ index_b }}</td>
              <td>{{ board.disposal }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.board-update-modal
                          @click="editBoard(board, index_b)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteBoard(board, index_b)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </b-col>
    </b-row>
    <b-modal ref="addSensorModal"
            id="sensor-modal"
            title="Add a new sensor"
            hide-footer>
        <b-form @submit=onSubmit @reset="onReset" class="w-100" ref="element-form">
            <vue-form-generator :model="model"
                                :schema="sensorTabSchema"
                                :options="formOptions"
                                ref="sensorTabSchema"
                                style="color: #343a40; flex: 0 0 0;">
            </vue-form-generator>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="updateSensorModal"
            id="sensor-update-modal"
            title="Update the sensor"
            hide-footer>
        <b-form @submit=onSubmitUpdate @reset="onReset" class="w-100">
            <vue-form-generator :model="editModel.sensor"
                                :schema="sensorTabSchema"
                                :options="formOptions"
                                ref="sensorEditTabSchema"
                                style="color: #343a40; flex: 0 0 0;"
                                >
            </vue-form-generator>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="addBoardModal"
            id="board-modal"
            title="Add a new board"
            hide-footer>
        <b-form @submit=onSubmitBoard @reset="onResetBoard" class="w-100" ref="board-form">
            <vue-form-generator :model="modelBoard"
                                :schema="boardTabSchema"
                                :options="formOptions"
                                ref="boardTabSchema"
                                style="color: #343a40; flex: 0 0 0;"
                                >
            </vue-form-generator>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="updateBoardModal"
            id="board-update-modal"
            title="Update the board"
            hide-footer>
        <b-form @submit=onSubmitUpdateBoard @reset="onResetBoard" class="w-100">
            <vue-form-generator :model="editModelBoard.board"
                                :schema="boardTabSchema"
                                :options="formOptions"
                                ref="boardEditTabSchema"
                                style="color: #343a40; flex: 0 0 0;"
                                >
            </vue-form-generator>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
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
  'board-form': 'board/',
};
const path = 'http://127.0.0.1:8888/api/';

export default {
  data() {
    return {
      // sensors: [],
      sensors: [{ area: 13.8,
        lifetime: 1000000.0,
        active_mode: 11.0,
        sleep_mode: 0.0,
        e_manufacturing: 76.5072 },
      { area: 0.278,
        lifetime: 1000000.0,
        active_mode: 0.006,
        sleep_mode: 0.0,
        e_manufacturing: 1.541232 },
      { area: 0.283,
        lifetime: 1000000.0,
        active_mode: 0.5,
        sleep_mode: 0.0,
        e_manufacturing: 1.5689519999999997 },
      { area: 0.976,
        lifetime: 1000000.0,
        active_mode: 0.38,
        sleep_mode: 0.0,
        e_manufacturing: 5.410944 },
      { area: 0.665,
        lifetime: 10.0,
        active_mode: 3.0,
        sleep_mode: 0.0,
        e_manufacturing: 3.68676 },
      { area: 0.636,
        lifetime: 10.0,
        active_mode: 26.0,
        sleep_mode: 0.0,
        e_manufacturing: 3.525984 },
      { area: 0.636,
        lifetime: 10.0,
        active_mode: 34.0,
        sleep_mode: 0.0,
        e_manufacturing: 3.525984 }],
      // boards: [],
      boards: [
        { weight: 0.02, active_mode: 0.0, sleep_mode: 0.0, disposal: 0.0076 },
        { weight: 0.02, active_mode: 0.0, sleep_mode: 0.0, disposal: 0.0076 }],
      message: '',
      model: {
        lifetime: 0,
        area: 0,
        active_mode: 0,
        sleep_mode: 0,
        e_manufacturing: null,
      },
      modelBoard: {
        weight: 0,
        active_mode: 0,
        sleep_mode: 0,
        disposal: null,
      },
      editModel: {
        sensor: {
          lifetime: 0,
          area: 0,
          active_mode: 0,
          sleep_mode: 0,
          e_manufacturing: null,
        },
        index: 0,
      },
      editModelBoard: {
        board: {
          weight: 0,
          active_mode: 0,
          sleep_mode: 0,
          disposal: null,
        },
        index: 0,
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
          min: Number.MIN_VALUE,
          step: 0.1,
          // eslint-disable-next-line no-undef
          validator: VueFormGenerator.validators.number,
          styleClasses: 'display-modal',
        },
        ],
      },
      boardTabSchema: {
        fields: [{
          type: 'input',
          inputType: 'number',
          label: 'Weight (kg)',
          model: 'weight',
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
          min: 0,
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
          min: Number.MIN_VALUE,
          step: 0.1,
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
      return this.$refs.sensorTabSchema.validate();
    },
    validateBoard() {
      return this.$refs.boardTabSchema.validate();
    },
    initForm() {
      this.model.lifetime = 0;
      this.model.area = 0;
      this.model.active_mode = 0;
      this.model.sleep_mode = 0;
      this.model.e_manufacturing = null;
      this.modelBoard.weight = 0;
      this.modelBoard.active_mode = 0;
      this.modelBoard.sleep_mode = 0;
      this.modelBoard.disposal = null;
    },
    addSensor() {
      return new Promise((resolve, reject) => {
        if (this.validate()) {
          axios.post(path + apiEnpoints['element-form'], this.model).then((res) => {
            this.sensors.push(res.data);
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
    updateSensor() {
      return new Promise((resolve, reject) => {
        axios.post(path + apiEnpoints['element-form'], this.editModel.sensor).then((res) => {
          this.sensors[this.editModel.index] = res.data;
          this.sensors.push(1);
          this.sensors.pop();
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
    editSensor(sensor, index) {
      this.editModel.sensor = sensor;
      this.editModel.index = index;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSensorModal.hide();
      this.addSensor();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addSensorModal.hide();
      this.$refs.updateSensorModal.hide();
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.updateSensorModal.hide();
      this.updateSensor();
    },
    onDeleteSensor(sensor, index) {
      this.sensors.splice(index, 1);
    },
    addBoard() {
      return new Promise((resolve, reject) => {
        if (this.validateBoard()) {
          axios.post(path + apiEnpoints['board-form'], this.modelBoard).then((res) => {
            this.boards.push(res.data);
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
    updateBoard() {
      return new Promise((resolve, reject) => {
        axios.post(path + apiEnpoints['board-form'], this.editModelBoard.board).then((res) => {
          this.boards[this.editModelBoard.index] = res.data;
          this.boards.push(1);
          this.boards.pop();
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
    editBoard(board, index) {
      this.editModelBoard.board = board;
      this.editModelBoard.index = index;
    },
    onSubmitBoard(evt) {
      evt.preventDefault();
      this.$refs.addBoardModal.hide();
      this.addBoard();
    },
    onResetBoard(evt) {
      evt.preventDefault();
      this.$refs.addBoardModal.hide();
      this.$refs.updateBoardModal.hide();
      this.initForm();
    },
    onSubmitUpdateBoard(evt) {
      evt.preventDefault();
      this.$refs.updateBoardModal.hide();
      this.updateBoard();
    },
    onDeleteBoard(board, index) {
      this.boards.splice(index, 1);
      console.log(this.boards);
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
