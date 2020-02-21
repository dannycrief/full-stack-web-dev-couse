const header = new Headers({
    'Access-Control-Allow-Credentials': true,
    'Access-Control-Allow-Origin': '*'
});

const ES = new EventSource('https://sf-pyw.mosyag.in/sse/stream', header);

ES.onopen = event => {
    console.log(event)
};

ES.onerror = error => {
    ES.readyState ? console.error("⛔ EventSource failed: ", error) : null;
};

ES.onmessage = message => {
    console.log(message.data)
};


// task1: Какое событие пришло, если открылось соединение?
// evtSource.____ = function(event) {
//     console.log(event)
// }
// answer : onopen

// task2: Какое событие мы перехватываем, если пришло сообщение?
// evtSource._______ = function(event) {
//     console.log(event)
// }
// answer : onmessage

// task1: Какое событие мы перехватили, если возникла ошибка?
// evtSource.____ = function(event) {
//     console.log(event)
// }
// answer : onerror

// task1: Что нужно дописать в коде, если мы решили закрыть соединение?
// evtSource._____();
// answer : close
