class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        new_time = []
        for time in timePoints:
            temp_list = time.split(':')
            new_time.append(int(temp_list[0])*60 + int(temp_list[1]))
        new_time = sorted(new_time)
        #print(new_time)
        min_ret = 100000
        for i in range(len(new_time) - 1):
            if abs(new_time[i]-new_time[i+1]) < min_ret:
                min_ret = abs(new_time[i]-new_time[i+1])
        if len(new_time) > 1 and abs(24*60 - new_time[-1] + new_time[0]) < min_ret:
            min_ret = abs(24*60 - new_time[-1] + new_time[0]) 
        return min_ret
            
            
        
