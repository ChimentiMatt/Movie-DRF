<template>
  <div class="mt-[2.5rem] text-black dark:text-[#F5F5F5]">

    <h1 class="font-semibold text-2xl ">Actors in theatres</h1>

    <div class="flex flex-col gap-2 items-center justify-evenly pt-2">
      <div v-for="movie in filteredMovies" class="">
        <p class="text-center">
          {{ movie.title }}
        </p>
        <div class="flex justify-end gap-2 text-[0.5rem]">
          Page {{ Math.floor(currentMovieSet) + 1 }} of {{ Math.ceil(this.movies.length) }}
          <button v-if="this.currentMovieSet - 1 >= 0" @click="previousMovies()">Previous</button>
          <button v-if="this.currentMovieSet + 1 < this.movies.length" @click="nextMovies()">Next</button>
        </div>
        <div class="flex flex-col lg:flex-row mt-2">

          <div v-for="person in movie.people" class="flex flex-col justify-center items-center w-[15rem]">

            <router-link :to="'/person/' + 'Tim Allen'">
              <img :src="`https://image.tmdb.org/t/p/w500/${person.headshot_url}`" alt="Robin Williams"
                class="rounded-full h-[10rem] w-[10rem] object-cover">
            </router-link>
            <div class="flex flex-col items-center justify-center">
              <p>
                {{ person.name }}
              </p>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { ref, computed, onMounted } from "vue";
import { useInTheatresStore } from "@/stores/inTheatres.js";

export default {
  setup() {
    const inTheatresStore = useInTheatresStore();
    const movies = computed(() => inTheatresStore.movies);
    const currentMovieSet = ref(0)

    onMounted(async () => {
      await inTheatresStore.fetchMovies();
      console.log(movies.value, inTheatresStore.movies)
    });

    return {
      inTheatresStore,
      movies,
      currentMovieSet,
    };
  },
  methods: {
    nextMovies() {

      console.log(this.currentMovieSet, this.movies.length)
      if (this.currentMovieSet + 1 <= this.movies.length) {
        this.currentMovieSet += 1
      }
    },
    previousMovies() {
      if (this.currentMovieSet - 1 >= 0) {
        this.currentMovieSet -= 1
      }
    }
  },
  computed: {
    filteredMovies() {
      console.log('!', this.currentMovieSet)
      return this.movies.slice(this.currentMovieSet, this.currentMovieSet + 1);
    }
  }
};
</script>