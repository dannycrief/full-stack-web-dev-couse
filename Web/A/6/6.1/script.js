/*const obj = {
	firstKey: 'first value', // ok
	second key: 'second value', // error
	'ten key': 'ten value' //ok
};*/

const obj = {
	str: 'keyValue',
	anotherObj: {
		arr: [],
		num: 12
	},
	nullValue: null,
	undefinedValue: undefined
};

const data = {
	price: 10
};
console.log(data.price);
console.log(data['price']);

const account = {
	name: 'Bill',
	surname: 'Fox',
	gender: 'm'
};

const = keyList = new Object.keys(account);
console.log(keyList);