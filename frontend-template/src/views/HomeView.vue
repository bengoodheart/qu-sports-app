<template>
    <div>
        <b-container>
        <HeaderComponent />
        <div class="content">
        <b-card>
            <b-row>
                <b-col cols="2"></b-col>
                <b-col cols="4">
                    <BlogComponent />
                </b-col>
                <b-row cols="2"></b-row>
            </b-row>
        </b-card>
        </div>
        <FooterComponent />
    </b-container>
    </div>
</template>
<script>
import HeaderComponent from '@/components/HeaderComponent.vue';
import FooterComponent from '@/components/FooterComponent.vue';
import BlogComponent from '@/components/blog/BlogComponent.vue';

export default {
    name: 'HomeView',
    components: {HeaderComponent, FooterComponent, BlogComponent},
    setup(){
        return {}
    }
}
</script>
<style lang="css">
    
</style>