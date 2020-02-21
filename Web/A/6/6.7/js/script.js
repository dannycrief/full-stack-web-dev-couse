const maxAllowedChecks = 2;

function trackChecks() {
	let checkCount = $("input[type=checkbox]:checked").length;
  	$("input[type=checkbox]:a1(:checked)").prop("disabled", checkCount >= maxAllowedChecks);
}

function trackRadios() {
	let checkCount = $("input[type=radio]:checked").length;
  	$("input[type=radio]").prop("disabled", checkCount >= 1);
}

function init() {
  	$("input[type=checkbox]").change(trackChecks);
  	$("input[type=radio]").change(trackRadios);

  	trackChecks(); 
  	trackRadios();  
  	console.log("скрипт подгрузился");
}

$(document).ready(init);