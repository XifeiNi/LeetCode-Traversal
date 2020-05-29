/**
 * @param {string[]} words
 * @return {string}
 */
var longestWord = function(words) {
    words.sort();
    const wordSet = new Set(words);
    let res = '';
    for (const word of words) {
        let isValid = true;
        let key = '';
        for (let i = 0; i < word.length - 1; i++) {
            key += word[i];
            if (!wordSet.has(key)) {
                isValid = false;
                break;
            }
            
        }
        if (isValid && word.length > res.length) {
            res = word;
        }
    }
    return res;
};
