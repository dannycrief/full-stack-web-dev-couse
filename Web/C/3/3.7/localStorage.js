// sessionStorage update even when web-page was reloaded
// localStorage update even when browser was reloaded
function populateStorage() {
    localStorage.setItem('bgcolor', 'red');
    localStorage.setItem('font', 'Helvetica');
    localStorage.setItem('image', 'myCat.png');
    localStorage.setItem('Max', 'Peter', 'Hans');
}

function setStyles() {
    const currentColor = localStorage.getItem('bgcolor');
    const currentFont = localStorage.getItem('font');
    const currentImage = localStorage.getItem('image');

    document.getElementById('bgcolor').value = currentColor;
    document.getElementById('font').value = currentFont;
    document.getElementById('image').value = currentImage;

    htmlElem.style.backgroundColor = '#' + currentColor;
    pElem.style.fontFamily = currentFont;
    imgElem.setAttribute('src', currentFont);
}

// Task

function setWeather() {
    const weather = localStorage.getItem('sun');
    document.getElementById('sun').value = weather;
}


function populateStorage() {
    localStorage.setItem('post1', 'post2');

    localStorage.removeItem('post');
}

// clear() remove all
// key(index) get key on index-position
// length get number of elements in storage
localStorage.setItem('cat', '2');
console.log( localStorage.getItem('cat') ); // 2

localStorage.test = 2;
console.log(localStorage.test);
delete localStorage.test;


// looping thought the keys
for (let i = 0; i < localStorage.length; i++) {
    let key = localStorage.key(i);
    console.log(`${key}: ${localStorage.getItem(key)}`);
}