class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        b = []
        for i in accounts:
            a = sum(i)
            b.append(a)
        return max(b)
