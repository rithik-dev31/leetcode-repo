# Last updated: 8/12/2026, 11:32:08 AM
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        result=[[1]]

        for i in range(rowIndex):
            temp=[0]+result[-1]+[0]
            temp_res=[]
            for j in range(len(temp)-1):
                temp_res.append(temp[j]+temp[j+1])
            
            result.append(temp_res)

        return result[rowIndex]