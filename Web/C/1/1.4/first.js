(function (a, b) {
    return a + b;
})(2, 2);

// ================= this functions are anon

((a,b) => a + b)(2, 2);

const foo = (a, b) => a + b;
console.log(foo(2, 2));

//================
const foo1 = a => a + a;
const bar = () => 2 + 2;

const bar2 = _ = 2 + 2;

const baz = (a, b) => {
    const temp = a;
    return temp + b;
};

const aray = [1, 2, 3, 4];
const newArray = aray.map( (number, index) => number * index );

console.log(newArray);


// TASKS 1
const celsius = [-15, -5, 0, 10, 16, 20, 24, 32];

const rate = value => value * 1.8 + 32;
const fahrenheit = celsius.map(t => rate(t));
console.log(celsius, fahrenheit);


// TASKS 2
const firstArr = [1, 4, 3, 2];
const secondArr = [5, 2, 6, 7, 1];

const output = firstArr.filter(value => secondArr.includes(value));
console.log(output);
