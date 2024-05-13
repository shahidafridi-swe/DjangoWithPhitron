function largeNumberFromArray(ar){
    let larger = ar[0];
    for(let i=0; i<ar.length; i++){
        let element = ar[i];
        if(element > larger){
            larger = element;
        }
    }
    return larger;
}

let arr = [2,1,23,34,52,45,34,45,23,2,5,3];

let result = largeNumberFromArray(arr)

console.log(result);