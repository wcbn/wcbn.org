import React from "react";
import { render } from "react-dom";
import Player from './player/index'

const container = document.getElementById("floyd");
if (container) {
  render(<Player />, container);
}
