/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var canMakePaliQueries = function(s, queries) {
    const freq = createFreq(s);
    return queries.map((query) => canMakePalInKSteps(s, freq, ...query));
};

function canMakePalInKSteps(s, freq, start, end, k) {
    var count = 0;
    for (let i = 0; i < 26; i ++) {
        const c = String.fromCharCode(97 + i);
        const f = freq[c][end] - (freq[c][start - 1] || 0);
        count += f % 2 === 1 ? 1 : 0;
    }
    return Math.floor(count / 2) <= k;
}
    
function createFreq(s) {
    const freq = {};
    for (var i = 0; i < 26; i++) {
        const c = String.fromCharCode(97 + i);
        freq[c] = new Array(s.length).fill(0);
    }
    
    for (var i = 0; i < s.length; i ++) {
        for (var j = 0; j < 26; j ++) {
            const c = String.fromCharCode(97 + j);
            freq[c][i] =  (freq[c][i - 1] || 0) + (s[i] === c ? 1 : 0);
        }
    }
    return freq;
}
