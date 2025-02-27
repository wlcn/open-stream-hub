<template>
  <div class="min-h-screen bg-gray-100 p-4">
    <div class="max-w-2xl mx-auto">
      <h1 class="text-2xl font-bold mb-4">OpenStreamHub</h1>
      <div class="mb-4">
        <input
          v-model="liveUrl"
          type="text"
          placeholder="输入直播源地址（HLS 或 DASH）"
          class="w-full p-2 border rounded"
        />
        <button
          @click="playLive"
          class="mt-2 w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
        >
          播放
        </button>
      </div>
      <LivePlayer v-if="currentUrl" :src="currentUrl" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import LivePlayer from './components/LivePlayer.vue';

const liveUrl = ref('');
const currentUrl = ref('');

const playLive = () => {
  if (liveUrl.value) {
    currentUrl.value = liveUrl.value;
  }
};
</script>