<template>
  <div class="fixed flex top-0 left-0 w-[99vw] h-[100vh] z-50 bg-gradient-to-br from-black via-gray-900 to-transparent">
    <p @click="$emit('update:modelValue', false)"
      class="cursor-pointer text-white text-2xl absolute top-4 right-[5rem]">✖️
    </p>

    <div v-if="trailerUrl !== 'Trailer not available' || error" class="flex justify-center w-full items-center"
      aria-hidden="true">
      <iframe :src="trailerUrlWithParams" frameborder="0" class=" h-[80vh] w-[70vw] rounded z-50"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
      </iframe>
    </div>
    <div v-if="error || trailerUrl === 'Trailer not available'" class="flex w-[99vw] justify-center items-center text-white text-xl">{{ title }} trailer not available at this time</div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    modelValue: Boolean,

  },
  data() {
    return {
      movieTitle: this.title,
      trailerUrl: null,
      error: null, // Error message if no trailer is found
      apiKey: import.meta.env.VITE_TMDB_API_KEY,
    };
  },
  mounted() {
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