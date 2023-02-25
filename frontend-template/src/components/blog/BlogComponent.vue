<template lang="">
    <div>
        <Suspense>
        <BlogFeedComponent />
        </Suspense>
    </div>
</template>
<script>
import AddNewPostComponent from "@/components/blog/AddNewPostComponent.vue"
import BlogFeedComponent from "@/components/blog/BlogFeedComponent.vue";

export default {
    name: 'BlogComponent',
    components: { AddNewPostComponent, BlogFeedComponent },
    setup(){
        return { }
    }
}
</script>
<style lang="">
    
</style>