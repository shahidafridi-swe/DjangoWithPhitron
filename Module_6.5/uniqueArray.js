function removeDuplicate(ar){
    var uniqueArray= [];
    for (let i=0; i< ar.length; i++){
        let element = ar[i];
        let check = uniqueArray.indexOf(element);
        if (check == -1){
            uniqueArray.push(element)
        }
    }
    return uniqueArray
}


const arr = [1,2,2,3,2,1,5,6,7]
const result = removeDuplicate(arr)
console.log(result)