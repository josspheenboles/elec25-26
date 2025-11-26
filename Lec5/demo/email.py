import re
pattern = r'\w+@\w+\.\w+'
email=input("Enter your email address:")
# email='asd@gmail.com'
# email='asd@gmail.com sdkjl'
#strat with email dfjkdfjlsdfj
print(re.match(pattern,email) )
#all str is email
print(re.fullmatch(pattern,email) )
#sfjslfj email sjdasjkdj email
#list of email
print(re.findall(pattern,email) )
#find first email
print(re.search(pattern,email) )




