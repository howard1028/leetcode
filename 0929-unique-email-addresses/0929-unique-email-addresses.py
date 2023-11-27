class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        # 處理local name
        local_name = []
        for i in range(len(emails)):
            s = emails[i].split("@")
            local = s[0]
            domain = s[1]

            if "+" in local:
                local = local.split("+")[0]
            local = local.replace('.','')
            print(local)
            local_name.append(local + " " + domain)

        # 轉成set(set不會包含重複的資料)
        set1 = set([i for i in local_name])

        print(set1)
        return len(set1)
