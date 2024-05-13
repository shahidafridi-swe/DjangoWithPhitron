function evenOdd(n){
    if( n % 2 == 0){
        return "Even";
    }
    else{
        return "Odd";
    }
}

let n = 4
console.log("This number is: ", evenOdd(n));