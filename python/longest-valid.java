public class Solution {
    public int shortestValidParentheses(String s) {

        if (s == null) {
            return 0;
        }

        Stack<Integer> stack = new Stack<Integer>();
        int maxLen = 0;
        int accumulatedLen = 0;

        for(int i = 0; i < s.length(); i++) {
    	    if (s.charAt(i).isLetter()) {
    		  continue;
    	    }
            
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                if (stack.isEmpty()) {   //如果栈为空，没有左括号可以匹配
                    accumulatedLen = 0;
                } else {
                    int matchedPos = stack.pop(); //从最近的'('作为起点
                    int matchedLen = i - matchedPos + 1;    //计算两括号间的长度

                    if (stack.isEmpty()) {			//如果栈为空，没有左括号可以匹配
                        accumulatedLen += matchedLen;	
                        matchedLen = accumulatedLen;	//更新当前匹配括号序列长度
                    } else {
                        matchedLen = i - stack.peek();  
                    }

                    minLen = Math.min(minLen, matchedLen);
                }
            }
        }

        return maxLen;
   }
}
