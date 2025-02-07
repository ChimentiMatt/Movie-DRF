<template>
  <div class="relative h-full overflow-hidden">
    <div class="flex transition-transform duration-500 ease-in-out h-full"
      :style="{ transform: `translateX(-${currentIndex * 100}%)` }">

      <div v-for="(movie, index) in movies" :key="index"
        class="flex justify-center items-center flex-shrink-0 w-full h-full relative rounded-lg overflow-hidden">

        <!-- Centered Image with Aspect Ratio Handling -->
        <img :src="movie.poster_url" :alt="movie.title" class="max-h-full max-w-full object-contain" />

        <!-- Side Title and border bottom effect -->
        <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-black to-transparent p-4">
          <h2 class="text-white text-2xl font-bold">{{ movie.title }}</h2>
        </div>
      </div>
    </div>

    <!-- Navigation Buttons -->
    <button @click="prevSlide"
      class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-gray-800 bg-opacity-50 p-2 rounded-full text-white">
      &#10094;
    </button>
    <button @click="nextSlide"
      class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-gray-800 bg-opacity-50 p-2 rounded-full text-white">
      &#10095;
    </button>
  </div>
</template>

<script>
import movieService from "../api/movieService.js";

export default {
  data() {
    return {
      currentIndex: 0,
      movies: [],
    };
  },
  async created() {
    try {
      this.movies = await movieService.getMovies();
    } catch (err) {
      console.error("Failed to fetch movies:", err);
    }
  },
  methods: {
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.movies.length;
    },
    prevSlide() {
      this.currentIndex = (this.currentIndex - 1 + this.movies.length) % this.movies.length;
    },
  },
};
</script>

<style scoped>
/* Add additional styling if needed */
</style>
