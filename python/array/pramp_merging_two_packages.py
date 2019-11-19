#  arr = [4, 6, 10, 15, 16],  lim = 21
def get_indices_of_item_wights(arr, limit):
  hashmap = {}
  for i in range(len(arr)):
    if arr[i] in hashmap:
      return [i, hashmap[arr[i]]]
    hashmap[limit-arr[i]] = i
  return []
