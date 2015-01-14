console.log('loaded!');

document.getElementById("sad-face").classList.remove("disabled");


// smile / frown face
document.getElementById("sad-face").addEventListener('mouseenter', function() {
	console.log('enter');
	document.getElementById("sad-face").innerHTML="<img src='images/smile.png'>"
})
document.getElementById("sad-face").addEventListener('mouseleave', function() {
	console.log('leave');
	document.getElementById("sad-face").innerHTML="<img src='images/frown.png'>"
})

// drag me home
document.getElementById("food").setAttribute("draggable", "true");
document.getElementById("feed-me").addEventListener("dragenter", function(event) {
	console.log('entered');
	document.getElementById("food").textContent="Actually, I'd rather stay here.";
})

// question 1
// document.getElementById("question1").addEventListener("change", function(){
// 	console.log('changed!');
// 	if (document.getElementById("question1").value == 'html') {
// 		alert('CORRECT!');
// 	}
// })