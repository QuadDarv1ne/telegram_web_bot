<template>
    <div class="p-4">
      <h1 class="text-2xl font-bold">Message from API:</h1>
      <p>{{ message }}</p>
    </div>
  </template>
  
  <script setup lang="ts">
  import { useMainStore } from './store'
  
  const store = useMainStore()
  store.fetchMessage()
  </script>
  
  <style>
  @import './assets/styles/tailwind.css';
  </style>
  