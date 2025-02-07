<template>
  <div class="dark:bg-[#121212] dark:text-[#F5F5F5] pl-[5rem] pr-[5rem] pt-[1.5rem]">
    <!-- Search Box -->
    <input
      v-model="searchQuery"
      type="text"
      placeholder="Search for a movie..."
      @input="loadPage(1)"
      class="search-box bg-gray-100 text-black dark:text-white rounded border-2 border-black dark:border-white dark:bg-[#121212]"
      />

    <!-- Movie Rankings Table -->
    <div v-if="movies.length">
      <table class="movie-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Vote Average</th>
            <th>Release Date</th>
          </tr>
        </thead>
        <tbody>
          <!-- Display movies -->
          <tr v-for="movie in movies" :key="movie.id" @click="goToMovieDetails(movie.id)" class="group hover:bg-blue-500">
            <td class="group-hover:text-white group-hover:bg-blue-500">{{ movie.title }}</td>
            <td class="group-hover:text-white group-hover:bg-blue-500">{{ movie.vote_average }}</td>
            <td class="group-hover:text-white group-hover:bg-blue-500">{{ movie.release_date }}</td>
          </tr>


        </tbody>
      </table>

      <!-- Pagination Controls -->
      <div class="pagination">
        <span>Page {{ currentPage }} of {{ totalPages }}</span>
        <button @click="loadPage(currentPage - 1)" :disabled="currentPage <= 1">Previous</button>
        <button @click="loadPage(currentPage + 1)" :disabled="currentPage >= totalPages">Next</button>
      </div>
    </div>

    <div v-else>
      <p>No movies found...</p>
    </div>
  </div>
</template>

<script>
import movieService from "../api/movieService.js";

export default {
  data() {
    return {
      currentPage: 1,
      totalPages: 1,
      movies: [],
      searchQuery: '',
    };
  },
  async created() {
    await this.loadPage(this.currentPage);
  },
  methods: {
    async loadPage(pageNumber) {
      if (pageNumber < 1 || pageNumber > this.totalPages) return; // Avoid out-of-bounds pages
      try {
        const data = await movieService.getMovieRankingList(pageNumber, this.searchQuery);
        this.movies = data.movies;
        this.totalPages = data.total_pages;
        this.currentPage = pageNumber;
      } catch (err) {
        console.error("Failed to load page:", err);
      }
    },
    goToMovieDetails(movieId) {
      // Programmatically navigate to the movie detail page
      this.$router.push(`/movie/${movieId}`);
    }
  },
};
</script>

<style scoped>
/* Table styling */
.movie-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.movie-table th,
.movie-table td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}

.movie-table th {
  background-color: #333;
  color: #fff;
  font-weight: bold;
}

.movie-table tr:nth-child(odd) {
  background-color: #f9f9f9; /* Alternate row colors */
  color: black;
}

.movie-table tr:nth-child(even) {
  background-color: #272727; /* Alternate row colors */
  color: white;
}

/* Pagination styling */
.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: end;
  gap: 10px;
}

.pagination button:disabled {
  opacity: 0.5;
}

.search-box {
  margin: 20px 0;
  padding: 10px;
  width: 300px;
  display: block;
  margin-bottom: 20px;
}
</style>
