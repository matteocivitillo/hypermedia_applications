import { ref, watch, onMounted, getCurrentInstance } from 'vue'

/**
 * Composable per la gestione del tema (chiaro/scuro)
 * Centralizza la logica di gestione del tema per l'intera applicazione
 */
export function useTheme() {
  // Stato del tema
  const isDark = ref(false)
  
  // Controlla se il tema è scuro
  const isThemeDark = () => isDark.value
  
  // Aggiorna il DOM in base allo stato del tema
  const applyTheme = () => {
    if (isDark.value) {
      document.documentElement.classList.add('dark')
      localStorage.setItem('theme', 'dark')
    } else {
      document.documentElement.classList.remove('dark')
      localStorage.setItem('theme', 'light')
    }
  }
  
  // Alterna tra tema chiaro e scuro
  const toggleTheme = () => {
    isDark.value = !isDark.value
    applyTheme()
  }
  
  // Imposta direttamente il tema (scuro o chiaro)
  const setTheme = (dark) => {
    isDark.value = dark
    applyTheme()
  }
  
  // Inizializza il tema basandosi sulle preferenze dell'utente
  const initTheme = () => {
    // Controllo prima il localStorage
    const savedTheme = localStorage.getItem('theme')
    
    if (savedTheme) {
      // Usa la preferenza salvata
      isDark.value = savedTheme === 'dark'
    } else {
      // Imposta sempre il tema chiaro come predefinito per nuovi utenti
      // ignorando le preferenze del sistema operativo
      isDark.value = false
    }
    
    // Applica il tema immediatamente
    applyTheme()
    
    // Ascolta i cambiamenti del tema del sistema operativo
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      // Aggiorna solo se l'utente non ha impostato una preferenza specifica
      if (!localStorage.getItem('theme')) {
        // Non seguiamo più le preferenze del sistema, manteniamo sempre light come default
        // isDark.value = e.matches 
        isDark.value = false
        applyTheme()
      }
    })
  }
  
  // Inizializza il tema al mount del componente (solo se nel contesto di un componente)
  const instance = getCurrentInstance()
  if (instance) {
    onMounted(() => {
      initTheme()
    })
  } else if (typeof window !== 'undefined') {
    // Se non siamo in un componente, inizializza direttamente
    initTheme()
  }
  
  // Osserva i cambiamenti dello stato e applica il tema
  watch(isDark, () => {
    applyTheme()
  })
  
  // Restituisci i metodi e le proprietà da utilizzare nei componenti
  return {
    isDark,
    isThemeDark,
    toggleTheme,
    setTheme
  }
} 