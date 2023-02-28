<!DOCTYPE html>
<html lang="en">
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
    <div id="leftDiv">
        <div id="insideDiv">
            <h1 id="LS">Light Show</h1>
            <h1 id="Controller">Controller</h1>
        </div>
    </div>
    <article>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <script>
            var strength =5;
            var speed =5;
            var color ="#ffffff";
            localStorage.setItem("color1", color);
            var length = 5;
            var count = 5;
            var type = "solid";

            function submitFunc() {
                strength = document.getElementById("strengthInput");
                speed = document.getElementById("speedInput");
                color = document.getElementById("color1");
                count = document.getElementById("countInput");
                elements = document.getElementsByClassName("type");
                for (let i=0;i<elements.length;i++){
                    if (elements[i].checked ===true){
                        type = elements[i].value;
                    }
                }

                localStorage.setItem("color1", color);
                localStorage.setItem("strength", strength);
                localStorage.setItem("speed", speed);
                localStorage.setItem("count", count);
                localStorage.setItem("type", type);
            }

            function initializeForm(){
                document.getElementById("strengthInput").value = localStorage.getItem("strength");
                document.getElementById("speedInput").value = localStorage.getItem("speed");
                if (!(document.getElementById("color1") == null)) {
                    document.getElementById("color1").value = color;
                }
                document.getElementById("countInput").value = localStorage.getItem("count");
                let foo =localStorage.getItem("type");
                document.getElementById(foo).checked = true;
            }


            //wave position and speed and color and length of wave
            //pulse count strength speed color
            //twinkle duration and speed and color
            function showOptions(){
                elements = document.getElementsByClassName("type");
                for (let i=0;i<elements.length;i++) {
                    if (elements[i].checked ===true){
                        var x = elements[i].value;
                    }
                }
                elements = document.getElementsByClassName("options");
                for (let i=0;i<elements.length;i++){
                    elements[i].style.display='none';
                }
                switch (x){
                    case 'pulse':
                        document.getElementById("colorsBorder").style.display='block';
                        document.getElementById("strength").style.display='block';
                        document.getElementById("count").style.display='block';
                        break;
                    case 'twinkle':
                        document.getElementById("colorsBorder").style.display='block';
                        document.getElementById("speed").style.display='block';
                        break;
                    case 'wave':
                        document.getElementById("colorsBorder").style.display='block';
                        document.getElementById("speed").style.display='block';
                        document.getElementById("strength").style.display='block';
                        break;
                    case 'cycle':
                        document.getElementById("speed").style.display='block';
                        break;
                    case 'solid':
                        document.getElementById("colorsBorder").style.display='block';
                        break;
                    case 'strobe':
                        document.getElementById("colorsBorder").style.display='block';
                        document.getElementById("speed").style.display='block';
                        break;
                    case 'microphone':
                        break;
                }
            }

            function setStrip(){
                elements = document.getElementsByClassName("type");
                for (let i=0;i<elements.length;i++){
                    if (elements[i].checked ===true){
                        type = elements[i].value;
                        elements[i].parentElement.style.borderBottom="white .1em solid"
                    }else{
                        elements[i].parentElement.style.borderBottom="0"
                    }
                }
                color = document.getElementById("color1").value;
                strip = document.getElementById("strip");
                backString = "linear-gradient(90deg, black, ";
                strength = document.getElementById("strengthInput").value;
                switch (type){
                    case 'pulse':
                        let nodes = document.getElementById("countInput").value;
                        for (i=0;i<nodes;i++){
                            for (j=0;j<strength;j++){
                                backString+=color+", "
                            }
                            backString+="black";
                            if(i<nodes-1){
                                backString+=", ";
                            }
                        }
                        backString+=")";
                        strip.style.background=backString;
                        // document.getElementById("strength").style.display='block';
                        // document.getElementById("count").style.display='block';
                        //

                        break;
                    case 'twinkle':
                        for(let i=0;i<30;i++){
                            backString+=color+", black, ";
                        }
                        backString+=color+", black)";
                        strip.style.background=backString;
                        // document.getElementById("speed").style.display='block';

                        break;
                    case 'wave':
                        strip.style.background="linear-gradient(90deg,black,"+color+" "+strength*9+"%)";

                        // document.getElementById("speed").style.display='block';
                        // document.getElementById("strength").style.display='block';
                        break;
                    case 'cycle':
                        backString = "linear-gradient(90deg";
                        for(let i=0;i<10;i++){
                            backString+=", rgb("+Math.floor(Math.random() * 255)+", "+Math.floor(Math.random() * 255)+", "+Math.floor(Math.random() * 255)+")";
                        }
                        backString+=")";
                        strip.style.background=backString;
                        break;
                    case 'solid':
                        strip.style.background=color;
                        break;
                    case 'strobe':
                        for(let i=0;i<40;i++){
                            backString+=color+", black, ";
                        }
                        backString+=color+", black)";
                        strip.style.background=backString;
                        break;
                    case 'microphone':
                        strip.style.background="linear-gradient(90deg,black, rgb("+Math.floor(Math.random() * 255)+", "+Math.floor(Math.random() * 255)+", "+Math.floor(Math.random() * 255)+"))";
                        break;
                }


            }
            //             Added from button.js

            var submitForm = document.getElementById("submit_button");
            var offButton = document.getElementById("offButtonDiv");

            //             submitForm.click(sendDataToPython);

            function sendDataToPython()
            {
                elements = document.getElementsByClassName("type");

                for (let i = 0; i < elements.length; i++){
                    if (elements[i].checked === true){
                        type = elements[i].value;
                    }
                }

                switch (type)
                {
                    case 'pulse':
                        myColor = document.getElementById("color1").value;
                        myColor = convertColor(myColor);
                        ajaxString="/pulse/";
                        count = document.getElementById("countInput").value;
                        ajaxString+=(count+"/");
                        strength = document.getElementById("strengthInput").value;
                        ajaxString+=(strength+"/");
                        ajaxString+=(myColor[0]+"/"+myColor[1]+"/"+myColor[2]);
                        runAjax();
                        break;
                    case 'twinkle':
                        myColor = document.getElementById("color1").value;
                        myColor = convertColor(myColor);
                        ajaxString="/twinkle/";
                        speed = document.getElementById("speedInput").value;
                        ajaxString+=(speed+"/");
                        ajaxString+=(myColor[0]+"/"+myColor[1]+"/"+myColor[2]);
                        runAjax();
                        break;
                    case 'wave':
                        myColor = document.getElementById("color1").value;
                        myColor = convertColor(myColor);
                        ajaxString="/wave/";
                        strength = document.getElementById("strengthInput").value;
                        speed =document.getElementById("speedInput").value;
                        ajaxString+=(strength+"/");
                        ajaxString+=(speed+"/");
                        ajaxString+=(myColor[0]+"/"+myColor[1]+"/"+myColor[2]);
                        runAjax();
                        break;
                    case 'cycle'://todo cycle
                        speed = document.getElementById("speedInput").value;
                        ajaxString="/cycle/"+speed;
                        runAjax();
                        break;
                    case 'solid':
                        let color = document.getElementById("color1").value;
                        let colorArray = new Array(3);
                        colorArray=convertColor(color);
                        ajaxString=("/solid/" + colorArray[0] + "/" + colorArray[1] + "/" + colorArray[2])
                        console.log("running solid")
                        runAjax();
                        break;
                    case 'strobe':
                        myColor = document.getElementById("color1").value;
                        myColor = convertColor(myColor);
                        ajaxString="/strobe/";
                        speed = document.getElementById("speedInput").value;
                        ajaxString+=(speed+"/");
                        ajaxString+=(myColor[0]+"/"+myColor[1]+"/"+myColor[2]);
                        runAjax();
                        break;
                    case 'microphone':
                        ajaxString="/microphone";
                        runAjax();
                        break;

                }

            }
            function convertColor(color) {
                let colorArray = new Array(3);
                console.log(color);
                let red_hex = color.substring(1, 3);
                let green_hex = color.substring(3, 5);
                let blue_hex = color.substring(5, 7);

                colorArray[0] = parseInt(red_hex, 16);
                colorArray[1] = parseInt(green_hex, 16);
                colorArray[2] = parseInt(blue_hex, 16);
                return colorArray;
            }

            function runAjax(){
                $.ajax({
                    url: ajaxString,
                    type: "post",
                    success: function(response) {
                        console.log(response);
                    }
                });
            }


            function off() {
                ajaxString="/led_off"
                runAjax();
            }

            window.onload = showOptions;
            window.onload = initializeForm;
        </script>
        <form id="myForm" onsubmit="submitFunc();" action="" method="post">
            <div id="optionsDiv">
                <div class="optionsSubDiv">
                    <input type="radio" oninput="showOptions(); setStrip()" id="solid" name="type" class="type" value="solid">
                    <label for="solid">Solid</label>
                </div>
                <div class="optionsSubDiv">
                    <input type="radio" oninput="showOptions(); setStrip()" id="cycle" name="type" class="type" value="cycle">
                    <label for="cycle">Cycle</label>
                </div>
                <div class="optionsSubDiv">
                    <input type="radio" oninput="showOptions(); setStrip()" id="pulse" name="type" class="type" value="pulse">
                    <label for="pulse">Pulse</label>
                </div>
                <div class="optionsSubDiv">
                    <input type="radio" oninput="showOptions(); setStrip()" id="wave" name="type" class="type" value="wave">
                    <label for="wave">Wave</label>
                </div>
                <div class="optionsSubDiv">
                    <input type="radio" oninput="showOptions(); setStrip()" id="twinkle" name="type" class="type" value="twinkle">
                    <label for="twinkle">Twinkle</label>
                </div>
                <div class="optionsSubDiv">
                    <input type="radio" oninput="showOptions(); setStrip()" id="strobe" name="type" class="type" value="strobe">
                    <label for="strobe">Strobe</label>
                </div>
                <div class="optionsSubDiv">
                    <input type="radio" oninput="showOptions(); setStrip()" id="microphone" name="type" class="type" value="microphone">
                    <label for="microphone">Microphone</label>
                </div>
            </div>
            <div id="rightDiv">
                <div id="colorsBorder" class="options" style="display: none">
                    <div id="colors">
                        <input type="color" name="color1" id="color1" value=color class="color" oninput="setStrip()"</input>
                        <label>Color</label>
                    </div>
                </div>
                <div id="speed" class="options" style="display: none">
                    <h2>SPEED:</h2>
                    <input id="speedInput" oninput="setStrip()" name="speedInput" type="range" min="1" max="10">
                </div>
                <div id="strength" class="options" style="display: none">
                    <h2>STRENGTH:</h2>
                    <input id="strengthInput" oninput="setStrip()" name="strengthInput" type="range" min="1" max="10">
                </div>
                <div id="length" class="options" style="display: none">
                    <h2>LENGTH:</h2>
                    <input id="lengthInput" oninput="setStrip()" name="lengthInput" type="range" min="1" max="10">
                </div>
                <div id="count" class="options" style="display: none">
                    <h2>NUMBER OF NODES:</h2>
                    <input id="countInput" oninput="setStrip()" name="countInput" type="range" min="1" max="10">
                </div>
                <div id="onOff">
                    <div id="submitDiv" >
                        <input type="submit" onclick="sendDataToPython()" value="PLAY" id="submit_button">
                    </div>
                    <div id="offButtonDiv">
                        <button id="off_led_button" onclick="off()">OFF</button>
                    </div>
                </div>
        </form>

        </div>
    </article>
    <div id="corner"></div>
    <div id="div1">
        <div id="t1Cover1"></div>
        <div id="t1Cover2"></div>
        <div class="triangle" id="t1"></div>
    </div>
    <div id="strip">
    </div>
</body>
</html>