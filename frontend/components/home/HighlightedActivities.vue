<template>
  <section class="py-12 bg-white">
    <div class="container mx-auto">
      <h2 class="text-3xl font-bold text-primary text-center mb-10">Highlighted Activities</h2>
      
      <div class="relative">
        <!-- Activity Cards Carousel -->
        <div class="flex overflow-x-auto pb-6 gap-8 no-scrollbar">
          <!-- Water Yoga -->
          <div class="shrink-0 w-64 h-80 relative rounded-2xl overflow-hidden shadow-custom">
            <div class="absolute inset-0 bg-black bg-opacity-20">
              <img src="/images/water-yoga.jpg" alt="Water Yoga" class="w-full h-full object-cover" />
            </div>
            <div class="absolute inset-0 flex items-center justify-center">
              <h3 class="text-2xl font-bold text-white">Water Yoga</h3>
            </div>
          </div>
          
          <!-- Zumba -->
          <div class="shrink-0 w-64 h-80 relative rounded-2xl overflow-hidden shadow-custom">
            <div class="absolute inset-0 bg-black bg-opacity-20">
              <img src="/images/zumba.jpg" alt="Zumba" class="w-full h-full object-cover" />
            </div>
            <div class="absolute inset-0 flex items-center justify-center">
              <h3 class="text-2xl font-bold text-white">Zumba</h3>
            </div>
          </div>
          
          <!-- Meditation -->
          <div class="shrink-0 w-64 h-80 relative rounded-2xl overflow-hidden shadow-custom">
            <div class="absolute inset-0 bg-black bg-opacity-20">
              <img src="/images/meditation.jpg" alt="Meditation" class="w-full h-full object-cover" />
            </div>
            <div class="absolute inset-0 flex items-center justify-center">
              <h3 class="text-2xl font-bold text-white">Meditation</h3>
            </div>
          </div>
          
          <!-- Ceramics -->
          <div class="shrink-0 w-64 h-80 relative rounded-2xl overflow-hidden shadow-custom">
            <div class="absolute inset-0 bg-black bg-opacity-20">
              <img src="/images/ceramics.jpg" alt="Ceramics" class="w-full h-full object-cover" />
            </div>
            <div class="absolute inset-0 flex items-center justify-center">
              <h3 class="text-2xl font-bold text-white">Ceramics</h3>
            </div>
          </div>
        </div>
        
        <!-- Navigation Arrows -->
        <button class="absolute left-2 top-1/2 -translate-y-1/2 bg-secondary w-10 h-10 rounded-full flex items-center justify-center shadow-custom">
          <img src="/images/icons/arrow-left.svg" alt="Previous" width="24" height="24" />
        </button>
        
        <button class="absolute right-2 top-1/2 -translate-y-1/2 bg-secondary w-10 h-10 rounded-full flex items-center justify-center shadow-custom">
          <img src="/images/icons/arrow-right.svg" alt="Next" width="24" height="24" />
        </button>
      </div>
    </div>
  </section>
</template>

<script>
export default {}
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style> 