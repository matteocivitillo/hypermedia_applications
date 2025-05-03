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
        <div class="container mx-auto px-4 h-full flex items-center relative z-10">
          <div class="max-w-3xl">
            <h1 class="text-5xl font-bold text-white mb-6">Transforming lives through the practice of yoga and meditation.</h1>
            <p class="text-xl text-gray-200">Join our community and transform your life with expert guidance in yoga, meditation, and mindful living.</p>
          </div>
        </div>
      </section>

      <!-- Features Section -->
      <section class="bg-secondary py-20">
        <div class="container mx-auto px-4">
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
      <section class="py-16">
        <div class="container mx-auto px-4">
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
              <img src="/images/water-yoga.jpg" alt="Yoga practice" class="w-full h-auto rounded-3xl shadow-lg" />
            </div>
          </div>
        </div>
      </section>

      <!-- Our Rooms -->
      <section class="bg-secondary py-16" id="rooms">
        <div class="container mx-auto px-4">
          <h2 class="text-4xl font-bold text-primary text-center mb-12">Our Yoga Rooms</h2>
          
          <div class="relative">
            <!-- Room Carousel -->
            <div class="bg-white p-6 md:p-8 rounded-xl shadow-lg flex flex-wrap md:flex-nowrap gap-16">
              <div class="w-full md:w-1/2">
                <img src="/images/meditation.jpg" alt="Oriental Room" class="w-full h-auto rounded-lg" />
              </div>
              <div class="w-full md:w-1/2 flex flex-col justify-center">
                <h3 class="text-2xl font-bold text-primary mb-4">Oriental Room</h3>
                <div class="prose prose-lg">
                  <p>A serene haven infused with Eastern tranquility. Practice amidst elegant Asian-inspired decor, where harmony flows through every detail.</p>
                  
                  <p class="font-medium mt-4">Features:</p>
                  <ul>
                    <li>Warm teak floors & silk drapery</li>
                    <li>Soft lantern lighting & incense scents</li>
                    <li>Traditional singing bowls & chimes</li>
                  </ul>
                  
                  <p class="font-medium mt-4">Activities:</p>
                  <ul>
                    <li>Kundalini & Hatha yoga</li>
                  </ul>
                  
                  <p class="italic mt-4">"Where ancient wisdom meets mindful movement."</p>
                </div>
              </div>
            </div>
            
            <!-- Carousel Controls -->
            <button class="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-5 bg-gray-400 w-10 h-10 rounded-full flex items-center justify-center text-white focus:outline-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
              </svg>
            </button>
            <button class="absolute right-0 top-1/2 -translate-y-1/2 translate-x-5 bg-gray-400 w-10 h-10 rounded-full flex items-center justify-center text-white focus:outline-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </div>
        </div>
      </section>

      <!-- Our Areas & Services -->
      <section class="py-16" id="areas">
        <div class="container mx-auto px-4">
          <div class="text-center mb-12">
            <h2 class="text-4xl font-bold text-primary mb-4">Serendipity Yoga Center - Areas</h2>
            <p class="text-xl text-gray-700">Our yoga center offers a cozy and complete environment with several areas dedicated to the well-being and relaxation of our guests</p>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="rounded-xl shadow-lg overflow-hidden">
              <img src="/images/zumba.jpg" alt="Yoga Area" class="w-full h-64 object-cover" />
            </div>
            <div class="rounded-xl shadow-lg overflow-hidden">
              <img src="/images/ceramics.jpg" alt="Meditation Area" class="w-full h-64 object-cover" />
            </div>
            <div class="rounded-xl shadow-lg overflow-hidden">
              <img src="/images/water-yoga.jpg" alt="Relaxation Area" class="w-full h-64 object-cover" />
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