$('.after-city').hide();
$('.after-check').hide();

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