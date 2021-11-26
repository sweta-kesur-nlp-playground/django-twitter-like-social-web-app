// settins of variables for playing and pausing audio files using js
var x = document.getElementById("sound1");
var x2 = document.getElementById("sound2");
var x3 = document.getElementById("sound3");
var x4 = document.getElementById("sound4");
var x5 = document.getElementById("sound5");

const y1 = document.getElementById("play1");
const p1 = document.getElementById("pause1");

const y2 = document.getElementById("play2");
const p2 = document.getElementById("pause2");

const y3 = document.getElementById("play3");
const p3 = document.getElementById("pause3");

const y4 = document.getElementById("play4");
const p4 = document.getElementById("pause4");

const y5 = document.getElementById("play5");
const p5 = document.getElementById("pause5");

const divsToHide = document.getElementsByClassName("pause"); //divsToHide is an array
const divsToShow = document.getElementsByClassName("play"); //divsToHide is an array

function hidePause() {
    for (var i = 0; i < divsToHide.length; i++) {
        divsToHide[i].style.display = "none";
        divsToShow[i].style.display = "inline";
    }
}

/**IF AUDIO ENDED***/

x.onended = function () {
    y1.style.display = "inline";
    p1.style.display = "none";
};

/**PLAY AUDIO***/

function playAudio() {
    hidePause();
    y1.style.display = "none";
    p1.style.display = "inline";
    x.play();
}
/**PAUSE AUDIO***/
function pauseAudio() {
    y1.style.display = "inline";
    p1.style.display = "none";
    x.pause();
}

/****2nd AUIOD****/

function playAudio2() {
    hidePause();
    y2.style.display = "none";
    p2.style.display = "inline";
    x2.play();
}

function pauseAudio2() {
    y2.style.display = "inline";
    p2.style.display = "none";
    x2.pause();
}

/****3rd AUIOD****/

function playAudio3() {
    hidePause();
    y3.style.display = "none";
    p3.style.display = "inline";
    x3.play();
}

function pauseAudio3() {
    y3.style.display = "inline";
    p3.style.display = "none";
    x3.pause();
}

/****4th AUIOD****/

function playAudio4() {
    hidePause();
    y4.style.display = "none";
    p4.style.display = "inline";
    x4.play();
}

function pauseAudio4() {
    y4.style.display = "inline";
    p4.style.display = "none";
    x4.pause();
}

/****5th AUIOD****/

function playAudio5() {
    hidePause();
    y5.style.display = "none";
    p5.style.display = "inline";
    x5.play();
}

function pauseAudio5() {
    y5.style.display = "inline";
    p5.style.display = "none";
    x5.pause();
}

// Ajax code to play audio files on home page
jQuery(document).ready(function () {
    jQuery(function () {
        jQuery("audio").on("play", function () {
            jQuery("audio")
                .not(this)
                .each(function (index, audio) {
                    audio.pause();
                    audio.currentTime = 0;
                });
        });
    });
});

// Ajax code for toggling the arrow up and down button for footer section
jQuery(document).ready(function () {
    jQuery(".arrow-up").on("click", function () {
        jQuery(".arrow-up").toggleClass("reverse");
        jQuery(".footer")
            .toggleClass("up")
            .delay(4000)
            .queue(function (next) {
                $(this).removeClass("up");
                next();
            });
        jQuery(".arrow-up")
            .toggleClass("reverse")
            .delay(4000)
            .queue(function (next) {
                $(this).removeClass("reverse");
                next();
            });
    });

    jQuery(window).on("resize", function (event) {
        jQuery(".rc_nav").removeClass("responsive");
        jQuery("#section").css("display", "block");
    });
});

