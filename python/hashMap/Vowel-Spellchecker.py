class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        setWords = set(wordlist)
        cap = {w.lower(): w for w in wordlist[::-1]}
        vowel = {re.sub("[aeiou]", '#', w.lower()): w for w in wordlist[::-1]}
        ret = []
        for query in queries:
            if query in setWords:
                ret.append(query)
            elif query.lower() in cap:
                ret.append(cap[query.lower()])
            elif re.sub("[aeiou]", '#', query.lower()) in vowel:
                ret.append(vowel[re.sub("[aeiou]", '#', query.lower())])
            else:
                ret.append("")
        return ret
