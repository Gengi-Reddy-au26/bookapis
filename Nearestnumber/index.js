const findClosest = (arr,num) => {
    if(array == null){
      return
    }
    return arr.sort((a,b) => Math.abs(b - num) - Math.abs(a-num)).pop();
  }
  
  const array = [10,20,30,40,50,60,70,80,90];
  const num = 50;
  console.log(findClosest(array,num));