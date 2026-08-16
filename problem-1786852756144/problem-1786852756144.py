# Last updated: 8/16/2026, 9:29:16 AM
1class Solution(object):
2    def nearestDrone(self, drones, target):
3        """
4        :type drones: List[List[int]]
5        :type target: List[int]
6        :rtype: int
7        """
8
9        tx,ty=target
10        m_d=float('inf')
11
12        a=-1
13
14        for i in range (len(drones)):
15            x,y,r=drones[i]
16            d=abs(x-tx)+abs(y-ty)
17
18            if d<=r:
19                if d<m_d:
20                    m_d=d
21                    a=i
22
23        return a
24            
25            
26        