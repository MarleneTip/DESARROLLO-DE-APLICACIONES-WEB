const imageUrlInput = document.getElementById('image-url');
const addImageBtn = document.getElementById('add-image');
const deleteImageBtn = document.getElementById('delete-image');
const gallery = document.getElementById('gallery');

let selectedImage = null;

function addImage() {
    const url = imageUrlInput.value.trim();
    if (!url) {
        alert('Por favor ingresa una URL válida');
        return;
    }

    const img = document.createElement('img');
    img.src = url;

    img.addEventListener('click', () => {
        if (selectedImage) {
            selectedImage.classList.remove('selected');
        }
        img.classList.add('selected');
        selectedImage = img;
    });

    gallery.appendChild(img);
    imageUrlInput.value = '';
}

function deleteImage() {
    if (selectedImage) {
        gallery.removeChild(selectedImage);
        selectedImage = null;
    } else {
        alert('No hay ninguna imagen seleccionada');
    }
}

addImageBtn.addEventListener('click', addImage);
deleteImageBtn.addEventListener('click', deleteImage);
