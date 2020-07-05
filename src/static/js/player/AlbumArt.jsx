import * as React from "react"
import { useState, useEffect } from "react"
import Zoom from "react-medium-image-zoom"

function buildItunesURL(song) {
  return (
    "https://itunes.apple.com/search?limit=1&entity=album&" +
    `term=${encodeURIComponent(`${song.album} ${song.artist}`)}`
  )
}

function AlbumArt({ song }) {
  const [imageSrc, setImageSrc] = useState(null)

  useEffect(() => {
    async function getArtworkURL() {
      fetch(buildItunesURL(song))
        .then((r) => r.json())
        .then((data) => {
          const { results } = data
          const [firstResult] = results
          const imageSrc =
            firstResult != null ? firstResult.artworkUrl100 : null
          setImageSrc(imageSrc)
        })
        .catch((reason) => {
          console.log("Cant get album art: " + reason)
        })
    }
    getArtworkURL()
  }, [song.at])

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
