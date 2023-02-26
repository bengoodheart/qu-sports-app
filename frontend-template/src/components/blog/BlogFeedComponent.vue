<template lang="">
    <div>
        <b-row>
        <b-col cols="2"><b-button to="/addPost"> New Post </b-button></b-col>
        <b-col cols="10">
        {{response}}
        </b-col>
        </b-row>
    </div>
</template>
<script>
import restHelper from "@/networking/rest/restHelper.js"
export default {
    name: 'BlogFeedComponent',
    async setup(){
        const rest = new restHelper()
        let response  = await rest.getAllPosts()
        return { response }
    }
}
</script>
<style lang="js">
    
</style>