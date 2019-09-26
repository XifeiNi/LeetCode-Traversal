from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentDict = defaultdict(list)
        for i in range(len(paths)):
            # get the path
            files = paths[i].split(' ')
            absolute = files[0]
            for i in range(1, len(files)):
                content_index = files[i].find('(')
                content = files[i][content_index+1:-1]
                name = absolute + '/' + files[i][:content_index]
                contentDict[content].append(name)
        ret = []
        for key in contentDict.keys():
            if len(contentDict[key]) > 1:
                ret.append(contentDict[key])
        return ret
                
