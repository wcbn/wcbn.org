<script>
  export let isPlaying
  export let song
  import mediumZoom from 'medium-zoom'

  let imageSrc = getArtworkURL()

  function buildItunesURL() {
    return (
      'https://itunes.apple.com/search?limit=1&entity=album&' +
      `term=${encodeURIComponent(`${song.album} ${song.artist}`)}`
    )
  }

  async function getArtworkURL() {
    return await fetch(buildItunesURL())
      .then((r) => r.json())
      .then((data) => {
        const { results } = data
        const [firstResult] = results

        return firstResult
          ? firstResult.artworkUrl100.replace(/100x100/, '1000x1000')
          : null
      })
      .catch((reason) => {
        console.log('Cant get album art: ' + reason)
      })
  }

  setTimeout(() => {
    mediumZoom('#on-air-album-artwork')
  }, 1000)
</script>

<div class="album-art {isPlaying ? 'open' : 'closed'}">

  {#await imageSrc then src}
    <img id="on-air-album-artwork" {src} alt="Album Artwork" />
  {/await}

</div>
