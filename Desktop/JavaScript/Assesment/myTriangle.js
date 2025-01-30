 const prompt = require('prompt-sync')();

const MyTriangle = {
    
	isValid: function(side1, side2, side3) {

		return (side1 + side2 > side3) && (side2 + side3 > side1) && (side3 + side1 > side2);
    },


	area: function(side1, side2, side3) {

		const sides = (side1 + side2 + side3) / 2; 
		return Math.sqrt(sides * (sides - side1) * (sides - side2) * (sides - side3));
    }
};

function testTriangle() {
	const side1 = parseFloat(prompt("Enter the length of side 1: "));
	const side2 = parseFloat(prompt("Enter the length of side 2: "));
	const side3 = parseFloat(prompt("Enter the length of side 3: "));

	if (MyTriangle.isValid(side1, side2, side3)) {

		const area = MyTriangle.area(side1, side2, side3);

	} else {

		console.log("The input is invalid. The sum of any two sides must be greater than the third side.");
    }
}
testTriangle();