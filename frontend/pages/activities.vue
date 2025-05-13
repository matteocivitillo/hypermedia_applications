<template>
  <div class="flex flex-col min-h-screen dark:bg-gray-800">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: t('activities') }
    ]" />
    <main class="flex-grow">
      <!-- Activities Section -->
      <section class="bg-white dark:bg-gray-800 py-14 px-20">
        <div class="container mx-auto">
          <!-- Section Header -->
          <div class="flex flex-col items-center gap-5 mb-12">
            <h1 v-if="isLoading" class="loading-title animate-fade-in">{{ t('loadingTitle') }}</h1>
            <h1 v-else class="text-3xl font-bold text-primary dark:text-[#9ACBD0] text-center animate-fade-in">{{ t('ourActivities') }}</h1>
            <p v-if="isLoading" class="loading-description animate-fade-in">{{ t('loadingDescription') }}</p>
            <p v-else class="text-xl text-gray-600 dark:text-gray-300 text-center max-w-4xl animate-fade-in">
              {{ t('activitiesDescription') }}
            </p>
          </div>

          <!-- Separator -->
          <div class="w-full h-px bg-gray-200 dark:bg-gray-600 mb-12"></div>

          <!-- Loading State -->
          <div v-if="isLoading" class="flex justify-center items-center h-56">
            <div class="loading-spinner">
              <div class="spinner"></div>
              <p class="mt-4 text-xl text-gray-600 dark:text-gray-300">{{ t('loadingActivities') }}</p>
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
              <h2 class="text-2xl font-bold text-primary dark:text-[#9ACBD0] mb-8 text-center animate-fade-in">{{ t('yogaClasses') }}</h2>
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <NuxtLink 
                  v-for="(activity, index) in yogaClasses" 
                  :key="activity.id"
                  :to="`/singleactivity?id=${activity.id}`" 
                  class="activity-card relative rounded-xl overflow-hidden shadow-lg dark:shadow-gray-900/70 h-80 group cursor-pointer transition-all duration-300 hover:shadow-2xl animate-fade-in"
                  :style="`animation-delay: ${index * 150}ms`"
                >
                  <div class="h-96 relative">
                    <img 
                      :src="activity.image || `/images/activities/default-activity.jpg`" 
                      alt="" 
                      class="w-full h-full object-cover rounded-t-xl animate-fade-in" 
                      :class="{ 'opacity-0': !imageLoaded }" 
                      @load="imageLoaded = true" 
                      @error="imageError = true"
                    />
                    <div v-if="!imageLoaded" class="absolute inset-0 flex items-center justify-center bg-gray-200 dark:bg-gray-600">
                      <p class="text-gray-600 dark:text-gray-300">{{ t('loadingImage') }}</p>
                    </div>
                  </div>
                  <div class="absolute inset-0 bg-black bg-opacity-30 group-hover:bg-opacity-20 transition-all duration-300"></div>
                  <div class="absolute bottom-0 left-0 right-0 p-6">
                    <div class="flex flex-wrap gap-2 items-center mb-2">
                      <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:translate-y-[-2px]">
                        {{ activity.level }}
                      </span>
                    </div>
                    <h3 class="text-2xl font-bold text-white group-hover:translate-y-[-2px] transition-all duration-300">{{ activity.title }}</h3>
                    <div class="flex flex-wrap gap-2 mt-2">
                      <span class="text-white py-1 text-sm transition-all duration-300 group-hover:translate-y-[-2px]">
                        {{ activity.short_description }}
                      </span>
                    </div>
                  </div>
                </NuxtLink>
              </div>
            </div>

            <!-- Other Activities Section -->
            <div>
              <h2 class="text-2xl font-bold text-primary dark:text-[#9ACBD0] mb-8 text-center animate-fade-in">{{ t('otherActivities') }}</h2>
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <NuxtLink 
                  v-for="(activity, index) in otherActivities" 
                  :key="activity.id"
                  :to="`/singleactivity?id=${activity.id}`" 
                  class="activity-card relative rounded-xl overflow-hidden shadow-lg dark:shadow-gray-900/70 h-80 group cursor-pointer transition-all duration-300 hover:shadow-2xl animate-fade-in"
                  :style="`animation-delay: ${index * 150}ms`"
                >
                  <div class="h-96 relative">
                    <img 
                      :src="activity.image || `/images/activities/default-activity.jpg`" 
                      alt="" 
                      class="w-full h-full object-cover rounded-t-xl animate-fade-in" 
                      :class="{ 'opacity-0': !imageLoaded }" 
                      @load="imageLoaded = true" 
                      @error="imageError = true"
                    />
                    <div v-if="!imageLoaded" class="absolute inset-0 flex items-center justify-center bg-gray-200 dark:bg-gray-600">
                      <p class="text-gray-600 dark:text-gray-300">{{ t('loadingImage') }}</p>
                    </div>
                  </div>
                  <div class="absolute inset-0 bg-black bg-opacity-30 group-hover:bg-opacity-20 transition-all duration-300"></div>
                  <div class="absolute bottom-0 left-0 right-0 p-6">
                    <div class="flex flex-wrap gap-2 items-center mb-2">
                      <span class="bg-primary bg-opacity-80 text-white px-3 py-1 rounded-full text-sm group-hover:bg-opacity-100 transition-all duration-300 group-hover:translate-y-[-2px]">
                        {{ activity.level }}
                      </span>
                    </div>
                    <h3 class="text-2xl font-bold text-white group-hover:translate-y-[-2px] transition-all duration-300">{{ activity.title }}</h3>
                    <div class="flex flex-wrap gap-2 mt-2">
                      <span class="text-white py-1 text-sm transition-all duration-300 group-hover:translate-y-[-2px]">
                        {{ activity.short_description }}
                      </span>
                    </div>
                  </div>
                </NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Activity Grid Section -->
      <section class="py-16 dark:bg-gray-800">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <!-- Existing content -->
        </div>
      </section>
    </main>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import NavBar, { selectedLang } from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'
import { API_URL } from '../utils/api'

// Translations
const translations = {
  en: {
    activities: 'Activities',
    loadingTitle: 'Loading title...',
    ourActivities: 'Our Activities',
    loadingDescription: 'Loading description...',
    activitiesDescription: 'Discover our diverse range of activities designed to nurture your body, mind, and spirit.',
    loadingActivities: 'Loading activities...',
    yogaClasses: 'Yoga Classes',
    otherActivities: 'Other Activities',
    loadingImage: 'Loading image...',
    seoTitle: 'Our Activities - Serendipity Yoga',
    seoDescription: 'Discover our diverse range of activities designed to nurture your body, mind, and spirit.',
    noActivitiesFound: 'No activities found',
    failedToLoad: 'Failed to load activities'
  },
  it: {
    activities: 'Attività',
    loadingTitle: 'Caricamento titolo...',
    ourActivities: 'Le Nostre Attività',
    loadingDescription: 'Caricamento descrizione...',
    activitiesDescription: 'Scopri la nostra variegata gamma di attività progettate per nutrire il tuo corpo, la tua mente e il tuo spirito.',
    loadingActivities: 'Caricamento attività...',
    yogaClasses: 'Lezioni di Yoga',
    otherActivities: 'Altre Attività',
    loadingImage: 'Caricamento immagine...',
    seoTitle: 'Le Nostre Attività - Serendipity Yoga',
    seoDescription: 'Scopri la nostra variegata gamma di attività progettate per nutrire il tuo corpo, la tua mente e il tuo spirito.',
    noActivitiesFound: 'Nessuna attività trovata',
    failedToLoad: 'Impossibile caricare le attività'
  },
  fr: {
    activities: 'Activités',
    loadingTitle: 'Chargement du titre...',
    ourActivities: 'Nos Activités',
    loadingDescription: 'Chargement de la description...',
    activitiesDescription: 'Découvrez notre gamme variée d\'activités conçues pour nourrir votre corps, votre esprit et votre âme.',
    loadingActivities: 'Chargement des activités...',
    yogaClasses: 'Cours de Yoga',
    otherActivities: 'Autres Activités',
    loadingImage: 'Chargement de l\'image...',
    seoTitle: 'Nos Activités - Serendipity Yoga',
    seoDescription: 'Découvrez notre gamme variée d\'activités conçues pour nourrir votre corps, votre esprit et votre âme.',
    noActivitiesFound: 'Aucune activité trouvée',
    failedToLoad: 'Échec du chargement des activités'
  },
  de: {
    activities: 'Aktivitäten',
    loadingTitle: 'Titel wird geladen...',
    ourActivities: 'Unsere Aktivitäten',
    loadingDescription: 'Beschreibung wird geladen...',
    activitiesDescription: 'Entdecken Sie unsere vielfältigen Aktivitäten, die Körper, Geist und Seele nähren.',
    loadingActivities: 'Aktivitäten werden geladen...',
    yogaClasses: 'Yoga-Kurse',
    otherActivities: 'Andere Aktivitäten',
    loadingImage: 'Bild wird geladen...',
    seoTitle: 'Unsere Aktivitäten - Serendipity Yoga',
    seoDescription: 'Entdecken Sie unsere vielfältigen Aktivitäten, die Körper, Geist und Seele nähren.',
    noActivitiesFound: 'Keine Aktivitäten gefunden',
    failedToLoad: 'Aktivitäten konnten nicht geladen werden'
  },
  zh: {
    activities: '活动',
    loadingTitle: '正在加载标题...',
    ourActivities: '我们的活动',
    loadingDescription: '正在加载描述...',
    activitiesDescription: '探索我们多样化的活动，为您的身体、心灵和精神提供滋养。',
    loadingActivities: '正在加载活动...',
    yogaClasses: '瑜伽课程',
    otherActivities: '其他活动',
    loadingImage: '正在加载图片...',
    seoTitle: '我们的活动 - Serendipity瑜伽',
    seoDescription: '探索我们多样化的活动，为您的身体、心灵和精神提供滋养。',
    noActivitiesFound: '未找到活动',
    failedToLoad: '加载活动失败'
  }
};

// Function to get translations
const t = (key) => {
  const lang = selectedLang.value;
  return translations[lang]?.[key] || translations.en[key];
};

// Data refs
const activities = ref([])
const isLoading = ref(true)
const error = ref(null)
const imageLoaded = ref(false)
const imageError = ref(false)

// Computed properties to filter activities by type
const yogaClasses = computed(() => {
  return activities.value.filter(activity => activity.type === 'Yoga_class')
})

const otherActivities = computed(() => {
  return activities.value.filter(activity => activity.type === 'Activity')
})

// Fetch activities from API con lingua
const fetchActivities = async () => {
  isLoading.value = true
  error.value = null
  try {
    const response = await fetch(`${API_URL}/activities?lang=${selectedLang.value}`)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    const data = await response.json()
    if (data.activities && data.activities.length > 0) {
      activities.value = data.activities.map(activity => ({
        ...activity,
        imageLoaded: false,
        imageError: false
      }))
    } else {
      error.value = t('noActivitiesFound')
    }
  } catch (err) {
    console.error('Error fetching activities:', err)
    error.value = t('failedToLoad')
  } finally {
    isLoading.value = false
  }
}

// Fetch data when component mounts
onMounted(fetchActivities)
watch(selectedLang, fetchActivities)

// SEO metadata for this page
useSeoMeta({
  title: t('seoTitle'),
  description: t('seoDescription'),
})
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

:root.dark .text-primary {
  color: #9ACBD0;
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

.dark .activity-card:hover {
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3) !important;
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

/* Dark mode transition */
.dark-transition {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
</style> 