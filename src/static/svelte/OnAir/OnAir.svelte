<script>
  import SongInfo from './SongInfo.svelte'
  import AlbumArt from './AlbumArt.svelte'
  export let isPlaying
  // import playlistPoll from './playlistPoll'

  const BASE_URL = 'https://app.wcbn.org'
  const POLL_INTERVAL = 10000

  const ickyThump = {
    name: 'Icky Thump',
    artist: 'The White Stripes',
    album: 'Icky Thump',
    label: 'jagwuar',
    year: '2010',
    at: '5pm',
  }

  let song = ickyThump

  setInterval(() => {
    // fetch(BASE_URL + '/playlist.json')
    //   .then(
    //     (response) => {
    //       if (response.ok) {
    //         return response
    //       } else {
    //         const error = new Error(
    //           `Error ${response.status}: ${response.statusText}`
    //         )
    //         throw error
    //       }
    //     },
    //     (error) => {
    //       const errMess = new Error(error.message)
    //       throw errMess
    //     }
    //   )
    //   .then((response) => response.json())
    //   .then((data) => {
    //     // data.on_air.songs.forEach((song: SongAPI) => {
    //     //   song.at = humanizeTime(song.at)
    //     // })
    //     console.log(data.on_air)
    //     // return data.on_air
    //     onAir = {
    //       song: {
    //         name: 'Icky Thump',
    //         artist: 'The White Stripes',
    //         album: 'Icky Thump',
    //         label: 'jagwuar',
    //         year: '2010',
    //         at: '5pm',
    //       },
    //     }
    //   })
    //   .catch(() => {
    //     // ignore
    //   })

    song = ickyThump // || null
  }, POLL_INTERVAL)
</script>

<div>
  <AlbumArt {isPlaying} {song} />
  <SongInfo {isPlaying} {song} />
</div>
