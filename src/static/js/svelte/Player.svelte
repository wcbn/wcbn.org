<script>
  import PlayPause from './PlayPause.svelte'
  import InfoBar from './InfoBar.svelte'

  const STREAM_URL = 'http://floyd.wcbn.org:8000/wcbn-hd.mp3'
  let audio = document.createElement('audio')
  let isPlaying = false

  const handleClick = function () {
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

<dev>
  <PlayPause {isPlaying} {handleClick} />
  <InfoBar {isPlaying} />
</dev>