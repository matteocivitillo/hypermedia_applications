<template>
  <div class="flex flex-col min-h-screen dark:bg-gray-800">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: 'The Center' }
    ]" />
    <main class="flex-grow">
      <!-- Hero Section -->
      <section class="relative bg-cover bg-center h-96" style="background-image: url('/images/hero-background.jpg')">
        <div class="absolute inset-0 bg-black bg-opacity-50"></div>
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32 h-full flex items-center relative z-10">
          <div class="max-w-3xl">
            <h1 class="text-5xl font-bold text-white mb-6">Transforming lives through the practice of yoga and meditation.</h1>
            <p class="text-xl text-gray-200">Join our community and transform your life with expert guidance in yoga, meditation, and mindful living.</p>
          </div>
        </div>
      </section>

      <!-- Features Section -->
      <section class="bg-beige dark:bg-gray-700 py-20">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <div class="flex flex-wrap justify-center gap-12">
            <div class="bg-white dark:bg-gray-600 p-8 rounded-xl shadow-lg dark:shadow-gray-900/70 max-w-sm">
              <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Mindful Practice</h3>
              <p class="text-gray-600 dark:text-gray-300">Experience transformative yoga sessions guided by expert instructors.</p>
            </div>
            
            <div class="bg-white dark:bg-gray-600 p-8 rounded-xl shadow-lg dark:shadow-gray-900/70 max-w-sm">
              <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Community</h3>
              <p class="text-gray-600 dark:text-gray-300">Join a welcoming community of like-minded individuals.</p>
            </div>
            
            <div class="bg-white dark:bg-gray-600 p-8 rounded-xl shadow-lg dark:shadow-gray-900/70 max-w-sm">
              <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-800 dark:text-white mb-2">Holistic Approach</h3>
              <p class="text-gray-600 dark:text-gray-300">Balance body, mind, and spirit through our comprehensive programs.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- About the Center -->
      <section class="py-16 bg-white dark:bg-gray-800">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <h2 class="text-4xl font-bold text-primary dark:text-[#9ACBD0] text-center mb-8">Serendipity Yoga Center</h2>
          <div class="flex flex-wrap md:flex-nowrap gap-16 items-center">
            <div class="w-full md:w-1/2">
              <div class="prose prose-lg max-w-none dark:prose-invert">
                <p class="mb-4 text-gray-700 dark:text-gray-300">At Serendipity Yoga Center, we believe true wellness begins with daily choices.</p>
                <p class="mb-4 text-gray-700 dark:text-gray-300">Our holistic approach blends dynamic yoga, meditation, and rejuvenating activities to guide your full transformation: a stronger body, a clearer mind, a lighter spirit.</p>
                <p class="mb-4 text-gray-700 dark:text-gray-300">From energizing classes to immersive retreats, sunset yoga socials to spa relaxation, every experience is a step toward your best self.</p>
                <p class="mb-4 text-gray-700 dark:text-gray-300">Because lifestyle change isn't about revolution, but conscious evolution.</p>
                <p class="font-medium text-gray-700 dark:text-gray-300">Start your journey today.</p>
              </div>
            </div>
            <div class="w-full md:w-1/2">
              <img 
                :src="orientalRoomImage" 
                alt="" 
                class="w-full h-auto rounded-3xl shadow-lg dark:shadow-gray-900/70 object-cover h-96" 
                loading="lazy"
              />  <!-- Alt text is empty because it's decorative only -->
            </div>
          </div>
        </div>
      </section>

      <!-- Our Rooms -->
      <section class="bg-beige dark:bg-gray-700 py-16" id="rooms">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <h2 class="text-4xl font-bold text-primary dark:text-[#9ACBD0] text-center mb-12">Our Yoga Rooms</h2>
          
          <div v-if="isLoadingRooms" class="text-center py-8">
            <p class="text-gray-600 dark:text-gray-300">Loading rooms...</p>
          </div>
          
          <div v-else-if="errorRooms" class="text-center py-8">
            <p class="text-gray-600 dark:text-gray-300">Error loading rooms. Please try again later.</p>
          </div>
          
          <div v-else-if="rooms.length === 0" class="text-center py-8">
            <p class="text-gray-600 dark:text-gray-300">No rooms available at the moment.</p>
          </div>
          
          <div v-else class="relative">
            <!-- Room Carousel -->
            <div class="room-card-fixed" :style="maxRoomCardHeight ? `height: ${maxRoomCardHeight}px` : ''">
              <RoomCard 
                :room="rooms[currentRoomIndex]" 
                :activityIdsMap="activityIdsMap"
                class="bg-white dark:bg-gray-800"
              />
            </div>
            
            <!-- Room navigation dots -->
            <div class="flex justify-center mt-8 space-x-2">
              <button 
                v-for="(room, index) in rooms" 
                :key="index"
                @click="currentRoomIndex = index"
                class="w-3 h-3 rounded-full transition-all duration-300 focus:outline-none"
                :class="currentRoomIndex === index ? 'bg-primary dark:bg-[#9ACBD0]' : 'bg-gray-300 dark:bg-gray-500 hover:bg-gray-400 dark:hover:bg-gray-400'"
                :aria-label="`View ${room.name}`"
              ></button>
            </div>
            
            <!-- Carousel Controls -->
            <button 
              @click="prevRoom" 
              class="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-5 bg-primary hover:bg-primary-dark w-12 h-12 rounded-full flex items-center justify-center text-white focus:outline-none z-10"
              aria-label="Previous room"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
              </svg>
            </button>
            <button 
              @click="nextRoom" 
              class="absolute right-0 top-1/2 -translate-y-1/2 translate-x-5 bg-primary hover:bg-primary-dark w-12 h-12 rounded-full flex items-center justify-center text-white focus:outline-none z-10"
              aria-label="Next room"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </div>
        </div>
      </section>

      <!-- Our Areas -->
      <section class="py-16 dark:bg-gray-800" id="areas">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <h2 class="text-4xl font-bold text-primary dark:text-[#9ACBD0] text-center mb-12">Serendipity Yoga Center - Areas</h2>
          
          <div v-if="areasLoading" class="text-center py-8">
            <p class="text-gray-600 dark:text-gray-300">Loading facilities...</p>
          </div>
          
          <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
            <!-- Display areas from database -->
            <div v-for="area in areas" :key="area.id" class="flex flex-col">
              <div class="rounded-xl shadow-lg dark:shadow-gray-900/70 overflow-hidden h-64 mb-4">
                <img 
                  :src="area.image" 
                  alt="" 
                  class="w-full h-full object-cover" 
                  loading="lazy"
                  @error="handleImageError($event, getDefaultImageForArea(area.title))"
                />  <!-- Alt text is empty because it's decorative only -->
              </div>
              <h3 class="text-xl font-bold text-primary dark:text-[#9ACBD0] mb-2">{{ area.title }}</h3>
              <p class="text-gray-700 dark:text-gray-300">{{ area.description || getDefaultDescription(area.title) }}</p>
            </div>
          </div>
        </div>
      </section>
    </main>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick, watch } from 'vue'
import NavBar, { selectedLang } from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'
import RoomCard from '~/components/misc/RoomCard.vue'
import { API_URL } from '../utils/api'

// Define languages locally
const languages = [
  { code: 'en', name: 'English', flag: '🇬🇧' },
  { code: 'it', name: 'Italiano', flag: '🇮🇹' },
  { code: 'fr', name: 'Français', flag: '🇫🇷' },
  { code: 'de', name: 'Deutsch', flag: '🇩🇪' },
  { code: 'zh', name: '中文', flag: '🇨🇳' }
];

// Room data
const rooms = ref([]);
const isLoadingRooms = ref(true);
const currentRoomIndex = ref(0);
const maxRoomCardHeight = ref(0);
const errorRooms = ref(null);

// Areas data
const areas = ref([]);
const areasLoading = ref(true);

// Map to store activity names to their IDs
const activityIdsMap = ref({});

// Reviews data
const reviews = ref([]);
const isLoadingReviews = ref(true);
const errorReviews = ref(null);

// Funzione per recuperare le recensioni
const fetchReviews = async () => {
  isLoadingReviews.value = true;
  errorReviews.value = null;
  try {
    const response = await fetch(`${API_URL}/reviews?lang=${selectedLang.value}`);
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    const data = await response.json();
    if (data.reviews && data.reviews.length > 0) {
      reviews.value = data.reviews;
    } else {
      errorReviews.value = 'No reviews found';
    }
  } catch (err) {
    errorReviews.value = 'Failed to load reviews';
  } finally {
    isLoadingReviews.value = false;
  }
};

// Funzione per aggiornare l'altezza massima delle card delle stanze
const updateMaxRoomCardHeight = async () => {
  // Attendiamo che il DOM si aggiorni dopo il cambio di room
  await nextTick();
  
  // Troviamo tutte le room cards
  const roomCards = document.querySelectorAll('.room-card');
  
  // Se non ci sono cards, non c'è nulla da fare
  if (roomCards.length === 0) return;
  
  // Troviamo l'altezza massima tra tutte le cards
  let maxHeight = 0;
  roomCards.forEach(card => {
    const height = card.offsetHeight;
    if (height > maxHeight) {
      maxHeight = height;
    }
  });
  
  // Impostiamo l'altezza massima nel ref
  maxHeight += 40; // Aggiungiamo un po' di spazio per sicurezza
  maxRoomCardHeight.value = maxHeight;
};

// Funzione per recuperare le stanze
const fetchRooms = async () => {
  isLoadingRooms.value = true;
  errorRooms.value = null;
  try {
    const response = await fetch(`${API_URL}/rooms?lang=${selectedLang.value}`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    const data = await response.json();
    
    if (data.error) {
      console.error('API Error:', data.error);
      errorRooms.value = data.error;
    }
    else if (data.rooms && data.rooms.length > 0) {
      rooms.value = data.rooms.map(room => {
        // Process room data if needed
        return {
          ...room,
          // Any additional transformations
        };
      });
      
      // Reset current index to 0 when rooms are fetched
      currentRoomIndex.value = 0;
    } else {
      console.log('No rooms found');
      rooms.value = [];
      errorRooms.value = 'No rooms found';
    }
  } catch (err) {
    console.error('Error fetching rooms:', err);
    errorRooms.value = err.message;
  } finally {
    isLoadingRooms.value = false;
    if (rooms.value.length > 0) {
      updateMaxRoomCardHeight();
    }
  }
};

// Aggiorna l'altezza anche quando cambi stanza
watch(currentRoomIndex, () => {
  updateMaxRoomCardHeight();
});

// Usa selectedLang globale per fetchRooms e fetchReviews
watch(selectedLang, fetchRooms);
watch(selectedLang, fetchReviews);

function nextRoom() {
  if (currentRoomIndex.value < rooms.value.length - 1) {
    currentRoomIndex.value++;
  } else {
    currentRoomIndex.value = 0;
  }
}

function prevRoom() {
  if (currentRoomIndex.value > 0) {
    currentRoomIndex.value--;
  } else {
    currentRoomIndex.value = rooms.value.length - 1;
  }
}

onMounted(() => {
  fetchRooms();
  fetchReviews();
  
  // Fetch areas
  areasLoading.value = true;
  fetch(`${API_URL}/areas`)
    .then(response => response.json())
    .then(data => {
      if (data.areas) {
        areas.value = data.areas;
      }
    })
    .catch(error => {
      console.error('Error fetching areas:', error);
      // In case of error, use default areas
      areas.value = getDefaultAreas();
    })
    .finally(() => {
      areasLoading.value = false;
    });
});

// SEO metadata for this page
useSeoMeta({
  title: 'Our Center - Serendipity Yoga',
  description: 'Explore our serene and spacious center designed to provide a comfortable and inspiring environment for your yoga practice.',
});

// Default areas per quando l'API fallisce
function getDefaultAreas() {
  return [
    {
      id: 1,
      title: 'Bar',
      image: 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/bar.jpg',
      description: getDefaultDescription('bar')
    },
    {
      id: 2,
      title: 'Play Area',
      image: 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/play_area.jpg',
      description: getDefaultDescription('play area')
    },
    {
      id: 3,
      title: 'SPA',
      image: 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/spa.jpg',
      description: getDefaultDescription('spa')
    }
  ];
}

// Oriental Room image for main section
const orientalRoomImage = computed(() => {
  if (rooms.value.length === 0) {
    return '/images/meditation.jpg'; // Fallback image if no rooms are available
  }
  const orientalRoom = rooms.value.find(room => room.name && room.name.toLowerCase().includes('oriental'));
  return orientalRoom ? orientalRoom.image : rooms.value[0].image;
});

// Get area image by title
function getAreaImage(title) {
  // Find the area case-insensitively
  const area = areas.value.find(a => a.title.toLowerCase() === title.toLowerCase());
  
  if (area && area.image) {
    return area.image;
  }
  
  // Fallback images if not found in database
  const fallbackImages = {
    'bar': 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/bar.jpg',
    'play area': 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/play_area.jpg',
    'spa': 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/spa.jpg'
  };
  
  return fallbackImages[title.toLowerCase()];
}

// Handle image loading errors
function handleImageError(event, fallbackSrc) {
  event.target.src = fallbackSrc;
}

// Default descriptions for areas
function getDefaultDescription(areaTitle) {
  const descriptions = {
    'bar': 'Our elegant bar serves fresh juices, smoothies, and healthy snacks. The perfect place to recharge after your yoga session or socialize with fellow practitioners in a peaceful atmosphere.',
    'play area': 'A colorful and safe space where children can play while parents practice yoga. Equipped with toys and games, supervised by trained staff, allowing you to focus on your practice with peace of mind.',
    'spa': 'Indulge in our tranquil spa offering massage therapy, aromatherapy, and relaxation treatments that complement your yoga practice. The perfect way to enhance your wellness journey and promote deeper healing.'
  };
  
  return descriptions[areaTitle.toLowerCase()] || 'Experience the transformative power of our specially designed spaces.';
}

// Get default image for an area based on title
function getDefaultImageForArea(title) {
  const fallbackImages = {
    'bar': 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/bar.jpg',
    'play area': 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/play_area.jpg',
    'spa': 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/spa.jpg'
  };
  
  const key = title.toLowerCase();
  return fallbackImages[key] || 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/default-area.jpg';
}

// Navigate to a specific activity
async function navigateToActivity(activityName) {
  try {
    // If we already have the ID in our mapping, use it
    if (activityIdsMap.value[activityName]) {
      const id = activityIdsMap.value[activityName];
      window.location.href = `/singleactivity?id=${id}`;
      return;
    }
    
    // Otherwise, fetch it from the backend
    const response = await fetch(`${API_URL}/activity_id_from_name?name=${encodeURIComponent(activityName)}`);
    if (response.ok) {
      const data = await response.json();
      if (data.id) {
        // Store the ID in our map for future use
        activityIdsMap.value[activityName] = data.id;
        
        // Navigate to the activity page
        window.location.href = `/singleactivity?id=${data.id}`;
      } else {
        console.error('Could not find activity ID for:', activityName);
        // Fallback to activities page
        window.location.href = '/activities';
      }
    } else {
      console.error('Error fetching activity ID:', response.statusText);
      window.location.href = '/activities';
    }
  } catch (error) {
    console.error('Error navigating to activity:', error);
    window.location.href = '/activities';
  }
}
</script>

<style scoped>
.text-primary {
  color: #006A71;
}

:root.dark .text-primary {
  color: #9ACBD0;
}

.bg-primary {
  background-color: #006A71;
}

.bg-primary-light {
  background-color: #e0f2f3;
}

.bg-primary-dark {
  background-color: #00585d;
}

.bg-beige {
  background-color: #F2EFE7;
}

.dark .bg-beige {
  background-color: #374151; /* gray-700 */
}

.bg-secondary {
  background-color: #F2EFE7;
}

.prose img {
  margin-top: 1.5rem;
  margin-bottom: 1.5rem;
}

/* Dark mode transition */
.dark-transition {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
</style> 