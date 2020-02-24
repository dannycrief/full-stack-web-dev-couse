const cat = document.querySelector('#cat');
const dog = document.querySelector('#dog');
const parrot = document.querySelector('#parrot');

const progressLines = document.querySelector('.progress-lines');
const questions = document.querySelector('.questions');

let request = new XMLHttpRequest();

cat.onclick = () => {
    request.open('POST', 'https://sf-pyw.mosyag.in/sse/vote/cats');
    request.send();
    request.onload = function () {
        if (request.status !== 200) {
            console.log(`Error ${request.status}: ${request.statusText}`);
        } else {
            console.log('Okay, you like cats more than other animals.');
        }
    };
    questions.style.display = 'none';
    progressLines.style.display = 'flex';
};

dog.onclick = () => {
    request.open('POST', 'https://sf-pyw.mosyag.in/sse/vote/dogs');
    request.send();
    request.onload = function () {
        if (request.status !== 200) {
            console.log(`Error ${request.status}: ${request.statusText}`);
        } else {
            console.log('Okay, you like dogs more than other animals.');
        }
    };
    questions.style.display = 'none';
    progressLines.style.display = 'flex';
};

parrot.onclick = () => {
    request.open('POST', 'https://sf-pyw.mosyag.in/sse/vote/parrots');
    request.send();
    request.onload = function () {
        if (request.status !== 200) {
            console.log(`Error ${request.status}: ${request.statusText}`);
        } else {
            console.log('Okay, you like parrots more than other animals.');
        }
    };
    questions.style.display = 'none';
    progressLines.style.display = 'flex';
};

const progressCats = document.querySelector('.progress-cats');
const processDogs = document.querySelector('.progress-dogs');
const processParrots = document.querySelector('.progress-parrots');


const url = new URL('https://sf-pyw.mosyag.in/sse/vote/stats');
const header = new Headers({
    'Access-Control-Allow-Credentials': true,
    'Access-Control-Allow-Origin': '*'
});
const ES = new EventSource(url, header);

ES.onerror = () => {
    !ES.readyState ? progressCats.textContent = "Some error" : null;
};

ES.onmessage = message => {
    let vote_data = JSON.parse(message.data);
    let pets_sum = vote_data.cats + vote_data.dogs + vote_data.parrots;
    let parsed_cats = (vote_data.cats * 100) / pets_sum;
    let parsed_dogs = (vote_data.dogs * 100) / pets_sum;
    let parsed_parrots = (vote_data.parrots * 100) / pets_sum;

    progressCats.style.cssText = `width: ${parsed_cats}%;`;
    progressCats.textContent = `${vote_data.cats} voices`;
    // dogs stat
    processDogs.style.cssText = `width: ${parsed_dogs}%;`;
    processDogs.textContent = `${vote_data.dogs} voices`;
    //parrots stat
    processParrots.style.cssText = `width: ${parsed_parrots}%;`;
    processParrots.textContent = `${vote_data.parrots} voices`
};

function goBack() {
    questions.style.display = 'block';
    progressLines.style.display = 'none';
}