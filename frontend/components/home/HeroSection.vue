<template>
  <section class="w-full bg-gray-100 relative -mt-[1px]">
    <div class="w-full h-screen relative overflow-hidden">
      <!-- Background Image with Overlay -->
      <div class="absolute inset-0 bg-black bg-opacity-40">
        <img src="/images/hero-background.jpg" alt="" class="w-full h-full object-cover" />  <!-- Alt text is empty because it's decorative only -->
      </div>
      
      <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32 h-full flex flex-col justify-center relative z-10">
        <!-- Center Logo -->
        <div class="flex flex-col items-center mb-12">
          <img src="/images/logo-large.svg" alt="Serendipity yoga" class="h-32 mb-4" />  <!-- The word "logo" is usually not an important part of the image's content or function.-->
        </div>
        
        <div class="max-w-3xl space-y-6 text-left pl-4 md:pl-16 self-start">
          <h1 class="text-5xl md:text-6xl font-bold text-white leading-tight">
            Discover Your Inner Peace Through Yoga
          </h1>
          <p class="text-xl text-gray-200">
            Join our community and transform your life with expert guidance in yoga, meditation, and mindful living.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

