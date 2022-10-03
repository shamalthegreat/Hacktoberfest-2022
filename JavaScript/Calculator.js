var num1 = window.prompt("Enter You first number", "0");
var num2 = window.prompt("Enter your second number", "0");
var opr = window.prompt("Enter your operator.", "Operator");
if (opr == "+") {
    let sum = parseInt(num1) + parseInt(num2);
    document.writeln(`The sum is ${sum}`);
    window.alert(`The sum is ${sum}`);

} else if (opr == "-") {

    let difference = parseInt(num1) - parseInt(num2);
    document.writeln(`The difference is ${difference}`);
    window.alert(`The difference is ${difference}`);
    
} else if (opr == "*") {

    let prduct = parseInt(num1) * parseInt(num2);
    document.writeln(`The product is ${prduct}`);
    window.alert(`The product is ${prduct}`);

} else if (opr == "/") {

    let divide = parseInt(num1) / parseInt(num2);
    document.writeln(`The divide is ${divide}`);
    window.alert(`The divide is ${divide}`);

} else {

    document.writeln("Invalid Input Please Try Again.");
}
