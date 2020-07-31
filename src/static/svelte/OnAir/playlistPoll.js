const BASE_URL = 'https://app.wcbn.org'
const POLL_INTERVAL = 40000

export default async function playlistPoll() {
  fetch(BASE_URL + '/playlist.json')
    .then(
      (response) => {
        if (response.ok) {
          return response
        } else {
          const error = new Error(
            `Error ${response.status}: ${response.statusText}`
          )
          throw error
        }
      },
      (error) => {
        const errMess = new Error(error.message)
        throw errMess
      }
    )
    .then((response) => response.json())
    .then((data) => {
      // data.on_air.songs.forEach((song: SongAPI) => {
      //   song.at = humanizeTime(song.at)
      // })
      // return data.on_air
      return {
        song: {
          name: 'Icky Thump',
          artist: 'The White Stripes',
          album: 'Icky Thump',
          label: 'jagwuar',
          year: '2010',
          at: '5pm',
        },
      }
    })
    .catch((error) => {
      // ignore
    })
}
