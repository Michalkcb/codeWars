import { string } from "prop-types";

function persistence(num){
    let persCount = 0;

   while (num >= 10){
    num = string(num).split(' ').reduce((acc,digit) => acc * digit,1)
    persCount++
   }

    return persCount;
}
