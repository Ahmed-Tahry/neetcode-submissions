class Solution:
    def isPalindrome(self, s: str) -> bool:
        n =  []
        for i in s:
            if i.isalnum():
                n.append(i)
        i=0
        j=len(n)-1
        while i<j:
            if n[i].upper() != n[j].upper():
                return False
            i= i +1
            j= j -1
        return True