/*const dataURL = 'https://api.myjson.com/bins/jcmhn';

function handleButton() {
	$.getJSON(dataURL, function (data) {
		handleData(data);
	})
}

const handleData = data => {
	// кажется, какой-то из этих способов сработает
	const var1 = $("input[name=var1]")[0].value;
	console.log(var1)
	// надо сделать так чтобы сообщения подменились на значения из формы
	let text = data.text;
	let $text = $(text);
	console.log(text.length);
	for (let i = 0; i < text.length; i++){
		$('#result').text(text);
	}

};

//$('#result').text(text);

function init() {
	$("#button-fetch").click(handleButton);
}

$(document).ready(init);*/
