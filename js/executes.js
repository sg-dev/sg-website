//When document is ready
$(document).ready(function () {

    cardRowClasses();

    if ($("section").hasClass("isteam")) {
        teamConnections();
    }

    $(".hamburger").click(function () {
        $(this).toggleClass("is-active");
        $(".header__nav-level--root").slideToggle(500);
    });

    //When screen resizes
    $(window).resize(function () {
        cardRowClasses();

        if ($("section").hasClass("isteam")) teamConnections(true);
    });
});

/***********
 * Functions
 **********/

//Adds classes to cards depending on how many columns are displayed
function cardRowClasses() {
    $(".cardwrapper .card").removeClass("card__row1 card__row2 card__row3 card__row4");
    let colCount = 1;
    if ($(".cardwrapper__columnTeam").length) colCount = 4;
    else if ($(window).width() >= 980) colCount = 3;
    else if ($(window).width() < 980 && $(window).width() >= 700) colCount = 2;
    else if ($(window).width() < 700) colCount = 1;
    // 4 columns
    $(".cardwrapper .card").each(function (i) {
        if (i % colCount == 0) $(this).addClass("card__row1").data("row", 1);
        else if (i % colCount == 1) $(this).addClass("card__row2").data("row", 2);
        else if (i % colCount == 2) $(this).addClass("card__row3").data("row", 3);
        else $(this).addClass("card__row4").data("row", 4);
    });
}

function teamConnections(resize = false) {
    let centers = [];
    $(".connection").remove();
    $(".team .card").each(function (i) {
        let left = $(this).position().left + ($(this).outerWidth() + 6) / 2;
        let top = $(this).position().top + $(this).outerHeight() / 2 + parseInt($(this).css('marginTop'), 10);
        centers[i] = {"left": left, "top": top};
    });
    for (let i = 0; i < centers.length; i++) {
        for (let j = centers.length - 1; j >= i; j--) {
            if (j != i) {
                let hyp = Math.sqrt(Math.pow((centers[j]["left"] - centers[i]["left"]), 2) + Math.pow((centers[j]["top"] - centers[i]["top"]), 2));
                let c = (centers[j]["left"] - centers[i]["left"]);
                let angle = Math.acos(c / hyp) * (180 / Math.PI);
                let angleReal = (centers[j]["top"] - centers[i]["top"] < 0 && Math.floor(j / 4) === Math.floor(i / 4)) ? -1 : 1;//angle * (-1) : angle;
                $('<div class="connection" data-cI="' + (i + 1) + '" data-cJ="' + (j + 1) + '">&nbsp;</div>').appendTo(".team").css({
                    width: hyp + "px",
                    left: ((centers[j]["left"] + centers[i]["left"]) / 2) + "px",
                    top: ((centers[j]["top"] + centers[i]["top"]) / 2) + "px",
                    transform: "translate(-50%,-50%) rotate(" + angleReal * angle + "deg)"
                });
            }
        }
    }
}


// timeago

if ( $(".render_elapsed_time")[0] ) {
    timeago.render(document.querySelectorAll('.render_elapsed_time'));
}

