

##Exception handling

##syntax error
##a=10
##b=20
##if(a>b)
##    print("bharani")





##exception

##mark=200
##a=mark/0
##print(a)






#type error

##x=10
##y="bharani"
##z=x+y
##print(z)




#try catch to resolve typeerror
##x = 5
##y = "hello"
##try:
##    z = x + y
##except TypeError:
##    print("Error: cannot add an int and a str")






####try except
##a = [1, 2, 3]
####try:
##    print ("Second element = %d" %(a[1]))
## 
##    # Throws error since there are only 3 elements in array
##    print ("Fourth element = %d" %(a[3]))
## 
####except:
####    print ("An error occurred")





##try except
##a = [1, 2, 3]
####try:
##print ("Second element = %d" %(a[1]))
## 
##    # Throws error since there are only 3 elements in array
##print ("Fourth element = %d" %(a[3]))
 
##except:
##    print ("An error occurred")






#zero division error and name error

def fun(a):
    if a < 4:

        b = a/(a-3)# throws ZeroDivisionError for a = 3
 
    print("Value of b = ", b) # throws NameError if a >= 4
     
try:
    #fun(3)
    fun(5)
 
# note that braces () are necessary here for
# multiple exceptions

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")







#zero division with try , except and else

def fun(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
fun(30,10)




try:
    a=10
    b=20
except exception as ex:
    
    
