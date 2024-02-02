function accum(s) {
    return s.split('').map((char,index) => {
      const repChar = char.toLowerCase().repeat(index+1);
      return repChar.charAt(0).toUpperCase() + repChar.slice(1);
    }).join('-');
  }