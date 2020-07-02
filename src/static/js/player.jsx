import React from "react";
import { render } from "react-dom";

const element = (
  <audio controls src="http://floyd.wcbn.org:8000/wcbn-hd.mp3">
    Your browser does not support the
    <code>audio</code> element.
  </audio>
);

const Container = document.getElementById("floyd");
if (Container) {
  render(element, Container);
}
