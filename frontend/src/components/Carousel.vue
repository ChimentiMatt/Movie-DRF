<template>
  <div class="flex flex-col">
    <h1 class="mb-2 lg:ml-[2.5rem] text-center lg:text-left text-2xl font-semibold">In Theatres</h1>

    <div class="relative overflow-hidden" @mouseenter="pauseCarousel" @mouseleave="startCarousel">
      <div class="flex lg:w-[290px] transition-transform duration-500 ease-in-out h-full"
        :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
        <div v-for="(movie, index) in movies" :key="index"
          class="flex justify-center items-center flex-shrink-0 w-full relative overflow-hidden">
          <router-link :to="'/movie/' + movie.id">
            <img :src="movie.poster_url" :alt="movie.title"
              class="h-[315px] w-[210px] rounded-lg object-cover object-contain hover:opacity-60" />
          </router-link>
        </div>
      </div>

      <!-- Navigation Buttons -->
      <button @click="prevSlide"
        class="absolute left-2 top-1/2 transform -translate-y-1/2 bg-gray-200 dark:bg-gray-900 bg-opacity-50 p-2 rounded-full text-blue-500">
        &#10094;
      </button>
      <button @click="nextSlide"
        class="absolute right-2 top-1/2 transform -translate-y-1/2 bg-gray-200 dark:bg-gray-900 bg-opacity-50 p-2 rounded-full text-blue-500">
        &#10095;
      </button>
    </div>

    <!-- Dots (Indicators) -->
    <div class="flex justify-center mt-2 gap-1">
      <span v-for="(movie, index) in movies" :key="index" @click="goToSlide(index)"
        class="w-[3.5px] h-[3.5px] rounded-full cursor-pointer transition-all"
        :class="index === currentIndex ? 'bg-blue-400' : 'bg-gray-400'">
      </span>
    </div>

    <!-- Movie Title -->
    <div class="flex justify-center mt-1">
      <h1 v-if="movies.length > 0" class="absolute font-semibold">{{ movies[currentIndex]?.title }}</h1>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from "vue";
import { useInTheatresStore } from "@/stores/inTheatres.js";

export default {
  setup() {
    const inTheatresStore = useInTheatresStore();
    const currentIndex = ref(0);
    const intervalId = ref(null);

    const movies = computed(() => inTheatresStore.movies);

    onMounted(async () => {
      await inTheatresStore.fetchMovies();
      startCarousel();
    });

    onUnmounted(() => {
      pauseCarousel();
    });

    function nextSlide() {
      currentIndex.value = (currentIndex.value + 1) % movies.value.length;
    }

    function prevSlide() {
      currentIndex.value = (currentIndex.value - 1 + movies.value.length) % movies.value.length;
    }

    function goToSlide(index) {
      currentIndex.value = index;
      pauseCarousel();
      startCarousel();
    }

    function startCarousel() {
      if (intervalId.value) clearInterval(intervalId.value);
      intervalId.value = setInterval(() => {
        currentIndex.value = (currentIndex.value + 1) % movies.value.length;
      }, 3000);
    }

    function pauseCarousel() {
      if (intervalId.value) {
        clearInterval(intervalId.value);
        intervalId.value = null;
      }
    }

    return {
      movies,
      currentIndex,
      nextSlide,
      prevSlide,
      goToSlide,
      startCarousel,
      pauseCarousel,
    };
  },
};
</script>
