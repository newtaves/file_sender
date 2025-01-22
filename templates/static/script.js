document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.getElementById("file-input")
    const fileList = document.getElementById("file-list")
  
    fileInput.addEventListener("change", (e) => {
      fileList.innerHTML = "" // Clear previous list
      const files = e.target.files
  
      if (files.length > 0) {
        const list = document.createElement("ul")
        for (let i = 0; i < files.length; i++) {
          const listItem = document.createElement("li")
          listItem.textContent = files[i].name
          list.appendChild(listItem)
        }
        fileList.appendChild(list)
      } else {
        fileList.textContent = "No files selected"
      }
    })
  })
  
  