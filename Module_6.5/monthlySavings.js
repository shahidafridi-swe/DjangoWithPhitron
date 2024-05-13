function monthlySavings(ar, livingCost){

    if (ar.constructor !== Array &&  typeof livingCost != 'number'){
        return "invalid input"
    }
    
    let totalBalance = 0;
    for(let i = 0 ; i < ar.length ; i++){
        if (ar[i] >= 3000){
            totalBalance += ar[i]*0.8;
        }
        else{
            totalBalance += ar[i];
        }
    }
    return (totalBalance - livingCost < 0 ) ? "earn more" : totalBalance - livingCost;
}


console.log(monthlySavings([1000,2000,3000], 5400));
console.log(monthlySavings([1000,2000,2500], 5000));
console.log(monthlySavings([900,2700,3400], 10000));
console.log(monthlySavings(100, [900,2700,3400]));