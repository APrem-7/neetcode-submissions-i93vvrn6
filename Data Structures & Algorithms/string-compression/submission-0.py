class Solution:
    def compress(self, chars: List[str]) -> int:

        s = []
        indi = 1

        for r, i in enumerate(chars):

            # handle last character
            if r == len(chars) - 1:
                if r > 0 and chars[r-1] == chars[r]:
                    s.append(i)
                    if indi > 1:
                        for digit in str(indi):
                            s.append(digit)
                else:
                    s.append(chars[r])

            # normal comparison
            elif i == chars[r+1]:
                indi += 1

            else:
                if indi > 1:
                    s.append(i)
                    for digit in str(indi):
                        s.append(digit)
                    indi = 1
                else:
                    s.append(i)
        
        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)