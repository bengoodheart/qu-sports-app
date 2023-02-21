<template>
    <div>
        <b-container>
            <HeaderComponent />
            <b-card>
                <h3>About</h3>
            </b-card>
            <FooterComponent />
        </b-container>
    </div>
</template>
<script>
import HeaderComponent from '@/components/HeaderComponent.vue';
import FooterComponent from '@/components/FooterComponent.vue';


export default {
    name: "AboutView.vue",
    components: {HeaderComponent, FooterComponent},
    setup() {
        return {};
    },
}
</script>
<style lang="">
    
</style>