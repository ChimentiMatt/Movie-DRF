<template>
  <div>

    <!-- Display trailer if found -->
    <div v-if="trailerUrl !== 'Trailer not available' || error" class="" aria-hidden="true">
      <iframe :src="trailerUrlWithParams" frameborder="0" class="rounded w-screen lg:w-[560px]"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
        height="315">
      </iframe>
    </div>

    <!-- Error message if no trailer found -->
    <div v-if="error || trailerUrl === 'Trailer not available'" class="text-red-300">Trailer not available</div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      movieTitle: this.title, // Default to the passed movie title
      trailerUrl: null, // URL of the trailer video
      error: null, // Error message if no trailer is found
      apiKey: import.meta.env.VITE_TMDB_API_KEY, // Access the TMDb API key from the environment
    };
  },
  mounted() {
    // Fetch trailer when the component is mounted
    this.fetchTrailer();
  },
  methods: {
    async fetchTrailer() {
      try {
        this.error = null;

        // Step 1: Search for the movie by title using TMDb API
        const searchQuery = this.movieTitle;
        const searchUrl = `https://api.themoviedb.org/3/search/movie?api_key=${this.apiKey}&query=${encodeURIComponent(searchQuery)}&language=en-US`;

        const searchResponse = await fetch(searchUrl);
        const searchData = await searchResponse.json();

        // Check if the movie was found
        if (searchResponse.ok && searchData.results && searchData.results.length > 0) {
          const movieId = searchData.results[0].id;

          // Step 2: Get the movie's videos (trailer) from TMDb API
          const videoUrl = `https://api.themoviedb.org/3/movie/${movieId}/videos?api_key=${this.apiKey}&language=en-US`;
          const videoResponse = await fetch(videoUrl);
          const videoData = await videoResponse.json();

          let trailerUrl = null;

          if (videoResponse.ok && videoData.results) {
            // Find a video of type 'Trailer'
            const trailer = videoData.results.find((video) => video.type === "Trailer");
            if (trailer) {
              // Embed the video using the correct YouTube embed URL format
              trailerUrl = `https://www.youtube.com/embed/${trailer.key}`;
            } else {
              trailerUrl = "Trailer not available";
            }
          } else {
            trailerUrl = "Unable to fetch trailer";
          }

          this.trailerUrl = trailerUrl;
        } else {
          this.error = `Movie '${this.movieTitle}' trailer not available`;
          this.trailerUrl = null;
        }
      } catch (error) {
        console.error(error);
        this.error = "Failed to fetch trailer.";
        this.trailerUrl = null;
      }
    },
  },
  computed: {
    trailerUrlWithParams() {
      // Ensure trailer URL exists before processing
      if (!this.trailerUrl || this.trailerUrl.includes('Trailer not available')) {
        return null;
      }
      const videoId = this.trailerUrl.split('/').pop(); // Extract YouTube video ID from URL
      return `https://www.youtube.com/embed/${videoId}?controls=0&modestbranding=1&rel=0&showinfo=0&autohide=1&iv_load_policy=3&fs=0`;
    },
  },
};
</script>
