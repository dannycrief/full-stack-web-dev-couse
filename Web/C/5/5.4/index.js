//This is fooBar
var foo = "foo"

function bar(first, second) {
    this.localThis = first

    console.log(this.localThis * second)
}

new bar(2, 3)

// uglifyjs index.js -c -m
// uglifyjs index.js -b - make code look better