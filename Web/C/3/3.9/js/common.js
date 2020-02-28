$('.after-city').hide();

city.value = localStorage.getItem('city');

if (Boolean(city.value)) {
    $('.before-city').hide();
    $('.after-city').show();
    $('.home').html(`<h4 class="user-home">Your city/town/village is ${city.value}</h4>`);
}
city.oninput = () => localStorage.setItem('city', city.value);

submitHome.onclick = () => {
    if (city.value !== '') {
        location.reload();
    } else {
        alert('Please fill all the fields');
    }
};

clearButton.onclick = () => {
    localStorage.removeItem('city');
    city.value = '';
    location.reload()
};

// Right side cookies
updatedStorage = localStorage.getItem('storage');
if (Boolean(updatedStorage)) {
    for (let i = 0; i < updatedStorage.length; i++) {
        nexItem = '#check' + String(1 + i);
        if (updatedStorage[i] === '1') {
            document.querySelector(nexItem).setAttribute('checked', 'true');
        } else {
            document.querySelector(nexItem).removeAttribute('checked');
        }
        document.querySelector(nexItem).setAttribute('disabled', 'true')
    }
    $('#checkSave').hide();
    $('#checkClear').show();
} else {
    $('#checkSave').show();
    $('#checkClear').hide();
}

checkSave.onclick = () => {
    let storage = '';
    const checked = document.querySelectorAll('input[name="check"]');
    for (let checkedElement = 0; checkedElement < checked.length; checkedElement++) {
        if (checked[checkedElement].checked) {
            storage += '1';
        } else {
            storage += '0';
        }
    }
    localStorage.setItem('storage', storage);
    location.reload();
};

checkClear.onclick = () => {
    localStorage.removeItem('storage');
    storage = '';
    location.reload();
};





