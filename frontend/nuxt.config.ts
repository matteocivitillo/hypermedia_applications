// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss'],
  tailwindcss: {
    cssPath: '~/assets/css/tailwind.css',
    configPath: 'tailwind.config.js',
  },
  css: ['~/assets/css/main.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    }
  },
  // SEO global settings
  app: {
    head: {
      title: 'Serendipity Yoga',
      meta: [
        { name: 'description', content: 'Transforming lives through the practise of yoga and meditation' },
        { name: 'keywords', content: 'yoga, meditation, wellbeing, health, fitness, training, yoga classes, yoga training, yoga retreats, hatha yoga, kundalini yoga, ashtanga yoga, gentle water yoga, mindfulness' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'author', content: 'Bada Bastu' }, // Author of the site
        { name: 'robots', content: 'index, follow' }, // Directs search engines on how to index the page
        { property: 'og:title', content: 'Serendipity Yoga' }, // Open Graph title
        { property: 'og:description', content: 'Transforming lives through the practise of yoga and meditation' }, // Open Graph description
        { property: 'og:image', content: '/favicon.ico' }, // Open Graph image
        { property: 'og:url', content: 'https://www.serendipityyoga.com' }, // Open Graph URL
        { property: 'og:type', content: 'website' }, // Open Graph type
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  }
})
