
String.prototype.shuffle = function () { 
    return this.split('').sort(() => Math.random() - 0.5).join('') 
}

console.log( '0123456789'.shuffle() )
// print '4382715906'