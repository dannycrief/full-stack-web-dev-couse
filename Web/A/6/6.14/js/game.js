const numDivs = 36; // max div's number 
const maxHits = 10; //max hits to the end of the game

let horisontalDivs = 6; // horizontal divs
let verticalDivs = 6; // vertical divs


let hits = 0;
let missies = 0;

let firstHitTime = 0;


const gameFieldDiv1 = '<div class="grid-item game-field" id="slot-'
const gameFieldDiv2 = '"></div>'


// creating game fields
function buildGameField(x, y) {
  for(let i = 1; i <= x; i++) {
    for(let j = 1; j <= y; j++) {
      $('.gameField').append(gameFieldDiv1 + i + j + gameFieldDiv2);
    }
  }
  $('.grid-wrapper').css('grid-template-columns', 'repeat(' + x + ', 1fr)');
  $('.grid-wrapper').css('grid-template-rows', 'repeat(' + y + ', 1fr)');
  $('.grid-wrapper').css('grid-gap', (3/x)+'vw');
}

// checking hits
function round() {
  let divSelector = randomDivId(horisontalDivs, verticalDivs);
  $(divSelector).addClass("target");
  $(divSelector).html(hits+1); // checking target with current nunmber

  if (hits === maxHits) {
    endGame();
  }
}

// ending the game
function endGame() {
  let totalPlayedMillis = getTimestamp() - firstHitTime;
  let totalPlayedSeconds = Number(totalPlayedMillis / 1000).toPrecision(3);
  $('.gameField').addClass('d-none');
  $("#total-time-played").text(totalPlayedSeconds);
  $('#missies').text(missies);
  $("#win-message").removeClass("d-none");
}

// checking click
function handleClick(event) {
  if ($(event.target).hasClass("target")) {
    $(event.target).removeClass("target");
    $(event.target).html("");
    $('.miss').removeClass('miss');
    hits = hits + 1;
    if (hits >= maxHits) {
      endGame();
    }
    else {
      round();
    }
  }
  else {
    $(event.target).addClass("miss"); // Отмечаем если мы промахнулись
    missies++;
  }
  

}

// initialing the game
function game() {
  horisontalDivs = $('#x').val();
  verticalDivs = $('#y').val();
  if (horisontalDivs * verticalDivs > numDivs) {
    alert("Sorry, but max is 6x6");
    location.reload();

  }else{
    buildGameField(horisontalDivs, verticalDivs);
    $("#button-reload").removeClass('d-none')

    $(".game-field").click(handleClick);
    $("#button-reload").click(function() {
      location.reload();
    });
    round();
  }
  

}

// just init function ^_^
function init() {
  $("#button-start").click(function() {
    $("#button-start").addClass('d-none');
    $("#game-conditions").addClass('d-none');
    firstHitTime = getTimestamp();
    game();
  });
  

}

// starts when page have been loaded
$(document).ready(init);
