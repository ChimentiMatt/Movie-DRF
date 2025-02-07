<template>
  <div class="w-[20rem] ml-2 pl-4 text-black dark:text-[#F5F5F5]">
    <h2 class="text-xl font-semibold mb-2">Up Next</h2>
    <div class="flex flex-col space-y-4">
      <div v-for="(movie, index) in upNextMovies" :key="index" class="flex items-center space-x-4">
        <img :src="movie.poster" alt="movie.title" class="w-16 h-[5rem] object-cover rounded-md" />
        <div>
          <h3 class="text-lg font-medium">{{ movie.title }}</h3>
          <p class="text-sm text-gray-500">{{ movie.releaseDate }}</p>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import Carousel from "@/components/Carousel.vue";

export default {
  components: {
    Carousel,
  },
  data() {
    return {
      upNextMovies: [
        { title: "Star Wars", releaseDate: "2025-05-10", poster: "https://image.tmdb.org/t/p/w500/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg" },
        { title: "The Avengers", releaseDate: "2025-06-15", poster: "https://image.tmdb.org/t/p/w500/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg" },
        { title: "Lord of The Rings: Return of the King", releaseDate: "2025-07-20", poster: "https://image.tmdb.org/t/p/w500/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg" },
      ],
    };
  },
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>