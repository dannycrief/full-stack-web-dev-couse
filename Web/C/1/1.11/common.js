const timer = document.querySelector('.countdown');
const minutes = document.querySelector('.minutes');
const seconds = document.querySelector('.seconds');
const message = document.querySelector('.message');

const plus = document.querySelector('.plus');
const minus = document.querySelector('.minus');
const start = document.querySelector('.start');
const reset = document.querySelector('.reset');

const inputMin = document.querySelector('.input-min');
const inputSec = document.querySelector('.input-sec');
const confirm = document.querySelector('.confirm');

let countSec = 0;
let countMin = 0;

const updateText = () => {
    minutes.innerHTML = (0 + String(countMin)).slice(-2);
    seconds.innerHTML = (0 + String(countSec)).slice(-2);
};
updateText();

const countDown = () => {
    let total = countSec + countMin * 60;
    const timeinterval = setTimeout(countDown, 1000);
    if (total <= 0) {
        clearInterval(timeinterval);
        timer.style.display = 'none';
        message.innerHTML = '<p>I am done...</p>';
    }
    if (countSec > 0) countSec--;
    else {
        countSec = 59;
        countMin--;
    }
    updateText();
};

plus.onclick = () => {
    message.innerHTML = '';
    if (countSec < 59) ++countSec;
    else {
        countSec = 0;
        ++countMin;
    }
    updateText()
};

minus.onclick = () => {
    message.innerHTML = '';
    if (countMin <= 0 && countSec === 0) {
        countSec = 0;
        countMin = 0;
        return;
    }
    if (countSec > 0) --countSec;
    else {
        countSec = 59;
        --countMin;
    }
    updateText();
};

start.onclick = () => {
    message.innerHTML = '';
    if (minutes.textContent === '00' && seconds.textContent === '00') {
        message.innerHTML = '<p>Please set timer...</p>';
    } else {
        console.log(countMin, countSec);
        countDown();
    }
};

reset.onclick = () => {
    message.innerHTML = '';
    timer.style.display = 'block';
    countSec = 0;
    countMin = 0;
    updateText();
};

confirm.onclick = () => {
    message.innerHTML = '';
    if (!inputMin.textContent || !inputSec.textContent) {
        message.innerHTML = 'Please fill all the fields'
    }
    if (inputMin.textContent > 59 || inputSec.textContent > 59) {
        message.innerHTML = 'You cannot set this timer. Max value is 59:59';
    }

    countMin = inputMin.valueAsNumber;
    countSec = inputSec.valueAsNumber;
    updateText();
    countDown();
};