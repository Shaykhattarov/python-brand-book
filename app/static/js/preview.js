document.getElementById('image-input').addEventListener('change', function () {
    var input = this;
    var imageContainer = document.getElementById('image-container');
    var previewImage = document.getElementById('preview-image');

    var file = input.files[0];

    if (file) {
        var reader = new FileReader();

        reader.onload = function (e) {
            imageContainer.style.background = 'none';
            previewImage.src = e.target.result;
        };

        reader.readAsDataURL(file);
    }
});