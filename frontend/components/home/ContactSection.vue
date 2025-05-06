<template>
  <section class="py-20 bg-white border-t border-gray-100">
    <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
      <h2 class="text-4xl font-bold text-primary text-center mb-16">Contact Us</h2>
      
      <!-- Prima riga: Form + Orari -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
        <!-- Quick Contact Form -->
        <div class="bg-gray-50 rounded-xl shadow-custom p-8 h-full">
          <h3 class="text-2xl font-bold text-primary mb-6">Send Us a Message</h3>
          
          <form class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label for="name" class="text-gray-600 block">Your Name</label>
                <input type="text" id="name" class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition" placeholder="John Doe" />
              </div>
              
              <div class="space-y-2">
                <label for="email" class="text-gray-600 block">Your Email</label>
                <input type="email" id="email" class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition" placeholder="john@example.com" />
              </div>
            </div>
            
            <div class="space-y-2">
              <label for="message" class="text-gray-600 block">Message</label>
              <textarea id="message" rows="4" class="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition resize-none" placeholder="How can we help you?"></textarea>
            </div>
            
            <button type="submit" class="w-full bg-primary hover:bg-primary-dark text-white font-medium py-3 px-4 rounded-lg transition-colors duration-300">
              Send Message
            </button>
          </form>
        </div>
        
        <!-- Working Hours -->
        <div class="bg-gray-50 rounded-xl shadow-custom p-8 h-full">
          <h3 class="text-2xl font-bold text-primary mb-6">Working Hours</h3>
          
          <div class="overflow-hidden rounded-lg">
            <table class="w-full border-collapse">
              <thead>
                <tr>
                  <th class="bg-primary text-white py-3 font-medium text-base text-left pl-4">DAY</th>
                  <th class="bg-primary text-white py-3 font-medium text-base text-center">OPEN</th>
                  <th class="bg-primary text-white py-3 font-medium text-base text-center">CLOSE</th>
                </tr>
              </thead>
              <tbody>
                <tr class="border-b border-gray-200">
                  <td class="py-3 pl-4 text-gray-700">Monday</td>
                  <td class="py-3 text-center text-gray-700">09:00</td>
                  <td class="py-3 text-center text-gray-700">21:00</td>
                </tr>
                <tr class="border-b border-gray-200 bg-gray-50">
                  <td class="py-3 pl-4 text-gray-700">Tuesday</td>
                  <td class="py-3 text-center text-gray-700">09:00</td>
                  <td class="py-3 text-center text-gray-700">21:00</td>
                </tr>
                <tr class="border-b border-gray-200">
                  <td class="py-3 pl-4 text-gray-700">Wednesday</td>
                  <td class="py-3 text-center text-gray-700">09:00</td>
                  <td class="py-3 text-center text-gray-700">21:00</td>
                </tr>
                <tr class="border-b border-gray-200 bg-gray-50">
                  <td class="py-3 pl-4 text-gray-700">Thursday</td>
                  <td class="py-3 text-center text-gray-700">09:00</td>
                  <td class="py-3 text-center text-gray-700">21:00</td>
                </tr>
                <tr class="border-b border-gray-200">
                  <td class="py-3 pl-4 text-gray-700">Friday</td>
                  <td class="py-3 text-center text-gray-700">09:00</td>
                  <td class="py-3 text-center text-gray-700">21:00</td>
                </tr>
                <tr class="border-b border-gray-200 bg-gray-50">
                  <td class="py-3 pl-4 text-gray-700">Saturday</td>
                  <td class="py-3 text-center text-gray-700">10:00</td>
                  <td class="py-3 text-center text-gray-700">19:00</td>
                </tr>
                <tr>
                  <td class="py-3 pl-4 text-gray-700">Sunday</td>
                  <td class="py-3 text-center text-gray-700">10:00</td>
                  <td class="py-3 text-center text-gray-700">15:00</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <!-- Contact Info -->
          <div class="mt-6 space-y-4">
            <div class="flex items-center space-x-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              <span class="text-gray-700 text-lg">+1 234 567 890</span>
            </div>
            
            <div class="flex items-center space-x-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <span class="text-gray-700 text-lg">info@serendipity.com</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Seconda riga: Mappa interattiva a tutta larghezza -->
      <div class="w-full bg-gray-50 rounded-xl shadow-custom overflow-hidden">
        <!-- Interactive Map -->
        <div class="w-full relative" style="padding-top: 28.125%;">  <!-- Aspect ratio 32:9 (half of 16:9) -->
          <!-- Placeholder for interactive map - in a real app this would be replaced with Google Maps or similar -->
          <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2797.1963944546087!2d9.215345715774256!3d45.47972887910111!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4786c6dd6eaaaaab%3A0xdee5f7e0c5112208!2sVia%20Stefano%20Canzio%2C%202%2C%2020131%20Milano%20MI!5e0!3m2!1sit!2sit!4v1614356585378!5m2!1sit!2sit" 
            width="100%" 
            height="100%" 
            style="border:0;" 
            allowfullscreen="" 
            loading="lazy"
            class="absolute inset-0 w-full h-full"
          ></iframe>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// Contact section doesn't need data fetching
</script>

<style scoped>
.shadow-custom {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
}
</style> 