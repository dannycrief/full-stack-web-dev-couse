<template>
  <div class="container">
    <div class="col-sm-10">
      <h1>Задачи</h1>
      <button type="button" id="task-add" class="btn btn-success btn-sm align-left d-block">Добавить
        задачу
      </button>

      <table class="table table-dark table-stripped table-hover">
        <thead class="thead-light">
        <tr>
          <th>Uid</th>
          <th>Описание</th>
          <th>Выполнена?</th>
          <th></th>
        </tr>
        </thead>

        <tbody>
        <tr v-for="(todo, index) in todos" :key="index">
          <td class="todo-uid">{{ todo.uid }}</td>
          <td>{{ todo.description }}</td>
          <td>
            <span v-if="todo.is_completed">Выполнено</span>
            <span v-else>Не выполнено</span>
          </td>
          <td>
            <div class="btn-group" role="group">
              <button type="button" class="btn btn-secondary btn-sm">Обновить</button>
              &nbsp;
              <button type="button" class="btn btn-danger btn-sm">X</button>
            </div>
          </td>
        </tr>
        </tbody>

      </table>

    </div>
  </div>
</template>

<style>
  button#task-add {
    margin-top: 20px;
    margin-bottom: 20px;
  }

  h1, td {
    text-align: left;
  }

  .todo-uid {
    text-align: right;
  }
</style>

<script>
import axios from 'axios';

const dataURL = 'http://localhost:5000/api/tasks/';

export default {
  name: 'Fetch',
  data() {
    return {
      todos: [],
    };
  },
  methods: {
    getTodos() {
      axios.get(dataURL).then((response) => {
        this.todos = response.data.tasks;
      });
    },
  },
  created() {
    this.getTodos();
  },
};
</script>
