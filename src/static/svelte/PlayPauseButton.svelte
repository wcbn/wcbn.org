<script>
  export let handlePlayPause
  export let isPlaying
</script>

<button on:click={handlePlayPause} data-playing={isPlaying}>
  <span>{isPlaying ? '■' : '►'}</span>
</button>
