const clock = document.querySelector("#clock");
const color = document.querySelector("#color");

const checkLength = (value, interval) =>{
	if(value.length < interval) return 0 + value;
  return value;
};

let count = 0;

(function rgbClock(){
	const date = new Date();
	const h = String(date.getHours());
  const m = String(date.getMinutes());
  const s = String(date.getSeconds());

  const colorString = `rgb(${h * 10}, ${m * 4.25}, ${s * 4.25})`;

  clock.innerText = checkLength(h, 2) + ':' + checkLength(m, 2) + ':' + checkLength(s, 2);
  color.innerText = colorString;

  document.body.style.background = colorString;

  const timer = window.setTimeout(rgbClock, 1000);
  count++;

  if(count > 5){
  	clearTimeout(timer)
  }
})();
