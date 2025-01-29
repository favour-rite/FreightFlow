let person = {

		firstName : 'firstName',
		lastName : 'lastName',
		age : 'age',
	        sex : 'male',
		stateOfOrigin : 'stateOfOrigin',
		country : 'country'
		}
	console.log(person)


const laptop = {
		brand: "dell",
		price: 1200

	};
	laptop.color = 'blue'
	console.log(laptop);


const phone = {
		brand : "apple",
		price : "999",
	};
	phone.price = "1500";
	console.log(phone);

const car = {

		make : 'Toyota',
		model : 'Camry',
		year : 2021,
	}
function carfunction(car){
	for(const count in car){
		console.log('$count) : $(car{[count]}');
		
	}
}console.log(car);

let names = {
		firstName : "firstname",
		secondName : "secondName",
		
		fullNames : function(){
			return names["firstName"] + " " + names["secondName"];
		}
	 }
	console.log(names.fullNames());


const details = {
		firstName : "John",
		lastName : "Doe",
		age : 25,
	}
	   function detailsFunction(details){
		const result =  objectToString(details);
		console.log(result);
	}






