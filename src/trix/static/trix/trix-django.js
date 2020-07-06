// Trix.config.attachments.preview.caption = {
//   name: false,
//   size: false,
// }

function uploadAttachment(attachment) {
  uploadFile(attachment.file, setProgress, setAttributes)

  function setProgress(progress) {
    attachment.setUploadProgress(progress)
  }

  function setAttributes(attributes) {
    attachment.setAttributes(attributes)
  }
}

function uploadFile(file, progressCallback, successCallback) {
  var key = createStorageKey(file)
  var formData = createFormData(key, file)
  var xhr = new XMLHttpRequest()
  xhr.open("POST", "/upload_media/", true)
  xhr.setRequestHeader(
    "X-CSRFToken",
    document.querySelector("[name=csrfmiddlewaretoken]").value
  )
  // xhr.setRequestHeader("Content-Type", "application/json",)
  xhr.setRequestHeader("enctype", "multipart/form-data")

  xhr.upload.addEventListener("progress", function (event) {
    var progress = (event.loaded / event.total) * 100
    progressCallback(progress)
  })

  xhr.addEventListener("load", function (event) {
    if (xhr.status == 200) {
      console.log(xhr.response)
      resp = JSON.parse(xhr.response)

      if (resp.message === "OK") {
        media_url = resp.url
        var attributes = {
          url: media_url,
          href: media_url + "?content-disposition=attachment",
        }
        successCallback(attributes)
      } else {
        alert(`File Upload Failed: ${resp.message}`)
      }
    } else {
      alert(`Error ${xhr.status}: ${xhr.statusText}`)
    }
  })

  xhr.send(formData)
}

function createStorageKey(file) {
  var date = new Date()
  var day = date.toISOString().slice(0, 10)
  var name = date.getTime() + "-" + file.name
  return [day, name].join("_")
}

function createFormData(key, file) {
  var data = new FormData()
  data.append("title", key)
  data.append("Content-Type", file.type)
  data.append("file", file)
  return data
}

// Listen for the Trix attachment event to trigger upload
// If Trix editor has prevent-uploads data attribute, disallow upload
addEventListener("trix-attachment-add", (event) => {
  if (event.target.dataset.trixPreventUploads) {
    return event.preventDefault()
  }
  if (event.attachment.file) {
    return uploadAttachment(event.attachment)
  }
})
