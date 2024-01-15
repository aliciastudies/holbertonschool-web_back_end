# Learning Objectives

## ES6

ES6 a version of JavaScript with these features:

### let and const

`let` allows values to be reassigned.

`const` cannot be reassigned.

```
let x = 5;
const pi = 3.14;
```

### Block-scoped variables

Variables declared with `let` and `const` are limited to the block (code between curly braces) in which they are defined.

```
if (true) {
    let y = 10;
}
// y is not accessible here
```

### Arrow functions

A concise way to write functions using the arrow `=>` syntax.

```
export default function getNeighborhoodsList() {
this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

const self = this;
this.addNeighborhood = (newNeighborhood) => {
 self.sanFranciscoNeighborhoods.push(newNeighborhood);
 return self.sanFranciscoNeighborhoods;
};
}
```

### Default function parameters

Set default values for function parameters.

```
export default function getSumOfHoods(
initialNumber,
expansion1989 = 89,
expansion2019 = 19,
) {
return initialNumber + expansion1989 + expansion2019;
}
```

### Rest and spread parameters

The rest parameter `...` allows a function to accept an indefinite number of arguments as an array.

```
export default function returnHowManyArguments(...theArgs) {
  return theArgs.length;
}
```

The spread operator `...` is used to spread array elements into individual values.

```
export default function concatArrays(array1, array2, string) {
const concatArrays = [...array1, ...array2, ...string];
return concatArrays;
}
```

### String templating

A more convenient way to concatenate strings using template literals.

```
const name = "World";
console.log(`Hello, ${name}!`);
```

### Object creation and properties

A shorthand for creating objects and defining properties.

```
const person = {
    name: "John",
    age: 25,
    sayHello() {
        console.log(`Hello, my name is ${this.name}.`);
    }
};
```

### Iterators and for-of loops

An iterator is an object that knows how to access items from a collection one at a time, while keeping track of its current position within that sequence.

An object that is returned by the iterable interface is also an iterator object.

Iterator object have a next() method which returns the next item in the sequence. This method returns an object with two properties: done and value and when next() calls reach to the end of sequence then the done property set to true else remain false .

```
// Creating an iterator for an array
const myArray = [1, 2, 3];
const iterator = myArray[Symbol.iterator]();

// Accessing elements using the iterator
console.log(iterator.next()); // { value: 1, done: false }
console.log(iterator.next()); // { value: 2, done: false }
console.log(iterator.next()); // { value: 3, done: false }
console.log(iterator.next()); // { value: undefined, done: true }
```

The for-of loop provides a concise way to iterate over the elements of an iterable object, such as an array or a string. It simplifies the process of looping through collections and eliminates the need for manually managing an iterator.

```
const numbers = [1, 2, 3];
for (const num of numbers) {
    console.log(num);
}
```
