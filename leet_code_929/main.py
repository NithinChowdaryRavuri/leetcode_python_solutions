class Solution(object):
    def numUniqueEmails(self, emails):
        unique_emails = set()
        for email in emails:
            local_name, domain = email.split("@")
            local_name = local_name.split("+")[0].replace(".", "")
            unique_emails.add(local_name + "@" + domain)
        return len(unique_emails)