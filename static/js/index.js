console.log("js load");

var inputRadio = document.querySelectorAll("input[type='radio']");  // Get all radio buttons


// JavaScript code for enabling/disabling the submit button
for (var i = 0; i < inputRadio.length; i++) {
    inputRadio[i].addEventListener("change", function () {
        var selectedAnswers = document.querySelectorAll('input[type="radio"]:checked'); // Get all selected answers
        if (selectedAnswers.length === inputRadio.length / 4) {
            document.getElementById("submitBtn").disabled = false; // Enable the submit button
        } else {
            document.getElementById("submitBtn").disabled = true; // Disable the submit button
        }
    });
}