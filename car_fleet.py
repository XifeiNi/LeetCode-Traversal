class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      cars = sorted(zip(position, speed))
      times = [(target - pos)/s for pos, s in cars]
      carFleet = 0
      i = len(cars) - 1
      if len(cars) == 1:
        return 1
      while i > 0:
        if times[i] < times[i-1]:
          carFleet+=1
        else:
          times[i-1] = times[i]
        i-=1
      if len(times) > 1:
        carFleet+=1
      
      return carFleet
