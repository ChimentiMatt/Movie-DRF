<!-- Change state name to not be actor -->


<template>

  <div v-if="loading"
    class="flex min-h-screen justify-center items-center min-h[40rem] dark:bg-[#121212] text-black dark:text-[#F5F5F5] pl-[5rem] pr-[5rem]">
    <p>Loading...</p>
  </div>
  <div v-if="person" class="flex flex-col dark:bg-[#121212] text-black dark:text-[#F5F5F5] pl-[5rem] pr-[5rem]">
    <h1>{{ person.name }}</h1>
    <img :src="'https://image.tmdb.org/t/p/original/' + person.headshot_url" alt="picture of person">
    <p>{{ person.birthday }}</p>
    <p>{{ person.place_of_birth }}</p>
    <p>{{ person.known_for_department }}</p>
    <p>{{ person.biography }}</p>
    <p v-if="person.gender === 1">female</p>
    <p v-else>male</p>

    <h1>Roles</h1>
    <h2>Upcoming</h2>
    <h2>Previous</h2>
    <div v-for="movie in personsMovies" class="flex pl-2 gap-2">
      {{ movie.title }}
      <div v-for="movie in movie.movie_person">
        <div v-if="movie.person_name === person.name">Role: {{ movie.role }}</div>
      </div>
      <p>Rating: {{ movie.vote_average }}</p>
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