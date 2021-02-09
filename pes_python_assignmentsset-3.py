import calendar

print (calendar.calendar(2016,w=2,l=1,c=10))

print ("number of leapdays between the years 1980 and 2025 is ",calendar.leapdays(1980,2025))

year=input("Enter the year:")
if calendar.isleap(year):
  print (year,"is leap year")
else:
  print (year,"is NOT leap year")


month=input("enter the month(between 1 and 12) for 2016:")
print (calendar.month(2016,month,w=2,l=1))

--------------------------------------------------------------------------------------------------


def fib(N):
  p2num=0
  p1num=1
  yield(p2num)
  yield(p1num)
  for i in range(N-2):
    cnum=p1num+p2num
    yield(cnum)
    p2num=p1num
    p1num=cnum  
N=input("Enter the required number of elements in series")
f=fib(N)
for i in f:
  print (i,)
  
-----------------------------------------------------------------------------------------------------------



def search(*arguments):
  list1=[1,2,3,4,5,6,7,8,9]
  for arg in arguments: 
    if arg in list1:
      print (arg,"is present in the list ",list1)
search(1,2,3)

--------------------------------------------------------------------------------------------------


add=lambda x,y: x+y
print (add(4,2))

sub=lambda x,y: x-y
print (sub(4,2))

mul=lambda x,y: x*y
print (mul(4,2))

div=lambda x,y: x/y
print (div(4,2))

modules=lambda x,y: x%y
print (modules(4,2))

fooler_division =lambda x,y: x//y
print (fooler_division(5,2))

--------------------------------------------------------------------------------------------------


def isPalindrome(str="nitin"):
  if str=="":
    print ("empty string")
  else:
    rev_str=str[::-1]
    if(str==rev_str):
      print (str," is palindrome")
    else:
      print (str," is not palindrome")
           
isPalindrome(input("Enter the string:"))

-------------------------------------------------------------------------------------------------

def biggestOfFour(n1,n2,n3,n4):
   bign=n1
   if(n2>bign):
     bign=n2
   if(n3>bign):
     bign=n3
   if(n4>bign):
     bign=n4
   print ("biggest among four numbers ",n1,n2,n3,n4," is ",bign)
   
biggestOfFour(10,22,333,43)


def biggestOfFour(n1=0,n2=0,n3=0,n4=0):
   bign=n1
   if(n2>bign):
     bign=n2
   if(n3>bign):
     bign=n3
   if(n4>bign):
     bign=n4
   print ("biggest among four numbers ",n1,n2,n3,n4," is ",bign)
   
biggestOfFour(23,34,43,41)
-------------------------------------------------------------------------------------------------

def addListToTuple(list1,tuple1):
   
   list1=list(tuple1)+list1
   
   tuple2=tuple(list1)
   print ("given list",list1,"is added to given tuple ",tuple1)
   print ("now the extened tuple is ",tuple2)

addListToTuple([11,22,33,44],(44,55,66,77))

-------------------------------------------------------------------------------------------------

def add(a1,a2):
  print ("addition of ",a1," and ",a2," is -> ",a1+a2)
  
def sub(a1,a2):
  print ("subtraction of %d from %d is -> %d"%(a2,a2,a1-a2))

def mul(a1,a2):
  print ("multiplication of ",a1," and ",a2," is -> ",a1*a2)

def div(a1,a2):
  print ("division of ",a1," by ",a2," is -> ",a1/a2)
    
x,y =input("Enter two numbers on which you want to perform math operations :").split()
x = int(x)
y= int(y)
add(x,y)
sub(x,y)
mul(x,y)
div(x,y)


from math import sqrt
def sq_root(num):
  print ("sq_root of the given number ",num," is ",sqrt(num))

num = int(input("Enter a number whose sqr root you want to find :"))  
sq_root(num) 


def makeSubStrings(main_str,delimiter):
  list_of_substr=main_str.split(delimiter,main_str.count(delimiter))
  print ("list_of_substr delimited by",delimiter,"is ",list_of_substr)
  
makeSubStrings("Pack: My: Box: With: Good: Food",':')

-------------------------------------------------------------------------------------------------

fileObj=open("file.txt","r")
content=fileObj.read()
print (content)
fileObj.close()


fileObj=open("newfile.txt","w")
fileObj.write("this is the first line\n")
fileObj.write("this is the second line\n")
fileObj.write("this is the third line\n")
fileObj.write("this is the fourth line\n")
fileObj.write("this is the fifth line\n")
fileObj.open

fileObj=open("newfile.txt","a")
fileObj.write("appending line1\n")
fileObj.write("appending line2\n")
fileObj.write("appending line3\n")
fileObj.write("appending line4\n")
fileObj.write("appending line5\n")
fileObj.close

-------------------------------------------------------------------------------------------------------

 
fileObj=open("file.txt","r")
content=fileObj.read(10)
i=10
while content!="":
	print ("current postion after reading ",i,"bytes is ",fileObj.tell())
	i+=10
	content=fileObj.read(10)
fileObj.close()
print ("\n\n\n")



fileObj=open("file.txt","r")
content=fileObj.read(100)
print ("current postion after reading 100 bytes is ",fileObj.tell())
fileObj.seek(0,0)
print ("current postion after resetting filepointer ",fileObj.tell())
fileObj.close()
print ("\n\n\n")



fileObj=open("file.txt","r")
content=fileObj.readlines()
fileObj.close()

i=1
for line in content:
	if i > 4:
		print (line)
	i+=1
print ("\n\n\n")

---------------------------------------------------------------------------------------------------

def countOfTreasureFiles(list_of_files):
	pattern="Treasure"
	count=0
	for f in list_of_files:
		fo=open(f,"r")
		content=fo.read()
		fo.close()
		if pattern in content:
			count+=1
	print ("Totllay ",count," number of files have the pattern",pattern)

countOfTreasureFiles(['file1.txt','file2.txt','file3.txt','file4.txt'])

print ("\n"*3)


def countOfTreasureInEachFile(list_of_files):
	pattern="Treasure"
	count=0
	for f in list_of_files:
		fo=open(f,"r")
		content=fo.read()
		fo.close()
		if pattern in content:
			numOfOccurences=content.count(pattern)
			print (f,"has ",numOfOccurences," times of ",pattern," in it")
		else:
			print (f,"has no",pattern) 
		

countOfTreasureInEachFile(['file1.txt','file2.txt','file3.txt','file4.txt'])
print ("\n"*3)
---------------------------------------------------------------------------------------------------------------------------------


fo=open("file.txt","r")
content=fo.readlines()
fo.close()

print ("actual file content\n--------")
for line in content:
	print (line,)

print ("\n")

print ("reversed(in terms of lines only)file content\n----------")
content.reverse()
for line in content:
	print (line,)

print ("\n\n\n")


fo=open("file.txt","r")
content=fo.read()
fo.close()

print ("actual file content\n------\n",content)
print ("\n"*3)


content=content[::-1]
print ("reversed(in terms of characters) file content\n-------\n",content)

--------------------------------------------------------------------------------------------

fname='mynewfile.txt'
fo=open(fname,"rw+")
print ("opened a file",fname," with mode ",fo.mode)


if fo.isatty():
	print ("file with decriptor ",fo.fileno,"is connected to tty device")
else:
	print ("file with decriptor ",fo.fileno,"is not connected to tty device")



print ("writing a string with write method")
fo.write("a sample string\n") 


print ("flushed the prveioulsy written string using flush()")
fo.flush()


print ("reading previously flushed (first) line without closing/reopening the file")
print ("and that line is",fo.read())



print ("now writing a list of lines using writelines()")
listOfLines=["Hi TopGear,I'm line 2\n",
				"Hi TopGear,I'm line 3\n",
				"Hi TopGear,I'm line 4\n",
				"Hi TopGear,I'm line 5\n",
				"Hi TopGear,I'm line 6\n",
				"Hi TopGear,I'm line 7\n",
			]

fo.writelines(listOfLines)

fo.flush()

fo.seek(0,0) #reset the file pointer
print ("after writing all the lines , now the file pointer is reset for reading pupose and tecnically the file pointer is at",fo.tell(),"position")


content=fo.read(10)
print ("first 10 bytes of ",fname,"is ",content)


fo.seek(10,2) #move to 10th position from the left side of the EOF
content=fo.read()
print ("last 10 bytes of ",fname,"is ",content)


fo.seek(0,0) #reset the file pointer


firstline=fo.readline()
print ("first line from the file using readline()",fname,"is ",firstline)

nextLine=fo.next()
print ("next line to above line from the file(used nextline())",fname,"is ",nextLine)

fo.seek(0,0) #reset the file pointer
listOfAllLines=fo.readlines()
print ("all lines from the file ",fname,"in list format\n",listOfAllLines)


print ("enough of file operations,so truncate this file to release your frustration using truncate()")
fo.truncate(0)

print ("now close the file using close() , take rest ,bye ")
fo.close()

----------------------------------------------------------------------------------------------------------------------------



import time
try:
	print (a)
except NameError:
	print ("NameError handled here\n\n")
else:
	print ("Everything looks fine")


 
try:
	print ("trying to print 1/0 wihich will cause AritmeticError")
	print (1/0)
except ArithmeticError:
	print ("Arithmetic Error is  handled here\n\n")
else:
	print ("Everything looks fine")



try:
	print ("press ctrl+c within 10 sec to see how KeyboardInterrurpt is handled")
	for i in range(10):
		time.sleep(1)
		print (i)
except KeyboardInterrupt:
	print ("\n\nKeyboardInterrurpt is handled here\n\nmagic programs runs even after u try to interupt by ctrl+c\n\nnice try\nbye\n")
else:
	print ("bad.. so bad...you dint interuupt the program")	
	
--------------------------------------------------------------------------------------------------------------------------------------------



def poundToKilo(weightInPounds):
	print 
    assert (weightInPounds > 0),"weight cannot be -ve\n"
	weightInKilo=weightInPounds/2.2
	assert (weightInKilo < 100),"\n\nwe can't carry more than 100 KG,so try reducing the pounds accordingly,Thanks \n"
	print (weightInPounds," pounds = ",weightInKilo," Kilo")
	return


print ("trying to convert 50 pounds in kilo")
print ("Result:\n",poundToKilo(50))


print ("trying to convert 250 pounds in kilo")
print ("Result:\n",poundToKilo(250))

------------------------------------------------------------------------------------------------------------

try:
	fo=open("file.txt","r")
	fo.write("onkar")
except IOError:
	print ("IOError handled here,you cant write a file with read only mode\n\n")
else:
	print ("Everything looks fine")



try:
	print ("trying to convert value for 'x' which is invalid and cause ValueError\n")
	int('x')
except ValueError:
	print ("the value passed is not of numerric type",)

------------------------------------------------------------------------------------------------------------

from math import sqrt

def add(a1,a2):
	a3=a1+a2
	print (a1," + ",a2," = ",a3)

def sub(a1,a2):
	a3=a1-a2
	print (a1," - ",a2," = ",a3)

def mul(a1,a2):
	a3=a1*a2
	print (a1," * ",a2," = ",a3)

def div(a1,a2):
	a3=a1/a2
	print (a1," / ",a2," = ",a3)

def sq_root(a1):
	sroot=sqrt(a1)
	print ("square root of ",a1," = ",sroot)


def floor_div(a1,a2):
	a3=a1//a2
	print (a1,"//",a2," = ",a3)

def modulus(a1,a2):
	a3=a1%a2
	print (a1,"%",a2," = ",a3)


def isPrime(number):
	prime=True
	for i in range(2,number+1):
		if number%i == 0:
			prime=False
			break
	if prime:
		print (number,"is prime")
	else:
		print (number," is not prime")

def fibonocci(N):
	p2num=0
	p1num=1
	print ("generated fibonocci series for the length of",N,"elements")
	print (p2num,p1num,)
	for i in range(N-2):
	  cnum=p1num+p2num
	  print (cnum,)
	  p2num=p1num
	p1num=cnum




from cal import *

add(1,2)
print ("\n\n")
sub(2,1)
print ("\n\n")
mul(2,2)
print ("\n\n")
div(2,2)
print ("\n\n")
floor_div(4,2)
print ("\n\n")
fibonocci(13)
print ("\n\n")
sq_root(100)
print ("\n\n")
modulus(5,3)
print ("\n\n")
isPrime(12)
print ("\n\n")

------------------------------------------------------------------------------------------------------



def sort(list_of_numbers):
	 
	swap_set=True
	length=len(list_of_numbers)
	while swap_set:
		swap_set=False
		for i in range(length):
		    if i+1 != length:
		        if list_of_numbers[i] > list_of_numbers[i+1]:
		            temp=list_of_numbers[i]
		            list_of_numbers[i]=list_of_numbers[i+1]
		            list_of_numbers[i+1]=temp
		            swap_set=True
	else:
		print ("sorted list is ",list_of_numbers)


def binarySearch(sorted_list,search_element):
	print ("Assuming user has provided sorted_list")
	low=0
	high=len(sorted_list)-1
	mid=low+(high-low)/2
	se=search_element
	found=False
	iterate=True
	while iterate:
	  if high<low:
		print ("element not found")
        break
	  if se < sorted_list[mid]:
		high=mid-1
		mid=low+(high-low)/2
	  elif se >sorted_list[mid]:
		low=mid+1
		mid=low+(high-low)/2
	  elif sorted_list[mid]==se:
		found=True
		iterate=False
	else:
	  if found:
		print ("element found at index",mid)


def rev_str(string):
	print ("reverse of the given string",string," is ",string[::-1])


from stringop import *

sort([2,5,1,3,6,8,7,9])



binarySearch([1,2,3,4,5,6,7],8)



rev_str("dinesh")



