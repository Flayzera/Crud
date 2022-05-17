<template>
  <div class="home">
    <div class="container mt-c">
      <div class="row mb-3">
        <div class="col-12">
          <button class="btn btn-primary float-end" @click="editTask(null)">Criar Tarefa</button>
        </div>
      </div>
      <div class="row">
        <div class="col-4 text-center">
          <div class="cols to-do">
            <p class="title">A FAZER</p>
            <p class="tasks" v-for="t in tasks_todo" :key="t.id" @click="editTask(t)">{{t.title}}</p>
          </div>
        </div>
        <div class="col-4 text-center">
          <div class="cols doing">
            <p class="title">FAZENDO</p>
            <p class="tasks" v-for="t in tasks_doing" :key="t.id" @click="editTask(t)">{{t.title}}</p>
          </div>
        </div>
        <div class="col-4 text-center">
          <div class="cols finish">
            <p class="title">FINALIZADO</p>
            <p class="tasks" v-for="t in tasks_finished" :key="t.id" @click="editTask(t)">{{t.title}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TasksDataService from "@/api/services/TasksDataService";
import { mapMutations } from 'vuex';
export default {
  name: "HomeView",
  data() {
    return {
      tasks_todo: [],
      tasks_doing: [],
      tasks_finished: [],
    }
  },
  methods: {
    ...mapMutations(['setTaskEdit',]),
    editTask(t){
      this.setTaskEdit(t)
      this.$router.push('newtask')
    },
    getTaskByFilter(filter){
      TasksDataService.getAll(`?status=${filter}`)
        .then(response => {
          if(filter == 0)
            this.tasks_todo = response.data;
          else if(filter == 1)
            this.tasks_doing = response.data;
          else if(filter == 2)
            this.tasks_finished = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    getTasks() {
      this.getTaskByFilter(0);
      this.getTaskByFilter(1);
      this.getTaskByFilter(2);
    },
  },
  mounted(){
    this.getTasks()
  }
}
</script>

<style lang="less" scoped>
  .mt-c{
    margin-top: 48px;
  }
  .cols{
    min-height: 360px;
    padding: 24px;
    border-radius: 8px;
    .title{
      font-weight: bold;
      font-size: 24px;
      background-color: rgba(0,0,0, 0.7);
      color: #fff;
    }
    .tasks{
      line-height: 21px;
      margin-bottom: 8px;
      border-radius: 8px;
      padding: 4px;
      background: #fff;
      &:hover{
        background: rgba(255,255,255, 0.7);
        cursor: pointer;
      }
    }
    &.to-do{
      background-color: #e40202;
    }
    &.doing{
      background-color: #f0ff17;
    }
    &.finish{
      background-color: #54EB36;
    }
  }
</style>