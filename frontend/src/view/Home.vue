<template>

    <BlogHeader/>

    <ArticleList/>

    <BlogFooter/>

</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import ArticleList from '@/components/ArticleList.vue'
    //import Tabs from "@/components/Tabs.vue";

    export default {
        name: 'Home',
        components: {BlogHeader, BlogFooter, ArticleList}
    }
</script>
<!--view是表示每个页面，注意区别于组件-->
