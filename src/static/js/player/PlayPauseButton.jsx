import * as React from "react"
import styled, { css } from "styled-components"
import IosPlay from "react-ionicons/lib/IosPlay"
import IosSquare from "react-ionicons/lib/IosSquare"

const Button = styled.button`
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-right: 1px solid black;

  &:hover {
    background: black;

    * {
      fill: white;
    }
  }
`

// const Icon = styled.i.attrs({
//   "aria-label": (p) =>
//     p.playing ? "Stop radio playback." : "Listen to the radio.",
//   className: (p) => `fa fa-2x fa-${p.playing ? "pause" : "play"}`,
// })`
//   ${(p) =>
//     p.playing ||
//     css`
//       margin-left: 4px; /* to make the play button visually centered */
//     `};
// `

const StyledIosPlay = styled(IosPlay)`
  padding-left: 5px;
`

const StyledIosSquare = styled(IosSquare)``

const PlayPauseButton = ({ onClick, playing }) => (
  <Button onClick={() => onClick()}>
    {playing ? (
      <StyledIosSquare fontSize="25px" />
    ) : (
      <StyledIosPlay fontSize="50px" />
    )}
  </Button>
)
export default PlayPauseButton
