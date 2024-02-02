function expandedForm(num) {
    const numStr = num.toString(); 
    const result = [];
  
    for (let i = 0; i < numStr.length; i++) {
      const d = parseInt(numStr[i], 10);
  
      if (d !== 0) {
        const placeValue = Math.pow(10, numStr.length - i - 1);
        result.push(d * placeValue);
      }
    }
  
    return result.join(' + ');
}