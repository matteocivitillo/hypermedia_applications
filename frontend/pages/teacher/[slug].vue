<template>
    <div class="flex flex-col min-h-screen bg-gray-100 dark:bg-gray-800">
      <NavBar />
      <BreadCrumbs v-if="teacher" :breadcrumbs="[
        { text: t('home'), url: '/' }, 
        { text: t('teachers'), url: '/teachers' }, 
        { text: `${teacher.name} ${teacher.surname}`, url: `/teacher/${slug}` }
      ]" />
      <main class="flex-grow">
        <!-- Loading State -->
        <div v-if="isLoading" class="flex justify-center items-center h-96 bg-white dark:bg-gray-700">
          <div class="loading-spinner animate-fade-in">
            <div class="spinner"></div>
            <p class="mt-4 text-xl text-gray-600 dark:text-gray-300 animate-fade-in">{{ t('loadingTeacher') }}</p>
          </div>
        </div>
            
        <!-- Error State -->
        <div v-else-if="error" class="flex justify-center items-center h-96 bg-white dark:bg-gray-700">
          <p class="text-xl text-red-600">{{ error }}</p>
        </div>
            
        <!-- Teacher Data Display -->
        <template v-else-if="teacher">
          <!-- Teacher Details with Cards Section -->
          <section class="py-14 bg-gray-100 dark:bg-gray-800">
            <div class="container mx-auto px-6 md:px-10 lg:px-20">
              <!-- Contenitore flessibile: colonna su mobile, riga su desktop -->
              <div class="flex flex-col md:flex-row gap-8 justify-center">
                <!-- Teacher Card (Photo) - Prima card -->
                <div class="w-full md:w-2/5 lg:w-1/3 teacher-card">
                  <div class="rounded-xl shadow-md overflow-hidden bg-white dark:bg-gray-700">
                    <div class="h-96 relative">
                      <img 
                        :src="`/images/teachers/${teacher.name.toLowerCase()}-${teacher.surname.toLowerCase()}.jpg`" 
                        alt="" 
                        class="w-full h-full object-cover rounded-t-xl animate-fade-in" 
                        :class="{ 'opacity-0': !imageLoaded }" 
                        @load="imageLoaded = true" 
                        @error="handleImageError"
                      />
                      <div v-if="!imageLoaded && !imageError" class="absolute inset-0 flex items-center justify-center bg-gray-200 dark:bg-gray-600">
                        <p class="text-gray-600 dark:text-gray-300">{{ t('loadingImage') }}</p>
                      </div>
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
                
                <!-- Teacher Information Card - Seconda card -->
                <div class="w-full md:w-3/5 lg:w-1/2 teacher-card">
                  <div class="bg-white dark:bg-gray-700 rounded-xl shadow-md p-8 h-full">
                    <!-- Teacher Name and Title -->
                    <div class="mb-6 border-b border-gray-300 dark:border-gray-600 pb-4">
                      <h1 class="text-4xl font-bold text-primary dark:text-[#9ACBD0] animate-fade-in">{{ teacher.name }} {{ teacher.surname }}</h1>
                    </div>
                    
                    <!-- Two column layout for information -->
                    <div class="flex flex-col sm:flex-row gap-8">
                      <!-- Left Column: Role and Expertise -->
                      <div class="w-full sm:w-1/2 space-y-6">
                        <!-- Role -->
                        <div class="space-y-2">
                          <span class="bg-primary bg-opacity-80 text-white px-4 py-1.5 rounded-full text-base inline-block mb-2 animate-fade-in">
                            {{ t('role') }}
                          </span>
                          <p class="text-xl text-gray-600 dark:text-gray-300 animate-fade-in">{{ teacher.role }}</p>
                        </div>
                        
                        <!-- Expertise -->
                        <div class="space-y-2">
                          <span class="bg-[#48A6A7] text-white px-4 py-1.5 rounded-full text-base inline-block mb-2 animate-fade-in">
                            {{ t('expertise') }}
                          </span>
                          <p class="text-xl text-gray-600 dark:text-gray-300 animate-fade-in">{{ teacher.main_expertise }}</p>
                        </div>
                      </div>
                      
                      <!-- Right Column: About -->
                      <div class="w-full sm:w-1/2 space-y-2">
                        <span class="bg-white dark:bg-gray-700 bg-opacity-80 border border-primary dark:border-[#9ACBD0] text-primary dark:text-[#9ACBD0] px-4 py-1.5 rounded-full text-base inline-block mb-2 animate-fade-in">
                          {{ t('about') }}
                        </span>
                        <p class="text-lg text-gray-600 dark:text-gray-300 animate-fade-in">{{ teacher.about }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
                
          <!-- Activities Section - Terza sezione su schermi piccoli -->
          <section class="py-14 bg-white dark:bg-gray-700 border-t border-gray-200 dark:border-gray-600">
            <div class="container mx-auto px-6 md:px-20 flex flex-col items-center">
              <h2 class="text-3xl font-bold text-primary dark:text-[#9ACBD0] mb-8 animate-fade-in text-center">{{ t('activities') }}</h2>
              
              <div v-if="isLoadingActivities" class="flex justify-center items-center h-32">
                <div class="loading-spinner animate-fade-in">
                  <div class="spinner"></div>
                  <p class="mt-4 text-xl text-gray-600 dark:text-gray-300 animate-fade-in">{{ t('loadingActivities') }}</p>
                </div>
              </div>
              
              <div v-else-if="activities.length === 0" class="text-gray-600 dark:text-gray-300 text-lg animate-fade-in p-8 bg-gray-50 dark:bg-gray-600 rounded-lg text-center">
                {{ t('noActivities') }}
              </div>
              
              <!-- Uso flex invece di grid per centrare meglio le card -->
              <div v-else class="flex flex-wrap justify-center gap-6 w-full max-w-5xl">
                <div v-for="(activity, index) in activities" :key="activity.id" class="w-full sm:w-[calc(50%-12px)] md:w-[calc(40%-16px)] flex justify-center">
                  <ActivityCard 
                    :activity="activity"
                    :style="`animation-delay: ${index * 150}ms`"
                  />
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
  import { ref, onMounted, watch, computed } from 'vue'
  import NavBar, { selectedLang } from '~/components/home/NavBar.vue'
  import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
  import SiteFooter from '~/components/home/SiteFooter.vue'
  import ActivityCard from '~/components/misc/ActivityCardSuggestion.vue'
  import { API_URL } from '~/utils/api'
  
  // Translations
  const translations = {
    en: {
      home: 'Home',
      teachers: 'Teachers',
      role: 'Role',
      expertise: 'Expertise',
      about: 'About',
      activities: 'Activities',
      loadingTeacher: 'Loading teacher data...',
      loadingImage: 'Loading image...',
      loadingActivities: 'Loading activities...',
      noActivities: 'No activities found for this teacher.',
      seoTitle: '{name} {surname} - Serendipity Yoga',
      seoDescription: 'Meet our dedicated teachers and learn more about their expertise and teaching style.'
    },
    it: {
      home: 'Home',
      teachers: 'Insegnanti',
      role: 'Ruolo',
      expertise: 'Specialità',
      about: 'Informazioni',
      activities: 'Attività',
      loadingTeacher: 'Caricamento dati insegnante...',
      loadingImage: 'Caricamento immagine...',
      loadingActivities: 'Caricamento attività...',
      noActivities: 'Nessuna attività trovata per questo insegnante.',
      seoTitle: '{name} {surname} - Serendipity Yoga',
      seoDescription: 'Incontra i nostri dedicati insegnanti e scopri di più sulla loro specialità e il loro stile di insegnamento.'
    },
    fr: {
      home: 'Accueil',
      teachers: 'Professeurs',
      role: 'Rôle',
      expertise: 'Expertise',
      about: 'À propos',
      activities: 'Activités',
      loadingTeacher: 'Chargement des données du professeur...',
      loadingImage: 'Chargement de l\'image...',
      loadingActivities: 'Chargement des activités...',
      noActivities: 'Aucune activité trouvée pour ce professeur.',
      seoTitle: '{name} {surname} - Serendipity Yoga',
      seoDescription: 'Rencontrez nos professeurs dévoués et découvrez leur expertise et leur style d\'enseignement.'
    },
    de: {
      home: 'Startseite',
      teachers: 'Lehrer',
      role: 'Rolle',
      expertise: 'Expertise',
      about: 'Über',
      activities: 'Aktivitäten',
      loadingTeacher: 'Lehrerdaten werden geladen...',
      loadingImage: 'Bild wird geladen...',
      loadingActivities: 'Aktivitäten werden geladen...',
      noActivities: 'Keine Aktivitäten für diesen Lehrer gefunden.',
      seoTitle: '{name} {surname} - Serendipity Yoga',
      seoDescription: 'Lernen Sie unsere engagierten Lehrer kennen und erfahren Sie mehr über ihre Expertise und ihren Unterrichtsstil.'
    },
    zh: {
      home: '首页',
      teachers: '教师',
      role: '角色',
      expertise: '专长',
      about: '关于',
      activities: '活动',
      loadingTeacher: '正在加载教师数据...',
      loadingImage: '正在加载图片...',
      loadingActivities: '正在加载活动...',
      noActivities: '未找到此教师的活动。',
      seoTitle: '{name} {surname} - Serendipity瑜伽',
      seoDescription: '认识我们敬业的教师，了解更多关于他们的专长和教学风格。'
    }
  };
  
  // Function to get translations
  const t = (key) => {
    const lang = selectedLang.value;
    return translations[lang]?.[key] || translations.en[key];
  };
  
  // Get the slug from the route
  const route = useRoute();
  const slug = ref(route.params.slug);
  
  // Data refs
  const teacher = ref(null);
  const teacherId = ref(null);
  const isLoading = ref(true);
  const error = ref(null);
  const imageLoaded = ref(false);
  const imageError = ref(false);
  
  // Handle image loading error
  const handleImageError = () => {
    imageError.value = true;
    imageLoaded.value = true;  // Consider the image "loaded" even if it's an error
  };
  
  // Activities managed by the teacher
  const activities = ref([]);
  const isLoadingActivities = ref(true);
  
  // Fetch all teachers to find the one matching the slug
  const findTeacherIdBySlug = async () => {
    try {
      const response = await fetch(`${API_URL}/teachers?lang=${selectedLang.value}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      const data = await response.json();
      
      if (data.teachers && data.teachers.length > 0) {
        // Find the teacher with the matching slug
        const foundTeacher = data.teachers.find(t => {
          const teacherSlug = `${t.name.toLowerCase()}-${t.surname.toLowerCase()}`.replace(/\s+/g, '-');
          return teacherSlug === slug.value;
        });
        
        if (foundTeacher) {
          teacherId.value = foundTeacher.id;
          return foundTeacher.id;
        } else {
          error.value = 'Teacher not found';
          isLoading.value = false;
          return null;
        }
      }
    } catch (err) {
      console.error('Error finding teacher by slug:', err);
      error.value = 'Failed to locate teacher';
      isLoading.value = false;
      return null;
    }
  };
  
  // Fetch teacher data from the API
  const fetchTeacher = async () => {
    if (!teacherId.value) {
      const id = await findTeacherIdBySlug();
      if (!id) return;
    }
    
    try {
      const response = await fetch(`${API_URL}/teacher/${teacherId.value}?lang=${selectedLang.value}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      
      const data = await response.json();
      
      if (data.teacher) {
        teacher.value = data.teacher;
        // Reset image loading state
        imageLoaded.value = false;
        imageError.value = false;
        // Fetch activities for this teacher
        fetchActivities();
      } else {
        error.value = 'Teacher not found';
      }
    } catch (err) {
      console.error('Error fetching teacher:', err);
      error.value = 'Failed to load teacher data';
    } finally {
      isLoading.value = false;
    }
  };
  
  // Fetch activities managed by this teacher
  const fetchActivities = async () => {
    isLoadingActivities.value = true;
    try {
      const response = await fetch(`${API_URL}/teacher/${teacherId.value}/activities?lang=${selectedLang.value}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      activities.value = data.activities || [];
    } catch (err) {
      console.error('Error fetching activities:', err);
      activities.value = [];
    } finally {
      isLoadingActivities.value = false;
    }
  };
  
  // Fetch data when component mounts
  onMounted(() => fetchTeacher());
  
  // Watch for language changes to reload data
  watch(selectedLang, () => {
    fetchTeacher();
    
    // Update SEO if teacher data is already loaded
    if (teacher.value) {
      useSeoMeta({
        title: t('seoTitle')
          .replace('{name}', teacher.value.name)
          .replace('{surname}', teacher.value.surname),
        description: t('seoDescription'),
      });
    }
  });
  
  // SEO metadata for this page (on initial load)
  watch(teacher, (newTeacher) => {
    if (newTeacher) {
      useSeoMeta({
        title: t('seoTitle')
          .replace('{name}', newTeacher.name)
          .replace('{surname}', newTeacher.surname),
        description: t('seoDescription'),
      });
    }
  });
  </script>
  
  <style scoped>
  .text-primary {
    color: #006A71;
  }

  :root.dark .text-primary {
    color: #9ACBD0;
  }

  /* Teacher Card Styles - Rimuovo effetto hover e applico lo stile di ombra delle card in prices */
  .teacher-card {
    transition: none;
  }

  .teacher-card > div {
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }

  .dark .teacher-card > div {
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
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

  .dark .activity-card:hover {
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3) !important;
  }

  /* Refined animations for labels within cards */
  .activity-card .group-hover\:translate-y-\[-2px\] {
    transition: all 0.5s cubic-bezier(0.25, 0.1, 0.25, 1) !important; /* Slightly delayed, more fluid motion */
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

  /* Dark mode transition */
  .dark-transition {
    transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
  }
  </style> 