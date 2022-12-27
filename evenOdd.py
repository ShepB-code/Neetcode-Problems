class Solution:
    def oddEvenJumps(self, arr) -> int:
        oddMemo = {}
        evenMemo = {}
        numValid = 0
        for i in range(0, len(arr)):
            if(self.isPossibleStart(i, arr, 1, oddMemo, evenMemo)):
                numValid += 1
            
        return numValid
    
    def isPossibleStart(self, index: int, arr, jumpNum: int, oddMemo, evenMemo) -> bool:
        # check if at end of array (base case)
        if index == len(arr) - 1:
            return True
        
        # now try to get to the end
        if jumpNum % 2 != 0: # odd jump
            # search for another index that satisfies arr[index] <= arr[new]
            if index in oddMemo: #previously found a valid jump from currPos

                if oddMemo[index] == -1:
                    return False

                return self.isPossibleStart(oddMemo[index], arr, jumpNum + 1, oddMemo, evenMemo)

            else: # index is unsearched
                nextIndex: int = self.searchForSmaller(index, arr)
                if nextIndex == index:
                    oddMemo[index] = -1
                    # no more possible moves
                    return False
                else:
                    # go another depth
                    oddMemo[index] = nextIndex
                    return self.isPossibleStart(nextIndex, arr, jumpNum + 1, oddMemo, evenMemo)
                    
        else: # even jump
            # search for another index that satisfies arr[index] >= arr[new]
            if index in evenMemo: #previously found a valid jump from currPos
                if evenMemo[index] == -1:
                    return False
                return self.isPossibleStart(evenMemo[index], arr, jumpNum + 1, oddMemo, evenMemo)
            else: # index is unsearched
                nextIndex: int = self.searchForLarger(index, arr)
                if nextIndex == index:
                    evenMemo[index] = -1
                    # no more possible moves
                    return False
                else:
                    # go another depth
                    #print("Jumping to ", nextIndex)
                    evenMemo[index] = nextIndex
                    return self.isPossibleStart(nextIndex, arr, jumpNum + 1, oddMemo, evenMemo)

    def searchForSmaller(self, index: int, arr) -> int:
        smallest: int = index
    
        for i in range(index + 1, len(arr)):
            if arr[index] <= arr[i]: # even condition

                # now get the smallest that satisfy this condition
                if smallest == index:
                    # set largest
                    smallest = i
                
                if arr[i] < arr[smallest]:
                    smallest = i
            
        return smallest

    def searchForLarger(self, index: int, arr) -> int:
        largest: int = index
    
        
        for i in range(index + 1, len(arr)):
            if arr[index] >= arr[i]: # even condition

                # now get the largest that satisfy this condition
                if largest == index:
                    # set largest
                    largest = i
                
                if arr[i] > arr[largest]:
                    largest = i
                    

        return largest