<template>
    <div>
        <b-navbar light>
            <b-navbar-brand to="/">Brand Name</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item to="/">Home</b-nav-item>
                <b-nav-item to="/about">About</b-nav-item>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>
<script>
export default {
    name: 'HeaderComponent',
    setup(){
        return { }
    }
}
</script>
<style lang="css">
    [light]{
        background-color: lightgoldenrodyellow;
    }
</style>