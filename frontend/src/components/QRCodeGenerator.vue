<template>
  <div id="app" class="container">
    <div class="column">
      <!-- Logo Image -->
      <img alt="Cat logo" class="logo full-width" src="@/assets/cat-bread.gif" />
      
      <!-- Form for URL input -->
      <form @submit.prevent="generateQRCode" class="form-box full-width">
        <label for="url" class="full-width">Kindly feed QR Cat:</label>
        <input
          type="text"
          id="url"
          v-model="url"
          placeholder="Enter URL"
          :class="{ 'input-error': urlError }"
          class="full-width"
        />
        <button type="submit" class="full-width">Generate QR Code</button>

        <p v-if="urlError" class="error-message error-text full-width">{{ urlErrorMessage }}</p>
      </form>
    </div>
    
    <div class="column">
      <!-- Display the generated QR code -->
      <div v-if="qrCodeUrl" class="qr-box">
        <h3>Your QR Code:</h3>
        <img :src="qrCodeUrl" alt="Generated QR Code" class="full-width" />
      </div>

      <!-- Display API error messages -->
      <div v-if="apiError" class="error-message error-text">
        <p>{{ apiError }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

// apiUrl from env var
const apiUrl = import.meta.env.VITE_API_URL;

// Reactive data
const url = ref<string>('');
const qrCodeUrl = ref<string>('');
const urlError = ref<boolean>(false);
const urlErrorMessage = ref<string>('');
const apiError = ref<string>('');

// URL validation function
const validateURL = (url: string): boolean => {
  const regex = /^(https?|ftp):\/\/([a-zA-Z0-9.-]+)(:\d{1,5})?(\/.*)?$/;
  return regex.test(url);
};

// API call to generate QR code
const generateQRCode = async () => {
  // Validate URL format
  if (!validateURL(url.value)) {
    urlError.value = true;
    urlErrorMessage.value = 'Please enter a valid URL (e.g., http://example.com)';
    return;
  }
  
  // Reset error states
  urlError.value = false;
  apiError.value = '';

  try {
    const api = axios.create({
      timeout: 1000
    })

    const response = await api.post(apiUrl, { url: url.value });

    qrCodeUrl.value = `data:image/png;base64,${response.data.qr_code}`

  } catch (error) {
    apiError.value = 'Something went wrong while generating the QR code. Please try again.';
  }
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  gap: 20px;
}
.column {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}
.form-box {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.full-width {
  width: 100%;
  max-width: 400px;
}
.qr-box {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.error-text {
  color: red;
  font-weight: bold;
}
</style>

