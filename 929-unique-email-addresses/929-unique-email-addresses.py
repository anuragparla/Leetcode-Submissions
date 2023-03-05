# split @ 
# . rule applies only for local if . then remove . and concat 
# + ru;e aplies only for local  if + then ignore every till @ 
# using hashmap gave me a higher efficiency


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for i in emails:
            temp = i.split("@")
            local = temp[0]
            domain = temp[1]
            local = local.split('+')[0].replace('.','')
            email = local +'@'+domain
            uniqueEmails.add(email) 
        return len(uniqueEmails)

