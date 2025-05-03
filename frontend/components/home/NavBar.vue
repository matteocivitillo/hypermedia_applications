<template>
  <nav class="bg-primary border-b-0 sticky top-0 z-50">
    <div class="container mx-auto px-6 md:px-16 lg:px-24 xl:px-32">
      <div class="flex items-center justify-between h-20">
        <!-- Logo Left, always same size -->
        <div class="flex items-center -ml-12">
          <a href="/" class="flex items-center">
            <img src="/images/logo-small.svg" alt="Yoga Center Logo" style="height: 48px; width: auto;" class="flex-shrink-0" />
          </a>
        </div>

        <!-- Hamburger Menu Button (visibile quando lo spazio non è sufficiente) -->
        <div class="lg:hidden">
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="text-white focus:outline-none">
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
            Home
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
                The Center
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </a>
              <div v-show="dropdownOpen" 
                  class="dropdown-menu">
                <div class="py-2 px-4">
                  <a href="#" 
                     @click.prevent="goToCenter"
                     class="block py-3 text-sm text-gray-700 hover:bg-gray-100 rounded px-2 -mx-2">
                    The Center
                  </a>
                  <a href="#" 
                     @click.prevent="goToRooms"
                     class="block py-3 text-sm text-gray-700 hover:bg-gray-100 rounded px-2 -mx-2">
                    Rooms
                  </a>
                  <a href="#" 
                     @click.prevent="goToAreas"
                     class="block py-3 text-sm text-gray-700 hover:bg-gray-100 rounded px-2 -mx-2">
                    Areas
                  </a>
                </div>
              </div>
            </div>
          </div>
          
          <router-link to="/activities" 
            class="text-white text-base font-medium hover:text-gray-300 transition-colors"
            :class="{ 'border-b-2 border-white pb-1': isActive('/activities') }">
            Activities
          </router-link>
          
          <a href="#" 
             @click.prevent="goToHighlights"
             class="text-white text-base font-medium hover:text-gray-300 transition-colors"
             :class="{ 'border-b-2 border-white pb-1': isActive('/highlights') }">
            Highlights
          </a>
          
          <router-link to="/teachers" 
            class="text-white text-base font-medium hover:text-gray-300 transition-colors"
            :class="{ 'border-b-2 border-white pb-1': isActive('/teachers') }">
            Teachers
          </router-link>
          
          <router-link to="/prices" 
            class="text-white text-base font-medium hover:text-gray-300 transition-colors"
            :class="{ 'border-b-2 border-white pb-1': isActive('/prices') }">
            Prices
          </router-link>
          
          <router-link to="/contact" 
            class="text-white text-base font-medium hover:text-gray-300 transition-colors"
            :class="{ 'border-b-2 border-white pb-1': isActive('/contact') }">
            Contact
          </router-link>
        </div>
      </div>
    </div>

    <!-- Mobile Menu (visibile quando aperto) -->
    <div v-show="mobileMenuOpen" class="lg:hidden bg-primary border-t border-gray-700">
      <div class="container mx-auto px-6 py-4">
        <router-link to="/" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-blue-900 rounded px-2': isActive('/') }"
          @click="mobileMenuOpen = false">
          Home
        </router-link>
        
        <!-- Mobile Dropdown -->
        <div class="relative">
          <button @click="mobileCenterOpen = !mobileCenterOpen"
                class="w-full text-left py-3 text-white text-base font-medium hover:text-gray-300 focus:outline-none flex justify-between items-center"
                :class="{ 'bg-blue-900 rounded px-2': isActive('/center') }">
            <span>The Center</span>
            <svg class="h-5 w-5 transform transition-transform" :class="{ 'rotate-180': mobileCenterOpen }" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div v-show="mobileCenterOpen" class="pl-4 border-l-2 border-gray-600 ml-2 mt-1">
            <a href="#" 
              @click.prevent="goToCenter(); mobileMenuOpen = false"
              class="block py-3 text-white text-base font-medium hover:text-gray-300">
              The Center
            </a>
            <a href="#" 
              @click.prevent="goToRooms(); mobileMenuOpen = false"
              class="block py-3 text-white text-base font-medium hover:text-gray-300">
              Rooms
            </a>
            <a href="#" 
              @click.prevent="goToAreas(); mobileMenuOpen = false"
              class="block py-3 text-white text-base font-medium hover:text-gray-300">
              Areas
            </a>
          </div>
        </div>
        
        <router-link to="/activities" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-blue-900 rounded px-2': isActive('/activities') }"
          @click="mobileMenuOpen = false">
          Activities
        </router-link>
        
        <a href="#" 
          @click.prevent="goToHighlights(); mobileMenuOpen = false"
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-blue-900 rounded px-2': isActive('/highlights') }">
          Highlights
        </a>
        
        <router-link to="/teachers" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-blue-900 rounded px-2': isActive('/teachers') }"
          @click="mobileMenuOpen = false">
          Teachers
        </router-link>
        
        <router-link to="/prices" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-blue-900 rounded px-2': isActive('/prices') }"
          @click="mobileMenuOpen = false">
          Prices
        </router-link>
        
        <router-link to="/contact" 
          class="block py-3 text-white text-base font-medium hover:text-gray-300"
          :class="{ 'bg-blue-900 rounded px-2': isActive('/contact') }"
          @click="mobileMenuOpen = false">
          Contact
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      dropdownOpen: false,
      dropdownTimer: null,
      mobileMenuOpen: false,
      mobileCenterOpen: false
    }
  },
  methods: {
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
        localStorage.setItem('scrollToTarget', 'rooms');
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
        localStorage.setItem('scrollToTarget', 'areas');
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
        localStorage.setItem('scrollToHighlights', 'true');
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
        // Trova il componente HighlightedActivities
        const highlightsSections = document.querySelectorAll('section');
        let highlightsSection = null;
        
        // Cerca la sezione che contiene "Highlighted Activities" come testo
        for (const section of highlightsSections) {
          if (section.textContent.includes('Highlighted Activities')) {
            highlightsSection = section;
            break;
          }
        }
        
        // Fallback alla prima sezione con classe bg-white se non troviamo la sezione per titolo
        if (!highlightsSection) {
          highlightsSection = document.querySelector('section.py-12.bg-white');
        }
        
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
    // Check if we need to scroll to a section on page load
    if (this.$route.path === '/center') {
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
    } else if (this.$route.path === '/' && localStorage.getItem('scrollToHighlights') === 'true') {
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
</style> 