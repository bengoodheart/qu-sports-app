import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'

import 'bootstrap/dist/css/bootstrap.css'
import router from './router'

const app = createApp(App).use(router)
const pinia = createPinia()

app.use(pinia)
app.mount('#app')