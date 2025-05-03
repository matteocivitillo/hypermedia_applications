<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <main class="flex-grow">
      <HeroSection />
      <YogaClasses />
      <HighlightedActivities />
      <ContactSection />
      <SocialWall />
    </main>
    <SiteFooter />
  </div>
</template>

<script setup>
import NavBar from '~/components/home/NavBar.vue'
import BreadCrumbs from '~/components/home/BreadCrumbs.vue'
import HeroSection from '~/components/home/HeroSection.vue'
import YogaClasses from '~/components/home/YogaClasses.vue'
import HighlightedActivities from '~/components/home/HighlightedActivities.vue'
import ContactSection from '~/components/home/ContactSection.vue'
import SocialWall from '~/components/home/SocialWall.vue'
import SiteFooter from '~/components/home/SiteFooter.vue'
</script> 