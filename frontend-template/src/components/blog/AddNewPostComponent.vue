<template lang="">
    <div>
        <b-form @submit="onSubmit" @reset="onReset">
            <b-form-input v-model="formData.title"></b-form-input>
        </b-form>
    </div>
</template>
<script>
import { reactive } from "vue"
export default {
    name: 'AddNewPostComponent',
    setup(){
        const formData = reactive({
            title: '',
            post: '',
            tags: []
        })
        return {formData}
    }
}
</script>
<style lang="">
    
</style>