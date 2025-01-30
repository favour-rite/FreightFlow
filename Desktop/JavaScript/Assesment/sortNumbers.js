const prompt = require('prompt-sync')();
function sortNumbers() {

	let userInputOne = (prompt('Enter number? '));
	let userInputTwo = (prompt('Enter number? '));
	let userInputThree = (prompt('Enter number? '));

	if (userInputOne <= userInputTwo && userInputOne <= userInputThree) {
		first = userInputOne;
	if (userInputTwo <= userInputThree) {
		second = userInputTwo;
		third = userInputThree;
	} else {
		second = userInputThree;
 		third = userInputTwo;
	}
	} else if (userInputTwo <= userInputOne && userInputTwo <= userInputThree) {
		first = userInputTwo;
	if (userInputOne <= userInputThree) {
        	second = userInputOne;
        	third = userInputThree;
   	 } else {
        	second = userInputThree;
        	third = userInputOne;
    	}
	} else {
    		first = userInputThree;
   	 if (num1 <= userInputTwo) {
        	second = userInputOne;
        	third = userInputTwo;
    	} else {
        	second = userInputTwo;
        	third = userInputOne;
    }
}

console.log(`The numbers in ascending order are: ${first}, ${second}, ${third}`);
	