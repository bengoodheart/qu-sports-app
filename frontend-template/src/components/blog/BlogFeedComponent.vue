<template lang="">
    <div>
        {{response}}
        {{status }}
    </div>
</template>
<script>
import restHelper from "@/networking/rest/restHelper.js"
export default {
    name: 'BlogFeedComponent',
    async setup(){
        const rest = new restHelper()
        let response  = await rest.pingServer()
        let status = await rest.status
        return { response, status }
    }
}
</script>
<style lang="js">
    
</style>