<h2>1032. Stream of Characters</h2><h3>Hard</h3><hr><div><p>Implement the <code>StreamChecker</code> class as follows:</p>

<ul>
	<li><code>StreamChecker(words)</code>: Constructor, init the data structure with the given words.</li>
	<li><code>query(letter)</code>: returns true if and only if for some <code>k &gt;= 1</code>, the last <code>k</code>&nbsp;characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 2000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 2000</code></li>
	<li>Words will only consist of lowercase English letters.</li>
	<li>Queries will only consist of lowercase English letters.</li>
	<li>The number of queries is at most&nbsp;40000.</li>
</ul>
</div>