let running = false;
let t; //setInterval(timerUpdate, 1000);
//let initialMinutes;
let initialSeconds;
function resetTimer() {
	$(".progress-bar").css("width", "0");
	$(".progress-bar").html("0%");
	document.getElementById("minutes").value = "0";
	document.getElementById("seconds").value = "0";
	$("#minute-minus").prop('disabled', true);
	$("#second-minus").prop('disabled', true);
	$("#time").css( "animation", "none");
	running = false;
	clearInterval(t);
}

function timerUpdate() {
	console.log(running);
	if (running) {
		let m = Number( $("#mm").text() );
		let s = Number( $("#ss").text() );
		s--;
		if (s < 0) {
			if (m > 0) {
				m--;
				s = 59;
			} else {
				s = 0;
				running = false;
				main();
				$('#exampleModal').modal('show');
			}
		}
		updateProgressbar(m, s);
		$("#mm").text(zeroFill(String(m)));
		$("#ss").text(zeroFill(String(s)));
	}
}

function updateProgressbar(m, s) {
	let currentPercent = Math.round((m * 60 + s) / initialSeconds * 100);
	$(".progress-bar").css("width", currentPercent + "%");
	$(".progress-bar").html(currentPercent + "%");
}

function buttonPress(btn) {
	$(".btn").prop('disabled', false);
	let m = Number( $("#mm").text() );
	let s = Number( $("#ss").text() );

	switch(btn.target.id) {
		case "minute-minus":
			m--;
			break;
		case "minute-plus":
			m++;
			break;
		case "second-minus":
			s--;
			break;
		case "second-plus":
			s++;
			break;
		case "start":
			initialSeconds = m * 60 + s;
			updateProgressbar(m, s)
			$("form").hide();
			$("#start").hide();
			$("#pause").show();
			$("#stop").show();
			running = true;
			t = setInterval(timerUpdate, 1000);
			break;
		case "pause":
			setPause(running);
			running = !running;

			break;
		case "stop":
			running = false;
			m = 0;
			s = 0;
			main();
			break;
	}

	$("#minute-minus").prop('disabled', m < 1);
	$("#minute-plus").prop('disabled', m >= 59);
	$("#second-minus").prop('disabled', s < 1);
	$("#second-plus").prop('disabled', s >= 59);

	document.getElementById("minutes").value = m;
	document.getElementById("seconds").value = s;
	$("#mm").text(zeroFill(String(m)));
	$("#ss").text(zeroFill(String(s)));

}

function setPause(b) {

	if (b) {
		$("#pause").text("Continue");
		$("#time").css( "animation", "blinker 1s linear infinite");
	} else {
		$("#pause").text("Pause");
		$("#time").css( "animation", "none");
	}
}

function zeroFill(s) {
	if (s.length < 2) s = "0" + s;
	return s
}

function main() {

	$("#mm").text("00");
	$("#ss").text("00");
	$(".btn").prop('disabled', false);
	$("#stop").hide();
	$("#pause").hide();
	$("form").show();
	$("#start").show();
	$("#start").text("Start timer");
	resetTimer();
}

function init() {

	$(".btn").click(buttonPress);
	$("#minutes").on('input', function() {
		$("#mm").text( zeroFill(this.value) );
		$(this).trigger('change');
		$("#minute-plus").prop('disabled', this.value >= 59);
	});

	$("#seconds").on('input', function() {
		$("#ss").text( zeroFill(this.value) );
		$(this).trigger('change');
		$("#second-plus").prop('disabled', this.value >= 59);
		$("#second-minus").prop('disabled', this.value < 1);
	});
	main();
}

$(document).ready(init);
