public class Solution {
    /**
     * @param s: the given string
     * @return: all the possible states of the string after one valid move
     */
    public List<String> generatePossibleNextMoves(String s) {
        // write your code here
        List rst = new ArrayList();
        for (int i = -1; (i = s.indexOf("++", i+1)) >= 0;) {
            rst.add(s.substring(0, i) + "--"+s.substring(i+2));
        }
        return rst;
    }
}
