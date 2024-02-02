function spinWords(string){
    return string.split(' ').map(word => (word.length >= 5) ? word.split('').reverse().join('') : word).join(' ');
  }