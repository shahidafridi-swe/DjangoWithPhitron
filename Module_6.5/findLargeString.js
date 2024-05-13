function findLargeString(ar){
    let largeString = ar[0];

    for(let i = 0 ; i < ar.length ; i++){
        if (largeString.length < ar[i].length){
            largeString = ar[i];
        }
    }
    return largeString;
}

var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];

let result = findLargeString(friends);
console.log(result);