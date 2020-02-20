let guessNumber = Math.round(Math.random() * 30);
let tries = 10;

//String const
function restartMessage() {
    return "Your number changed";
}
function triesMore() {
    return tries + " tries left";
}

//Boolean funcs
function isLose() {
    return tries === 0;
}
function isWin(number) {
    return guessNumber === number;
}
function isGt(number) {
    return guessNumber > number;
}
function isLt(number) {
    return guessNumber < number;
}

//Action funcs
function makeTriesLess() {
    tries--;
}

function init() {
    guessNumber = Math.round(Math.random() * 30);
    tries = 10;
}

function win() {
    init();
    return `Yes, you're right ${restartMessage()}`;
}

function lose() {
    init();
    return `Your tries ended - You lose. ${restartMessage()}`;
}

function gt() {
 makeTriesLess();
 return `Number is greater than you say. ${triesMore()}`;
}

function lt() {
 makeTriesLess();
 return `Number is lesser than you say. ${triesMore()}`;
}

function guess(number) {
 if (isLose()) {
   return lose();
 }
 if (isWin(number)) {
   return win();
 }
 if (isGt(number)) {
   return gt();
 }
 if (isLt(number)) {
   return lt();
 }
 return "ошибка";
}

$(document).ready(function() {
    $(".btn").click(function () {
        const inputValue = $("input").val();
        const resultValue = guess(+inputValue); //+'15' == 15 <=> convert string to num
        const $result = $(".result");
        $result.html(resultValue);
    });
});