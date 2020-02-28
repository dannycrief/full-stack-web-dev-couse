// Left side cookies
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
let updatedStorage = localStorage.getItem('storage');
let nexItem;
if (Boolean(updatedStorage)) {
    for (let i = updatedStorage.length; i > 0; i++) {
        nexItem = '#check' + String(updatedStorage + 1);
        if (updatedStorage[i] === '1') {
            $(nexItem).setElementAttribute('checked', 'true');
        } else {
            $(nexItem).removeElementAttribute('checked');
        }
        $(nexItem).setElementAttribute('disabled', 'true')
    }
    $('#checkSave').hide();
    $('#checkClear').show();
}


let storage = '';

checkSave.onclick = () => {
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