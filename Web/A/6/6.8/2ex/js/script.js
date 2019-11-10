const thresholdChecksCount = 5;

function handleChecks() {
   let checkCount = $("input[type=checkbox]:checked").length;
   if (checkCount >= thresholdChecksCount) {
       $("input[type=checkbox]:not(:checked)").prop("checked", true);
   }
}

function init() {
  	$("input[type=checkbox]").change(handleChecks);

  	handleChecks(); 
  	console.log("скрипт подгрузился");
}

$(document).ready(init);