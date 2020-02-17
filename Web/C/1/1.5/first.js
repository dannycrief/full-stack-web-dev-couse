function object() {
    return new Array(10).fill(10).map( (item, id) => {
        return {
            name: Math.random().toString(36).substring(2),
            data: JSON.stringify({
                some: ( item * item ).toString(36).substring(2),
            }),
            id,
        }
    } )
}

console.log(object());
console.table(object());

// task
const value = '101';
console.log("\n",value);

console.log('%i', value);