class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[1,1,0]
        for nb in nums:
            if nb !=0:
                product[0] *=nb
            else:
                product[2]+=1
            product[1] *=nb
        
        output=[]
        for nb in nums:
            if nb==0 and product[2]<2:
                output.append(product[0])
            elif nb==0:
                output.append(0)
            else:
                output.append(product[1]//nb)
        
        return output
            