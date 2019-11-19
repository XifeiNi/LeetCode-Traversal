'''
slotsA = [[5, 10], [60, 120], [140, 210]]
slotsB = [[0, 15], [20, 55], [60 , 70]]
        dur = 8
'''
'''
def meeting_planner(slotsA, slotsB, dur):
  
  points = []
  
  for element in slotsA:
    points.append((element[0], 1))
    points.append((element[1], -1))
  for element in slotsB:
    points.append((element[0], 1))
    points.append((element[1], -1))
  #print(points)
  before, after = 0, 0
  count = 0
  for time, delta in sorted(points):
    #print(time, delta)
    count+=delta
    before = after
    after = time
    if count == 1:
      if delta == -1:
        if after - before >= dur:
          return [before, before + dur]
  return []
'''
def meeting_planner(slotsA, slotsB, dur):
  i = 0
  j = 0
  count = 0
  while i < len(slotsA) and j < len(slotsB):
    while slotsA[i][1] < slotsB[j][0]:
      i+=1
    while slotsB[j][1] < slotsA[i][0]:
      j+=1
    if min(slotsB[j][1], slotsA[i][1]) - max(slotsA[i][0], slotsB[j][0]) >= dur:
      return [max(slotsA[i][0], slotsB[j][0]),max(slotsA[i][0], slotsB[j][0]) + dur]
    else:
      if slotsB[j][1] > slotsA[i][1]:
        i+=1
      else:
        j+=1
      
  
  return []

 

# 
slotsA = [[0, 50], [60, 120], [140, 210]]
slotsB = [[0, 1], [3, 4], [10,30], [60, 70]]
dur = 8

meeting_planner(slotsA, slotsB, dur)
     
      
    
