class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_value=[1,1,0]
        for nb in nums:
            if nb !=0:
                list_value[0] *=nb
            else:
                list_value[2]+=1
            list_value[1] *=nb
        
        output=[]
        for nb in nums:
            if nb==0 and list_value[2]<2:
                output.append(list_value[0])
            elif nb==0:
                output.append(0)
            else:
                output.append(list_value[1]//nb)
        
        return output
            