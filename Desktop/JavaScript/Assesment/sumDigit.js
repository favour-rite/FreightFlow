 const prompt = require('prompt-sync')();

function sumDigits() {
	let userInput = prompt('Enter number? ');
	
	let sum = 0;
		while (userInput !== 0) {
			sum += userInput % 10;
			userInput = Math.floor(userInput / 10); 
			
		return sum;
	};		
};
console.log(sumDigits())

function displaySortedNumbers(number1, number2, number3) {

  let numbers = [number1, number2, number3];
  numbers.sort(numbers)
  return numbers;
}
const number1 = parseFloat(prompt("Enter the first number: "));
const number2 = parseFloat(prompt("Enter the second number: "));
const number3 = parseFloat(prompt("Enter the third number: "));

const sortedNumbers = displaySortedNumbers(number1, number2, number3);
console.log(displaySortedNumbers());


	 	