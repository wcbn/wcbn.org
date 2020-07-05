import * as React from "react"
import styled from "styled-components"

const InfoText = ({ onAir, playing }) => {
  const { artist, name, album, label, year } = onAir["songs"][0]

  let texts = ["← Listen to 88.3 FM in your browser", ""]

  if (playing) {
    const t1 = `${artist ? artist + ": " : ""}“${name}”`
    let t2 = `${album ? album : ""}`
    if (label && year !== null) {
      t2 += ` (${label}, ${year})`
    }

    texts = [t1, t2]
  }

  return (
    <div className="flex justify-center items-center text-sm mx-4">
      <strong>{texts[0]}</strong>
      <span className="ml-2">{texts[1] && " — "}</span>
      <span className="ml-2">{texts[1]}</span>
    </div>
  )
}
export default InfoText
