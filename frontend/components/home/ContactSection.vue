<template>
  <section class="py-20 dark:bg-gray-800">
    <div class="container mx-auto px-8 sm:px-12 md:px-16 lg:px-24 xl:px-32">
      <h2 class="text-4xl font-bold text-primary dark:text-[#9ACBD0] text-center mb-6">{{ t('aboutUs') }}</h2>
      
      <!-- Contact Info -->
      <div class="flex flex-col md:flex-row justify-center items-center space-y-4 md:space-y-0 md:space-x-12 mb-12">
        <a href="tel:+1234567890" class="flex items-center space-x-3 text-gray-700 dark:text-gray-300 text-lg hover:text-primary dark:hover:text-[#9ACBD0] transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary dark:text-[#9ACBD0]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
          </svg>
          <span>+1 234 567 890</span>
        </a>
        
        <a href="mailto:info@serendipity.com" class="flex items-center space-x-3 text-gray-700 dark:text-gray-300 text-lg hover:text-primary dark:hover:text-[#9ACBD0] transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary dark:text-[#9ACBD0]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
          </svg>
          <span>info@serendipity.com</span>
        </a>
      </div>
      
      <!-- Map + Orari nella prima riga -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
        <!-- Interactive Map -->
        <div class="bg-gray-50 dark:bg-gray-600 rounded-xl shadow-custom dark:shadow-gray-900/70 p-8 h-full min-h-[400px] flex">
          <div class="w-full h-full rounded-lg overflow-hidden flex-1">
            <!-- Google Maps Static Image - No JavaScript Errors -->
            <div class="relative w-full h-full rounded-lg overflow-hidden" style="min-height:340px;">
              <img 
                src="https://maps.googleapis.com/maps/api/staticmap?center=45.47972887910111,9.215345715774256&zoom=15&size=600x400&maptype=roadmap&markers=color:red%7C45.47972887910111,9.215345715774256&key=AIzaSyCQXJKnqpGY-8X8uEgqXYrJZz6cGiEqcnA"
                alt="Serendipity Yoga Location Map - Via Stefano Canzio, 2, 20131 Milano MI"
                class="w-full h-full object-cover rounded-lg cursor-pointer hover:opacity-90 transition-opacity"
                style="min-height:340px;"
                onclick="window.open('https://www.google.com/maps/search/?api=1&query=45.47972887910111,9.215345715774256', '_blank')"
              />
              <!-- Overlay with click instruction -->
              <div class="absolute bottom-4 left-4 bg-black bg-opacity-70 text-white px-3 py-2 rounded-lg text-sm">
                📍 Click to open in Google Maps
              </div>
            </div>
          </div>
        </div>
        
        <!-- Working Hours -->
        <div class="bg-gray-50 dark:bg-gray-600 rounded-xl shadow-custom dark:shadow-gray-900/70 p-8 h-full">
          <h3 class="text-2xl font-bold text-primary dark:text-[#9ACBD0] mb-6">{{ t('workingHours') }}</h3>
          
          <div class="overflow-hidden rounded-lg">
            <table class="w-full border-collapse table-alternate">
              <thead>
                <tr>
                  <th class="bg-primary text-white py-3 font-medium text-base text-left pl-4">{{ t('day') }}</th>
                  <th class="bg-primary text-white py-3 font-medium text-base text-center">{{ t('open') }}</th>
                  <th class="bg-primary text-white py-3 font-medium text-base text-center">{{ t('close') }}</th>
                </tr>
              </thead>
              <tbody>
                <tr class="border-b border-gray-200 dark:border-gray-500">
                  <td class="py-3 pl-4 text-gray-700 dark:text-gray-300">{{ t('monday') }}</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">09:00</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">21:00</td>
                </tr>
                <tr class="border-b border-gray-200 dark:border-gray-500 bg-gray-50 dark:bg-gray-500">
                  <td class="py-3 pl-4 text-gray-700 dark:text-gray-300">{{ t('tuesday') }}</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">09:00</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">21:00</td>
                </tr>
                <tr class="border-b border-gray-200 dark:border-gray-500">
                  <td class="py-3 pl-4 text-gray-700 dark:text-gray-300">{{ t('wednesday') }}</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">09:00</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">21:00</td>
                </tr>
                <tr class="border-b border-gray-200 dark:border-gray-500 bg-gray-50 dark:bg-gray-500">
                  <td class="py-3 pl-4 text-gray-700 dark:text-gray-300">{{ t('thursday') }}</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">09:00</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">21:00</td>
                </tr>
                <tr class="border-b border-gray-200 dark:border-gray-500">
                  <td class="py-3 pl-4 text-gray-700 dark:text-gray-300">{{ t('friday') }}</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">09:00</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">21:00</td>
                </tr>
                <tr class="border-b border-gray-200 dark:border-gray-500 bg-gray-50 dark:bg-gray-500">
                  <td class="py-3 pl-4 text-gray-700 dark:text-gray-300">{{ t('saturday') }}</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">10:00</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">19:00</td>
                </tr>
                <tr>
                  <td class="py-3 pl-4 text-gray-700 dark:text-gray-300">{{ t('sunday') }}</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">10:00</td>
                  <td class="py-3 text-center text-gray-700 dark:text-gray-300">15:00</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { selectedLang } from '../home/NavBar.vue';

// Translations
const translations = {
  en: {
    aboutUs: 'About Us',
    workingHours: 'Working Hours',
    day: 'DAY',
    open: 'OPEN',
    close: 'CLOSE',
    monday: 'Monday',
    tuesday: 'Tuesday',
    wednesday: 'Wednesday',
    thursday: 'Thursday',
    friday: 'Friday',
    saturday: 'Saturday',
    sunday: 'Sunday'
  },
  it: {
    aboutUs: 'Chi Siamo',
    workingHours: 'Orari di Apertura',
    day: 'GIORNO',
    open: 'APRE',
    close: 'CHIUDE',
    monday: 'Lunedì',
    tuesday: 'Martedì',
    wednesday: 'Mercoledì',
    thursday: 'Giovedì',
    friday: 'Venerdì',
    saturday: 'Sabato',
    sunday: 'Domenica'
  },
  fr: {
    aboutUs: 'À Propos de Nous',
    workingHours: 'Heures d\'Ouverture',
    day: 'JOUR',
    open: 'OUVERT',
    close: 'FERMÉ',
    monday: 'Lundi',
    tuesday: 'Mardi',
    wednesday: 'Mercredi',
    thursday: 'Jeudi',
    friday: 'Vendredi',
    saturday: 'Samedi',
    sunday: 'Dimanche'
  },
  de: {
    aboutUs: 'Über Uns',
    workingHours: 'Öffnungszeiten',
    day: 'TAG',
    open: 'ÖFFNET',
    close: 'SCHLIEßT',
    monday: 'Montag',
    tuesday: 'Dienstag',
    wednesday: 'Mittwoch',
    thursday: 'Donnerstag',
    friday: 'Freitag',
    saturday: 'Samstag',
    sunday: 'Sonntag'
  },
  zh: {
    aboutUs: '关于我们',
    workingHours: '营业时间',
    day: '天',
    open: '开放',
    close: '关闭',
    monday: '星期一',
    tuesday: '星期二',
    wednesday: '星期三',
    thursday: '星期四',
    friday: '星期五',
    saturday: '星期六',
    sunday: '星期日'
  }
};

// Function to get translations
const t = (key) => {
  const lang = selectedLang.value;
  return translations[lang]?.[key] || translations.en[key];
};
</script>

<style scoped>
.shadow-custom {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
}

.dark .shadow-custom {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.2);
}
</style> 