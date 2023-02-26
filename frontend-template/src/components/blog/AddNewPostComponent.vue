<template lang="">
    <div>
        <b-form @submit="onSubmit" @reset="onReset">
            <label>Title</label>
            <b-form-input v-model="formData.title" placeholder="Blog Title" class="p-3"></b-form-input>
            <label>Post</label>
            <b-form-textarea v-model="formData.post" placeholder="Post Text"></b-form-textarea>
            <label>Tags</label>
            <b-form-tags v-model="formData.tags" placeholder="Tags"></b-form-tags>
            <b-button variant="primary">Submit</b-button>
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