

##Regular expression:
##search()
##import re
##txt="my name is bharani"
##x=re.search("name",txt)
##print("yes it is have:",x)

##white space
##import re
##txt="my name is bharani"
##x=re.search("\s",txt)
##print("white space in the position of:",x.start())

##
##import re
##txt="myname isbharani"
##x=re.search("\s",txt)
##print("white space in the position of:",x.start())##it will throw a nonetype attribute error

##findall()
##import re
##txt="my name is bharani"
##x=re.findall("a",txt)
##print("it is have:",x)

##import re
##txt="my name is bharani"
##x=re.findall("z",txt)
##print("it is have:",x)

##split()
##import re
##txt="age is 24"
##x=re.split("\s",txt)
##print(x)

#maximum splitting
##import re
##txt="my name is bhrani and age is 24"
##x=re.split("\s",txt,5)##number indicates the maximum splitting
##print(x)

#sub()-replace every white space character into given value $
##import re
##txt="my name is bhrani and age is 24"
##x=re.sub("\s","$",txt)
##print(x)


##import re
##txt="my name is bhrani and age is 24"
##x=re.sub("\s","$",txt,3)
##print(x)

##import re
##txt="my Name is bharani"
##x=re.search("",txt)
##print(":",x)




##import re
##
### Regular expression pattern for a 10-digit mobile number
##pattern = r"^[1-9]\d{9}$"
##
### Input phone number
##phone_number = "9876543213"
##
### Match the pattern against the phone number
##match = re.match(pattern, phone_number)
##
##if match:
##    print("Valid mobile number")
##else:
##    print("Invalid mobile number")

import re

# Regular expression pattern for a Gmail email address
pattern = r"^[a-zA-Z0-9_.+-]+@gmail\.com$"

# Input email address
email = "example@gmail.com"

# Match the pattern against the email address
match = re.match(pattern, email)

if match:
    print("Valid Gmail address")
else:
    print("Invalid Gmail address")



