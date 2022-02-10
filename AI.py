import numbers
from tokenize import Number
from numpy import append
import random

def findqs(list1, list2): #gives similarity between two lists
    for x in list1:
        for y in list2:
            if x == y:
                if list1!=list2:
                    return list2
def returnsims(list1, list2): #gives similarity between two lists and returens them
    simi=[]
    for x in list1:
        for y in list2:
            if x == y:
                simi.append(x)
    return simi

def inatlystruggling(dic,list): #gives the number of the question based off its answers
    for x in dic:
        if dic[x]==list:
            return x

def numberofstuff():
    global numbers
    numbers=[]
    for i in range (0,len(answersbank)): #literallynummberofstuff
        if i in answers:
            numbers.append(i)
    return numbers
def getoutdaway(list1,list2): #removes when answers not wanted
    zztop=returnsims(list1,list2)
    for i in zztop:
        list1.remove(i)
    return list1

Questionbanck=["Do you know this person personnaly?","Is this person male","Is this person in ISSH"] #questions
Qs={}
for i in range(0,len(Questionbanck)): 
    Qs[i]=Questionbanck[i]#questionsyettoaskdamniforgotyoucoulddospaces in coments

answersbank={ #answersbabk
    0:["Lisa",'step sis',"Louis"],
    1:["donald trump","Louis"],
    2:["Lisa","Louis"]
}
answers=answersbank.copy()
possibleanswers=[]


print ("Think of a person")
while len(possibleanswers)!=1:
    numberofstuff()
    chosen=random.choice(numbers)
    print(Qs[chosen])
    del Qs[chosen]
    x=input()
    if x=="y":
        possibleanswers.extend(answers[chosen])
        del answers[chosen]
        while len(possibleanswers)!=1:
            for i in answers:
                No=inatlystruggling(answers,(findqs(possibleanswers,answers[i]))) #element in Q2 belong to any other questions reture those questions:
                if No!=None:
                    x=input(Qs[No])
                    del Qs[No]
                    break
            if x=="y":
                possibleanswers=returnsims(possibleanswers,answers[No])
                del answers[No]
            else:
                possibleanswers=getoutdaway(possibleanswers,answers[No])
                del answers[No]

        else: 
            print(possibleanswers)
        
        x1=input("Is it right?")
        if x1=="y":
            print("great")
            break
        else:
            x2=input("What is it?")
            answers[0].append(x2)
            y1=input("Write a question that applies to your person")
            Qs.append(y1)#needs revition
            print(answers[1])
            print(Qs)
    else:
        caretaker=[]
        caretaker.extend(answers[chosen])
        for i in answers:
            answers[i]=getoutdaway(answers[i],caretaker)
        del answers[chosen]
else: 
    print(possibleanswers)
