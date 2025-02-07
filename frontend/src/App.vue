<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
import HeaderSubmenu from './components/HeaderSubmenu.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <Header />
  <HeaderSubmenu />
  <RouterView />
  <Footer />
</template>

<style scoped>

</style>
