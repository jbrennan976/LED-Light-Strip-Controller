<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset="UTF-8">
    <title>Light Display Final Project</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Noel Desmarais, Joe Brennan, Julian Henry">
    <meta name="description" content="Website to control a light strip - CS121A Final">
    <link rel="stylesheet" href="../static/custom.css?version=<?php print time(); ?>" type="text/css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lora:400,700|Montserrat:300">
    <!--    <link rel="stylesheet" media="(max-width: 800px)" href="css/custom-tablet.css?version=--><!--" type="text/css">-->
    <!--    <link rel="stylesheet" media="(max-width: 600px)" href="css/custom-phone.css?version=--><!--" type="text/css">-->
</head>
<body>
<main>
    <h1>Light Show Controller</h1>
    <article>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <script>
            function showColors() {
                var x = document.getElementById("numColors").value;
                var elements = document.getElementsByClassName("color");
                while(elements.length>x*2){
                    elements[elements.length-1].parentNode.removeChild(elements[elements.length-1]);
                }

                for (let i = elements.length/2+1; i <= x; i++) {
                    let input = document.createElement("input");
                    input.type="color";
                    input.id = "color " + i;
                    input.name = "color";
                    input.value = "#000000";
                    input.setAttribute("class", "color");
                    let label = document.createElement("label");
                    label.htmlFor = "color "+ i;
                    label.setAttribute("class", "color");
                    const node = document.createTextNode("Color "+i);
                    label.appendChild(node);
                    element = document.getElementById("colors");
                    element.appendChild(input);
                    element.appendChild(label);
                }
            }
            function showColors(x) {
                for (let i = 1; i <= x; i++) {
                    let input = document.createElement("input");
                    input.type="color";
                    input.id = "color " + i;
                    input.name = "color";
                    input.value = "#000000";
                    input.setAttribute("class", "color");
                    let label = document.createElement("label");
                    label.htmlFor = "color "+ i;
                    label.setAttribute("class", "color");
                    const node = document.createTextNode("Color "+i);
                    label.appendChild(node);
                    element = document.getElementById("colors");
                    element.appendChild(input);
                    element.appendChild(label);
                }
            }
            //wave position and speed and color and length of wave
            //pulse count strength speed color
            //twinkle duration and speed and color
            function showOptions(){
                document.getElementById('default').style.display='none';
                let elements = document.getElementsByClassName("options");
                for (let i=0;i<elements.length;i++){
                    elements[i].style.display='none';
                }
                document.getElementById("colorOption").style.display='none';
                let x = document.getElementById("type").value;
                switch (x){
                    case 'pulse':
                        document.getElementById("strength").style.display='block';
                        showOptions(1);
                        break;
                    case 'twinkle':
                        document.getElementById("speed").style.display='block';
                        document.getElementById("duration").style.display='block';
                        showOptions(1);
                        break;
                    case 'wave':
                        document.getElementById("speed").style.display='block';
                        document.getElementById("position").style.display='block';
                        document.getElementById("length").style.display='block';
                        showOptions(1);
                        break;
                    case 'chaser':
                        document.getElementById("speed").style.display='block';
                        document.getElementById("length").style.display='block';
                        break;
                    case 'solid':
                        showColors(1);
                        break;
                    case 'block':
                        document.getElementById("colorOption").style.display='block';
                        break;
                }
            }

            var form = $("#myForm");
            form.submit(function() {
                console.log("in php submit");
                    $.ajax({
                        url: "/submit",
                        type: "post",
                        success: function(response) {
                            console.log(response);
                        }
                    });
            })
            function submitForm() {
                console.log("submit function called");
                $.ajax({
                    url: "/submit",
                    type: "post",
                    success: function (response) {
                        console.log(response);
                    }
                });
            }
        </script>

        <form id="myForm" method="post">
            <div>
                <h2>Select the type of the show:</h2>
                <select name="type" oninput="showOptions()" id="type">
                    <option value="choose" id="default">Choose one...</option>
                    <option value="chaser">Chaser</option>
                    <option value="solid">Solid</option>
                    <option value="block">Block</option>
                    <option value="pulse">Pulse</option>
                    <option value="wave">Wave</option>
                    <option value="twinkle">Twinkle</option>
                </select>
            </div>

            <div class="options" id="colorOption" style="display: none">
                <h2>Choose the number of colors (1-10)</h2>
                <select name="numColors" oninput="showColors()" id="numColors">
                    <?php
                    for ($i=1;$i<=10;$i++){
                        print('<option value="'.$i.'">'.$i.'</option>');
                    }
                    ?>
                </select>
            </div>
            <div id="colors"></div>
            <div id="position" class="options" style="display: none">
                <h2>Select a starting position:</h2>
                <input type="range" min="1" max="100" value="50">
            </div>
            <div id="speed" class="options" style="display: none">
                <h2>Select a speed:</h2>
                <input type="range" min="1" max="100" value="50">
            </div>
            <div id="strength" class="options" style="display: none">
                <h2>Select a strength:</h2>
                <input type="range" min="1" max="10" value="5">
            </div>
            <div id="length" class="options" style="display: none">
                <h2>Select a length:</h2>
                <input type="range" min="1" max="10" value="5">
            </div>
            <input id="submit" type="submit" value="Run Display">
        </form>
    </article>
</main>
</body>
