<template>
    <div class="search">
        <form>
            <input v-model="searchText" type="text" placeholder="输入搜索内容...">
            <button v-on:click.prevent="searchArticles"></button>
        </form>
    </div>
</template>

<script>
    export default {
        name: "SearchButton.vue",
        data:function(){
            return {
                serachText:'',
            }
        },
        methods:{
            searchArticles(){
                const text = this.searchText.trim();
                //trim()方法：去除字符串头尾空格.charAt返回指定位置的字符
                if (text.charAt(0) !== '') {
                    //点击搜索即可实现页面跳转（编程式导航，替代了<router-link>
                    //`this.$route` 和 `this.$router` ，前者代表路径对象，后者代表路由器对象
                    this.$router.push({name: 'Home', query: { search: text }})
                }
            },
        }
    }
</script>

<style scoped>

    .search {
        padding-top: 22px;
    }


    * {
        box-sizing: border-box;
    }

    form {
        position: relative;
        width: 200px;
        margin: 0 auto;
    }

    input, button {
        border: none;
        outline: none;
    }

    input {
        width: 100%;
        height: 35px;
        padding-left: 13px;
        padding-right: 46px;
    }

    button {
        height: 35px;
        width: 35px;
        cursor: pointer;
        position: absolute;
    }

    .search input {
        border: 2px solid gray;
        border-radius: 5px;
        background: transparent;
        top: 0;
        right: 0;
    }

    .search button {
        background: gray;
        border-radius: 0 5px 5px 0;
        width: 45px;
        top: 0;
        right: 0;
    }

    .search button:before {
        content: "搜索";
        font-size: 13px;
        color: white;
    }

</style>