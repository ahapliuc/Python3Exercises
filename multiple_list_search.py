#import random
#a=random.randint(0,100)
listOfNumbers1=[1,2,6,7]
listOfNumbers2=[1,2,3,4,5]
def list_overlap(listOfNumbers1,listOfNumbers2):
    list_overlap=[]
    for number in listOfNumbers1:
        if number in listOfNumbers1 and number in listOfNumbers2:
            list_overlap.append(number)
            print(list_overlap)
        else:
            print("No numbers are in both lists")

list_overlap(listOfNumbers1,listOfNumbers2)