class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for strings in details:
            age = int(strings[11:13])   # extract age
            if age > 60:
                count += 1
        return count