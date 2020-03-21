function giveMeMore() {
    if (typeof (giveMeMore.count) == 'undefined') {
        giveMeMore.count = 0;
    } else {
        giveMeMore.count++;
    }
    return giveMeMore.count;
}

// console.log(giveMeMore());
// console.log(giveMeMore());
// console.log(giveMeMore());
// console.log(giveMeMore());
//
// console.log("");


function reverseWords(str) {
    str = str.split(" ");
    let reversed = "";
    for (let i = 0; i < str.length; i++) {
        reversed += str[str.length - 1 - i];
        if (i !== str.length-1) {
        	 reversed +=  " ";
		}
    }
    return reversed;
}

console.log(reverseWords('Ala ma kota'));

