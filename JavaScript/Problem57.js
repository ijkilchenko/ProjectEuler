var Big = require('big-integer');

var s = new Object();

function getFraction(i) {
    if (s[i] != undefined) {
        return s[i];
    }
    else {
        s[i] = _getFraction(i, {'n' : 2, 'd' : 1});
        return s[i];
    }
}

function _getFraction(i, f) {
    if (i == 0) {
        var den = Big(f['n']);
        var num = Big(f['n']).add(f['d']);
        return {'n' : num, 'd' : den};
} else {
        var den = Big(f['n']);
        var num = Big(2).multiply(f['n']).add(f['d']);
        f = {'n' : num, 'd' : den};
        return _getFraction(i - 1, f);
    }
}

function isNumLonger(f) {
    var numLength = getLength(f['n']);
    var denLength = getLength(f['d']);
    if (numLength > denLength) {
        return true;
    } else {
        return false;
    }
}

function simplify(f) {
    var gcd = Big.gcd(f['n'], f['d']).value;
    while (gcd != 1) {
        f['n'] = f['n'].divide(gcd);
        f['d'] = f['d'].divide(gcd);
        gcd = Big.gcd(f['n'], f['d']).value;
    }
    return f;
}

function getLength(num) {
    return num.toString().replace(/,/g, '').length; 
}

var count = 0;
for (i = 0; i < 1000; i++) {
    z = getFraction(i);
    /*
    Question to self: is it immediately clear that you don't need to simplify ever?
    */

    //z = simplify(z);
    if (isNumLonger(z)) {
        count += 1;
    }
}
console.log(count);

