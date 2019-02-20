#re is the package for regular expression
import re
sentence="Hllo everyone!i m regular epression 123"

#\d is for knowing any integer /number in the sentence
x=re.findall('\d',sentence)
print(x)

#[a-z] is for matching the set of charaters for the given range
y=re.findall('[a-z][A-Z]*',sentence)
print(y)

str="hello"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
z=re.findall('he..o' ,str)
print(z)

#for matching start of the sentence
start=re.findall("^Hllo",sentence)
print(start)

#for checking for 0 or more occurence
occur=re.findall("e*",sentence)
print(occur)

#for checking for 1 or more occurence
occur1=re.findall("e+",sentence)
print(occur1)

#Check if the string contains "a" followed by exactly two "l" characters:
str1="hello all alla all"
str11=re.findall('al{2}',str1)
print(str11)

#Check if the string contains either "falls" or "stays":
hey="hey either falls or stays"
gg=re.findall("falls|stays",hey)
print(gg)

#Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
findd=re.findall("\Ball",sentence)
print(findd)

#	Returns a match where the string DOES NOT contain digits
finddd=re.findall('/D',sentence)
print(finddd)

import re

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())

import re

str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)

x=re.sub("\s","9",str,2)
print(x)

#regular expression
import re
data="Jassica is friend whoes age is 34 and Bharni is 44"
name=re.findall('[A-Z][a-z]*',data)
age=re.findall('\d{2}',data)
# print(name)
# print(age)
ageDict={}
x=0
for eachname in name:
    ageDict[eachname]=age[x]
    x+=1

print(ageDict)

#iterator
datadata="information is kind of information which is information"
for i in re.finditer("inform",datadata):
    lockup=i.span()
    print(lockup)



#match words
strr="sat mat tat "
ff=re.findall("[smt]at",strr)
print(ff)

