import { useTheme } from '../utils/theme'

export default defineNuxtPlugin(nuxtApp => {
  // Assicurati che il tema sia inizializzato quando l'app parte
  // ma non esporre nulla tramite nuxtApp.provide
  // Gli utenti useranno direttamente il composable useTheme
  useTheme()
}) 