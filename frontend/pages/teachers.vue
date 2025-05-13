<template>
  <div class="flex flex-col min-h-screen dark:bg-gray-800">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[{ text: 'Home', url: '/' }, { text: 'Teachers', url: '/teachers' }]" />
    <main class="flex-grow">
      <!-- Teachers Section -->
      <section class="bg-white dark:bg-gray-800 py-14 px-20">
        <div class="container mx-auto">
          <!-- Section Header -->
          <div class="flex flex-col items-center gap-5 mb-12">
            <h1 v-if="isLoading" class="loading-title animate-fade-in">Loading title...</h1>
            <h1 v-else class="text-3xl font-bold text-primary dark:text-[#9ACBD0] text-center animate-fade-in">Our Teachers</h1>
            <p v-if="isLoading" class="loading-description animate-fade-in">Loading description...</p>
            <p v-else class="text-xl text-gray-600 dark:text-gray-300 text-center max-w-3xl animate-fade-in">
              At Serendipity Yoga, we pride ourselves on having a team of passionate and experienced instructors who bring their diverse skills and expertise to every class.<br/><br/> Below, you'll meet the wonderful individuals who lead our various activities and help guide you on your journey to wellness.<br />
            </p>
          </div>

          <!-- Loading State -->
          <div v-if="isLoading" class="flex justify-center items-center h-56">
            <div class="loading-spinner">
              <div class="spinner"></div>
              <p class="mt-4 text-xl text-gray-600 dark:text-gray-300">Loading teachers...</p>
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
              class="teacher-card relative rounded-xl overflow-hidden shadow-lg dark:shadow-gray-900/70 h-80 w-full sm:w-[calc(50%-1rem)] lg:w-[calc(33.333%-1.334rem)] group cursor-pointer transition-all duration-300 hover:shadow-2xl animate-fade-in"
              :style="`animation-delay: ${index * 150}ms`"
            >
              <div class="h-96 relative">
                <img 
                  :src="`/images/teachers/${teacher.name.toLowerCase()}-${teacher.surname.toLowerCase()}.jpg`" 
                  alt="" 
                  class="w-full h-full object-cover rounded-t-xl animate-fade-in" 
                  :class="{ 'opacity-0': !teacher.imageLoaded }" 
                  @load="teacher.imageLoaded = true" 
                  @error="teacher.imageError = true"
                />
                <div v-if="!teacher.imageLoaded && !teacher.imageError" class="absolute inset-0 flex items-center justify-center bg-gray-200 dark:bg-gray-600">
                  <p class="text-gray-600 dark:text-gray-300">Loading image...</p>
                </div>
              </div>
              <div class="absolute inset-0 bg-black bg-opacity-30 group-hover:bg-opacity-20 transition-all duration-300"></div>
              <div class="absolute bottom-0 left-0 right-0 p-6">
                <div class="flex flex-wrap gap-2 items-center mb-2">
                  <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:translate-y-[-2px]">
                    {{ teacher.role }}
                  </span>
                </div>
                <h3 class="text-2xl font-bold text-white group-hover:translate-y-[-2px] transition-all duration-300">{{ teacher.name }} {{ teacher.surname }}</h3>
                <div class="flex flex-wrap gap-2 mt-2">
                  <span v-if="teacher.main_expertise && teacher.main_expertise.includes('&')" 
                        class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:translate-y-[-2px]">
                    {{ teacher.main_expertise.split('&')[0].trim() }}
                  </span>
                  <span v-else class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:translate-y-[-2px]">
                    {{ teacher.main_expertise }}
                  </span>
                  <span v-if="teacher.main_expertise && teacher.main_expertise.includes('&')" 
                        class="bg-white bg-opacity-80 text-gray-600 px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:translate-y-[-2px]">
                    {{ teacher.main_expertise.split('&')[1].trim() }}
                  </span>
                </div>
              </div>
            </NuxtLink>
          </div>
        </div>
      </section>

      <!-- Teachers List -->
      <section class="py-16 hidden dark:bg-gray-800">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <!-- Existing content -->
        </div>
      </section>
    </main>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import NavBar, { selectedLang } from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'
import { API_URL } from '../utils/api'

// Define languages locally
const languages = [
  { code: 'en', name: 'English', flag: '🇬🇧' },
  { code: 'it', name: 'Italiano', flag: '🇮🇹' },
  { code: 'fr', name: 'Français', flag: '🇫🇷' },
  { code: 'de', name: 'Deutsch', flag: '🇩🇪' },
  { code: 'zh', name: '中文', flag: '🇨🇳' }
];

const teachers = ref([])
const isLoadingTeachers = ref(true)
const errorTeachers = ref(null)

const fetchTeachers = async () => {
  isLoadingTeachers.value = true
  errorTeachers.value = null
  try {
    const response = await fetch(`${API_URL}/teachers?lang=${selectedLang.value}`)
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`)
    const data = await response.json()
    if (data.teachers && data.teachers.length > 0) {
      teachers.value = data.teachers
    } else {
      errorTeachers.value = 'No teachers found'
    }
  } catch (err) {
    errorTeachers.value = 'Failed to load teachers'
  } finally {
    isLoadingTeachers.value = false
  }
}

onMounted(fetchTeachers)
watch(selectedLang, fetchTeachers)

// SEO metadata for this page
useSeoMeta({
    title: 'Our Teachers - Serendipity Yoga',
    description: 'Meet our dedicated teachers and learn more about their expertise and teaching style.',
  })
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

:root.dark .text-primary {
  color: #9ACBD0;
}

/* Card Animation Styles - Unified across site */
.teacher-card {
  animation: fadeInUp 0.8s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
  opacity: 0;
  transition: all 0.4s cubic-bezier(0.25, 0.1, 0.25, 1) !important; /* Slower, more fluid cubic-bezier easing */
  will-change: transform; /* Performance optimization for animations */
  backface-visibility: hidden; /* Prevents flickering in some browsers */
}

.teacher-card:hover {
  transform: scale(1.025) !important;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1) !important;
  z-index: 10;
}

.dark .teacher-card:hover {
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3) !important;
}

/* Refined animations for labels within cards */
.teacher-card .group-hover\:translate-y-\[-2px\] {
  transition: all 0.5s cubic-bezier(0.25, 0.1, 0.25, 1) !important; /* Slightly delayed, more fluid motion */
}

.teacher-card:hover .group-hover\:translate-y-\[-2px\] {
  transform: translateY(-2px) !important;
}

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

.dark .spinner {
  border-color: rgba(154, 203, 208, 0.2);
  border-top-color: #9ACBD0;
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
    transform: scale(1.1); /* Slightly scale up */
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
  animation: fadeIn 0.8s cubic-bezier(0.25, 0.1, 0.25, 1) forwards; /* Slower, more fluid animation */
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

/* Dark mode transition */
.dark-transition {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
</style> 