const clock = document.querySelector('#clock');
const color = document.querySelector('#color');
const body = document.querySelector('body');

const checkLength = value => {
    if (value.length < 2) {
        return 0 + value;
    }
    return value
};

(function rgbClock() {
    const date = new Date();
    const h = String(date.getHours());
    const m = String(date.getMinutes());
    const s = String(date.getSeconds());

    const colorString = `rgb(${h * 10}, ${m * 4.25}, ${s * 4.25})`;

    clock.innerText = checkLength(h) + ':' + checkLength(m) + ':' + checkLength(s)
    color.innerText = colorString;

    body.style.background = colorString;

    window.setTimeout(rgbClock, 1000);
})();