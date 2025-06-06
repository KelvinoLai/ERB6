const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
// Resemble lambda function in Python
// call jQuery-3.3.1 to fade out the message after 3 seconds
// # means find the id of container in _alert.html
setTimeout(() => $("#message").fadeOut("slow"), 3000);
