class Solution:
    #taking all the elemnents/keys into an arrya and from there looping throught that array 
    #to and printing out all the values pertaining to that key and inserting then in the form of a 2D
    #array inside our 1D array

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #creating a dict to store values
        groups = {}

        for string in strs:
            key = ''.join(sorted(string))
        
            if key in groups:
                groups[key].append(string)
            else:
               groups[key]= [string]
        result = list(groups.values())
        return result
        #now array will have all the key now just check in my dict all the value in that    
        
        #so now i have the sorted the stuff and must return

