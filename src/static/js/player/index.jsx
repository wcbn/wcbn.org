import * as React from "react"
import styled from "styled-components"

import PlayPauseButton from "./PlayPauseButton"
import SongInformation from "./SongInformation"
import InfoText from "./InfoText"
import AlbumArt from "./AlbumArt"

const WCBN_HD_STREAM_URL = "http://floyd.wcbn.org:8000/wcbn-hd.mp3"

const Container = styled.div`
  display: flex;
  flex: 1;
  border-top: 1px solid black;
  border-bottom: 1px solid black;

  * {
    flex-shrink: 0;
  }
`

class Player extends React.Component {
  audioElement
  state = {
    playing: false,
    onAir: {
      songs: [
        {
          name: "Icky Thump",
          artist: "The White Stripes",
          album: "Icky Thump",
          label: "jagwuar",
          year: "2010",
          at: "5pm"
        },
      ],
    },
  }

  constructor(props) {
    super(props)

    this.audioElement = document.createElement("audio")
  }

  componentDidMount() {
    //TODO listen to playlist websocket, or poll the playlist endpoint
    //TODO transform onAir JSON
    // const onAir = {
    //   songs: [
    //     {
    //       name: "Icky Thump",
    //       artist: "The White Stripes",
    //       album: "Icky Thump",
    //     },
    //   ],
    // }
    // this.setState({ onAir })
  }

  // handleChangeVolume = (e) => {
  //   this.audioElement.volume = parseInt(e.currentTarget.value) / 10
  // }

  render() {
    const { playing, onAir } = this.state

    return (
      <Container>
        <PlayPauseButton playing={playing} onClick={this.handlePlayPause} />
        <InfoText playing={playing} onAir={onAir} />
        {playing && <AlbumArt song={onAir.songs[0]} />}
      </Container>
    )
  }

  handlePlayPause = () => (this.state.playing ? this._pause() : this._play())

  _play = () =>
    this.setState({ playing: true }, () => {
      this.audioElement.src = WCBN_HD_STREAM_URL
      this.audioElement.play()
    })
  _pause = () =>
    this.setState({ playing: false }, () => {
      this.audioElement.pause()
      this.audioElement.src = ""
    })
}
export default Player
