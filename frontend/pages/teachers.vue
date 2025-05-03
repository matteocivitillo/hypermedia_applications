<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[{ text: 'Home', url: '/' }, { text: 'Teachers', url: '/teachers' }]" />
    <main class="flex-grow">
      <!-- Teachers Section -->
      <section class="bg-white py-14 px-20">
        <div class="container mx-auto">
          <!-- Section Header -->
          <div class="flex flex-col items-center gap-5 mb-12">
            <h1 v-if="isLoading" class="loading-title animate-fade-in">Loading title...</h1>
            <h1 v-else class="text-3xl font-bold text-primary text-center animate-fade-in">Our Teachers</h1>
            <p v-if="isLoading" class="loading-description animate-fade-in">Loading description...</p>
            <p v-else class="text-xl text-gray-600 text-center max-w-3xl animate-fade-in">
              At Serendipity Yoga, we pride ourselves on having a team of passionate and experienced instructors who bring their diverse skills and expertise to every class.<br/><br/> Below, you'll meet the wonderful individuals who lead our various activities and help guide you on your journey to wellness.<br />
            </p>
          </div>

          <!-- Loading State -->
          <div v-if="isLoading" class="flex justify-center items-center h-56">
            <div class="loading-spinner">
              <div class="spinner"></div>
              <p class="mt-4 text-xl text-gray-600">Loading teachers...</p>
            </div>
          </div>
          
          <!-- Error State -->
          <div v-else-if="error" class="flex justify-center items-center h-56">
            <p class="text-xl text-red-600">{{ error }}</p>
          </div>

          <!-- Teachers Grid - Flexible layout with auto-placement -->
          <div v-else class="flex flex-wrap justify-center gap-8 max-w-6xl mx-auto">
            <!-- Dynamic Teacher Cards -->
            <NuxtLink 
              v-for="(teacher, index) in teachers" 
              :key="teacher.id"
              :to="`/singleteacher?id=${teacher.id}`" 
              class="teacher-card relative rounded-xl overflow-hidden shadow-lg h-80 w-full sm:w-[calc(50%-1rem)] lg:w-[calc(33.333%-1.334rem)] group cursor-pointer transition-all duration-300 transform hover:scale-105 hover:shadow-2xl animate-fade-in"
              :style="`animation-delay: ${index * 100}ms`"
            >
              <div class="absolute inset-0 bg-cover bg-center" :style="`background-image: url('/images/teachers/${teacher.name.toLowerCase()}-${teacher.surname.toLowerCase()}.jpg');`"></div>
              <div class="absolute inset-0 bg-black bg-opacity-30 group-hover:bg-opacity-20 transition-all duration-300"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6">
                <div class="flex flex-wrap gap-2 items-center mb-2">
                  <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:transform group-hover:translate-y-[-2px]">
                    {{ teacher.role }}
                  </span>
                </div>
                <h3 class="text-2xl font-bold text-white group-hover:transform group-hover:translate-y-[-2px] transition-all duration-300">{{ teacher.name }} {{ teacher.surname }}</h3>
                <div class="flex flex-wrap gap-2 mt-2">
                  <span v-if="teacher.main_expertise && teacher.main_expertise.includes('&')" 
                        class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:transform group-hover:translate-y-[-2px]">
                    {{ teacher.main_expertise.split('&')[0].trim() }}
                  </span>
                  <span v-else class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:transform group-hover:translate-y-[-2px]">
                    {{ teacher.main_expertise }}
                  </span>
                  <span v-if="teacher.main_expertise && teacher.main_expertise.includes('&')" 
                        class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:transform group-hover:translate-y-[-2px]">
                    {{ teacher.main_expertise.split('&')[1].trim() }}
                  </span>
                </div>
              </div>
            </NuxtLink>
          </div>
        </div>
      </section>

      <!-- Teachers List -->
      <section class="py-16 hidden">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <!-- Existing content -->
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

// Data refs
const teachers = ref([])
const isLoading = ref(true)
const error = ref(null)

// Fetch teachers from API
const fetchTeachers = async () => {
  try {
    const response = await fetch('http://localhost:8000/teachers')
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    
    const data = await response.json()
    
    if (data.teachers && data.teachers.length > 0) {
      teachers.value = data.teachers
    } else {
      error.value = 'No teachers found'
    }
  } catch (err) {
    console.error('Error fetching teachers:', err)
    error.value = 'Failed to load teachers'
  } finally {
    isLoading.value = false
  }
}

// Fetch data when component mounts
onMounted(fetchTeachers)
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

/* Hover effect for teacher cards */
.teacher-card {
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
}

/* Loading spinner */
.loading-spinner {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid rgba(0, 106, 113, 0.2);
  border-radius: 50%;
  border-top-color: #006A71;
  animation: spin 1s ease-in-out infinite;
}

/* Animations */
@keyframes spin {
  to {
    transform: rotate(360deg);
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
  animation: fadeIn 0.8s ease-out forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.loading-title, .loading-description {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.spinner {
  width: 30px;
  height: 30px;
  border: 4px solid rgba(0, 106, 113, 0.2);
  border-radius: 50%;
  border-top-color: #006A71;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
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