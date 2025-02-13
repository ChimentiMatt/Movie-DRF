<template>
  <main class="flex flex-col justify-center dark:bg-[#121212] text-black dark:text-[#F5F5F5] p-[2rem]">

    <div class="flex flex-col lg:flex-row justify-center ">
      <Carousel />
      <UpcomingMovies />
    </div>

    <TrendingCelebs />
    <Test />

  </main>
</template>

<script>
import Carousel from "@/components/Carousel.vue";
import TrendingCelebs from "@/components/TrendingCelebs.vue";
import UpcomingMovies from "@/components/UpcomingMovies.vue"
import Test from "@/components/Test.vue";
import movieService from "../api/movieService.js";
import { useInTheatresStore } from "@/stores/inTheatres.js"


export default {
  components: {
    Carousel,
    UpcomingMovies,
    TrendingCelebs,
    Test,
  },
  setup() {
    const inTheatresStore = useInTheatresStore();
    inTheatresStore.fetchMovies();

    return { inTheatresStore };
  },
  data() {
    return {
      upNextMovies: [
        { title: "Movie 1", releaseDate: "2025-05-10", poster: "https://via.placeholder.com/80x120" },
        { title: "Movie 2", releaseDate: "2025-06-15", poster: "https://via.placeholder.com/80x120" },
        { title: "Movie 3", releaseDate: "2025-07-20", poster: "https://via.placeholder.com/80x120" },
      ],
    };
  },
  async created() {
    try {
      movieService.getInTheatreMovies();
    } catch (err) {
      console.error("Failed to fetch movies:", err);
    }
  },
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>