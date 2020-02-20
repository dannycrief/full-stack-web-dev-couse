const render = data => {
    const card = `
        <div class="person">
            name: <div class="person__name">${data.name}</div>
            birth year: <div class="person__birth-year">${data.birth_year}</div>
            gender: <div class="person__gender">${data.gender}</div>
            mass: <div class="person__mass">${data.mass}</div>
        </div> 
    `;

    const $card = $(card);


    $card.appendTo(document.body);
};

$.getJSON(
    ' https://swapi.co/api/people/1/', // url
    function (data) { // callback
        render(data);
    }
);