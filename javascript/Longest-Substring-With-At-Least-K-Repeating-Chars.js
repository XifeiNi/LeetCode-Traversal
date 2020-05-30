/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function(s, k) {
    let hash = {}, max = 0;
    s.split('').forEach((val) => {hash[val] = hash[val] + 1 || 1});
    let chars = Object.entries(hash).filter(([key, val]) => val < k);
    if (chars[0]) {
        for (var seg of s.split(chars.shift()[0])){
            max = Math.max(longestSubstring(seg, k), max);
        }
        return max;
    }
    return s.length;
    
};
