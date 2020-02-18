import re
'''
marks = "123 1234 12345 123456 1234567"
print("matches", len(re.findall("\d{5,7}", marks)))


phone = "412-55555-1212"

if re.search("\d{3}-\d{4}-\d{4}", phone):
    print("Phone no is valid")
else:
    print("Phone no is not valid")
'''

if re.search("\w{2,20}\s\w{2,20}","Varsha Mohite"):
    print("FullName is valid")

email = "vm@mp.com md2@ab.com xyzz.com a@a a2a@gmail.com"

print("Email Matches", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,5}", email)))