<template>
  <div v-if="loading"
    class="flex min-h-screen justify-center items-center min-h[40rem] dark:bg-[#121212] text-black dark:text-[#F5F5F5] pl-[5rem] pr-[5rem]">
    <p>Loading...</p>
  </div>
  <div v-if="person"
    class="flex flex-col dark:bg-[#121212] text-black dark:text-[#F5F5F5]  pl-[1rem] pr-[1rem] lg:pl-[5rem] lg:pr-[5rem]">
    <h1>{{ person.name }}</h1>
    <div class="flex flex-col lg:flex-row">

      <img :src="'https://image.tmdb.org/t/p/original/' + person.headshot_url" alt="picture of person" class="w-screen">
      <div class="lg:ml-[1rem]">
        
        <p>Date of Birth: {{ person.birthday }}</p>
        <p>Place of Birth: {{ person.place_of_birth }}</p>
        <p>Known for: {{ person.known_for_department }}</p>
        <p>Biography: {{ person.biography }}</p>
        
        <p v-if="person.gender === 1">female</p>
        <p v-else>male</p>
        
        <h1>Roles</h1>
        <h2>Upcoming</h2>
        <h2>Previous</h2>
      </div>
    </div>

    <div class=" lg:border border-gray-300 rounded-lg shadow-md p-4 mb-4 mt-[1rem]">
      <div v-for="movie in personsMovies" :key="movie.id" class="pt-2">
        <div class="flex justify-between items-center">
          <div class="flex items-center">
            <!-- Movie Poster -->
            <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" :alt="movie.title"
              class=" h-[5rem] object-cover object-contain" />

            <!-- Movie Details -->
            <div class="flex flex-col pl-4 ">
              <p class="font-bold">{{ movie.title }}</p>
              <p>⭐ {{ movie.vote_average }}</p>

              <!-- Display Person's Role in the Movie -->
              <div v-for="personRole in movie.movie_person" :key="personRole.id">
                <div v-if="personRole.person_name === person.name">Role: {{ personRole.role }}</div>
              </div>

              <!-- Release Date Small Screen-->
              <p class="block lg:hidden">{{ movie.release_date }}</p>
            </div>
          </div>

          <!-- Release Date Large Screen-->
          <p class="hidden lg:block">{{ movie.release_date }}</p>

        </div>

      </div>
    </div>
  </div>

  <div v-else class="flex flex-col dark:bg-[#121212] text-black dark:text-[#F5F5F5] pl-[5rem] pr-[5rem]">
    <h1>404 Actor not found</h1>
  </div>
</template>


<script>
import personService from '../api/personService';

export default {
  name: "PersonPage",
  data() {
    return {
      person: null,
      personsMovies: null,
      loading: true
    };
  },
  mounted() {
    this.fetchActorData()
  },
  methods: {
    async fetchActorData() {
      const personId = this.$route.params.personId;
      try {
        const personData = await personService.getPerson(personId);
        this.person = personData;  // Update actor data in the component
      } catch (error) {
        console.error("Error fetching actor data:", error);
      } finally {
        this.loading = false
        this.fetchPersonsMoviesData()
      }
    },
    async fetchPersonsMoviesData() {

      try {
        const personsMoviesData = await personService.getPersonsMovies(this.person.name);
        this.personsMovies = personsMoviesData['movies'];  // Update actor data in the component
        console.log(this.personsMovies)
      } catch (error) {
        console.error("Error fetching actor data:", error);
      } finally {
        this.loading = false
      }
    },
  },
};
</script>

<style scoped>
/* You can add styling here to customize the look of the page */
h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

img {
  max-width: 300px;
  border-radius: 8px;
}
</style>