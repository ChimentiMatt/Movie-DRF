<template>
  <div v-if="movie" class="flex justify-center items-center dark:bg-[#121212] text-black dark:text-[#F5F5F5] p-[5rem]">

    <!-- Main Movie Section -->
    <section class="w-[50rem] flex flex-col gap-6">
      <header>
        <h1 class="text-4xl font-bold  mb-4">{{ movie.title }}</h1>
        <div class="flex justify-between">

          <p>Runtime: {{ movie.runtime }}m</p>
          <p>Rating: {{ movie.vote_average }}</p>
          <p>Release Date: {{ movie.release_date }}</p>
          <p>Revenue: ${{ movie.revenue }}</p>
        </div>
      </header>

      <!-- Movie Poster and Trailer -->
      <div class="flex justify-between ">
        <MovieTrailer :title="movieTitle" />
        <img :src="movie.poster_url" alt="Movie Poster" class="h-[315px] w-[210px] object-cover" />

      </div>

      <div class="flex flex-row space-x-2">
        <div v-for="genre in movie.genres" :key="genre">
          <p class="border-2 rounded p-2">
            {{ genre }}
          </p>
        </div>
      </div>

      <article class="">
        <p>{{ movie.overview }}</p>
      </article>

      <div class="flex gap-2">
        <h1 class="font-bold ">Stars</h1>
        <div v-for="person in movie.people" :key="person.name">
          <router-link :to="`/person/${person.name}`">
            <p v-if="person.job === 'ACT'">{{ person.name }}</p>
          </router-link>
        </div>
      </div>
    </section>
  </div>

  <!-- Movie Missing Page -->
  <div v-else>
    <p>The movie with that id does not exist</p>
  </div>

</template>

<script>
import { ref, onMounted, computed } from 'vue';
import movieService from '../api/movieService';
import MovieTrailer from '@/components/MovieTrailer.vue';

export default {
  components: {
    MovieTrailer,
  },
  props: ['id'], // Receiving the movie ID as a prop from the router
  setup(props) {
    const movie = ref(null);

    onMounted(async () => {
      try {
        movie.value = await movieService.getMovieById(props.id);
      } catch (error) {
        console.error('Failed to fetch movie details:', error);
      }
    });

    // Define computed property for dynamic movie title
    const movieTitle = computed(() => movie.value ? movie.value.title : 'Loading...');

    return { movie, movieTitle };
  },
};
</script>
