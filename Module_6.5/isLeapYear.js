function isLeapYear(year){
    if(year % 400 == 0){
        return true;
    }
    else if (year % 4 == 0 && year % 100 != 0){
        return true;
    }
    else return false
}

let y = 2401;

isLeapYear(y) ? console.log("This year is : 'Leap Year'") : console.log("This Year is : 'NOT Leap Year'");