<template>
  <div class="relative h-full overflow-hidden">
    <div class="flex transition-transform duration-500 ease-in-out h-full"
      :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
      <div v-for="(slide, index) in slides" :key="index" class="w-full flex-shrink-0 h-full relative rounded-lg overflow-hidden">
        <img :src="slide.image" :alt="slide.title" class="w-full h-full object-cover" />

        <!-- Side Title and border bottom effect -->
        <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-black to-transparent p-4">
          <h2 class="text-white text-2xl font-bold">{{ slide.title }}</h2>
        </div>
      </div>
    </div>

    <!-- Navigation Buttons -->
    <button @click="prevSlide"
      class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-gray-800 bg-opacity-50 p-2 rounded-full text-white">
      &#10094;
    </button>
    <button @click="nextSlide"
      class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-gray-800 bg-opacity-50 p-2 rounded-full text-white">
      &#10095;
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentIndex: 0,
      slides: [
        { title: "Inception", image: "https://www.movieposterdb.com/posters/12_05/2008/468569/l_468569_0c3a3b3b.jp" },
        { title: "The Dark Knight", image: "https://www.movieposterdb.com/posters/12_05/2008/468569/l_468569_0c3a3b3b.jpg" },
        { title: "Interstellar", image: "https://www.movieposterdb.com/posters/12_05/2008/468569/l_468569_0c3a3b3b.jp" },
      ],
    };
  },
  methods: {
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.slides.length;
    },
    prevSlide() {
      this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
    },
  },
};
</script>

<style scoped>
/* Add any additional styling if needed */
</style>