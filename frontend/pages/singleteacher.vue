<template>
    <div class="flex flex-col min-h-screen">
      <NavBar />
      <BreadCrumbs v-if="teacher" :breadcrumbs="[
        { text: 'Home', url: '/' }, 
        { text: 'Teachers', url: '/teachers' }, 
        { text: `${teacher.name} ${teacher.surname}`, url: '/singleteacher' }
      ]" />
      <main class="flex-grow">
        <!-- Teacher Details Section -->
        <section class="bg-gray-50 py-14 border-b border-gray-200">
          <div class="container mx-auto px-6 md:px-20">
            <!-- Loading State -->
            <div v-if="isLoading" class="flex justify-center items-center h-96">
              <p class="text-xl text-gray-600">Loading teacher data...</p>
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
                    <img :src="`/images/teachers/${teacher.name.toLowerCase()}-${teacher.surname.toLowerCase()}.jpg`" 
                         :alt="`${teacher.name} ${teacher.surname}`" 
                         class="w-full h-full object-cover">
                    <div class="absolute inset-0 bg-black bg-opacity-30"></div>
                    <div class="absolute inset-x-0 bottom-0 p-6">
                      <div class="flex flex-wrap gap-2 items-center mb-2">
                        <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm">
                          Lead Instructor
                        </span>
                      </div>
                      <h3 class="text-2xl font-bold text-white">{{ teacher.name }} {{ teacher.surname }}</h3>
                      <div class="flex flex-wrap gap-2 mt-2">
                        <span v-if="teacher.main_expertise && teacher.main_expertise.includes('&')" 
                              class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm">
                          {{ teacher.main_expertise.split('&')[0].trim() }}
                        </span>
                        <span v-else-if="teacher.main_expertise"
                              class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm">
                          {{ teacher.main_expertise }}
                        </span>
                        <span v-if="teacher.main_expertise && teacher.main_expertise.includes('&')" 
                              class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm">
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
                  <h1 class="text-4xl font-bold text-primary">{{ teacher.name }} {{ teacher.surname }}</h1>
                  <p class="text-2xl text-gray-600">Lead Instructor</p>
                </div>
                
                <!-- Expertise -->
                <div class="space-y-2">
                  <h2 class="text-3xl font-bold text-black">Expertise</h2>
                  <p class="text-xl text-gray-600">{{ teacher.main_expertise }}</p>
                </div>
                
                <!-- About -->
                <div class="space-y-2">
                  <h2 class="text-3xl font-bold text-black">About</h2>
                  <p class="text-xl text-gray-600">
                    {{ teacher.about }}
                  </p>
                </div>
                
                <!-- Activities -->
                <div class="space-y-6">
                  <h2 class="text-3xl font-bold text-black">Activities</h2>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                    <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition">
                      Morning Class
                    </NuxtLink>
                    <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition">
                      Afternoon Workshop
                    </NuxtLink>
                    <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition">
                      Advanced Session
                    </NuxtLink>
                    <NuxtLink to="/activities" class="block bg-gray-200 rounded-xl px-6 py-4 text-center font-bold hover:bg-gray-300 transition">
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
  </style> 