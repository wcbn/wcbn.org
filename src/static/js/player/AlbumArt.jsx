import * as React from "react"
import { useState, useEffect } from "react"
import Zoom from "react-medium-image-zoom"

// function buildItunesURL(song) {
//   return (
//     "https://itunes.apple.com/search?limit=1&entity=album&" +
//     `term=${encodeURIComponent(`${song.album} ${song.artist}`)}` +
//     `&callback="handleItunes"`
//   )
// }

// function AlbumArt(props) {
//   const { song } = props
//   const [imageSrc, setImageSrc] = useState(null)

//   useEffect(() => {
//     async function getArtworkURL() {
//       fetch(buildItunesURL(song))
//         .then((r) => r.json())
//         .then((data) => {
//           const { results } = data
//           const [firstResult] = results
//           const imageSrc =
//             firstResult != null ? firstResult.artworkUrl100 : null
//           setImageSrc(imageSrc)
//         })
//         .catch((reason) => {
//           console.log("Cant fetch album artwork: " + reason)
//         })
//     }
//     getArtworkURL()
//   }, [song.at])

//   console.log(imageSrc)

//   if (imageSrc === null) return null
//   return (
//     <Zoom>
//       <img
//         src={imageSrc.replace(/100x100/, "1000x1000")}
//         alt="Album Artwork"
//         className="h-10 w-10"
//       />
//     </Zoom>
//   )
// }

class AlbumArt extends React.Component {
  state = { imageSrc: null }

  componentDidMount() {
    this._getArtworkURL()
  }

  componentDidUpdate(prevProps) {
    if (this.props.song !== prevProps.song) this._getArtworkURL()
  }

  render() {
    console.log(this.state.imageSrc)
    if (this.state.imageSrc == null) return null
    return (
      <Zoom>
        <img
          src={this.state.imageSrc.replace(/100x100/, "1000x1000")}
          alt="Album Artwork"
          className="h-10 w-10"
        />
      </Zoom>
    )
  }

  _getArtworkURL() {
    fetch(this._queryURL())
      .then((r) => r.json())
      .then((data) => {
        const { results } = data
        const [firstResult] = results
        const imageSrc = firstResult != null ? firstResult.artworkUrl100 : null
        this.setState({ imageSrc })
      })
  }

  /**
   * The high-resolution image is lazy-loaded when the album art is zoomed in
   */
  _largeImageSrc() {
    const { imageSrc } = this.state
    if (imageSrc == null) return null
    return imageSrc.replace(/100x100/, "1000x1000")
  }

  _queryURL() {
    const { album, artist } = this.props.song
    return (
      "https://itunes.apple.com/search?limit=1&version=2&entity=album&" +
      `term=${encodeURIComponent(`${album} ${artist}`)}`
    )
  }
}

export default AlbumArt
