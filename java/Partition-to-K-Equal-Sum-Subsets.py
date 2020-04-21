class Solution {
       public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0;
        for (Integer num : nums) {
            sum += num;
        }
        
        if (sum % k != 0) {
            return false;
        }
        
        boolean[] visited = new boolean[nums.length];
        return helper(nums, visited, 0, k, 0, sum/k);
    }
    
    public boolean helper(int[] nums, boolean[] visited,
                          int start, int k, int sum, int target) {
       
        if (k == 1) {
           return true;
        }

        if (sum == target) {
            return helper(nums, visited, 0, k - 1, 0, target);
        }
        
        for (int i = start; i < nums.length; i++) {
            if (visited[i] || sum + nums[i] > target) {
                continue;
            }
            
            visited[i] = true;
            if (helper(nums, visited, i + 1, k, sum + nums[i], target)) {
                return true;
            }
            visited[i] = false;
        }
        
        return false;
    }   
    
}
