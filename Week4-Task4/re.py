

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

##
##import re
##
##txt = "my name Swetha and age is 24"
##x = re.search(r"\bS\w+", txt)
##print(x.span())
##
##import re

##txt = "my name swetha and age is 24"
##x = re.search(r"\bs\w+", txt)
##print(x.span())

##import re
##txt = "my name swetha and age is 24"
##x=re.search(r'\.',txt)
##print(x)








