// This function clear all the values
function clearScreen() {
    document.getElementById("result").value = "";
}
 
// This function display values
function display(value) {
    document.getElementById("result").value += value;
}
 
// This function evaluates the expression and returns result
function calculate() {
    var expression = document.getElementById("result").value;
    var output = eval(expression);
    document.getElementById("result").value = output;
}
