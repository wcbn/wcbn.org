<script>
  import PlayPauseButton from './PlayPauseButton.svelte'
  import OnAir from './OnAir/OnAir.svelte'

  const STREAM_URL = 'http://floyd.wcbn.org:8000/wcbn-hd.mp3'
  const audio = document.createElement('audio')
  let isPlaying = false

  const handlePlayPause = function () {
    if (isPlaying) {
      audio.src = ''
      audio.pause()
      setTimeout(function () {
        audio.load() // This stops the stream from downloading
      })
    } else {
      if (!audio.getAttribute('src')) {
        audio.src = STREAM_URL
        audio.load() // This restarts the stream download
      }
      audio.play()
    }

    isPlaying = !isPlaying
  }
</script>

<div>
  <div>
    <PlayPauseButton {isPlaying} {handlePlayPause} />
    <OnAir {isPlaying} />
  </div>
</div>
