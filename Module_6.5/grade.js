var result = -66;

if (0 <= result && result < 33 ){
    console.log("Opps!!! You Have Failed.")
}
else if ( 33 <= result && result < 40 ){
    console.log("Congratulations! You Got 'D'.")
}
else if ( 40 <= result && result < 50 ){
    console.log("Congratulations! You Got 'C'.")
}
else if ( 50 <= result && result < 60 ){
    console.log("Congratulations! You Got 'B'.")
}
else if ( 60 <= result && result < 70 ){
    console.log("Congratulations! You Got 'A-'.")
}
else if ( 70 <= result && result < 80 ){
    console.log("Congratulations! You Got 'A'.")
}
else if ( 80 <= result && result <= 100 ){
    console.log("Congratulations! You Got 'A+'.")
}
else {
    console.log("Invalid Number")
}