class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        if len(order) == 0 or order is None or len(friends) == 0 or friends is None:
            return []
        id_to_position = dict()
        temp = [0]*len(order)
        res = []
        for i in range(0,len(order)):
            id_to_position[order[i]] = i
        
        for i in range(0,len(friends)):
            temp[id_to_position[friends[i]]]= friends[i]
        for i in range(0, len(temp)):
            if temp[i] != 0:
                res.append(temp[i])
        return res
        
         
        