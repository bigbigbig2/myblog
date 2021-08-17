//路由配置文件
import {createWebHistory, createRouter} from "vue-router";
import Home from "../view/Home";
import ArticleDetail from "../view/ArticleDetail";
import Login from "../view/Login";
import UserCenter from "../view/UserCenter";
import ArticleCreate from "../view/ArticleCreate";
import ArticleEdit from "../view/ArticleEdit";


//使用前端来配置路由
const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/article/:id",
        name: "ArticleDetail",
        component: ArticleDetail
    },
    {
        path: "/login",
        name: "Login",
        component: Login
    },
    {
        path: "/user/:username",
        name:"UserCenter",
        component: UserCenter
    },
    {
    path: "/article/create",
    name: "ArticleCreate",
    component: ArticleCreate
    },
    {
    path: "/article/edit/:id",
    name: "ArticleEdit",
    component: ArticleEdit
    },
];
//实例化路由
const router = createRouter({
    //路由形式：哈希模式
    history: createWebHistory(),
    routes,
});

export default router;