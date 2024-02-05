function persistence(num) {
    let persistenceCount = 0;

    function calculateProduct(n) {
        return n.toString().split('').reduce((acc, digit) => acc * parseInt(digit, 10), 1);
    }

    while (num >= 10) {
        num = calculateProduct(num);
        persistenceCount++;
    }

    return persistenceCount;
}