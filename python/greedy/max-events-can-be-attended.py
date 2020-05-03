class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        # heappop(events)
        # print(events)
        
        ans=0
        heap=[]
        cur=0
        buf=0
        
        for i in events:
            if heap:
                if cur==i[0]:
                    heappush(heap, i[1])
                    continue
                else:
                    while cur<i[0] and heap:
                        buf=heappop(heap)
                        while buf<cur and heap:
                            buf=heappop(heap)
                        if buf < cur:
                            break
                        else:
                            ans+=1
                            cur+=1
            heappush(heap, i[1])
            cur=i[0]
        
        while heap:
            buf=heappop(heap)
            while buf<cur and heap:
                buf=heappop(heap)
            if buf < cur:
                break
            else:
                ans+=1
                cur+=1
        
        return ans
