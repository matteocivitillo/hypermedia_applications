<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <BreadCrumbs :breadcrumbs="[
      { text: 'Home', url: '/' }, 
      { text: 'Prices' }
    ]" />
    <main class="flex-grow">
      <!-- Monthly Plans Section -->
      <section class="py-14 px-4 border-b border-gray-200">
        <div class="container mx-auto">
          <h2 class="text-3xl font-bold text-gray-900 text-center mb-10">Monthly subscription plans</h2>
          
          <div class="flex flex-wrap justify-center gap-11">
            <!-- Basic Plan Card -->
            <div class="max-w-sm w-full bg-gray-100 bg-opacity-40 rounded-xl shadow-lg overflow-hidden">
              <div class="bg-white bg-opacity-60 p-6 rounded-t-xl">
                <h3 class="text-xl font-bold text-primary mb-4">Yoga4You</h3>
                <div class="space-y-2 text-gray-600 mb-6">
                  <p>✔️ Unlimited access to all classes</p>
                  <p>✔️ Access to meditation room</p>
                  <p>✔️ Use of shower facilities</p>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">25€/month</h3>
                <p class="text-gray-600">The perfect choice for a yoga lover</p>
              </div>
            </div>
            
            <!-- Standard Plan Card -->
            <div class="max-w-sm w-full bg-gray-100 bg-opacity-40 rounded-xl shadow-lg overflow-hidden">
              <div class="bg-white bg-opacity-60 p-6 rounded-t-xl">
                <h3 class="text-xl font-bold text-primary mb-4">Standard</h3>
                <div class="space-y-2 text-gray-600 mb-6">
                  <p>✔️ Unlimited access to all classes</p>
                  <p>✔️ Access to meditation room</p>
                  <p>✔️ Use of shower facilities</p>
                  <p>✔️ Access to all activites under reservation</p>
                  <p>✔️ Access to all the areas</p>
                  <p>✔️ Spa access</p>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">35€/month</h3>
                <p class="text-gray-600">Standard subscription not to miss anything</p>
              </div>
            </div>
            
            <!-- Premium Plan Card -->
            <div class="max-w-sm w-full bg-gray-100 bg-opacity-40 rounded-xl shadow-lg overflow-hidden">
              <div class="bg-white bg-opacity-60 p-6 rounded-t-xl">
                <h3 class="text-xl font-bold text-primary mb-4">Plus membership</h3>
                <div class="space-y-2 text-gray-600 mb-6">
                  <p>✔️ Unlimited access to all classes</p>
                  <p>✔️ Privilaged access to meditation room</p>
                  <p>✔️ Use of shower facilities</p>
                  <p>✔️ Access to all activites without reservation</p>
                  <p>✔️ Access to all the areas</p>
                  <p>✔️ Spa access</p>
                  <p>✔️ Discounts and free drinks at the bar</p>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">40€/month</h3>
                <p class="text-gray-600">The best choice you could take</p>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <!-- 6-Month Plans Section -->
      <section class="py-14 px-4 border-b border-gray-200">
        <div class="container mx-auto">
          <h2 class="text-3xl font-bold text-gray-900 text-center mb-10">6 - month subscription plans</h2>
          
          <div class="flex flex-wrap justify-center gap-11">
            <!-- Basic Plan Card -->
            <div class="max-w-sm w-full bg-gray-100 bg-opacity-40 rounded-xl shadow-lg overflow-hidden">
              <div class="bg-white bg-opacity-60 p-6 rounded-t-xl">
                <h3 class="text-xl font-bold text-primary mb-4">Yoga4You</h3>
                <div class="space-y-2 text-gray-600 mb-6">
                  <p>✔️ Unlimited access to all classes</p>
                  <p>✔️ Access to meditation room</p>
                  <p>✔️ Use of shower facilities</p>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">140€</h3>
                <p class="text-gray-600">The perfect choice for a yoga lover</p>
              </div>
            </div>
            
            <!-- Standard Plan Card -->
            <div class="max-w-sm w-full bg-gray-100 bg-opacity-40 rounded-xl shadow-lg overflow-hidden">
              <div class="bg-white bg-opacity-60 p-6 rounded-t-xl">
                <h3 class="text-xl font-bold text-primary mb-4">Standard</h3>
                <div class="space-y-2 text-gray-600 mb-6">
                  <p>✔️ Unlimited access to all classes</p>
                  <p>✔️ Access to meditation room</p>
                  <p>✔️ Use of shower facilities</p>
                  <p>✔️ Access to all activites under reservation</p>
                  <p>✔️ Access to all the areas</p>
                  <p>✔️ Spa access</p>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">200€</h3>
                <p class="text-gray-600">Standard subscription not to miss anything</p>
              </div>
            </div>
            
            <!-- Premium Plan Card -->
            <div class="max-w-sm w-full bg-gray-100 bg-opacity-40 rounded-xl shadow-lg overflow-hidden">
              <div class="bg-white bg-opacity-60 p-6 rounded-t-xl">
                <h3 class="text-xl font-bold text-primary mb-4">Plus membership</h3>
                <div class="space-y-2 text-gray-600 mb-6">
                  <p>✔️ Unlimited access to all classes</p>
                  <p>✔️ Privilaged access to meditation room</p>
                  <p>✔️ Use of shower facilities</p>
                  <p>✔️ Access to all activites without reservation</p>
                  <p>✔️ Access to all the areas</p>
                  <p>✔️ Spa access</p>
                  <p>✔️ Discounts and free drinks at the bar</p>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">220€</h3>
                <p class="text-gray-600">The best choice you could take</p>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      <!-- Yearly Plans Section -->
      <section class="py-14 px-4">
        <div class="container mx-auto">
          <h2 class="text-3xl font-bold text-gray-900 text-center mb-10">Yearly subscription plans</h2>
          
          <div class="flex flex-wrap justify-center gap-11">
            <!-- Basic Plan Card -->
            <div class="max-w-sm w-full bg-gray-100 bg-opacity-40 rounded-xl shadow-lg overflow-hidden">
              <div class="bg-white bg-opacity-60 p-6 rounded-t-xl">
                <h3 class="text-xl font-bold text-primary mb-4">Yoga4You</h3>
                <div class="space-y-2 text-gray-600 mb-6">
                  <p>✔️ Unlimited access to all classes</p>
                  <p>✔️ Access to meditation room</p>
                  <p>✔️ Use of shower facilities</p>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">270€</h3>
                <p class="text-gray-600">The perfect choice for a yoga lover</p>
              </div>
            </div>
            
            <!-- Standard Plan Card -->
            <div class="max-w-sm w-full bg-gray-100 bg-opacity-40 rounded-xl shadow-lg overflow-hidden">
              <div class="bg-white bg-opacity-60 p-6 rounded-t-xl">
                <h3 class="text-xl font-bold text-primary mb-4">Standard</h3>
                <div class="space-y-2 text-gray-600 mb-6">
                  <p>✔️ Unlimited access to all classes</p>
                  <p>✔️ Access to meditation room</p>
                  <p>✔️ Use of shower facilities</p>
                  <p>✔️ Access to all activites under reservation</p>
                  <p>✔️ Access to all the areas</p>
                  <p>✔️ Spa access</p>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">380€</h3>
                <p class="text-gray-600">Standard subscription not to miss anything</p>
              </div>
            </div>
            
            <!-- Premium Plan Card -->
            <div class="max-w-sm w-full bg-gray-100 bg-opacity-40 rounded-xl shadow-lg overflow-hidden">
              <div class="bg-white bg-opacity-60 p-6 rounded-t-xl">
                <h3 class="text-xl font-bold text-primary mb-4">Plus membership</h3>
                <div class="space-y-2 text-gray-600 mb-6">
                  <p>✔️ Unlimited access to all classes</p>
                  <p>✔️ Privilaged access to meditation room</p>
                  <p>✔️ Use of shower facilities</p>
                  <p>✔️ Access to all activites without reservation</p>
                  <p>✔️ Access to all the areas</p>
                  <p>✔️ Spa access</p>
                  <p>✔️ Discounts and free drinks at the bar</p>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">420€</h3>
                <p class="text-gray-600">The best choice you could take</p>
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