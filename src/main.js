// main.js
import { createApp } from 'vue'
import App from './App.vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'dark',
    themes: {
      dark: {
        colors: {
          primary: '#42b883',
          surface: '#1a1a1a',
          background: '#242424',
        },
      },
    },
  },
})

// Create Vue app instance
const app = createApp(App)

// Use Vuetify
app.use(vuetify)

// Mount the app
app.mount('#app')