<template>
    <div class="newtask mt-3">
        <div class="container">
            <form @submit.prevent>
                <div class="form-group">
                    <label for="nametask">Nome da Tarefa</label>
                    <input v-model="task.title" type="text" class="form-control" id="nametask" aria-describedby="nameHelp" placeholder="Insira um nome pra tarefa">
                </div>
                <div class="form-group">
                    <label for="statusTask">Status da Tarefa</label>
                    <select class="form-control" id="statusTask" v-model="task.status">
                        <option value="0">A fazer</option>
                        <option value="1">Fazendo</option>
                        <option value="2">Finalizado</option>
                    </select>
                </div>
                <div class="row mt-3">
                    <div class="col-12">
                        <button type="submit" class="btn btn-primary float-end" @click="saveTask()">Salvar</button>
                        <button type="submit" class="btn btn-danger float-end me-3" @click="rmTask()" v-if="edit">Remover</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>
<script>
import TasksDataService from "@/api/services/TasksDataService";
import { mapState } from 'vuex';
export default {
    name: 'NewTask',
    data(){
        return {
            edit: false,
            task: {
                title: null,
                status: 0
            },
        }
    },
    methods: {
        saveTask(){
        if(this.edit){
            TasksDataService.update(this.task.id, this.task)
                .then(() => {
                    //console.log(response);
                    this.$router.push('/')
                })
                .catch(e => {
                    console.log(e);
                });
        }else{
            TasksDataService.create(this.task)
                .then(() => {
                    //console.log(response);
                    this.$router.push('/')
                })
                .catch(e => {
                    console.log(e);
                });
            }
        },
        rmTask(){
            if(this.edit){
                TasksDataService.delete(this.task.id)
                    .then(() => {
                        //console.log(response);
                        this.$router.push('/')
                    })
                    .catch(e => {
                        console.log(e);
                    });
            }
        }
    },
    computed:{
        ...mapState(['taskEdit'])
    },
    mounted(){
        if(this.taskEdit){
            this.task = Object.assign({}, this.taskEdit);
            this.edit = true;
        }
    }
}
</script>
<style lang="less" scoped>
    
</style>