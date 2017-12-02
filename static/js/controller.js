// (1) Adapted from - https://stackoverflow.com/questions/12368910/html-display-image-after-selecting-filename
// (2) Adapted from - https://www.w3schools.com/howto/howto_js_tab_header.asp
// (3) Adapted from - https://dev.opera.com/articles/html5-canvas-painting/example-2.html

// Function for selecting and uploading a file to the web page - (1)
function uploadImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#img')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };
        reader.readAsDataURL(input.files[0]);
    }
    // saveImage();
}


// Function for tab views (2)
function openTab(tabName, elmnt, color) {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }

    // Show the specific tab content
    document.getElementById(tabName).style.display = "block";

    // Add the specific color to the button used to open the tab content
    elmnt.style.backgroundColor = color;
}


// context = canvas.fillRect(255,255,255)


// Get the element with id="defaultOpen" and click on it - (3)
document.getElementById("defaultOpen").click();

// Function for creating a canvas and allowing the user to draw/erase - (3)
if (window.addEventListener) {

    var canvas, context, tool;
    

    window.addEventListener('load', function () {

        function init() {
            // Find the canvas element.
            canvas = document.getElementById('imageView');
            context = canvas.getContext('2d');
            context.fillStyle="#FFFFFF";
            context.fillRect(0, 0, 320, 200)


            if (!canvas) {
                alert('Error: I cannot find the canvas element!');
                return;
            }

            if (!canvas.getContext) {
                alert('Error: no canvas.getContext!');
                return;
            }

            // Get the 2D canvas context.
            if (!context) {
                alert('Error: failed to getContext!');
                return;
            }

            // Pencil tool instance.
            tool = new tool_pencil();



            // Attach the mousedown, mousemove and mouseup event listeners.
            canvas.addEventListener('mousedown', ev_canvas, false);
            canvas.addEventListener('mousemove', ev_canvas, false);
            canvas.addEventListener('mouseup', ev_canvas, false);

        }

        // This painting tool works like a drawing pencil which tracks the mouse 
        // movements.
        function tool_pencil() {
            var tool = this;
            this.started = false;

            // This is called when you start holding down the mouse button.
            // This starts the pencil drawing.
            this.mousedown = function (ev) {
                context.beginPath();
                context.moveTo(ev._x, ev._y);
                tool.started = true;
            };

            // This function is called every time you move the mouse. Obviously, it only 
            // draws if the tool.started state is set to true (when you are holding down 
            // the mouse button).
            this.mousemove = function (ev) {
                if (tool.started) {
                    context.lineTo(ev._x, ev._y);
                    context.lineWidth = 15;
                    context.stroke();

                }
            };

            // This is called when you release the mouse button.
            this.mouseup = function (ev) {
                if (tool.started) {
                    tool.mousemove(ev);
                    tool.started = false;
                }
            };
        }

        // The general-purpose event handler. This function just determines the mouse 
        // position relative to the canvas element.
        function ev_canvas(ev) {
            if (ev.layerX || ev.layerX == 0) { // Firefox
                ev._x = ev.layerX;
                ev._y = ev.layerY;
            } else if (ev.offsetX || ev.offsetX == 0) { // Opera
                ev._x = ev.offsetX;
                ev._y = ev.offsetY;
            }

            // Call the event handler of the tool.
            var func = tool[ev.type];
            if (func) {
                func(ev);
            }
        }

        init();

    }, false);
}

document.getElementById('clear').addEventListener('click', function () {
    context.fillStyle="#FFFFFF";
    context.fillRect(0, 0, 320, 200)

    
}, false);

function saveDrawing() {

    var img = canvas.toDataURL("images/png");
    console.log(img);


    $.ajax({
        url: '/upload',
        method: 'POST',
        data: img,
        success: function (res) {
            console.log(res);
        }, error: function (err) {
            console.log(err);
        }
    });
}

// function saveImage() {

//     var img = document.getElementById("img").getAttribute("src");
//     console.log(img);


//     // $.ajax({
//     //     url: '/upload',
//     //     method: 'POST',
//     //     data: img,
//     //     success: function (res) {
//     //         console.log(res);
//     //     }, error: function (err) {
//     //         console.log(err);
//     //     }
//     // });

// }