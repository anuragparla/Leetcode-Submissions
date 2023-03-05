# split @ 
# . rule applies only for local if . then remove . and concat 
# + ru;e aplies only for local  if + then ignore every till @ 



class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        map = dict()
        for i in emails:
            temp = i.split("@")
            local = temp[0]
            domain = temp[1]
            if '+' in local:
                index = local.find('+')
                local = local[:index]
            if '.' in local:
                local = local.replace('.','')
            email = local +'@'+domain
            if email not in map:
                map[email] =1 
            else:
                map[email] +=1 
        return len(map.keys())
