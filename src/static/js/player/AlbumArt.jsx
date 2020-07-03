import * as React from "react"
import { useState, useEffect } from "react"
import Zoom from "react-medium-image-zoom"

function buildItunesURL(song) {
  console.log("getting itunes url")
  const { album, artist } = song
  return (
    "https://itunes.apple.com/search?limit=1&version=2&entity=album&" +
    `term=${encodeURIComponent(`${album} ${artist}`)}`
  )
}

function AlbumArt(props) {
  const { song } = props
  const [imageSrc, setImageSrc] = useState(null)

  useEffect(() => {
    async function getArtworkURL() {
      console.log("getting artwork")
      fetch(buildItunesURL(song))
        .then((r) => r.json())
        .then((data) => {
          const { results } = data
          const [firstResult] = results
          const imageSrc =
            firstResult != null ? firstResult.artworkUrl100 : null
          setImageSrc(imageSrc)
        })
    }
    getArtworkURL()
  }, [song.at])

  console.log(imageSrc)

  if (imageSrc === null) return null
  return (
    <Zoom>
      <img
        src={imageSrc.replace(/100x100/, "1000x1000")}
        alt="Album Artwork"
        className="h-10 w-10"
      />
    </Zoom>
  )
}

export default AlbumArt
