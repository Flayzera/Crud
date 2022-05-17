import { createStore } from 'vuex'

export default createStore({
  state: {
    taskEdit: null,
  },
  getters: {
    getTaskEdit(state){
      return state.taskEdit;
    }
  },
  mutations: {
    setTaskEdit(state, obj){
      state.taskEdit = obj;
    },
  },
  actions: {
  },
  modules: {
  }
})
