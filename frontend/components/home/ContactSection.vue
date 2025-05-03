<template>
  <section class="py-16 bg-gray-100 border-t border-gray-200">
    <div class="container mx-auto grid grid-cols-1 lg:grid-cols-2 gap-20">
      <!-- Map -->
      <div class="w-full h-[400px] rounded-xl overflow-hidden">
        <img src="/images/map.jpg" alt="Map Location" class="w-full h-full object-cover" />
      </div>
      
      <!-- Contact Info -->
      <div class="space-y-10">
        <div class="space-y-4">
          <h3 class="text-2xl font-bold text-primary">Contact Us</h3>
          
          <div class="flex items-center space-x-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-900" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
            <span class="text-gray-900 text-lg">+1 234 567 890</span>
          </div>
          
          <div class="flex items-center space-x-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-900" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            <span class="text-gray-900 text-lg">info@serendipity.com</span>
          </div>
        </div>
        
        <div class="space-y-4">
          <h3 class="text-2xl font-bold text-primary">Location</h3>
          
          <div class="flex items-start space-x-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-900 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span class="text-gray-900 text-lg">Via Stefano Canzio, 2, 20131 Milano MI</span>
          </div>
        </div>
        
        <div class="space-y-4">
          <h3 class="text-2xl font-bold text-primary">Working Hours</h3>
          
          <div class="grid grid-cols-3 gap-2 text-center">
            <div class="bg-primary text-white py-2 font-normal text-base">DAY</div>
            <div class="bg-primary text-white py-2 font-normal text-base">OPEN</div>
            <div class="bg-primary text-white py-2 font-normal text-base">CLOSE</div>
            
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">Monday</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">09:00</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">21:00</div>
            
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">Tuesday</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">09:00</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">21:00</div>
            
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">Wednesday</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">09:00</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">21:00</div>
            
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">Thursday</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">09:00</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">21:00</div>
            
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">Friday</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">09:00</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">21:00</div>
            
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">Saturday</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">10:00</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">19:00</div>
            
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">Sunday</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">10:00</div>
            <div class="border-b border-primary border-opacity-65 py-2 text-gray-600">15:00</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {}
</script> 