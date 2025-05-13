<template>
  <section class="py-16 bg-white dark:bg-gray-800">
    <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
      <h2 class="text-4xl font-bold text-primary dark:text-[#9ACBD0] text-center mb-12">{{ t('highlightedActivities') }}</h2>
      
      <div v-if="isLoading" class="flex justify-center">
        <div class="animate-pulse flex space-x-4">
          <div class="h-80 w-full bg-gray-200 dark:bg-gray-600 rounded-xl"></div>
        </div>
      </div>
      
      <div class="relative" v-else-if="activities.length > 0">
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
                :to="`/activity/${activity.title.toLowerCase().replace(/\s+/g, '-')}`" 
                class="block cursor-pointer h-64 relative rounded-2xl overflow-hidden group shadow-lg dark:shadow-gray-900/70 transition-shadow duration-300 hover:shadow-none"
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
            :class="currentIndex === (i-1) ? 'bg-primary' : 'bg-gray-300 dark:bg-gray-500 hover:bg-gray-400 dark:hover:bg-gray-400'"
          ></button>
        </div>
      </div>
      
      <div v-else class="text-center py-8">
        <p class="text-xl text-gray-600 dark:text-gray-300">{{ t('couldNotLoadActivities') }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { API_URL } from '../../utils/api';
import { selectedLang } from '../home/NavBar.vue';

const activities = ref([]);
const currentIndex = ref(0);
const isLoading = ref(true);

// List of activities we want to display with variations in different languages
const highlightedActivityNames = [
  // English
  'Zumba', 'Zumba Fitness',
  'Meditation', 'Mindfulness', 'Mindfulness Meditation',
  'Ceramics', 'Pottery', 'Mindful Pottery',
  'Water Yoga', 'Aqua Yoga',
  'Sunset Yoga',
  'Dance Fit Fusion', 'Dance Fitness',
  
  // Italian
  'Zumba', 'Fitness Zumba',
  'Meditazione', 'Mindfulness', 'Meditazione Mindfulness',
  'Ceramica', 'Ceramica Consapevole', 'Pottery',
  'Yoga in Acqua', 'Yoga Acquatico',
  'Yoga al Tramonto',
  'Danza Fitness', 'Fusion Dance',
  
  // French
  'Zumba', 'Zumba Fitness',
  'Méditation', 'Pleine Conscience',
  'Céramique', 'Poterie',
  'Yoga Aquatique',
  'Yoga au Coucher du Soleil',
  'Danse Fitness',
  
  // German
  'Zumba',
  'Meditation', 'Achtsamkeit',
  'Keramik', 'Töpfern',
  'Wasser-Yoga', 'Aqua-Yoga',
  'Sonnenuntergang-Yoga',
  'Tanz-Fitness',
  
  // Chinese (using pinyin for simplicity)
  'Zumba',
  'Meditation', 'Mindfulness',
  'Ceramics', 'Pottery',
  'Water Yoga',
  'Sunset Yoga',
  'Dance Fitness'
];

// Traduzioni
const translations = {
  en: {
    highlightedActivities: 'Highlighted Activities',
    couldNotLoadActivities: 'Could not load activities. Please try again later.'
  },
  it: {
    highlightedActivities: 'Attività in Evidenza',
    couldNotLoadActivities: 'Impossibile caricare le attività. Riprova più tardi.'
  },
  fr: {
    highlightedActivities: 'Activités en Vedette',
    couldNotLoadActivities: 'Impossible de charger les activités. Veuillez réessayer plus tard.'
  },
  de: {
    highlightedActivities: 'Hervorgehobene Aktivitäten',
    couldNotLoadActivities: 'Aktivitäten konnten nicht geladen werden. Bitte versuchen Sie es später erneut.'
  },
  zh: {
    highlightedActivities: '精选活动',
    couldNotLoadActivities: '无法加载活动。请稍后再试。'
  }
};

// Funzione per ottenere traduzioni
const t = (key) => {
  const lang = selectedLang.value;
  return translations[lang]?.[key] || translations.en[key];
};

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

// Helper function to check if an activity title matches our highlighted list
function isHighlightedActivity(title) {
  if (!title) return false;
  
  // Normalize activity names for comparison
  const normalizedTitle = title.toLowerCase().trim();
  
  // Log per debug
  console.log(`Checking activity: "${normalizedTitle}"`);
  
  // Check direct matches and known variations
  for (const name of highlightedActivityNames) {
    const normalizedName = name.toLowerCase().trim();
    
    // Direct match
    if (normalizedTitle === normalizedName) {
      console.log(`Found direct match: ${normalizedTitle} = ${normalizedName}`);
      return true;
    }
    
    // Check if the title contains the name (more lenient matching)
    if (normalizedTitle.includes(normalizedName)) {
      console.log(`Found partial match: ${normalizedTitle} contains ${normalizedName}`);
      return true;
    }
    
    // Check for variations of meditation
    if (normalizedName === 'meditation' && 
        (normalizedTitle.includes('meditation') || 
         normalizedTitle.includes('mindfulness'))) {
      console.log(`Found meditation match: ${normalizedTitle}`);
      return true;
    }
    
    // Check for variations of ceramics
    if (normalizedName === 'ceramics' && 
        (normalizedTitle.includes('pottery') || 
         normalizedTitle.includes('ceramic'))) {
      console.log(`Found ceramics match: ${normalizedTitle}`);
      return true;
    }
    
    // Check for variations of yoga
    if ((normalizedName === 'water yoga' || normalizedName === 'sunset yoga') && 
        normalizedTitle.includes('yoga')) {
      console.log(`Found yoga match: ${normalizedTitle} for ${normalizedName}`);
      return true;
    }
    
    // Check for variations of dance
    if (normalizedName === 'dance fit fusion' && 
        (normalizedTitle.includes('dance') || 
         normalizedTitle.includes('fitness') || 
         normalizedTitle.includes('zumba'))) {
      console.log(`Found dance match: ${normalizedTitle}`);
      return true;
    }
    
    // Check for Zumba specifically
    if (normalizedName === 'zumba' && 
        normalizedTitle.includes('zumba')) {
      console.log(`Found zumba match: ${normalizedTitle}`);
      return true;
    }
  }
  
  return false;
}

// Fetch activities function
const fetchActivities = async () => {
  isLoading.value = true;
  activities.value = []; // Resetta le attività
  
  try {
    const response = await fetch(`${API_URL}/activities?lang=${selectedLang.value}`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    const data = await response.json();
    console.log(`Fetched ${data.activities?.length || 0} activities in language: ${selectedLang.value}`);
    
    if (data.activities && data.activities.length > 0) {
      // Mostra le prime 5 attività per debug
      const sampleActivities = data.activities.slice(0, 5);
      console.log("Sample activities:", sampleActivities.map(a => ({
        id: a.id,
        title: a.title || a.name,
        type: a.type
      })));
      
      // Filter activities to include only those from our highlighted list
      const filteredActivities = data.activities.filter(activity => 
        isHighlightedActivity(activity.title || activity.name)
      );
      
      console.log(`Found ${filteredActivities.length} activities matching our highlighted list`);
      
      // Se non abbiamo abbastanza attività filtrate, mostriamo alcune attività casuali
      if (filteredActivities.length < 3) {
        console.log("Not enough highlighted activities, adding some random activities");
        
        // Seleziona attività casuali che non sono già nella lista filtrata
        const remainingActivities = data.activities.filter(a => 
          !filteredActivities.some(fa => fa.id === a.id)
        );
        
        // Prendi attività casuali fino a raggiungere almeno 3 attività totali
        const randomActivities = remainingActivities
          .sort(() => Math.random() - 0.5)
          .slice(0, Math.max(3 - filteredActivities.length, 0));
        
        // Unisci le attività filtrate con quelle casuali
        const combinedActivities = [...filteredActivities, ...randomActivities];
        console.log(`Total activities after adding random: ${combinedActivities.length}`);
        
        // Aggiorna la lista di attività
        activities.value = combinedActivities.map(activity => ({
          ...activity,
          name: activity.title || activity.name,
          image_url: activity.image || `/images/activities/${activity.id}.jpg`
        }));
      } else {
        // Se abbiamo abbastanza attività filtrate, le usiamo direttamente
        activities.value = filteredActivities.map(activity => ({
          ...activity,
          name: activity.title || activity.name,
          image_url: activity.image || `/images/activities/${activity.id}.jpg`
        }));
      }
      
      // Log final activities
      console.log(`Final activities to display: ${activities.value.length}`);
    } else {
      console.error("No activities found in response");
    }
  } catch (error) {
    console.error('Failed to fetch activities:', error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchActivities();
  // Auto slide every 5 seconds
  autoSlideInterval = setInterval(nextSlide, 5000);
});

// Quando cambia la lingua, aggiorna le attività
watch(selectedLang, () => {
  fetchActivities();
});

// Auto slide every 5 seconds
let autoSlideInterval;

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

.dark .text-primary {
  color: #9ACBD0;
}

.dark .bg-primary {
  background-color: #006A71;
}

.dark .shadow-custom {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.2);
}
</style> 