// (1) Adapted from - https://stackoverflow.com/questions/12368910/html-display-image-after-selecting-filename
// (2) Adapted from - https://www.w3schools.com/howto/howto_js_tab_header.asp
// (3) Adapted from - https://stackoverflow.com/questions/2368784/draw-on-html5-canvas-using-a-mouse

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

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

// Function for creating a canvas and allowing the user to draw/erase
var canvas, ctx, flag = false,
prevX = 0,
currX = 0,
prevY = 0,
currY = 0,
dot_flag = false;

var x = "black",
y = 2;

function init() {
canvas = document.getElementById('can');
ctx = canvas.getContext("2d");
w = canvas.width;
h = canvas.height;

canvas.addEventListener("mousemove", function(e) {
    findxy('move', e)
}, false);
canvas.addEventListener("mousedown", function(e) {
    findxy('down', e)
}, false);
canvas.addEventListener("mouseup", function(e) {
    findxy('up', e)
}, false);
canvas.addEventListener("mouseout", function(e) {
    findxy('out', e)
}, false);
}

function draw() {
ctx.beginPath();
ctx.moveTo(prevX, prevY);
ctx.lineTo(currX, currY);
ctx.strokeStyle = x;
ctx.lineWidth = y;
ctx.stroke();
ctx.closePath();
}

function erase() {
var m = confirm("Want to clear");
if (m) {
    ctx.clearRect(0, 0, w, h);
    document.getElementById("canvasimg").style.display = "none";
}
}

function findxy(res, e) {
if (res == 'down') {
    prevX = currX;
    prevY = currY;
    currX = e.clientX - canvas.offsetLeft - 235;
    currY = e.clientY - canvas.offsetTop - 28;

    flag = true;
    dot_flag = true;
    if (dot_flag) {
        ctx.beginPath();
        ctx.fillStyle = x;
        ctx.fillRect(currX, currY, 2, 2);
        ctx.closePath();
        dot_flag = false;
    }
}
if (res == 'up' || res == "out") {
    flag = false;
}
if (res == 'move') {
    if (flag) {
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft - 235;
        currY = e.clientY - canvas.offsetTop - 28;
        draw();
    }
}
}