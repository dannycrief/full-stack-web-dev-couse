<template>
  <div class='container'>
    <div class='col-sm-10'>
      <h1>Задачи</h1>
      <confirmation :message='confirmationMessage' v-if='showConfirmation'></confirmation>

      <button
        type='button'
        id='task-add'
        class='btn btn-success btn-sm align-left d-block'
        v-b-modal.todo-modal
      >Добавить задачу</button>

      <div class="text-center my-3">
        <b-button title="Super, we did a good job!">
          выполненных задач: {{getCompletedTodos()}}
        </b-button>
      </div>

      <div class="text-center my-3">
        <b-button title="Hm need to work more">
          невыполненных задач: {{getNotCompletedTodos()}}
        </b-button>
      </div>

      <table class='table table-dark table-stripped table-hover'>
        <thead class='thead-light'>
          <tr>
            <th>Uid</th>
            <th>Описание</th>
            <th>Выполнена?</th>
            <th></th>
          </tr>
        </thead>

        <tbody>
          <tr v-for='(todo, index) in todos' :key='index'>
            <td class='todo-uid'>{{ todo.uid }}</td>
            <td>{{ todo.description }}</td>
            <td>
              <span v-if='todo.is_completed'>Выполнено</span>
              <span v-else>Не выполнено</span>
            </td>
            <td>
              <div class='btn-group' role='group'>
                <!-- <button type='button' class='btn btn-secondary btn-sm'>Обновить</button> -->
                <button
                  type='button'
                  class='btn btn-secondary btn-sm'
                  v-b-modal.todo-modal
                  @click='updateTodo(todo)'
                >Обновить</button>
                &nbsp;
                <!-- <button type='button' class='btn btn-danger btn-sm'>X</button> -->
                <button type='button' class='btn btn-danger btn-sm'
                @click='deleteTodo(todo)'>X</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <b-modal ref='addTodoModal' id='todo-modal' title='Добавить задачу' hide-footer>
        <b-form @submit='onSubmit' @reset='onReset' class='w-100'>
          <b-form-group
            id='form-description-group'
            label='Описание:'
            label-for='form-description-input'
          >
            <b-form-input
              id='form-description-input'
              type='text'
              v-model='addTodoForm.description'
              required
              placeholder='Завести задачу'
            ></b-form-input>
          </b-form-group>
          <b-form-group id='form-complete-group'>
            <b-form-checkbox-group v-model='addTodoForm.is_completed' id='form-checks'>
              <b-form-checkbox value='true'>Задача выполнена?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <b-button type='submit' variant='primary'>Добавить</b-button>
          <b-button type='reset' variant='danger'>Сброс</b-button>
        </b-form>
      </b-modal>

    </div>
  </div>
</template>

<style>
button#task-add {
  margin-top: 20px;
  margin-bottom: 20px;
}
h1,
td {
  text-align: left;
}
.todo-uid {
  text-align: right;
}
</style>

<script>
import axios from 'axios';
import Confirmation from './Confirmation.vue';

const dataURL = 'http://localhost:5000/api/tasks/';

export default {
  name: 'Todo',
  data() {
    return {
      todos: [],
      addTodoForm: {
        uid: 0,
        description: '',
        is_completed: [],
      },
      confirmationMessage: '',
      showConfirmation: false,
    };
  },
  mounted() {
    console.log('App mounted!');
    if (localStorage.getItem('todos')) this.todos = JSON.parse(localStorage.getItem('todos'));
  },
  watch: {
    todos: {
      handler() {
        console.log('Todos changed!');
        localStorage.setItem('todos', JSON.stringify(this.todos));
      },
      deep: true,
    },
  },
  methods: {
    getTodos() {
      axios.get(dataURL)
        .then((response) => {
          this.todos = response.data.tasks;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getNotCompletedTodos() {
      return this.todos.filter((todo) => todo.is_completed === false).length;
    },
    getCompletedTodos() {
      return this.todos.filter((todo) => todo.is_completed !== false).length;
    },
    resetForm() {
      this.addTodoForm.description = '';
      this.addTodoForm.is_completed = [];
      this.uid = 0;
    },
    onSubmit(event) {
      event.preventDefault();
      this.$refs.addTodoModal.hide();
      const requestData = {
        description: this.addTodoForm.description,
        is_completed: this.addTodoForm.is_completed[0],
      };
      if (!this.addTodoForm.uid) {
        axios.post(dataURL, requestData)
          .then(() => {
            this.getTodos();
            this.confirmationMessage = `Задача '${requestData.description}' добавлена`;
            this.showConfirmation = true;
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        if (this.addTodoForm.uid > 0) {
          const todoURL = dataURL + this.addTodoForm.uid;
          axios.put(todoURL, requestData)
            .then(() => {
              this.getTodos();
              this.confirmationMessage = 'Задача обновлена';
              this.showConfirmation = true;
            })
            .catch((error) => {
              console.log(error);
            });
        }
        this.confirmationMessage = 'UID not valid';
        this.showConfirmation = false;
      }
      this.resetForm();
    },
    onReset(event) {
      event.preventDefault();
      this.$refs.addTodoModal.hide();
      this.resetForm();
    },
    updateTodo(todo) {
      this.addTodoForm = todo;
    },
  },
  deleteTodo(todo) {
    const todoURL = dataURL + todo.uid;
    axios.delete(todoURL)
      .then(() => {
        this.getTodos();
        this.confirmationMessage = 'Задача удалена из списка';
        this.showConfirmation = true;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  components: {
    confirmation: Confirmation,
  },
  created() {
    this.getTodos();
  },
};
</script>
