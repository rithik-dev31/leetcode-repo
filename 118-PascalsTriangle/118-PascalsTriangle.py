# Last updated: 8/12/2026, 11:32:11 AM
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """


        result=[[1]]

        for i in range(numRows-1):
            temp=[0]+result[-1]+[0]
            temp_res=[]
            for j in range(len(temp)-1):
                temp_res.append(temp[j]+temp[j+1])
            result.append(temp_res)

        return result