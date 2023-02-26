import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BlogComponent from "@/components/blog/BlogComponent.vue"
import AddNewPostComponent from '@/components/blog/AddNewPostComponent.vue'
import BlogFeedComponent from '../components/blog/BlogFeedComponent.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    children:[{
      path: '/',
      component: BlogComponent,
      children: [{
        path: '/',
        component: BlogFeedComponent
      },
      {
        path: '/addPost',
        component: AddNewPostComponent
      }]
    },
    
    ]
  },  
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
]

const router = createRouter({
    history: createWebHistory("http://localhost"),
    routes
  })
  
  export default router