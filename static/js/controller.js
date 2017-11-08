// Adapted from - https://stackoverflow.com/questions/12368910/html-display-image-after-selecting-filename

$("input").change(function(e) {
    
        for (var i = 0; i < e.originalEvent.srcElement.files.length; i++) {
            
            var file = e.originalEvent.srcElement.files[i];
            
            var img = document.createElement("img");
            var reader = new FileReader();
            
            reader.onloadend = function() {
                 img.src = reader.result;
            }
            
            reader.readAsDataURL(file);
            $("input").after(img);
        }
    });