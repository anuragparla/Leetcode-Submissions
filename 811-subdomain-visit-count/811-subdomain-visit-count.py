def retreiveDomains(self, cpdomains):
        map = collections.Counter()
        for i in range(len(cpdomains)):
            domainWithCount = cpdomains[i].split(" ")
            count = int(domainWithCount[0])
            domain = domainWithCount[1].split(".")

            # self.storeDomains(map, count, domain)
            for i in range(len(domain)):
                map[".".join(domain[i:])] += count
        res =[]
        for domain,count in map.items():
            count = str(count)
            res.append(count + " " + domain)
        
        return res


        

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        return self.retreiveDomains(cpdomains)
