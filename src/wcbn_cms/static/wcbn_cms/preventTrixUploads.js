window.addEventListener('load', function () {
  document
    .querySelectorAll('trix-editor')
    .forEach((editor) => editor.setAttribute('data-trix-prevent-uploads', true))
})
