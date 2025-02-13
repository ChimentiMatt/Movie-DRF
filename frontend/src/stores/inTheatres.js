import { defineStore } from 'pinia';
import movieService from '@/api/movieService'; // Ensure you have the correct import path

export const useInTheatresStore = defineStore('inTheatres', {
  state: () => ({
    movies: [],
    moviesIndex: [], // Fix: Added this to state
  }),
  actions: {
    async fetchMovies() {
      try {
        // Fetch movies from service
        this.movies = await movieService.getInTheatreMovies();
        
        // Fix: Ensure `moviesIndex` is properly updated
        this.moviesIndex = this.movies.map((movie, index) => ({
          index,
          title: movie.title,
        }));

      } catch (err) {
        console.error("Failed to fetch movies:", err);
      }
    },
  }
});
