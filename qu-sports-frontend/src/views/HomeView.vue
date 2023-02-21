<template>
    <div>
        <b-container>
        <HeaderComponent />
        <b-card>
        </b-card>
        <FooterComponent />
    </b-container>
    </div>
</template>
<script>
import HeaderComponent from '@/components/HeaderComponent.vue';
import FooterComponent from '@/components/FooterComponent.vue';

export default {
    name: 'HomeView',
    components: {HeaderComponent, FooterComponent},
    setup(){
        return {}
    }
}
</script>
<style lang="css">
    
</style>