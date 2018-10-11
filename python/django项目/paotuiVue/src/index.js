// 入口文件js
import Vue from 'vue'
import App from './app.vue'
import './assets/styles/test.css'
import './assets/images/h.jpg'
import './assets/styles/test-stylus.styl'
import './assets/styles/global.styl'
const root =document.createElement('div')
document.body.appendChild(root)
new Vue({
   
    render:(h) =>h(App)//新建一个app

}).$mount(root)//挂载到html中的div里