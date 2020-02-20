const arr = [1, 2, 3, 4, 5];
arr.map(function (item) {
	return 'item: ' +  item; 
});


const someArr = [
{
	name: 'Bob',
	surname: 'Fix'
},
{
	name: 'Lily',
	surname: 'Bix'
}
];

someArr.map(function(index){
	return index.name + ' ' + index.surname;
});

someArr.map(function(index){
	return index.surname + ' ' + index.surname;
});


const numbers = [2, 5, 7, 4, 24, 16, 2, 1, 2, 2, 7];
numbers.filter(function(item){
	return item > 5;
});


//6.5
const arr = [1, 2, 3, 4, 5];
const newArr = doubleArr(arr);
console.log(newArr);
//6.5.1
//Написать функцию, которая принимает на вход массив массивов и возвращает массив, в котором есть только те массивы, в которых есть элементы.
const arrayOfArrays = [[], [], [1,2,3], [], [1,4]]
const newArr = notEmptyArray(arrayOfArrays);
console.log(newArr);  // [[1,2,3],[1,4]]

const arrayOfArrays = [[], [], [1,2,3], [], [1,4]]
function notEmptyArray(arr) {
    return arr.filter(
        function(item) {
            return item.length !== 0;
    });
}