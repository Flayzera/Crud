import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView'
import NewTask from '../views/NewTask'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/newtask',
    name: 'NewTask',
    component: NewTask
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
