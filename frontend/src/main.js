import { createApp } from 'vue'
//导入主组件并挂载到html
import App from './App'
import router from './router'
//全局的方式导入element-PLUS
//按需导入有点烦
import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
//通过原型链将 appendIfExists()添加到已有对象中（包括内置原生对象），以扩展此对象的功能
URLSearchParams.prototype.appendIfExists = function (key, value) {
    if (value !== null && value !== undefined) {
        this.append(key, value)
    }
};
createApp(App).use(router).use(ElementPlus).mount('#app')
//注册路由
