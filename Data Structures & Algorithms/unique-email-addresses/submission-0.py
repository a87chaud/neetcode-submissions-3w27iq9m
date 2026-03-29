class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # . in local name = sent to both addresses
        # + in local name = ignore everything
        email_set = set()
                
        def clean(s) -> s:
            s_split = s.split('+')[0]
            final_s = ''.join(s_split.split('.'))
            return final_s
        for e in emails:
            name_and_domain = e.split('@')
            final_name = clean(name_and_domain[0])
            final_domain = name_and_domain[1]
            final_addr = final_name + '@' + final_domain
            print(final_addr)
            email_set.add(final_addr)

        return len(email_set)