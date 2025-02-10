<template>
  <div class="flex flex-col mt-[5rem] lg:mt-0">

    <div v-if="showTrailer">
      <FullScreenMovieTrailer :title="selectedMovieTitle" v-model="showTrailer" />
    </div>

    <div class="flex justify-between items-center relative font-semibold ml-2 text-2xl">

      <h1>Upcoming Movies</h1>


    </div>

    <div class="h-[315px] lg:w-[25rem] lg:ml-2 mt-[0.5rem] pl-4 rounded text-black dark:text-white rounded-xl custom-shadow">
      <div class="flex pt-2 pb-2 flex-col h-full justify-between">

        <div v-for="(movie, index) in filteredMovies" :key="index">

          <div v-if="index < 3" class=" flex space-x-4">
            <router-link :to="'/movie/' + movie.id" class="flex">
              <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_url}`" alt="movie.title"
                class="h-[5rem] object-cover rounded-md hover:opacity-60" />
            </router-link>

            <div class="flex flex-col justify-center">
              <p class="">{{ movie.title }}</p>
              <p class="opacity-80">{{ movie.release_date }}</p>
              <p @click="openTrailer(movie)" class="opacity-80 cursor-pointer hover:opacity-60">🎥 Trailer</p>
            </div>

          </div>

        </div>

      </div>
        <div class="flex justify-end items-center gap-2 text-[0.5rem]">
          <p class="relative top-1">
            Page {{ Math.floor(currentMovieSet / 3) + 1 }} of {{ Math.ceil(upNextMovies.length / 3) }}
          </p>

          <button v-if="this.currentMovieSet - 3 >= 0" @click="previousMovies()"
            class=" cursor-pointer mt-2 hover:opacity-60">Previous
          </button>
          <button v-if="this.currentMovieSet + 3 <= this.upNextMovies.length" @click="nextMovies()"
            class="cursor-pointer mt-2 hover:opacity-60">Next
          </button>
        </div>

    </div>

  </div>
</template>

<script>
import movieService from "../api/movieService.js";
import FullScreenMovieTrailer from "./FullScreenMovieTrailer.vue";

export default {
  components: {
    FullScreenMovieTrailer
  },
  data() {
    return {
      upNextMovies: [],
      currentMovieSet: 0, // Starting index of the movies in the component example 0 (- 2)
      showTrailer: false, // Controls visibility of the trailer
      selectedMovieTitle: '',
    };
  },
  async created() {
    try {
      this.upNextMovies = await movieService.getUpcomingMovies();
    } catch (err) {
      console.error("Failed to fetch movies:", err);
    }
  },
  methods: {
    openTrailer(movie) {
      this.selectedMovieId = movie.id;
      this.selectedMovieTitle = movie.title;
      this.showTrailer = true;
    },
    nextMovies() {
      if (this.currentMovieSet + 3 <= this.upNextMovies.length) {
        this.currentMovieSet += 3
      }
    },
    previousMovies() {
      if (this.currentMovieSet - 3 >= 0) {
        this.currentMovieSet -= 3
      }
    }
  },
  computed: {
    filteredMovies() {
      return this.upNextMovies.slice(this.currentMovieSet, this.currentMovieSet + 3);
    }
  }
};
</script>
