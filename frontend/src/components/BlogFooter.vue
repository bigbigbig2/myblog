<template>
    <!--  br 标签给页脚留出位置  -->
    <br>
    <div id="footer">
        <div id="aaa">Simple and crude</div>
        <el-button id="bbb" plain @click="open1">注册与登录说明</el-button>
    </div>
</template>

<script>
    import { h } from 'vue';
    export default {
        name: 'BlogFooter',
        methods:{
            open1(){
                this.$notify({
                    title:'注册与登录说明',
                    message:h('i',{style:'color:teal'},'在此网站注册的用户为普通用户，对文章的增删改查需要管理员用户。。。')
                })
            }
        }
    }
</script>

<style scoped>
    #footer {
        position:fixed;
        left: 0;
        bottom: 0;
        height: 40px;
        width: 100%;
        background: whitesmoke;
        font-weight: bold;
    }


    #bbb{
        position: absolute;
        right: 0;
        bottom: 0;
    }
    #aaa{
        position: absolute;
        right: 45%;
        bottom: 50%;
    }



</style>