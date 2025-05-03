<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[{ text: 'Home', url: '/' }, { text: 'Contact', url: '/contact' }]" />
    <main class="flex-grow">
      <!-- Map and Contact Info Section -->
      <section class="bg-gray-50 py-16 border-b border-gray-200">
        <div class="container mx-auto px-4">
          <div class="flex flex-wrap md:flex-nowrap justify-center gap-16 lg:gap-24">
            <!-- Map -->
            <div class="w-full md:w-1/2 h-96 lg:h-auto rounded-xl overflow-hidden shadow-lg relative">
              <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2797.756!2d9.217562!3d45.4860319!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4786c6ce44ac16bb%3A0xee001206635a5c3e!2sVia%20Stefano%20Canzio%2C%202%2C%2020131%20Milano%20MI!5e0!3m2!1sen!2sit!4v1715511467732!5m2!1sen!2sit" 
                width="100%" 
                height="100%" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
              </iframe>
              <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-6xl">
                📍
              </div>
            </div>
            
            <!-- Contact Information -->
            <div class="w-full md:w-1/2 flex flex-col">
              <div class="mb-12">
                <h2 class="text-3xl font-bold text-primary mb-4">Contact Us</h2>
                <div class="flex items-center gap-5 mb-4">
                  <div class="w-5 h-5 flex justify-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                    </svg>
                  </div>
                  <span class="text-xl">+1 234 567 890</span>
                </div>
                <div class="flex items-center gap-5">
                  <div class="w-5 h-5 flex justify-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <span class="text-xl">info@serendipity.com</span>
                </div>
              </div>
              
              <div class="mb-12">
                <h2 class="text-3xl font-bold text-primary mb-4">Location</h2>
                <div class="flex items-start gap-8">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                  <span class="text-xl">Via Stefano Canzio, 2, 20131 Milano MI</span>
                </div>
              </div>
              
              <div>
                <h2 class="text-3xl font-bold text-primary mb-4">Working Hours</h2>
                <div class="w-full overflow-x-auto">
                  <table class="w-full border-collapse">
                    <thead class="bg-primary text-white">
                      <tr>
                        <th class="py-3 px-4 text-center">DAY</th>
                        <th class="py-3 px-4 text-center">OPEN</th>
                        <th class="py-3 px-4 text-center">CLOSE</th>
                      </tr>
                    </thead>
                    <tbody class="text-gray-600">
                      <tr class="border-b border-gray-200">
                        <td class="py-3 px-4 text-center">Monday</td>
                        <td class="py-3 px-4 text-center">09:00</td>
                        <td class="py-3 px-4 text-center">21:00</td>
                      </tr>
                      <tr class="border-b border-gray-200">
                        <td class="py-3 px-4 text-center">Tuesday</td>
                        <td class="py-3 px-4 text-center">09:00</td>
                        <td class="py-3 px-4 text-center">21:00</td>
                      </tr>
                      <tr class="border-b border-gray-200">
                        <td class="py-3 px-4 text-center">Wednesday</td>
                        <td class="py-3 px-4 text-center">09:00</td>
                        <td class="py-3 px-4 text-center">21:00</td>
                      </tr>
                      <tr class="border-b border-gray-200">
                        <td class="py-3 px-4 text-center">Thursday</td>
                        <td class="py-3 px-4 text-center">09:00</td>
                        <td class="py-3 px-4 text-center">21:00</td>
                      </tr>
                      <tr class="border-b border-gray-200">
                        <td class="py-3 px-4 text-center">Friday</td>
                        <td class="py-3 px-4 text-center">09:00</td>
                        <td class="py-3 px-4 text-center">21:00</td>
                      </tr>
                      <tr class="border-b border-gray-200">
                        <td class="py-3 px-4 text-center">Saturday</td>
                        <td class="py-3 px-4 text-center">10:00</td>
                        <td class="py-3 px-4 text-center">19:00</td>
                      </tr>
                      <tr>
                        <td class="py-3 px-4 text-center">Sunday</td>
                        <td class="py-3 px-4 text-center">10:00</td>
                        <td class="py-3 px-4 text-center">15:00</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <!-- FAQ Section -->
      <section class="bg-secondary py-16">
        <div class="container mx-auto px-4">
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
import NavBar from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'
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