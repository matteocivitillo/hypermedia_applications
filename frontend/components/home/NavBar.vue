<template>
  <nav class="bg-primary navbar border-b-0 sticky top-0 z-50 transition-colors duration-300">
    <div class="container mx-auto px-6 md:px-16 lg:px-24 xl:px-32">
      <div class="flex items-center justify-between h-20">
        <!-- Logo Left, always same size -->
        <div class="flex items-center -ml-12">
          <a href="/" class="flex items-center">
            <img src="/images/logo-small.svg" alt="Serendipity yoga" style="height: 48px; width: auto;" class="flex-shrink-0" />  <!-- The word "logo" is usually not an important part of the image's content or function.-->
          </a>
        </div>

        <!-- Hamburger Menu Button (visibile quando lo spazio non è sufficiente) -->
        <div class="lg:hidden flex items-center">
          <ThemeToggle class="mr-2" />
          <LanguageSelector v-model="selectedLang" :languages="languages" />
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="text-white focus:outline-none p-1 rounded-lg hamburger-btn ml-2">
            <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>

        <!-- Navigation Items Desktop - nascosti quando lo spazio non è sufficiente -->
        <div class="hidden lg:flex items-center space-x-8 xl:space-x-10">
          <router-link to="/" 
            class="text-white text-base font-medium hover:text-gray-300 transition-colors"
            :class="{ 'border-b-2 border-white pb-1': isActive('/') }">
            {{ t('home') }}
          </router-link>
          
          <!-- The Center Dropdown -->
          <div class="dropdown-wrapper">
            <div class="dropdown-container" 
               @mouseenter="openDropdown" 
               @mouseleave="closeDropdownWithDelay">
              <a href="#" 
                @click.prevent="goToCenter"
                class="text-white text-base font-medium hover:text-gray-300 transition-colors flex items-center"
                :class="{ 'border-b-2 border-white pb-1': isActive('/center') || isActive('/rooms') || isActive('/areas') }">
                {{ t('theCenter') }}
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </a>
              <div v-show="dropdownOpen" 
                  class="dropdown-menu">
                <div class="py-2 px-4">
                  <a href="#" 
                     @click.prevent="goToCenter"
                     class="block py-3 text-sm text-gray-700 hover:bg-gray-100 rounded px-2 -mx-2 dark:text-gray-200 dark:hover:bg-gray-700">
                    {{ t('ourPhilosophy') }}
                  </a>
                  <a href="#" 
                     @click.prevent="goToRooms"
                     class="block py-3 text-sm text-gray-700 hover:bg-gray-100 rounded px-2 -mx-2 dark:text-gray-200 dark:hover:bg-gray-700">
                    {{ t('rooms') }}
                  </a>
                  <a href="#" 
                     @click.prevent="goToAreas"
                     class="block py-3 text-sm text-gray-700 hover:bg-gray-100 rounded px-2 -mx-2 dark:text-gray-200 dark:hover:bg-gray-700">
                    {{ t('areas') }}
                  </a>
                </div>
              </div>
            </div>
          </div>
          
          <router-link to="/activities" 
            class="text-white text-base font-medium hover:text-gray-300 transition-colors"
            :class="{ 'border-b-2 border-white pb-1': isActive('/activities') }">
            {{ t('activities') }}
          </router-link>
          
          <a href="#" 
             @click.prevent="goToHighlights"
             class="text-white text-base font-medium hover:text-gray-300 transition-colors"
             :class="{ 'border-b-2 border-white pb-1': isActive('/highlights') }">
            {{ t('highlights') }}
          </a>
          
          <router-link to="/teachers" 
            class="text-white text-base font-medium hover:text-gray-300 transition-colors"
            :class="{ 'border-b-2 border-white pb-1': isActive('/teachers') }">
            {{ t('teachers') }}
          </router-link>
          
          <router-link to="/prices" 
            class="text-white text-base font-medium hover:text-gray-300 transition-colors"
            :class="{ 'border-b-2 border-white pb-1': isActive('/prices') }">
            {{ t('prices') }}
          </router-link>
          
          <router-link to="/contact" 
            class="text-white text-base font-medium hover:text-gray-300 transition-colors"
            :class="{ 'border-b-2 border-white pb-1': isActive('/contact') }">
            {{ t('contact') }}
          </router-link>
          
          <div class="flex items-center space-x-2">
            <ThemeToggle />
            <LanguageSelector v-model="selectedLang" :languages="languages" />
          </div>
        </div>
      </div>
    </div>

    <!-- Mobile Menu (visibile quando aperto) -->
    <div v-show="mobileMenuOpen" class="lg:hidden bg-primary border-t border-gray-200 dark:border-gray-700">
      <div class="container mx-auto px-6 py-4">
        <router-link to="/" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-[#9ACBD0] rounded-lg px-4 text-primary': isActive('/') }"
          @click="mobileMenuOpen = false">
          {{ t('home') }}
        </router-link>
        
        <!-- Mobile Dropdown -->
        <div class="relative">
          <button @click="mobileCenterOpen = !mobileCenterOpen"
                class="w-full text-left py-3 text-white text-base font-medium hover:text-gray-300 focus:outline-none flex justify-between items-center"
                :class="{ 'bg-[#9ACBD0] rounded-lg px-4 text-primary': isActive('/center') }">
            <span>{{ t('theCenter') }}</span>
            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div v-show="mobileCenterOpen" class="pl-4 border-l-2 border-[#9ACBD0] ml-2 mt-2 mb-2 rounded-r-lg bg-[#006A7115] dark:bg-white/5">
            <a href="#" 
              @click.prevent="goToCenter(); mobileMenuOpen = false"
              class="block py-3 text-white text-base font-medium hover:bg-[#9ACBD0] hover:text-primary rounded-lg px-4 my-1 transition-colors">
              {{ t('ourPhilosophy') }}
            </a>
            <a href="#" 
              @click.prevent="goToRooms(); mobileMenuOpen = false"
              class="block py-3 text-white text-base font-medium hover:bg-[#9ACBD0] hover:text-primary rounded-lg px-4 my-1 transition-colors">
              {{ t('rooms') }}
            </a>
            <a href="#" 
              @click.prevent="goToAreas(); mobileMenuOpen = false"
              class="block py-3 text-white text-base font-medium hover:bg-[#9ACBD0] hover:text-primary rounded-lg px-4 my-1 transition-colors">
              {{ t('areas') }}
            </a>
          </div>
        </div>
        
        <router-link to="/activities" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-[#9ACBD0] rounded-lg px-4 text-primary': isActive('/activities') }"
          @click="mobileMenuOpen = false">
          {{ t('activities') }}
        </router-link>
        
        <a href="#" 
          @click.prevent="goToHighlights(); mobileMenuOpen = false"
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-[#9ACBD0] rounded-lg px-4 text-primary': isActive('/highlights') }">
          {{ t('highlights') }}
        </a>
        
        <router-link to="/teachers" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-[#9ACBD0] rounded-lg px-4 text-primary': isActive('/teachers') }"
          @click="mobileMenuOpen = false">
          {{ t('teachers') }}
        </router-link>
        
        <router-link to="/prices" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-[#9ACBD0] rounded-lg px-4 text-primary': isActive('/prices') }"
          @click="mobileMenuOpen = false">
          {{ t('prices') }}
        </router-link>
        
        <router-link to="/contact" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-[#9ACBD0] rounded-lg px-4 text-primary': isActive('/contact') }"
          @click="mobileMenuOpen = false">
          {{ t('contact') }}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import ThemeToggle from './ThemeToggle.vue'
import LanguageSelector from './LanguageSelector.vue'
import { ref, watch } from 'vue'

const languages = [
  { code: 'en', name: 'English', flag: 'https://dcrgvkmnavjahkprnkem.supabase.co/storage/v1/object/sign/flags/gb.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzI0MmJkN2U5LTVjNTQtNGViYy1iYmQwLWZhZGJjMjQ0NDMyOSJ9.eyJ1cmwiOiJmbGFncy9nYi5wbmciLCJpYXQiOjE3NDcxNDI5MDEsImV4cCI6MTkwNDgyMjkwMX0.gI5MGHW6Ol-B5QM_oBwC_ijHR6dLUDZZC1vXjH5pmsE' },
  { code: 'it', name: 'Italiano', flag: 'https://dcrgvkmnavjahkprnkem.supabase.co/storage/v1/object/sign/flags/ita.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzI0MmJkN2U5LTVjNTQtNGViYy1iYmQwLWZhZGJjMjQ0NDMyOSJ9.eyJ1cmwiOiJmbGFncy9pdGEucG5nIiwiaWF0IjoxNzQ3MTQyODEwLCJleHAiOjE5MDQ4MjI4MTB9.gGqlPw-_1auGlQayER_AzOjv46aMwJh3Y1myQMW_P00' },
  { code: 'fr', name: 'Français', flag: 'https://dcrgvkmnavjahkprnkem.supabase.co/storage/v1/object/sign/flags/francia.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzI0MmJkN2U5LTVjNTQtNGViYy1iYmQwLWZhZGJjMjQ0NDMyOSJ9.eyJ1cmwiOiJmbGFncy9mcmFuY2lhLnBuZyIsImlhdCI6MTc0NzE0MjkyMCwiZXhwIjoxOTA0ODIyOTIwfQ.PuOYAY3xRUPlf6BytlmM1OBQnB4nBYnnirVBAHrYOCw' },
  { code: 'de', name: 'Deutsch', flag: 'https://dcrgvkmnavjahkprnkem.supabase.co/storage/v1/object/sign/flags/germania.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzI0MmJkN2U5LTVjNTQtNGViYy1iYmQwLWZhZGJjMjQ0NDMyOSJ9.eyJ1cmwiOiJmbGFncy9nZXJtYW5pYS5wbmciLCJpYXQiOjE3NDcxNDI4ODAsImV4cCI6MTkwNDgyMjg4MH0.bz5-eZHqvrAVWLtSeMBWEPmxSoHksxQdCJ6uRBSyIH0' },
  { code: 'zh', name: '中文', flag: 'https://dcrgvkmnavjahkprnkem.supabase.co/storage/v1/object/sign/flags/cina.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InN0b3JhZ2UtdXJsLXNpZ25pbmcta2V5XzI0MmJkN2U5LTVjNTQtNGViYy1iYmQwLWZhZGJjMjQ0NDMyOSJ9.eyJ1cmwiOiJmbGFncy9jaW5hLnBuZyIsImlhdCI6MTc0NzE0MjkzOCwiZXhwIjoxOTA0ODIyOTM4fQ.5D8Z3NPE1X3voQeks9DNx3t9xsUxkR-AJCmFbL8OjuI' }
];

// Stato globale della lingua selezionata con valore di default
export const selectedLang = ref('en')

// Traduzioni per la navbar
const translations = {
  en: {
    home: 'Home',
    theCenter: 'The Center',
    ourPhilosophy: 'Our Philosophy',
    rooms: 'Rooms',
    areas: 'Areas',
    activities: 'Activities',
    highlights: 'Highlights',
    teachers: 'Teachers',
    prices: 'Prices',
    contact: 'Contact'
  },
  it: {
    home: 'Home',
    theCenter: 'Il Centro',
    ourPhilosophy: 'La Nostra Filosofia',
    rooms: 'Sale',
    areas: 'Aree',
    activities: 'Attività',
    highlights: 'In Evidenza',
    teachers: 'Insegnanti',
    prices: 'Prezzi',
    contact: 'Contatti'
  },
  fr: {
    home: 'Accueil',
    theCenter: 'Le Centre',
    ourPhilosophy: 'Notre Philosophie',
    rooms: 'Salles',
    areas: 'Espaces',
    activities: 'Activités',
    highlights: 'À la Une',
    teachers: 'Professeurs',
    prices: 'Tarifs',
    contact: 'Contact'
  },
  de: {
    home: 'Startseite',
    theCenter: 'Das Zentrum',
    ourPhilosophy: 'Unsere Philosophie',
    rooms: 'Räume',
    areas: 'Bereiche',
    activities: 'Aktivitäten',
    highlights: 'Highlights',
    teachers: 'Lehrer',
    prices: 'Preise',
    contact: 'Kontakt'
  },
  zh: {
    home: '首页',
    theCenter: '中心',
    ourPhilosophy: '我们的理念',
    rooms: '房间',
    areas: '区域',
    activities: '活动',
    highlights: '精选',
    teachers: '教师',
    prices: '价格',
    contact: '联系我们'
  }
};

// Funzione per ottenere traduzioni
const t = (key) => {
  const lang = selectedLang.value;
  return translations[lang]?.[key] || translations.en[key];
};

// La parte di localStorage verrà gestita nel ciclo di vita del componente

export default {
  components: {
    ThemeToggle,
    LanguageSelector
  },
  data() {
    return {
      dropdownOpen: false,
      dropdownTimer: null,
      mobileMenuOpen: false,
      mobileCenterOpen: false,
      languages,
      selectedLang
    }
  },
  methods: {
    t,
    isActive(route) {
      return this.$route && this.$route.path === route;
    },
    openDropdown() {
      if (this.dropdownTimer) {
        clearTimeout(this.dropdownTimer);
        this.dropdownTimer = null;
      }
      this.dropdownOpen = true;
    },
    closeDropdown() {
      this.dropdownOpen = false;
    },
    closeDropdownWithDelay() {
      // Add a delay before closing to prevent accidental closures
      this.dropdownTimer = setTimeout(() => {
        this.dropdownOpen = false;
      }, 200);
    },
    goToCenter() {
      // Close the dropdown
      this.closeDropdown();
      
      // Navigate to center page and scroll to top
      if (this.$route.path !== '/center') {
        this.$router.push('/center');
      } else {
        // Already on center page, scroll to top
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      }
    },
    goToRooms() {
      // Close the dropdown
      this.closeDropdown();
      
      // First navigate to center page if not already there
      if (this.$route.path !== '/center') {
        // Set a flag in localStorage to indicate we want to scroll to rooms after navigation
        if (typeof localStorage !== 'undefined') {
          localStorage.setItem('scrollToTarget', 'rooms');
        }
        this.$router.push('/center');
      } else {
        this.scrollToSection('rooms');
      }
    },
    goToAreas() {
      // Close the dropdown
      this.closeDropdown();
      
      // First navigate to center page if not already there
      if (this.$route.path !== '/center') {
        // Set a flag in localStorage to indicate we want to scroll to areas after navigation
        if (typeof localStorage !== 'undefined') {
          localStorage.setItem('scrollToTarget', 'areas');
        }
        this.$router.push('/center');
      } else {
        this.scrollToSection('areas');
      }
    },
    goToHighlights() {
      // Close the dropdown
      this.closeDropdown();
      
      // Navigate to home page if not already there
      if (this.$route.path !== '/') {
        // We want to scroll to the highlighted activities section
        if (typeof localStorage !== 'undefined') {
          localStorage.setItem('scrollToHighlights', 'true');
        }
        this.$router.push('/');
      } else {
        this.scrollToHighlights();
      }
    },
    scrollToSection(sectionId) {
      // Wait for DOM to update
      this.$nextTick(() => {
        const section = document.getElementById(sectionId);
        if (section) {
          // Calculate position to center the element in viewport
          const elementRect = section.getBoundingClientRect();
          const absoluteElementTop = elementRect.top + window.pageYOffset;
          const middle = absoluteElementTop - (window.innerHeight / 2) + (elementRect.height / 2);
          
          // Smooth scroll with animation
          window.scrollTo({
            top: middle,
            behavior: 'smooth'
          });
        }
      });
    },
    scrollToHighlights() {
      // Find the Highlighted Activities section
      this.$nextTick(() => {
        // Metodo 1: HighlightedActivities è la seconda section all'interno di main
        const mainElement = document.querySelector('main');
        if (mainElement) {
          const sections = mainElement.querySelectorAll(':scope > section');
          if (sections.length >= 2) {
            const highlightsSection = sections[1]; // HighlightedActivities è la seconda sezione
            if (highlightsSection) {
              // Calculate position to center the element in viewport
              const elementRect = highlightsSection.getBoundingClientRect();
              const absoluteElementTop = elementRect.top + window.pageYOffset;
              const middle = absoluteElementTop - (window.innerHeight / 2) + (elementRect.height / 2);
              
              // Smooth scroll with animation
              window.scrollTo({
                top: middle,
                behavior: 'smooth'
              });
              return; // Termina qui se abbiamo trovato e scrollato
            }
          }
        }
        
        // Metodo 2: Fallback - cerca una sezione con il componente HighlightedActivities
        // che di solito ha classi specifiche
        const highlightsSection = document.querySelector('section.py-16.bg-white') ||
                                 document.querySelector('section.py-16.dark\\:bg-gray-800');
                                 
        if (highlightsSection) {
          // Calculate position to center the element in viewport
          const elementRect = highlightsSection.getBoundingClientRect();
          const absoluteElementTop = elementRect.top + window.pageYOffset;
          const middle = absoluteElementTop - (window.innerHeight / 2) + (elementRect.height / 2);
          
          // Smooth scroll with animation
          window.scrollTo({
            top: middle,
            behavior: 'smooth'
          });
        }
      });
    }
  },
  mounted() {
    // Inizializza selectedLang con il valore da localStorage, se disponibile
    if (typeof localStorage !== 'undefined') {
      const storedLang = localStorage.getItem('language');
      if (storedLang) {
        selectedLang.value = storedLang;
      } else {
        // Se non c'è una lingua salvata, imposta inglese come default
        selectedLang.value = 'en';
        localStorage.setItem('language', 'en');
      }
    }
    
    // Check if we need to scroll to a section on page load
    if (this.$route.path === '/center' && typeof localStorage !== 'undefined') {
      // Check if we're coming from another page with the intent to scroll to a section
      const scrollTarget = localStorage.getItem('scrollToTarget');
      if (scrollTarget) {
        // Clear the flag
        localStorage.removeItem('scrollToTarget');
        
        // Add a small delay to ensure the page is fully rendered
        setTimeout(() => {
          this.scrollToSection(scrollTarget);
        }, 300);
      } else if (this.$route.hash) {
        // Handle direct hash navigation
        const sectionId = this.$route.hash.substring(1); // Remove the # character
        setTimeout(() => {
          this.scrollToSection(sectionId);
        }, 300);
      }
    } else if (this.$route.path === '/' && typeof localStorage !== 'undefined' && localStorage.getItem('scrollToHighlights') === 'true') {
      // If we're on the homepage and want to scroll to highlights
      localStorage.removeItem('scrollToHighlights');
      setTimeout(() => {
        this.scrollToHighlights();
      }, 300);
    }
    
    // Close mobile menu when route changes
    this.$watch('$route', () => {
      this.mobileMenuOpen = false;
    });
  },
  watch: {
    // Watch for route changes to handle hash navigation
    '$route'(to) {
      if (to.path === '/center' && to.hash) {
        const sectionId = to.hash.substring(1); // Remove the # character
        setTimeout(() => {
          this.scrollToSection(sectionId);
        }, 300);
      }
    },
    selectedLang(newLang) {
      if (typeof localStorage !== 'undefined') {
        localStorage.setItem('language', newLang);
      }
      this.$emit('language-changed', newLang);
    }
  }
}
</script>

<style scoped>
.dropdown-wrapper {
  position: relative;
  padding: 10px 0;
}

.dropdown-container {
  position: static;
  padding: 10px;
  margin: -10px;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  width: 200px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
  z-index: 100;
  margin-top: 5px;
  @apply dark:bg-gray-700 dark:shadow-gray-900/60;
}

/* Create a safe area to prevent gap between link and dropdown */
.dropdown-container::after {
  content: '';
  position: absolute;
  height: 20px;
  left: 0;
  right: 0;
  bottom: -20px;
}

/* Stili moderni per il menu mobile */
.lg\:hidden.bg-primary {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

/* Rimuovo hover dal pulsante hamburger ma mantengo negli altri elementi */
.hamburger-btn {
  transition: none !important;
  background-color: transparent !important;
}

.hamburger-btn:hover {
  background-color: #9ACBD0 !important;
  transform: none !important;
  padding: 0.25rem !important; /* p-1 */
}

/* Mantengo lo stile di hover per gli altri elementi del menu mobile */
.lg\:hidden a, 
.lg\:hidden button:not(.hamburger-btn) {
  margin: 4px 0;
  transition: all 0.2s ease-in-out;
  border-radius: 8px;
}

.lg\:hidden a:hover, 
.lg\:hidden button:not(.hamburger-btn):hover {
  background-color: #9ACBD0;
  color: #006A71;
  padding-left: 16px;
}

/* Navbar transition */
.navbar {
  transition: background-color 0.3s ease, color 0.3s ease;
}
</style> 