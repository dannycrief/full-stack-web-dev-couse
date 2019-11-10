let currentValue = 0;
function addValue (newValue) {
	currentValue = currentValue + newValue;
	console.log(currentValue.toString());
	if (newValue == 0) {
		currentValue = 0;
	}
	if (currentValue >= 100) {
		currentValue = 100;
	}
	$('#value').width(String(currentValue) + "%");
	$('.progress-bar').text(currentValue + '%');
}

