<script>
  export let isPlaying
  export let song

  function buildStrongStr() {
    const { artist, name, album, label, year } = song
    const artistName = `${artist ? artist + ': ' : ''}“${name}”`
    let albumLabelYear = `${album ? album : ''}`
    if (label && year !== null) {
      albumLabelYear += ` (${label}, ${year})`
    }

    return albumLabelYear ? `${artistName} — ${albumLabelYear}` : artistName
  }

  $: text = isPlaying ? buildStrongStr() : '← Listen to 88.3 FM in your browser'
</script>

<p>{text}</p>
