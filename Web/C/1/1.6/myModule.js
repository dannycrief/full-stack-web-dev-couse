function smallQuery(element) {
    return document.querySelector(element);
}

smallQuery.prototype.all = function (element) {
    return document.querySelectorAll(element);
};

Number.prototype._toInt = function () {
    return this | 0;
};

console.log( 101.0011010 . _toInt() );
// task 1
const obj = {
  a: "Hello",
  b(){return obj.a;}
};

// task2
Number.prototype._str = function() {
  return String(this);
};
let name = 101 ._str();
console.log( name );