var submitForm = $("#led_button");
var offButton = $("#off_led_button");
var myArray = new Array();
var ajaxString="";
var myColor;
var strength;
var speed;
var count;

submitForm.click(function() {
    var x = document.getElementById("type").value;
    switch (x){
        case 'pulse':
            myColor = document.getElementById("color 1").value;
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
            myColor = document.getElementById("color 1").value;
            myColor = convertColor(myColor);
            ajaxString="/twinkle/";
            strength = document.getElementById("speedInput").value;
            ajaxString+=(strength+"/");
            ajaxString+=(myColor[0]+"/"+myColor[1]+"/"+myColor[2]);
            runAjax();
            break;
        case 'wave':
            myColor = document.getElementById("color 1").value;
            myColor = convertColor(myColor);
            ajaxString="/wave/";
            strength = document.getElementById("strengthInput").value;
            speed =document.getElementById("speedInput").value;
            ajaxString+=(strength+"/");
            ajaxString+=(speed+"/");
            ajaxString+=(myColor[0]+"/"+myColor[1]+"/"+myColor[2]);
            runAjax();
            break;
        case 'chaser'://todo CHASER
            break;
        case 'solid':
            let color = document.getElementById("color 1").value;
            let colorArray = new Array(3);
            colorArray=convertColor(color);
            ajaxString=("/solid/" + colorArray[0] + "/" + colorArray[1] + "/" + colorArray[2])
            runAjax();
            break;
        case 'block':
            numColors = document.getElementById("numColors").value;
            for (let i=0;i<numColors;i++){
                let color = document.getElementById("color "+i).value;
                let myColor = convertColor(color);
                myArray[i]=myColor;
            }
            ajaxString="/wave/";
            ajaxString+=(document.getElementById("strength").value+"/");
            ajaxString+=(document.getElementById("speed").value+"/");
            ajaxString+=(numColors+"/");
            for (let j=0;j<myArray.length;j++){
                ajaxString+=(myArray[j][0]+"/"+myArray[j][1]+"/"+myArray[j][2]+"/");
            }
            runAjax();
            break;    }
    // let color = document.getElementById("color").value;
});
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


offButton.click(function() {
    ajaxString="/led_off"
    runAjax();
});
