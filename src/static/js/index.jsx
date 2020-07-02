// turbolinks
var Turbolinks = require("turbolinks");
Turbolinks.start();

// google analytics
window.subscribeGTAG = (GA_MEASUREMENT_ID) => {
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    dataLayer.push(arguments);
  }
  gtag("js", new Date());

  document.addEventListener("turbolinks:load", (event) => {
    if (typeof gtag == "function") {
      gtag("config", GA_MEASUREMENT_ID, {
        page_title: event.target.title,
        page_path: event.data.url.replace(
          window.location.protocol +
            "//" +
            window.location.hostname +
            (location.port && ":" + location.port),
          ""
        ),
      });
    }
  });
};

// TODO only add listener in dev
// django debug toolbar
document.addEventListener("turbolinks:load", (event) => {
  if ("djdt" in window) {
    setTimeout(() => {
      window.djdt.init();
    }, 1000); //race condition? #hack
  }
});

// jquery
import jQuery from "jquery";
window.$ = window.jQuery = jQuery;

// global since recaptcha injects itself before anything else *rolls eyes*
window.enableFormSubmit = () => {
  document
    .querySelector("[data-callback='enableFormSubmit']")
    .closest("form")
    .querySelector('input[type="submit"]')
    .removeAttribute("disabled");
};
