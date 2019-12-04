const currentDate = new Date();

const greeting = `Good ${currentDate.getHours < 12 ? 'morning' : 'afternoon'}, ${prompt('Enter your name:')}`;

document.querySelector('h1').innerHTML = greeting;

alert(greeting);
