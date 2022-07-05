// var arrow = () => {
//     for (var i = 1;  i<=10 ;i++) {
        
//         console.log(i,"hello!");
//     }
// }
// arrow()



// Q-2) write an ARROW FUNCTION to find the bigger of the 2 variables?
// Hint: use the ternary operator
let a=8
let b=9
let arrow =(a,b) => (a>b) ? a : b;

          
console.log(arrow(6,9), " is biggest of 2 variables")

let arr =(a,b) => {

const ans =(a>b) ? a : b;
return ans
}

          
console.log(arr(11,10), " is biggest of 2 variables")