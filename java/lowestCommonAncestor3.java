public class lowestCommonAncestor3{
    /*
     * @param root: The root of the binary tree.
     * @param A: A TreeNode
     * @param B: A TreeNode
     * @return: Return the LCA of the two nodes.
     */
    public TreeNode lowestCommonAncestor3(TreeNode root, TreeNode A, TreeNode B) {
        // write your code here
        TreeNode res = divideConquer(root, A, B);
        if (foundA && foundB){
            return res;
        } else {
            return null;
        }
        
    }
    
    private boolean foundA = false, foundB = false;
    public TreeNode divideConquer(TreeNode root, TreeNode A, TreeNode B){
        if (root == null){
            return null;
        }
        
        TreeNode leftAncestor = divideConquer(root.left, A, B);
        TreeNode rightAncestor =  divideConquer(root.right, A, B);
        if (root == A || root == B){
            foundA = (root == A) || foundA;
            foundB = (root == B) || foundB;
            return root;
        }
        if (leftAncestor != null && rightAncestor != null){
            return root;
        }
        if (leftAncestor != null){
            return leftAncestor;
        }
        if (rightAncestor != null){
            return rightAncestor;
        }
        
        return null;
    }
}
