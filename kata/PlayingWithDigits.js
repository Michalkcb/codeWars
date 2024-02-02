function digPow(n, p) {
    const digits = Array.from(String(n), Number);
    const sum = digits.reduce((acc, digit, index) => acc + Math.pow(digit, p + index), 0);
    const k = sum / n;
  
    return Number.isInteger(k) ? k : -1;
  }