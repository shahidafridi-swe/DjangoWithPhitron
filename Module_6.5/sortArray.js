const ar = [12,14,16,18,20,1,3,5,7,9,10,11,13,15,17,19,20,4,6,8]

function sortNumericArray(ar){
    for (let i = 0 ; i< ar.length-1 ; i++){
        for(let j = i+1 ; j < ar.length ; j++ ){
            if (ar[i] > ar[j]){
                let temp = ar[i];
                ar[i] = ar[j];
                ar[j] = temp;
            }
                
        }
    }
    return ar;
} 

let result = sortNumericArray(ar)
console.log(result);