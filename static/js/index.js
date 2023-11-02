let name = prompt("Enter Your Name: ");

const greet = `Heya <b>${name}</b>!`;

const div = document.createElement("div");
div.className = "container alert alert-primary mt-5";
document.body.appendChild(div);

const greetBox = document.createElement("h1");
greetBox.innerHTML = greet;
div.appendChild(greetBox);

const div1 = document.createElement("div");
div1.className = "container alert alert-danger mt-5";
document.body.appendChild(div1);

const greetBox1 = document.createElement("h2");
greetBox1.innerHTML =
  "This TodoApp is Made with &hearts; by KAUSTAV <br> Thanks for Visiting &#128516;";
div1.appendChild(greetBox1);

document.getElementById("myForm").addEventListener("submit", function (event) {
  var input = document.getElementById("myInput");

  if (input.value.trim() === "") {
    alert("Input cannot be blank");
    event.preventDefault(); // Prevent form submission
  }
});
