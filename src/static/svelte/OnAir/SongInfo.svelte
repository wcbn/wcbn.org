<script>
  export let isPlaying
  export let song

  // NOTE one-liner for all song data
  // function buildStrongStr() {
  //   const { artist, name, album, label, year } = song
  //   const artistName = `${artist ? artist + ': ' : ''}“${name}”`
  //   let albumLabelYear = `${album ? album : ''}`
  //   if (label && year !== null) {
  //     albumLabelYear += ` (${label}, ${year})`
  //   }

  //   return albumLabelYear ? `${artistName} — ${albumLabelYear}` : artistName
  // }

  function getLineOne() {
    const { artist, name } = song
    return `${artist ? artist + ': ' : ''}“${name}”`
  }

  function getLineTwo() {
    const { album, label, year } = song
    let result = `${album ? album : ''}`
    if (label && year !== null) {
      result += ` (${label}, ${year})`
    }
    return result
  }

  $: lineOne = getLineOne()
  $: lineTwo = getLineTwo()
  $: alt = '← Listen to 88.3 FM in your browser'
</script>

<section>
  {#if isPlaying}
    <p>{lineOne}</p>
    <p>{lineTwo}</p>
  {:else}
    <p>{alt}</p>
  {/if}
</section>
