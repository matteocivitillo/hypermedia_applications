<template>
  <section class="py-16 bg-gray-100">
    <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
      <h2 class="text-4xl font-bold text-primary text-center mb-12">Highlighted Activities</h2>
      
      <div class="relative" v-if="activities.length > 0">
        <!-- Activity Cards Carousel -->
        <div class="overflow-hidden">
          <div 
            class="flex" 
            :class="{ 'transition-transform duration-500 ease-in-out': transitionEnabled }"
            :style="{ transform: `translateX(-${currentIndex * 33.33}%)` }"
          >
            <div 
              v-for="activity in activities" 
              :key="activity.id"
              class="shrink-0 w-full md:w-1/3 px-4 transition-all duration-300"
            >
              <NuxtLink 
                :to="`/singleactivity?id=${activity.id}`" 
                class="block cursor-pointer h-64 relative rounded-2xl overflow-hidden group hover:shadow-xl transition-all duration-300"
              >
                <img :src="activity.image_url" :alt="activity.name" class="w-full h-full object-cover" />
                <div class="absolute inset-0 flex flex-col items-center justify-end p-6">
                  <div class="bg-white bg-opacity-90 rounded-lg py-3 px-6 mb-6 w-5/6 text-center shadow-lg transform group-hover:scale-105 transition-transform duration-300">
                    <h3 class="text-2xl font-bold text-primary">{{ activity.name || activity.title }}</h3>
                  </div>
                </div>
              </NuxtLink>
            </div>
          </div>
        </div>
        
        <!-- Navigation Arrows - moved further from images and vertically centered -->
        <button 
          @click="prevSlide"
          class="absolute -left-4 top-1/2 -translate-y-1/2 bg-primary w-14 h-14 rounded-full flex items-center justify-center shadow-lg hover:bg-primary-dark transition-colors duration-300 z-20"
          style="transform: translateY(-50%) translateX(-50%);"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M15 19l-7-7 7-7" />
          </svg>
        </button>
        
        <button 
          @click="nextSlide"
          class="absolute -right-4 top-1/2 -translate-y-1/2 bg-primary w-14 h-14 rounded-full flex items-center justify-center shadow-lg hover:bg-primary-dark transition-colors duration-300 z-20"
          style="transform: translateY(-50%) translateX(50%);"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M9 5l7 7-7 7" />
          </svg>
        </button>
        
        <!-- Dots Navigation -->
        <div class="flex justify-center mt-8 space-x-2">
          <button 
            v-for="i in activities.length" 
            :key="i"
            @click="currentIndex = i - 1"
            class="w-3 h-3 rounded-full transition-all duration-300 focus:outline-none"
            :class="currentIndex === i - 1 ? 'bg-primary' : 'bg-gray-300 hover:bg-gray-400'"
          ></button>
        </div>
      </div>
      
      <div v-else class="flex justify-center">
        <div class="animate-pulse flex space-x-4">
          <div class="h-80 w-full bg-gray-200 rounded-xl"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';

const activities = ref([]);
const currentIndex = ref(0);
const visibleSlides = ref(3);
const isLoading = ref(true);
const transitionEnabled = ref(true);

// Dummy data in case the API call fails
const dummyActivities = [
  {
    id: 1,
    name: 'Water Yoga',
    short_description: 'Experience the relaxing practice of yoga while floating on water',
    image_url: '/images/water-yoga.jpg'
  },
  {
    id: 2,
    name: 'Zumba',
    short_description: 'Energetic dance fitness program combining Latin and international music',
    image_url: '/images/zumba.jpg'
  },
  {
    id: 3,
    name: 'Meditation',
    short_description: 'Find inner peace through guided meditation sessions',
    image_url: '/images/meditation.jpg'
  },
  {
    id: 4,
    name: 'Ceramics',
    short_description: 'Express your creativity through the art of pottery making',
    image_url: '/images/ceramics.jpg'
  },
  {
    id: 5,
    name: 'Aerial Yoga',
    short_description: 'Combine traditional yoga with aerial arts using a hammock',
    image_url: '/images/aerial-yoga.jpg'
  }
];

function prevSlide() {
  if (currentIndex.value > 0) {
    currentIndex.value--;
  } else {
    // Go to the end without animation
    transitionEnabled.value = false;
    currentIndex.value = activities.value.length - visibleSlides.value;
    // Re-enable transition after a brief delay
    setTimeout(() => {
      transitionEnabled.value = true;
    }, 10);
  }
}

function nextSlide() {
  if (currentIndex.value < activities.value.length - visibleSlides.value) {
    currentIndex.value++;
  } else {
    // Go to start without animation
    transitionEnabled.value = false;
    currentIndex.value = 0;
    // Re-enable transition after a brief delay
    setTimeout(() => {
      transitionEnabled.value = true;
    }, 10);
  }
}

onMounted(async () => {
  try {
    // Using the same method as in activities.vue
    const response = await fetch('http://localhost:8000/activities');
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    const data = await response.json();
    
    if (data.activities && data.activities.length > 0) {
      // Limit to 5 activities
      activities.value = data.activities.slice(0, 5).map(activity => ({
        ...activity,
        // Ensure we use the name or title field for the activity
        name: activity.name || activity.title,
        // Use the image provided by the server or fallback to a local image
        image_url: activity.image || `/images/activities/${activity.id}.jpg`
      }));
    } else {
      activities.value = dummyActivities;
    }
  } catch (error) {
    console.error('Failed to fetch activities:', error);
    activities.value = dummyActivities;
  } finally {
    isLoading.value = false;
  }
});

// Auto slide every 5 seconds
let autoSlideInterval;
onMounted(() => {
  autoSlideInterval = setInterval(nextSlide, 5000);
});

// Clean up interval when component is unmounted
onUnmounted(() => {
  clearInterval(autoSlideInterval);
});
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

.bg-primary {
  background-color: #006A71;
}

.bg-primary-dark {
  background-color: #00585d;
}

.shadow-custom {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
}
</style> 