import axios from "axios";

const API_BASE_URL = import.meta.env.VUE_APP_API_BASE_URL || "http://localhost:8000"; // Default to local if not set

export const movieService = {
  async getMovies() {
    try {
      const response = await axios.get(`${API_BASE_URL}/movies/`);
      return response.data.movies; // Return only movie data
    } catch (error) {
      console.error("Error fetching movies:", error);
      throw error;
    }
  },

  async getMovieRankingList(page = 1, searchQuery = '') {
    try {
      const response = await axios.get(`${API_BASE_URL}/movies-ranking-list/`, {
        params: {
          page,
          search: searchQuery,  // Pass search query to backend
        },
      });
      return response.data;  // Return the response data (movie and pagination metadata)
    } catch (error) {
      console.error("Error fetching movie ranking list:", error);
      throw error;
    }
  },

  async getMovieById(movieId) {
    try {
      const response = await axios.get(`${API_BASE_URL}/movies/${movieId}/`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching movie ID ${movieId}:`, error);
      throw error;
    }
  },
};

export default movieService;