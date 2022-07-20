// clear button 

function cl() {
	console.log("hh");
    document.getElementById("num1").value = "";
    document.getElementById("num2").value = "";
    document.getElementById("result").innerHTML = "  ";
}
 

 
// This function evaluates the expression and returns result

function calculate(operatorr) {
        var val1 = document.getElementById("num1").value;
        var val2 = document.getElementById("num2").value;
        // var opr = document.getElementById("plus").value;
        // if opr == '+':
        console.log(val1);
        console.log(val2); 

        switch (operatorr) {
  		case plus:
    	console.log("plus")
    	out=parseInt(val1)+parseInt(val2)
    	break;
  		case minus:
    		console.log("minus")
    		out=parseInt(val1)-parseInt(val2)
    	break;
    	case pro:
    		console.log("pro")
    		out=parseInt(val1)*parseInt(val2)
    	break;
    	case div:
    		console.log("div")
            try {
            	out=parseInt(val1)/parseInt(val2);
        } catch (ZeroDivisionError){
               out="unable to zero division error"
    	break;}
  	
         }
       document.getElementById("result").innerHTML=out;  
}
