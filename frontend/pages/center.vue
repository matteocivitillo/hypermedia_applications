<template>
  <div class="flex flex-col min-h-screen">
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
      <section class="bg-beige py-20">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <div class="flex flex-wrap justify-center gap-12">
            <div class="bg-white p-8 rounded-xl shadow-lg max-w-sm">
              <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-800 mb-2">Mindful Practice</h3>
              <p class="text-gray-600">Experience transformative yoga sessions guided by expert instructors.</p>
            </div>
            
            <div class="bg-white p-8 rounded-xl shadow-lg max-w-sm">
              <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-800 mb-2">Community</h3>
              <p class="text-gray-600">Join a welcoming community of like-minded individuals.</p>
            </div>
            
            <div class="bg-white p-8 rounded-xl shadow-lg max-w-sm">
              <div class="w-12 h-12 bg-primary rounded-full flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-800 mb-2">Holistic Approach</h3>
              <p class="text-gray-600">Balance body, mind, and spirit through our comprehensive programs.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- About the Center -->
      <section class="py-16 bg-white">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <h2 class="text-4xl font-bold text-primary text-center mb-8">Serendipity Yoga Center</h2>
          <div class="flex flex-wrap md:flex-nowrap gap-16 items-center">
            <div class="w-full md:w-1/2">
              <div class="prose prose-lg max-w-none">
                <p class="mb-4">At Serendipity Yoga Center, we believe true wellness begins with daily choices.</p>
                <p class="mb-4">Our holistic approach blends dynamic yoga, meditation, and rejuvenating activities to guide your full transformation: a stronger body, a clearer mind, a lighter spirit.</p>
                <p class="mb-4">From energizing classes to immersive retreats, sunset yoga socials to spa relaxation, every experience is a step toward your best self.</p>
                <p class="mb-4">Because lifestyle change isn't about revolution, but conscious evolution.</p>
                <p class="font-medium">Start your journey today.</p>
              </div>
            </div>
            <div class="w-full md:w-1/2">
              <img 
                :src="orientalRoomImage" 
                alt="" 
                class="w-full h-auto rounded-3xl shadow-lg object-cover h-96" 
                loading="lazy"
              />  <!-- Alt text is empty because it's decorative only -->
            </div>
          </div>
        </div>
      </section>

      <!-- Our Rooms -->
      <section class="bg-beige py-16" id="rooms">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <h2 class="text-4xl font-bold text-primary text-center mb-12">Our Yoga Rooms</h2>
          
          <div v-if="isLoading" class="text-center py-8">
            <p class="text-gray-600">Loading rooms...</p>
          </div>
          
          <div v-else-if="rooms.length === 0" class="text-center py-8">
            <p class="text-gray-600">No rooms available at the moment.</p>
          </div>
          
          <div v-else class="relative">
            <!-- Room Carousel -->
            <div class="bg-white p-6 md:p-8 rounded-xl shadow-lg flex flex-wrap md:flex-nowrap gap-16 room-card-fixed" :style="maxRoomCardHeight ? `height: ${maxRoomCardHeight}px` : ''">
              <div class="w-full md:w-1/2 flex items-center justify-center">
                <div class="h-96 w-full rounded-lg overflow-hidden">
                  <img 
                    :src="rooms[currentRoomIndex].image" 
                    alt="" 
                    class="w-full h-full object-cover" 
                    loading="lazy"
                  />  <!-- Alt text is empty because it's decorative only -->
                </div>
              </div>
              <div class="w-full md:w-1/2 flex flex-col justify-center">
                <h3 class="text-2xl font-bold text-primary mb-4">{{ rooms[currentRoomIndex].name }}</h3>
                
                <!-- Description Paragraph -->
                <div class="prose prose-lg mb-6">
                  <p>{{ rooms[currentRoomIndex].description }}</p>
                </div>
                
                <!-- Features Paragraph -->
                <div v-if="rooms[currentRoomIndex].features && rooms[currentRoomIndex].features.length > 0" class="mb-6">
                  <h4 class="text-lg font-semibold text-primary mb-2">Features:</h4>
                  <ul class="list-disc pl-5 space-y-1">
                    <li v-for="feature in rooms[currentRoomIndex].features" :key="feature" class="text-gray-700">
                      {{ feature }}
                    </li>
                  </ul>
                </div>
                
                <!-- Activities Paragraph -->
                <div v-if="rooms[currentRoomIndex].activities && rooms[currentRoomIndex].activities.length > 0" class="mb-6">
                  <h4 class="text-lg font-semibold text-primary mb-2">Activities:</h4>
                  <div class="flex flex-wrap gap-2">
                    <nuxt-link 
                      v-for="activity in rooms[currentRoomIndex].activities" 
                      :key="activity"
                      :to="`/singleactivity?id=${activityIdsMap[activity] || ''}`"
                      class="inline-flex items-center px-3 py-1 rounded-full bg-primary-light text-primary hover:bg-primary hover:text-white transition-colors"
                      @click.prevent="navigateToActivity(activity)"
                    >
                      {{ activity }}
                    </nuxt-link>
                  </div>
                </div>
                
                <!-- Quote -->
                <div v-if="rooms[currentRoomIndex].quote" class="italic text-gray-600 mt-4">
                  "{{ rooms[currentRoomIndex].quote }}"
                </div>
              </div>
            </div>
            
            <!-- Room navigation dots -->
            <div class="flex justify-center mt-8 space-x-2">
              <button 
                v-for="(room, index) in rooms" 
                :key="index"
                @click="currentRoomIndex = index"
                class="w-3 h-3 rounded-full transition-all duration-300 focus:outline-none"
                :class="currentRoomIndex === index ? 'bg-primary' : 'bg-gray-300 hover:bg-gray-400'"
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
      <section class="py-16" id="areas">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <h2 class="text-4xl font-bold text-primary text-center mb-12">Serendipity Yoga Center - Areas</h2>
          
          <div v-if="areasLoading" class="text-center py-8">
            <p class="text-gray-600">Loading facilities...</p>
          </div>
          
          <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
            <!-- Display areas from database -->
            <div v-for="area in areas" :key="area.id" class="flex flex-col">
              <div class="rounded-xl shadow-lg overflow-hidden h-64 mb-4">
                <img 
                  :src="area.image" 
                  alt="" 
                  class="w-full h-full object-cover" 
                  loading="lazy"
                  @error="handleImageError($event, getDefaultImageForArea(area.title))"
                />  <!-- Alt text is empty because it's decorative only -->
              </div>
              <h3 class="text-xl font-bold text-primary mb-2">{{ area.title }}</h3>
              <p class="text-gray-700">{{ area.description || getDefaultDescription(area.title) }}</p>
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
import NavBar from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'

// Room data
const rooms = ref([]);
const isLoading = ref(true);
const currentRoomIndex = ref(0);
const maxRoomCardHeight = ref(0);

// Areas data
const areas = ref([]);
const areasLoading = ref(true);

// Map to store activity names to their IDs
const activityIdsMap = ref({});

// Default room data in case the API call fails
const defaultRooms = [
  {
    id: 1,
    name: 'Oriental Room',
    image: '/images/meditation.jpg',
    description: 'A serene haven infused with Eastern tranquility. Practice amidst elegant Asian-inspired decor, where harmony flows through every detail.',
    features: [
      'Warm teak floors & silk drapery',
      'Soft lantern lighting & incense scents',
      'Traditional singing bowls & chimes'
    ],
    activities: [
      'Kundalini & Hatha yoga'
    ],
    quote: 'Where ancient wisdom meets mindful movement.'
  },
  {
    id: 2,
    name: 'Forest Room',
    image: '/images/water-yoga.jpg',
    description: 'Experience the rejuvenating energy of nature in our forest-inspired practice space. Surrounded by natural elements and botanical accents.',
    features: [
      'Natural wood elements & living plant wall',
      'Ambient nature sounds & essential oil diffusers',
      'Adjustable daylight-simulating lighting'
    ],
    activities: [
      'Ashtanga yoga & Nature meditation',
      'Dynamic flow sequences'
    ],
    quote: 'Connect with nature\'s rhythm and find your inner strength.'
  },
  {
    id: 3,
    name: 'Zen Studio',
    image: '/images/aerial-yoga.jpg',
    description: 'A minimalist sanctuary designed for focus and clarity. Our Zen studio offers a distraction-free environment for deep practice.',
    features: [
      'Bamboo flooring & Japanese shoji screens',
      'Neutral color palette & natural light',
      'Meditation cushions & props'
    ],
    activities: [
      'Meditation & Mindfulness practices',
      'Gentle yoga & Breathing workshops'
    ],
    quote: 'Simplicity is the ultimate sophistication for the mindful practitioner.'
  }
];

// Dopo aver caricato le stanze, calcola l'altezza massima delle card
async function updateMaxRoomCardHeight() {
  await nextTick();
  const cards = document.querySelectorAll('.room-card-fixed');
  let maxHeight = 0;
  cards.forEach(card => {
    maxHeight = Math.max(maxHeight, card.offsetHeight);
  });
  maxRoomCardHeight.value = maxHeight;
}

// Modifica fetchRooms per aggiornare l'altezza dopo il caricamento
async function fetchRooms() {
  try {
    isLoading.value = true;
    const response = await fetch('http://localhost:8000/rooms');
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    if (data.rooms && data.rooms.length > 0) {
      let roomsData = data.rooms.map(room => ({
        id: room.id,
        name: room.title || 'Yoga Room',
        image: room.image || `/images/default-room.jpg`,
        description: room.description || 'Experience the tranquility of our specially designed yoga spaces.',
        features: room.features || [],
        activities: room.activities || [],
        quote: room.quote || 'Experience the transformative power of our specially designed spaces.'
      }));
      rooms.value = roomsData.reverse();
    } else {
      rooms.value = defaultRooms.slice().reverse();
    }
  } catch (error) {
    rooms.value = defaultRooms.slice().reverse();
  } finally {
    isLoading.value = false;
    updateMaxRoomCardHeight();
  }
}

// Aggiorna l'altezza anche quando cambi stanza
watch(currentRoomIndex, () => {
  updateMaxRoomCardHeight();
});

function nextRoom() {
  if (rooms.value.length === 0) return;
  currentRoomIndex.value = (currentRoomIndex.value + 1) % rooms.value.length;
}

function prevRoom() {
  if (rooms.value.length === 0) return;
  currentRoomIndex.value = (currentRoomIndex.value - 1 + rooms.value.length) % rooms.value.length;
}

// Fetch rooms and activities when component is mounted
onMounted(async () => {
  await fetchRooms();
  fetchAreas();
  
  // Fetch all activities to build the name-to-id mapping
  try {
    const response = await fetch('http://localhost:8000/activities');
    if (response.ok) {
      const data = await response.json();
      if (data.activities && data.activities.length > 0) {
        // Build a map from activity names to IDs
        const mapping = {};
        data.activities.forEach(activity => {
          mapping[activity.title] = activity.id;
          
          // Add aliases for common variations
          if (activity.title === 'Mindfulness Meditation') {
            mapping['Meditation'] = activity.id;
            mapping['Mindfulness'] = activity.id;
          } else if (activity.title === 'Mindful Pottery') {
            mapping['Mindful Potter'] = activity.id;
          } else if (activity.title === 'Wellness Workshop') {
            mapping['Wellness Workshops'] = activity.id;
          } else if (activity.title === 'Kundalini Yoga') {
            mapping['Kundalini & Hatha yoga'] = activity.id;
          } else if (activity.title === 'Ashtanga Yoga') {
            mapping['Ashtanga yoga'] = activity.id;
          }
        });
        
        activityIdsMap.value = mapping;
        console.log('Activity ID mapping created:', activityIdsMap.value);
      }
    }
  } catch (error) {
    console.error('Error fetching activities for ID mapping:', error);
  }
});

// Fetch areas data from API
async function fetchAreas() {
  try {
    areasLoading.value = true;
    console.log('Fetching areas from API...');
    const response = await fetch('http://localhost:8000/areas');
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    const data = await response.json();
    console.log('Areas data received:', data);
    
    if (data.areas && data.areas.length > 0) {
      // Store the areas data directly
      areas.value = data.areas;
      console.log('Successfully loaded areas from server:', areas.value);
    } else {
      console.error('No areas found in API response or areas array is empty');
      setupDefaultAreas();
    }
  } catch (error) {
    console.error('Error fetching areas:', error);
    setupDefaultAreas();
  } finally {
    areasLoading.value = false;
  }
}

// Setup default areas as fallback
function setupDefaultAreas() {
  console.log('Setting up default areas');
  areas.value = [
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

// Get area image by title
function getAreaImage(title) {
  console.log(`Getting image for area: ${title}`);
  console.log('Current areas:', areas.value);
  
  // Find the area case-insensitively
  const area = areas.value.find(a => a.title.toLowerCase() === title.toLowerCase());
  
  if (area && area.image) {
    console.log(`Found image for ${title}:`, area.image);
    return area.image;
  }
  
  console.log(`No image found for ${title}, using fallback`);
  
  // Fallback images if not found in database
  const fallbackImages = {
    'bar': 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/bar.jpg',
    'play area': 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/play_area.jpg',
    'spa': 'https://dcrgvkmnnavjahkprnkem.supabase.co/storage/v1/object/public/yoga/spa.jpg'
  };
  
  return fallbackImages[title.toLowerCase()];
}

// Get area description by title
function getAreaDescription(title) {
  // Find the area case-insensitively
  const area = areas.value.find(a => a.title.toLowerCase() === title.toLowerCase());
  
  if (area && area.description) {
    return area.description;
  }
  return getDefaultDescription(title);
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

// Oriental Room image for main section
const orientalRoomImage = computed(() => {
  const orientalRoom = rooms.value.find(room => room.name === 'Oriental Room');
  return orientalRoom ? orientalRoom.image : '/images/meditation.jpg';
});

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
    const response = await fetch(`http://localhost:8000/activity_id_from_name?name=${encodeURIComponent(activityName)}`);
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

 // SEO metadata for this page
 useSeoMeta({
    title: 'Our Center - Serendipity Yoga',
    description: 'Explore our serene and spacious center designed to provide a comfortable and inspiring environment for your yoga practice.',
  })
</script>

<style scoped>
.text-primary {
  color: #006A71;
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

.bg-secondary {
  background-color: #F2EFE7;
}

.prose img {
  margin-top: 1.5rem;
  margin-bottom: 1.5rem;
}
</style> 