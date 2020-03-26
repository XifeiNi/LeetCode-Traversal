// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {
    Iterator<Integer> iter;
    Integer peek;
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
        iter = iterator;
        peek = (iter.hasNext() ? iter.next() : null);
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return peek;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    Integer next = null;
        if (hasNext()) {
            next = peek;
            peek = (iter.hasNext() ? iter.next() : null);
        }
        return next;
	}

	@Override
	public boolean hasNext() {
	    return peek == null ? false : true;
	}
}
