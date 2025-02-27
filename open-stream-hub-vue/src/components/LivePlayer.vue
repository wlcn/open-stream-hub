<template>
  <div class="w-full max-w-2xl mx-auto">
    <video ref="videoRef" controls class="w-full"></video>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import videojs from 'video.js';
import 'video.js/dist/video-js.css';
import Hls from 'hls.js';

const props = defineProps<{
  src: string;
}>();

const videoRef = ref<HTMLVideoElement | null>(null);

onMounted(() => {
  if (videoRef.value) {
    if (Hls.isSupported()) {
      const hls = new Hls();
      hls.loadSource(props.src);
      hls.attachMedia(videoRef.value);
    } else if (videoRef.value.canPlayType('application/vnd.apple.mpegurl')) {
      videoRef.value.src = props.src;
    }
  }
});

watch(
  () => props.src,
  (newSrc) => {
    if (videoRef.value) {
      if (Hls.isSupported()) {
        const hls = new Hls();
        hls.loadSource(newSrc);
        hls.attachMedia(videoRef.value);
      } else if (videoRef.value.canPlayType('application/vnd.apple.mpegurl')) {
        videoRef.value.src = newSrc;
      }
    }
  }
);
</script>