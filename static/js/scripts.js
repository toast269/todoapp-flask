document.addEventListener("DOMContentLoaded", function () {
  document
    .querySelector("#myForm")
    .addEventListener("submit", function (event) {
      var input = document.getElementById("myInput");

      if (input.value.trim() === "") {
        alert("Dude Chill! Name your Task First 😑");
        event.preventDefault();
      }
    });
});
