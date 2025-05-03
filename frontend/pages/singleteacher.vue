<template>
    <div class="flex flex-col min-h-screen bg-gray-100">
      <NavBar />
      <BreadCrumbs v-if="teacher" :breadcrumbs="[
        { text: 'Home', url: '/' }, 
        { text: 'Teachers', url: '/teachers' }, 
        { text: `${teacher.name} ${teacher.surname}`, url: '/singleteacher' }
      ]" />
      <main class="flex-grow">
        <!-- Teacher Details Section -->
        <section class="bg-white py-14 border-b border-gray-200 shadow-md">
          <div class="container mx-auto px-6 md:px-20">
            <!-- Loading State -->
            <div v-if="isLoading" class="flex justify-center items-center h-96">
              <div class="loading-spinner animate-fade-in">
                <div class="spinner"></div>
                <p class="mt-4 text-xl text-gray-600 animate-fade-in">Loading teacher data...</p>
              </div>
            </div>
            
            <!-- Error State -->
            <div v-else-if="error" class="flex justify-center items-center h-96">
              <p class="text-xl text-red-600">{{ error }}</p>
            </div>
            
            <!-- Teacher Data Display -->
            <div v-else-if="teacher" class="flex flex-col md:flex-row gap-16 lg:gap-24">
              <!-- Teacher Card Preview -->
              <div class="w-full md:w-1/3">
                <div class="rounded-xl shadow-lg overflow-hidden">
                  <div class="h-96 relative">
                    <img 
                      :src="`/images/teachers/${teacher.name.toLowerCase()}-${teacher.surname.toLowerCase()}.jpg`" 
                      :alt="`${teacher.name} ${teacher.surname}`" 
                      class="w-full h-full object-cover rounded-t-xl animate-fade-in" 
                      :class="{ 'opacity-0': !imageLoaded }" 
                      @load="imageLoaded = true" 
                      @error="imageError = true"
                    />
                    <div v-if="!imageLoaded" class="absolute inset-0 flex items-center justify-center bg-gray-200">
                      <p class="text-gray-600">Loading image...</p>
                    </div>
                    <div class="absolute inset-0 bg-black bg-opacity-30"></div>
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
              
              <!-- Teacher Information -->
              <div class="w-full md:w-2/3 flex flex-col gap-8">
                <!-- Teacher Name and Title -->
                <div class="space-y-1">
                  <h1 class="text-4xl font-bold text-primary animate-fade-in">{{ teacher.name }} {{ teacher.surname }}</h1>
                  <p class="text-2xl text-gray-600 animate-fade-in">{{ teacher.role }}</p>
                </div>
                
                <!-- Expertise -->
                <div class="space-y-2">
                  <h2 class="text-3xl font-bold text-black animate-fade-in">Expertise</h2>
                  <p class="text-xl text-gray-600 animate-fade-in">{{ teacher.main_expertise }}</p>
                </div>
                
                <!-- About -->
                <div class="space-y-2">
                  <h2 class="text-3xl font-bold text-black animate-fade-in">About</h2>
                  <p class="text-xl text-gray-600 animate-fade-in">{{ teacher.about }}</p>
                </div>
                
                <!-- Activities -->
                <div class="space-y-6">
                  <h2 class="text-3xl font-bold text-black animate-fade-in">Activities</h2>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                    <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition animate-fade-in">
                      Morning Class
                    </NuxtLink>
                    <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition animate-fade-in">
                      Afternoon Workshop
                    </NuxtLink>
                    <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition animate-fade-in">
                      Advanced Session
                    </NuxtLink>
                    <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition animate-fade-in">
                      Beginners Class
                    </NuxtLink>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
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
  
  // Fetch data when component mounts
  onMounted(fetchTeacher)
  </script>
  
  <style scoped>
  .text-primary {
    color: #006A71;
  }

  /* Loading spinner */
  .loading-spinner {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    opacity: 0; /* Start hidden */
    animation: fadeIn 0.8s ease forwards; /* Adjust duration */
  }

  .spinner {
    width: 50px;
    height: 50px;
    border: 5px solid rgba(0, 106, 113, 0.2);
    border-radius: 50%;
    border-top-color: #006A71;
    animation: spin 1s ease-in-out infinite, scale 0.5s ease-in-out forwards; /* Add scale effect */
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
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
    animation: fadeIn 0.6s ease-out forwards;
  }
  </style> 