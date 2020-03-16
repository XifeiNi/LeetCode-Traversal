class MyCalendar {
    TreeMap<Integer, Integer> calendar;
    public MyCalendar() {
        this.calendar = new TreeMap();
    }
    
    public boolean book(int start, int end) {
        Integer previous = calendar.floorKey(start);
        Integer next = calendar.ceilingKey(start);
        if ((previous == null 
             || calendar.get(previous) <= start) 
            && (next == null 
                || end <= next)) {
            calendar.put(start, end);
            return true;
        }
        return false;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
