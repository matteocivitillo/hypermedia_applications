<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: 'Activities' }
    ]" />
    <main class="flex-grow">
      <!-- Activities Section -->
      <section class="bg-white py-14 px-20">
        <div class="container mx-auto">
          <!-- Section Header -->
          <div class="flex flex-col items-center gap-5 mb-12">
            <h1 v-if="isLoading" class="loading-title animate-fade-in">Loading title...</h1>
            <h1 v-else class="text-3xl font-bold text-primary text-center animate-fade-in">Our Activities</h1>
            <p v-if="isLoading" class="loading-description animate-fade-in">Loading description...</p>
            <p v-else class="text-xl text-gray-600 text-center max-w-4xl animate-fade-in">
              Discover our diverse range of activities designed to nurture your body, mind, and spirit.
            </p>
          </div>

          <!-- Separator -->
          <div class="w-full h-px bg-gray-200 mb-12"></div>

          <!-- Loading State -->
          <div v-if="isLoading" class="flex justify-center items-center h-56">
            <div class="loading-spinner">
              <div class="spinner"></div>
              <p class="mt-4 text-xl text-gray-600">Loading activities...</p>
            </div>
          </div>
          
          <!-- Error State -->
          <div v-else-if="error" class="flex justify-center items-center h-56">
            <p class="text-xl text-red-600">{{ error }}</p>
          </div>

          <!-- Activities Content -->
          <div v-else>
            <!-- Yoga Classes Section -->
            <div class="mb-16">
              <h2 class="text-2xl font-bold text-primary mb-8 text-center animate-fade-in">Yoga Classes</h2>
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <NuxtLink 
                  v-for="(activity, index) in yogaClasses" 
                  :key="activity.id"
                  :to="`/singleactivity?id=${activity.id}`" 
                  class="activity-card relative rounded-xl overflow-hidden shadow-lg h-80 group cursor-pointer transition-all duration-300 hover:shadow-2xl animate-fade-in"
                  :style="`animation-delay: ${index * 150}ms`"
                >
                  <div class="absolute inset-0 bg-cover bg-center" :style="`background-image: url('${activity.image || `/images/activities/default-activity.jpg`}');`"></div>
                  <div class="absolute inset-0 bg-black bg-opacity-30 group-hover:bg-opacity-20 transition-all duration-300"></div>
                  <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                    <h3 class="text-xl font-bold mb-2 bg-white bg-opacity-70 text-primary p-2 rounded-lg group-hover:transform group-hover:translate-y-[-2px] transition-all duration-300">
                      {{ activity.title }}
                    </h3>
                    <p class="text-base bg-white bg-opacity-70 text-gray-600 p-2 rounded-lg group-hover:transform group-hover:translate-y-[-2px] transition-all duration-300">
                      {{ activity.short_description }}
                    </p>
                  </div>
                </NuxtLink>
              </div>
            </div>

            <!-- Other Activities Section -->
            <div>
              <h2 class="text-2xl font-bold text-primary mb-8 text-center animate-fade-in">Other Activities</h2>
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <NuxtLink 
                  v-for="(activity, index) in otherActivities" 
                  :key="activity.id"
                  :to="`/singleactivity?id=${activity.id}`" 
                  class="activity-card relative rounded-xl overflow-hidden shadow-lg h-80 group cursor-pointer transition-all duration-300 hover:shadow-2xl animate-fade-in"
                  :style="`animation-delay: ${index * 150}ms`"
                >
                  <div class="absolute inset-0 bg-cover bg-center" :style="`background-image: url('${activity.image || `/images/activities/default-activity.jpg`}');`"></div>
                  <div class="absolute inset-0 bg-black bg-opacity-30 group-hover:bg-opacity-20 transition-all duration-300"></div>
                  <div class="absolute bottom-0 left-0 right-0 p-6 text-white">
                    <h3 class="text-xl font-bold mb-2 bg-white bg-opacity-70 text-primary p-2 rounded-lg group-hover:transform group-hover:translate-y-[-2px] transition-all duration-300">
                      {{ activity.title }}
                    </h3>
                    <p class="text-base bg-white bg-opacity-70 text-gray-600 p-2 rounded-lg group-hover:transform group-hover:translate-y-[-2px] transition-all duration-300">
                      {{ activity.short_description }}
                    </p>
                  </div>
                </NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Activity Grid Section -->
      <section class="py-16">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <!-- Existing content -->
        </div>
      </section>
    </main>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import NavBar from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'

// Data refs
const activities = ref([])
const isLoading = ref(true)
const error = ref(null)

// Computed properties to filter activities by type
const yogaClasses = computed(() => {
  return activities.value.filter(activity => activity.type === 'Yoga_class')
})

const otherActivities = computed(() => {
  return activities.value.filter(activity => activity.type === 'Activity')
})

// Fetch activities from API
const fetchActivities = async () => {
  try {
    const response = await fetch('http://localhost:8000/activities')
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    
    const data = await response.json()
    
    if (data.activities && data.activities.length > 0) {
      activities.value = data.activities
    } else {
      error.value = 'No activities found'
    }
  } catch (err) {
    console.error('Error fetching activities:', err)
    error.value = 'Failed to load activities'
  } finally {
    isLoading.value = false
  }
}

// Fetch data when component mounts
onMounted(fetchActivities)

 // SEO metadata for this page
 useSeoMeta({
    title: 'Our Activities - Serendipity Yoga',
    description: 'Discover our diverse range of activities designed to nurture your body, mind, and spirit.',
  })
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

/* Activity card animation */
.activity-card {
  animation: fadeInUp 0.8s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
  opacity: 0;
  transition: all 0.4s cubic-bezier(0.25, 0.1, 0.25, 1) !important;
  will-change: transform;
  backface-visibility: hidden;
}

.activity-card:hover {
  transform: scale(1.025) !important;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1) !important;
  z-index: 10;
}

/* Refined animations for labels within cards */
.activity-card .group-hover\:translate-y-\[-2px\] {
  transition: all 0.5s cubic-bezier(0.25, 0.1, 0.25, 1) !important;
}

.activity-card:hover .group-hover\:translate-y-\[-2px\] {
  transform: translateY(-2px) !important;
}

.activity-card .group-hover\:bg-opacity-100 {
  transition: all 0.5s cubic-bezier(0.25, 0.1, 0.25, 1) !important;
}

/* Loading spinner */
.loading-spinner {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: 0;
  animation: fadeIn 1s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid rgba(0, 106, 113, 0.2);
  border-radius: 50%;
  border-top-color: #006A71;
  animation: spin 1.2s cubic-bezier(0.5, 0.1, 0.5, 1) infinite, scale 0.8s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
}

/* Animations */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes scale {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.8s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.loading-title, .loading-description {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
</style> 