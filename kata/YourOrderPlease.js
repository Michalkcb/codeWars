function order(words) {
    if (words.trim() === '') {
        return '';
    }

    return words
        .split(' ')
        .sort((a, b) => a.match(/\d/) - b.match(/\d/))
        .join(' ');
}