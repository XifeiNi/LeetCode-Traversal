from collections import defaultdict
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = defaultdict(int)
        for domain in cpdomains:
            visits = int(domain.split()[0])
            domain_seg = domain.split()[1].split('.')
            top_level = domain_seg[-1]
            second_level = domain_seg[-2] + '.' + domain_seg[-1]
            count[top_level]+=visits
            count[second_level]+=visits
            if domain.count('.') == 2:
                count[domain.split()[1]]+=visits
        return [str(link) + ' ' + str(visit) for visit, link in count.items()]
            
