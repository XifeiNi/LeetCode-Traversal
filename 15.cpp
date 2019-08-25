class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 0; i < n-2; ++i) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            int target = nums[i]*(-1);
            int left = i + 1;
            int right = n - 1;
            while (left < right) {
                if (nums[left] + nums[right] == target) {
                    vector<int> tmp;
                    tmp.push_back(target*(-1));
                    tmp.push_back(nums[left]);
                    tmp.push_back(nums[right]);
                    results.push_back(tmp);
                    while (left < right && nums[left] == nums[left+1]) left++;
                    while (left < right && nums[right] == nums[right -1]) right--;
                    left++;
                    right--;
                } else if (nums[left] + nums[right] <  target) {
                    left ++;
                } else {
                    right--;
                }
            }
        }
        return results;
    }
    
    
};
