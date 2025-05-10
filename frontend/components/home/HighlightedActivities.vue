<template>
  <section class="py-16 bg-white">
    <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
      <h2 class="text-4xl font-bold text-primary text-center mb-12">Highlighted Activities</h2>
      
      <div class="relative" v-if="activities.length > 0">
        <!-- Activity Cards Carousel -->
        <div class="overflow-hidden w-full">
          <div 
            class="flex transition-transform duration-500 ease-in-out"
            :style="{ width: `calc(100% * ${activities.length / 3})`, transform: `translateX(-${currentIndex * (100 / activities.length)}%)` }"
          >
            <div 
              v-for="activity in activities" 
              :key="activity.id"
              :style="{ width: `calc(100% / ${activities.length})` }"
              class="px-4 shrink-0"
            >
              <NuxtLink 
                :to="`/singleactivity?id=${activity.id}`" 
                class="block cursor-pointer h-64 relative rounded-2xl overflow-hidden group shadow-lg transition-shadow duration-300 hover:shadow-none"
              >
                <div class="absolute inset-0 bg-cover bg-center z-0" :style="`background-image: url('${activity.image_url}')`"></div>
                <div class="absolute inset-0 bg-black bg-opacity-30 group-hover:bg-opacity-10 transition-all duration-300 z-10"></div>
                <div class="absolute inset-0 flex items-center justify-center z-20">
                  <h3 class="text-2xl font-bold text-white text-center drop-shadow-lg">{{ activity.name || activity.title }}</h3>
                </div>
              </NuxtLink>
            </div>
          </div>
        </div>
        
        <!-- Navigation Arrows -->
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
        
        <!-- Dots Navigation: 3 dots for 5 cards, each dot for a window of 3 cards -->
        <div class="flex justify-center mt-8 space-x-2">
          <button 
            v-for="i in 3" 
            :key="i"
            @click="goToSlide(i-1)"
            class="w-3 h-3 rounded-full transition-all duration-300 focus:outline-none"
            :class="currentIndex === (i-1) ? 'bg-primary' : 'bg-gray-300 hover:bg-gray-400'"
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
import { ref, onMounted, onUnmounted } from 'vue';
import { API_URL } from '../../utils/api';

const activities = ref([]);
const currentIndex = ref(0);
const isLoading = ref(true);

const visibleSlides = 3;
const totalDots = 3; // For 5 cards, always 3 dots

function prevSlide() {
  if (currentIndex.value > 0) {
    currentIndex.value--;
  } else {
    currentIndex.value = totalDots - 1;
  }
}

function nextSlide() {
  if (currentIndex.value < totalDots - 1) {
    currentIndex.value++;
  } else {
    currentIndex.value = 0;
  }
}

function goToSlide(index) {
  currentIndex.value = index;
}

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

onMounted(async () => {
  try {
    const response = await fetch(`${API_URL}/activities`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    if (data.activities && data.activities.length > 0) {
      activities.value = data.activities.slice(0, 5).map(activity => ({
        ...activity,
        name: activity.name || activity.title,
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