<template>
    <div>
        <b-container>
        <HeaderComponent />
        <div class="content">
        <b-card>
            <b-row>
                <b-col cols="4"></b-col>
                <b-col cols="4">
                    <Suspense>
                    <BlogFeedComponent/>
                    </Suspense>
                </b-col>
                <b-row cols="4"></b-row>
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
import BlogFeedComponent from '../components/blog/BlogFeedComponent.vue';

export default {
    name: 'HomeView',
    components: {HeaderComponent, FooterComponent, BlogFeedComponent},
    setup(){
        return {}
    }
}
</script>
<style lang="css">
    
</style>