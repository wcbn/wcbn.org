// Trix.config.attachments.preview.caption = {
//   name: false,
//   size: false,
// }

// const uploadAttachment = (attachment) => {
//   // console.log(attachment)
//   const file = attachment
//   console.log(file)

// const data = {}
// data['file'] = file

// console.log(data)

// fetch("/upload_media", { method: "POST", body: JSON.stringify(data) })
//   .then((r) => r.json())
//   .then((x) => {
//     console.log(x)
//   })

// Example POST method implementation:
// async function postData(url, data) {
//   // Default options are marked with *

//   const response = await fetch(url, {
//     method: "POST", // *GET, POST, PUT, DELETE, etc.
//     mode: "cors", // no-cors, *cors, same-origin
//     cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
//     credentials: "same-origin", // include, *same-origin, omit
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
//       "enctype": "multipart/form-data"
//     },
//     redirect: "follow", // manual, *follow, error
//     referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
//     body: JSON.stringify(data), // body data type must match "Content-Type" header
//   })
//   return response.json() // parses JSON response into native JavaScript objects
// }

// postData("/upload_media/", { file: file }).then((data) => {
//   console.log(data) // JSON data parsed by `data.json()` call
// })

// let upload = new DirectUpload(file, '/rails/active_storage/direct_uploads')

// upload.create((error, blob) => {
//   if (error) {
//     console.log('Error uploading file from Trix')
//   } else {
//     // Add an appropriately-named hidden input to the form with a
//     //  value of blob.signed_id so that the blob ids will be
//     //  transmitted in the normal upload flow
//     const hiddenField = document.createElement('input')
//     hiddenField.setAttribute('type', 'hidden')
//     hiddenField.name = 'dj[images][]'
//     hiddenField.setAttribute('value', blob.signed_id)
//     document.querySelector('form').appendChild(hiddenField)

//     return attachment.setAttributes({
//       url:
//         '/rails/active_storage/blobs/' +
//         blob.signed_id +
//         '/' +
//         encodeURIComponent(blob.filename),
//     })
//   }
// })
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
