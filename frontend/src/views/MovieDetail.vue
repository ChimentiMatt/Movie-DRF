<template>
  <div v-if="movie" class="flex justify-center items-center dark:bg-[#121212] text-black dark:text-[#F5F5F5] pt-[2rem]">

    <!-- Main Movie Section -->
    <section class="w-[50rem] flex flex-col  gap-6">
      <header class="ml-[1rem] mr-[1rem] lg:m-0">
        <h1 class="text-4xl font-bold mb-4">{{ movie.title }}</h1>
        <div class="flex flex-col lg:flex-row justify-between text-[0.5rem] lg:text-[1rem] ml-[1rem] mr-[1rem] lg:m-0">

          <p>Runtime: {{ movie.runtime }}m</p>
          <p>Rating: {{ movie.vote_average }}</p>
          <p>Release Date: {{ movie.release_date }}</p>
          <p>Revenue: ${{ movie.revenue }}</p>
          <p>Mpaa {{ movie.mpaa_rating }}</p>
        </div>
      </header>

      <!-- Movie Poster and Trailer -->
      <div class="flex flex-col lg:flex-row justify-between ">
        <MovieTrailer :title="movieTitle" class="rounded" />
        <img :src="movie.poster_url" alt="Movie Poster"
          class="lg:h-[315px] lg:w-[210px] object-cover rounded custom-shadow" />
      </div>

      <div class="flex flex-col gap-2 ml-[1rem] mr-[1rem] lg:ml-0 lg:mr-0">

        <div class="flex flex-row space-x-2 ">
          <div v-for="genre in movie.genres" :key="genre">
            <p class="border-2 rounded p-2">
              {{ genre }}
            </p>
          </div>
        </div>

        <article>
          <p>{{ movie.overview }}</p>
        </article>
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
