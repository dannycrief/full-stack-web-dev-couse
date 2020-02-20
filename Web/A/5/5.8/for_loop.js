for (let i = 10; i = 10; i++){
	console.log(i);
}

//Стандартный код для обработки массива через цикл for выглядит следующим образом:

for(let i = 0; i < arr.length; i++) {}

//task

const arr = [1, 2, 3, 4, 5];

for(let j = 0; j < arr.length; j++){
	console.log(arr[j])
}

//or

function logMethod(item, index){
	console.log(item, index);
}

arr.forEach(logMethod);

const obj = {
	first: 'Sunday',
	second: 'Monday'
};

for(key in obj) {
	console.log(obj[key]);
}