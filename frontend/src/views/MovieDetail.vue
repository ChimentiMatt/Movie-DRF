<template>
  <div v-if="movie"
    class="flex justify-center items-center dark:bg-[#121212] text-black dark:text-[#F5F5F5] p-[5rem]">

    <!-- Main Movie Section --> <!-- needs RD after UI plan is finalized-->
    <section class="w-[50rem] flex flex-col gap-6">
      <header>
        <h1 class="text-4xl font-bold  mb-4">{{ movie.title }}</h1>
        <p>{{ movie.runtime }}m </p>
      </header>

      <!-- Movie Poster and Trailer -->
      <div class="flex justify-between">
        <img :src="movie.poster_url" alt="Movie Poster" />
        <div class="bg-black w-[20rem]"> Trailer Here</div>
      </div>

      <div class="flex flex-row space-x-2">
        <div v-for="genre in movie.genres">
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
        <div v-for="person in movie.people">
          <p v-if="person.job === 'Actor' ">{{ person.name }}</p>
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
import { ref, onMounted } from 'vue';
import movieService from '../api/movieService';

export default {
  props: ['id'], // Receiving the movie ID as a prop from the router
  setup(props) {
    const movie = ref(null);

    // Fetch movie details when the component is mounted
    onMounted(async () => {
      try {
        movie.value = await movieService.getMovieById(props.id);
      } catch (error) {
        console.error('Failed to fetch movie details:', error);
      }
    });

    return { movie };
  },
};
</script>