def minPartitions(self, n: str) -> int:
        for d in "987654321":
            if d in n:
                return int(d)
            
# second approach
def minPartitions(self, n: str) -> int:
        return int(max(n))

# third approach
def minPartitions(self, n: str) -> int:
        a=set(n)
        a=max(a)
        return int(a)

# fourth approach
def minPartitions(self, n: str) -> int:
        s = set(n)
        for ch in '9876543210':
            if ch in s:
                return int(ch)