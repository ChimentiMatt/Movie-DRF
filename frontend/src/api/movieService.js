import axios from "axios";

const API_BASE_URL = import.meta.env.VUE_APP_API_BASE_URL || "http://localhost:8000"; // Default to local if not set

export const movieService = {
  async getUpcomingMovies(limit = null) {
    try {
      let url = `${API_BASE_URL}/upcoming-movies/`;

      // Append limit as a query parameter if provided
      if (limit) {
        url += `?limit=${limit}`;
      }

      const response = await axios.get(url);
      return response.data.movies;
    } catch (error) {
      console.error("Error fetching movies:", error);
      throw error;
    }
  },

  async getInTheatreMovies() {
    try {
      const response = await axios.get(`${API_BASE_URL}/in-theatres-movies/`);
      return response.data.movies;
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
          search: searchQuery,
        },
      });
      return response.data;
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