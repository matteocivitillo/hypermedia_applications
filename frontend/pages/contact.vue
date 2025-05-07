<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: 'Contact' }
    ]" />
    <main class="flex-grow">
      <!-- Contact section from the home page -->
      <ContactSection />
      
      <!-- FAQ Section -->
      <section class="bg-white py-16 border-t border-gray-200">
        <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
          <h2 class="text-3xl font-bold text-primary text-center mb-10">FAQ</h2>
          
          <div class="max-w-4xl mx-auto space-y-6">
            <!-- FAQ Item 1 -->
            <div class="bg-gray-50 rounded-xl shadow-lg p-8">
              <div class="flex justify-between items-center">
                <h3 class="text-xl font-medium">What makes Serendipity different from other yoga studios?</h3>
                <button class="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center focus:outline-none">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </button>
              </div>
              <div class="mt-4 hidden">
                <p class="text-gray-600">At Serendipity, we focus on creating a complete wellness experience. Unlike typical studios, we blend traditional yoga practices with modern techniques, offering a range of complementary activities. Our spaces are designed for tranquility with attention to every sensory detail, and our instructors are not just teachers but guides on your wellness journey.</p>
              </div>
            </div>
            
            <!-- FAQ Item 2 -->
            <div class="bg-gray-50 rounded-xl shadow-lg p-8">
              <div class="flex justify-between items-center">
                <h3 class="text-xl font-medium">Do I need to be experienced to join your classes?</h3>
                <button class="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center focus:outline-none">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </button>
              </div>
              <div class="mt-4 hidden">
                <p class="text-gray-600">Not at all! We welcome practitioners of all levels, from complete beginners to advanced yogis. Our classes are designed to be adaptable, with modifications offered for different experience levels. Our supportive instructors will guide you through each pose, ensuring you practice safely at your own pace.</p>
              </div>
            </div>
            
            <!-- FAQ Item 3 -->
            <div class="bg-gray-50 rounded-xl shadow-lg p-8">
              <div class="flex justify-between items-center">
                <h3 class="text-xl font-medium">Is the swimming pool included with membership?</h3>
                <button class="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center focus:outline-none">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </button>
              </div>
              <div class="mt-4 hidden">
                <p class="text-gray-600">Yes, access to our swimming pool is included with our Standard and Plus memberships. The pool is available during regular center hours, with dedicated times for different activities like open swimming, water yoga, and aqua fitness classes.</p>
              </div>
            </div>
            
            <!-- FAQ Item 4 -->
            <div class="bg-gray-50 rounded-xl shadow-lg p-8">
              <div class="flex justify-between items-center">
                <h3 class="text-xl font-medium">Do you have childcare during morning classes?</h3>
                <button class="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center focus:outline-none">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </button>
              </div>
              <div class="mt-4 hidden">
                <p class="text-gray-600">We offer childcare services during select morning classes from Monday to Friday, between 9:00 AM and 12:00 PM. Our childcare specialists engage kids with age-appropriate activities while you enjoy your yoga practice. This service is available for Plus members at no extra cost and can be added to other memberships for a small fee.</p>
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
import { ref } from 'vue'
import NavBar from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'
import ContactSection from '~/components/home/ContactSection.vue'

const formData = ref({
  name: '',
  surname: '',
  email: '',
  message: ''
})

const submitForm = () => {
  // Here you would typically send the form data to a server
  // For now, we'll just log it to the console
  console.log('Form submitted:', formData.value)
  
  // Reset form after submission
  formData.value = {
    name: '',
    surname: '',
    email: '',
    message: ''
  }
  
  // You could also show a success message to the user
  alert('Message sent successfully!')
}

  // SEO metadata for this page
  useSeoMeta({
    title: 'Contact Us - Serendipity Yoga',
    description: 'Contact us for more information or to schedule a visit. We are here to help you on your wellness journey.',
  })
</script>

<script>
export default {
  mounted() {
    // Add event listeners for FAQ toggles
    document.querySelectorAll('.bg-gray-50.rounded-xl.shadow-lg.p-8 button').forEach(button => {
      button.addEventListener('click', function() {
        const content = this.parentNode.nextElementSibling;
        content.classList.toggle('hidden');
        
        // Toggle the arrow icon
        const svg = this.querySelector('svg path');
        if (content.classList.contains('hidden')) {
          svg.setAttribute('d', 'M19 9l-7 7-7-7');
        } else {
          svg.setAttribute('d', 'M19 14l-7-7-7 7');
        }
      });
    });
  }
}
</script> 
