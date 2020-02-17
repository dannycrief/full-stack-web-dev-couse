const person = {
  first: 'Yagami',
  last: 'Light',
  full: () => console.log(this.first + ' ' + this.last),
  personTwo: {
    first: 'Dio',
    last: 'Brando',
    full: function() {
      console.log(this.first + ' ' + this.last);
    }
  }
};

// task 1: person.full()
// answer task 1: undefined undefined
// task 2: person.personTwo.full()
// answer 2: Dio Brando
