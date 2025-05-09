<template>
    <div class="flex flex-col min-h-screen bg-gray-100">
      <NavBar />
      <BreadCrumbs v-if="teacher" :breadcrumbs="[
        { text: 'Home', url: '/' }, 
        { text: 'Teachers', url: '/teachers' }, 
        { text: `${teacher.name} ${teacher.surname}`, url: '/singleteacher' }
      ]" />
      <main class="flex-grow">
        <!-- Loading State -->
        <div v-if="isLoading" class="flex justify-center items-center h-96 bg-white">
          <div class="loading-spinner animate-fade-in">
            <div class="spinner"></div>
            <p class="mt-4 text-xl text-gray-600 animate-fade-in">Loading teacher data...</p>
          </div>
        </div>
            
        <!-- Error State -->
        <div v-else-if="error" class="flex justify-center items-center h-96 bg-white">
          <p class="text-xl text-red-600">{{ error }}</p>
        </div>
            
        <!-- Teacher Data Display -->
        <template v-else-if="teacher">
          <!-- Teacher Details with Cards Section -->
          <section class="py-14 bg-gray-100">
            <div class="container mx-auto px-6 md:px-10 lg:px-20 flex justify-center">
              <div class="flex flex-col md:flex-row gap-8 justify-center">
                <!-- Teacher Card (Left) -->
                <div class="w-full md:w-1/3 teacher-card">
                  <div class="rounded-xl shadow-lg overflow-hidden bg-white hover:shadow-xl transition">
                    <div class="h-96 relative">
                      <img 
                        :src="`/images/teachers/${teacher.name.toLowerCase()}-${teacher.surname.toLowerCase()}.jpg`" 
                        alt="" 
                        class="w-full h-full object-cover rounded-t-xl animate-fade-in" 
                        :class="{ 'opacity-0': !imageLoaded }" 
                        @load="imageLoaded = true" 
                        @error="imageError = true"
                      />
                      <div v-if="!imageLoaded" class="absolute inset-0 flex items-center justify-center bg-gray-200">
                        <p class="text-gray-600">Loading image...</p>
                      </div>
                      <div class="absolute inset-0 bg-black bg-opacity-40"></div>
                      <div class="absolute inset-x-0 bottom-0 p-6">
                        <div class="flex flex-wrap gap-2 items-center mb-2">
                          <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm animate-fade-in">
                            {{ teacher.role }}
                          </span>
                        </div>
                        <h3 class="text-2xl font-bold text-white animate-fade-in">{{ teacher.name }} {{ teacher.surname }}</h3>
                        <div class="flex flex-wrap gap-2 mt-2">
                          <span v-if="teacher.main_expertise && teacher.main_expertise.includes('&')" 
                                class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm animate-fade-in">
                            {{ teacher.main_expertise.split('&')[0].trim() }}
                          </span>
                          <span v-else class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm animate-fade-in">
                            {{ teacher.main_expertise }}
                          </span>
                          <span v-if="teacher.main_expertise && teacher.main_expertise.includes('&')" 
                                class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm animate-fade-in">
                            {{ teacher.main_expertise.split('&')[1].trim() }}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Teacher Information Card (Right) -->
                <div class="w-full md:w-1/2 teacher-card">
                  <div class="bg-white rounded-xl shadow-lg p-8 h-full">
                    <!-- Teacher Name and Title -->
                    <div class="mb-6 border-b border-gray-300 pb-4">
                      <h1 class="text-4xl font-bold text-primary animate-fade-in">{{ teacher.name }} {{ teacher.surname }}</h1>
                    </div>
                    
                    <!-- Two column layout for information -->
                    <div class="flex flex-col md:flex-row gap-8">
                      <!-- Left Column: Role and Expertise -->
                      <div class="w-full md:w-1/2 space-y-6">
                        <!-- Role -->
                        <div class="space-y-2">
                          <span class="bg-primary bg-opacity-80 text-white px-4 py-1.5 rounded-full text-base inline-block mb-2 animate-fade-in">
                            Role
                          </span>
                          <p class="text-xl text-gray-600 animate-fade-in">{{ teacher.role }}</p>
                        </div>
                        
                        <!-- Expertise -->
                        <div class="space-y-2">
                          <span class="bg-[#48A6A7] text-white px-4 py-1.5 rounded-full text-base inline-block mb-2 animate-fade-in">
                            Expertise
                          </span>
                          <p class="text-xl text-gray-600 animate-fade-in">{{ teacher.main_expertise }}</p>
                        </div>
                      </div>
                      
                      <!-- Right Column: About -->
                      <div class="w-full md:w-1/2 space-y-2">
                        <span class="bg-white bg-opacity-80 border border-primary text-primary px-4 py-1.5 rounded-full text-base inline-block mb-2 animate-fade-in">
                          About
                        </span>
                        <p class="text-lg text-gray-600 animate-fade-in">{{ teacher.about }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
                
          <!-- Activities Section -->
          <section class="py-14 bg-white border-t border-gray-200">
            <div class="container mx-auto px-6 md:px-20 flex flex-col items-center">
              <h2 class="text-3xl font-bold text-primary mb-8 animate-fade-in text-center">Activities</h2>
              
              <div v-if="isLoadingActivities" class="flex justify-center items-center h-32">
                <div class="loading-spinner animate-fade-in">
                  <div class="spinner"></div>
                  <p class="mt-4 text-xl text-gray-600 animate-fade-in">Loading activities...</p>
                </div>
              </div>
              
              <div v-else-if="activities.length === 0" class="text-gray-600 text-lg animate-fade-in p-8 bg-gray-50 rounded-lg text-center">
                No activities found for this teacher.
              </div>
              
              <!-- Uso flex invece di grid per centrare meglio le card -->
              <div v-else class="flex flex-wrap justify-center gap-6 w-full max-w-5xl">
                <div v-for="(activity, index) in activities" :key="activity.id" class="w-full sm:w-[calc(50%-12px)] md:w-[calc(40%-16px)] flex justify-center">
                  <NuxtLink
                    :to="`/singleactivity?id=${activity.id}`"
                    class="block w-full rounded-xl shadow-lg overflow-hidden bg-white transition animate-fade-in relative group activity-card"
                    :style="`animation-delay: ${index * 150}ms`"
                  >
                    <div class="h-64 relative">
                      <img
                        :src="activity.image ? activity.image : `/images/activities/${activity.id}.jpg`"
                        alt=""
                        class="w-full h-full object-cover rounded-t-xl"
                        loading="lazy"
                        @error="(e) => { e.target.style.display = 'none' }"
                      />
                      <div class="absolute inset-0 bg-black bg-opacity-40 group-hover:bg-opacity-30 transition-all duration-300"></div>
                      <div class="absolute inset-x-0 bottom-0 p-4">
                        <h3 class="text-2xl font-bold text-white group-hover:translate-y-[-2px] transition-all duration-300">{{ activity.title || activity.name }}</h3>
                        <div class="flex flex-wrap gap-2 mt-2">
                          <span v-if="activity.level" class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm group-hover:translate-y-[-2px] transition-all duration-300">{{ activity.level }}</span>
                          <span v-if="activity.schedule" class="bg-[#48A6A7] text-white px-3 py-1 rounded-full text-sm group-hover:translate-y-[-2px] transition-all duration-300">{{ activity.schedule }}</span>
                          <span v-if="activity.short_description" class="text-white text-sm group-hover:translate-y-[-2px] transition-all duration-300 shadow-md">{{ activity.short_description }}</span>
                        </div>
                      </div>
                    </div>
                  </NuxtLink>
                </div>
              </div>
            </div>
          </section>
        </template>
      </main>
      <SiteFooter />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import NavBar from '~/components/home/NavBar.vue'
  import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
  import SiteFooter from '~/components/home/SiteFooter.vue'
  
  // Query parameters to get teacher ID
  const route = useRoute()
  const teacherId = ref(route.query.id)
  
  // Data refs
  const teacher = ref(null)
  const isLoading = ref(true)
  const error = ref(null)
  const imageLoaded = ref(false)
  const imageError = ref(false)
  
  // Activities managed by the teacher
  const activities = ref([])
  const isLoadingActivities = ref(true)
  
  // Fetch teacher data from the API
  const fetchTeacher = async () => {
    if (!teacherId.value) {
      error.value = 'No teacher ID specified'
      isLoading.value = false
      return
    }
    
    try {
      const response = await fetch(`http://localhost:8000/teacher/${teacherId.value}`)
      
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`)
      }
      
      const data = await response.json()
      
      if (data.teacher) {
        teacher.value = data.teacher
        // Fetch activities for this teacher
        fetchActivities()
      } else {
        error.value = 'Teacher not found'
      }
    } catch (err) {
      console.error('Error fetching teacher:', err)
      error.value = 'Failed to load teacher data'
    } finally {
      isLoading.value = false
    }
  }
  
  // Fetch activities managed by this teacher
  const fetchActivities = async () => {
    isLoadingActivities.value = true
    try {
      const response = await fetch(`http://localhost:8000/teacher/${teacherId.value}/activities`)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`)
      }
      const data = await response.json()
      activities.value = data.activities || []
    } catch (err) {
      console.error('Error fetching activities:', err)
      activities.value = []
    } finally {
      isLoadingActivities.value = false
    }
  }
  
  // Fetch data when component mounts
  onMounted(fetchTeacher)

  // SEO metadata for this page
  watch(teacher, (newTeacher) => {
    if (newTeacher) {
      useSeoMeta({
        title: `${newTeacher.name} ${newTeacher.surname} - Serendipity Yoga`, // Use template literals
        description: 'Meet our dedicated teachers and learn more about their expertise and teaching style.',
      });
    }
  });
  </script>
  
  <style scoped>
  .text-primary {
    color: #006A71;
  }

  /* Teacher Card Styles - No hover effect */
  .teacher-card {
    transition: none; /* Remove any transition effects */
  }

  .teacher-card:hover {
    transform: none; /* No scaling effect on hover */
  }

  /* Activity Card Styles - With hover effect */
  .activity-card {
    transition: all 0.4s cubic-bezier(0.25, 0.1, 0.25, 1) !important; /* Slower, more fluid cubic-bezier easing */
    will-change: transform; /* Performance optimization for animations */
    backface-visibility: hidden; /* Prevents flickering in some browsers */
  }

  .activity-card:hover {
    transform: scale(1.025) !important;
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1) !important;
    z-index: 10;
  }

  /* Refined animations for labels within cards */
  .activity-card .group-hover\:translate-y-\[-2px\],
  .teacher-card .group-hover\:translate-y-\[-2px\] {
    transition: all 0.5s cubic-bezier(0.25, 0.1, 0.25, 1) !important; /* Slightly delayed, more fluid motion */
  }

  .activity-card:hover .group-hover\:translate-y-\[-2px\],
  .teacher-card:hover .group-hover\:translate-y-\[-2px\] {
    transform: translateY(-2px) !important;
  }

  .activity-card .group-hover\:bg-opacity-100,
  .teacher-card .group-hover\:bg-opacity-100 {
    transition: all 0.5s cubic-bezier(0.25, 0.1, 0.25, 1) !important;
  }

  /* Loading spinner */
  .loading-spinner {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    opacity: 0; /* Start hidden */
    animation: fadeIn 1s cubic-bezier(0.25, 0.1, 0.25, 1) forwards; /* Slower, more fluid animation */
  }

  .spinner {
    width: 50px;
    height: 50px;
    border: 5px solid rgba(0, 106, 113, 0.2);
    border-radius: 50%;
    border-top-color: #006A71;
    animation: spin 1.2s cubic-bezier(0.5, 0.1, 0.5, 1) infinite, scale 0.8s cubic-bezier(0.25, 0.1, 0.25, 1) forwards; /* Slower animations */
  }

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
      transform: scale(1.1); /* Slightly scale up */
    }
    100% {
      transform: scale(1);
    }
  }

  /* Animations */
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

  .animate-fade-in {
    animation: fadeIn 0.8s cubic-bezier(0.25, 0.1, 0.25, 1) forwards; /* Slower, more fluid animation */
  }
  </style> 