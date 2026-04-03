class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #we will find the total number of customers satisfied with the base + window
        cur=0
        for i in range(minutes):
            if grumpy[i]==1:
                cur+=customers[i]

        best=cur
        
        base = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]
        #this is the base initilaly fow window then with this we will add the grumpy array and check and just keep sliding this window forward
        for i in range(minutes, len(customers)):

            if grumpy[i]==1:
                #we add this in the array
               cur+=customers[i]
            
            if grumpy[i - minutes] == 1:
                cur -= customers[i - minutes]

            best=max(cur,best)
        return best+base

