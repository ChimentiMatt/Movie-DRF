<template>
  <div class="mt-[2.5rem] text-2xl font-bold text-black dark:text-[#F5F5F5]">

    <h1>Iconic Celebrities</h1>

    <!-- replace later with images from backend with help of a img api-->
    <div class="flex justify-evenly pt-2">
      <router-link :to="'/person/' + 'George Lucas'">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Robin_Williams_2011a_%282%29.jpg" alt="Robin Williams" class="rounded-full h-[10rem] w-[10rem] object-cover">
      </router-link>

      <router-link :to="'/person/' + 'Tim Allen'">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Robin_Williams_2011a_%282%29.jpg" alt="Robin Williams" class="rounded-full h-[10rem] w-[10rem] object-cover">
      </router-link>
        


    </div>

  </div>

</template>