<template>
  <header class="bg-gray-100 dark:bg-gray-800 text-black dark:text-gray-200 flex justify-between p-4">
    <h1>LOGO</h1>
    <nav class="flex gap-4">
      <input type="text" placeholder="Search..."
        class="border px-2 dark:bg-gray-700 dark:text-gray-200 dark:border-gray-600">
      <a href="#" class="text-blue-500 dark:text-blue-300">Settings</a>

      <button @click="toggleTheme">
        <p v-if="!isDark" class="w-6 h-6">🌑</p>
       
        <p v-if="isDark" class="w-6 h-6">☀️</p>
      </button>
    </nav>
  </header>
</template>
<script>

export default {
  data() {
    return {
      // Directly retrieve the theme preference from localStorage
      isDark: localStorage.getItem('dark-theme') === 'enabled',
    };
  },
  methods: {
    // Method to toggle dark mode
    toggleTheme() {
      // Toggle the dark mode class on the <html> element
      this.isDark = !this.isDark;

      // Update the dark mode class and localStorage based on the toggle state
      if (this.isDark) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('dark-theme', 'enabled');
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('dark-theme', 'disabled');
      }
    }
  },
  mounted() {
    // Apply the saved theme preference when the component is mounted
    if (this.isDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }
};
</script>