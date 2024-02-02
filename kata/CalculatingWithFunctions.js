function zero(o) {return o ? o(0) : 0}
function one(o) {return o ? o(1) : 1}
function two(o) {return o ? o(2) : 2}
function three(o) {return o ? o(3) : 3}
function four(o) {return o ? o(4) : 4}
function five(o) {return o ? o(5) : 5}
function six(o) {return o ? o(6) : 6}
function seven(o) {return o ? o(7) : 7}
function eight(o) {return o ? o(8) : 8}
function nine(o) {return o ? o(9) : 9}

function plus(r) {return function(l){return l + r}}
function minus(r) {return function(l){return l - r}}
function times(r) {return function(l){return l * r}}
function dividedBy(r) {return function(l){return Math.floor(l / r)}}