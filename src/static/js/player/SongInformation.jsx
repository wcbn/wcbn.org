import * as React from "react"
import styled from "styled-components"

import { Motion, spring } from "react-motion"

import AlbumArt from "./AlbumArt"
import Volume from "./Volume"

const Container = styled.div`
  background-color: ${(props) => props.theme.blue};
  border-top-right-radius: 4px;
  display: flex;
  align-items: center;
`

const InfoBox = styled.div`
  max-width: 700px;
  max-height: 60px;
  padding: 0 15px;
  display: flex;
  align-items: flex-start;
  overflow: hidden;
`

const SongInformation = ({ song, visible, handleChangeVolume }) => {
  const { artist, name, album, label, year } = song
  return (
    <Motion style={{ x: spring(visible ? 0 : 1) }}>
      {({ x }) => (
        <Container
          style={{
            transform: `translate(calc(${x * -100}% + ${x * 4}px))`,
          }}
        >
          <Volume onChange={handleChangeVolume} />
          <InfoBox>
            <AlbumArt song={song} />
            <div>
              <div>
                <strong>
                  {artist && `${artist}: `}“{name}”
                </strong>
              </div>
              <div>
                <span>
                  <cite>{album}</cite>
                  {(label || year != null) &&
                    ` (${label}${label && year ? " " : ""}${year || ""})`}
                </span>
              </div>
            </div>
          </InfoBox>
        </Container>
      )}
    </Motion>
  )
}
export default SongInformation
