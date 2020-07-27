"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employeesMap = {}
        for em in employees:
            employeesMap[em.id] = em
        return self.dfs(employeesMap, id)
    def dfs(self, employeesMap, id):
        for employee in employeesMap[id].subordinates:
            employeesMap[id].importance += self.dfs(employeesMap, employee)
        return employeesMap[id].importance
