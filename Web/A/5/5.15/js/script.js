$(document).ready(function(){
	$.getJSON(
		'https://api.myjson.com/bins/jcmhn',
		function(data) {
			render(data.text);
		}
	);

	$('.create').click(function() {
		for (let i = 1; i < $("input").length; i++) {
			writeHtml(`.field-${i}`, $(`input-field${i}`).val());
		}

		$("input").each(function(index) {
			writeHtml(`.${$( this ).attr('class').replace(/input-(.+)/, "$1")}`, $( this ).val());

		});
	});
});

function render(data) {
	let fairyTail = "";
	let templates = {};
	let count = 0;

	data.forEach(function(string) {

		string = string.replace(/\{.+?\}/g,
							function(match) {
								let flagFound = false;
								for (let key in templates) {
									if (templates[key] === match) {
										flagFound = true;
										return `<span class="${key}">${templates[key]}</span>`
									}
								}
								if (flagFound === false) {
									templates[`field-${++count}`] = match;
									return `<span class="field-${count}">${match}</span>`
								}
							});

		fairyTail = fairyTail + `<p>${string}</p>`;
	});
	let formContent = ``;
	for (let key in templates) {
        formContent += `<input type="text" class="input-${key}"" placeholder="${templates[key]}">`
    }

    writeHtml('form', formContent);
	writeHtml('.result', fairyTail);
}

function writeHtml(field, data) {
	const $result = $(field);
	$result.html(data);
}