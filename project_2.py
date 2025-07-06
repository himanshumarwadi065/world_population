import pandas as pd
import matplotlib.pyplot as mt 


find = pd.read_csv("world_population.csv")
df = pd.DataFrame(find)

def country():
    mt.figure(figsize=(10 , 10))


    lab = ["Afghanistan","China","Brazil","Bangladesh","Canada","France","Germany","Iran","Indonesia","India"]
    result = [0.52,17.88,2.7,2.15,0.48,0.81,1.05,1.11,3.45,17.77]
    ex = [0, 0.2,0,0,0,0,0,0,0,0]
    mt.pie(result,labels=lab, explode=ex , autopct="%1.1f%%")
    mt.title("Distribution of World Population Percentage")
    mt.show()


def population_year_find():
    x = [1970,1980,1990,2000,2010,2015,2020,2022]
    y = [557501301,696828385,870452165,1059633675,1240613620,1322866505,1396387127,1417173173]

    mt.plot(x,y,marker="o",label="Population Growth")
    mt.xlabel("Year")
    mt.ylabel("Number of Population")
    mt.title("Distribution of Indian Population in Year Wise")
    mt.legend()
    mt.show()



def growth():
    lab = ["Afghanistan","China","Brazil","Bangladesh","Canada","France","Germany","Iran","Indonesia","India"]
    # result = [1.0257,1,1.0046,1.0108,1.0078,1.0015,0.9995,1.0071,1.0064,1.0068]
    result = df["Growth Rate"].head(10)
    mt.pie(result , labels=lab , autopct="%1.1f%%")
    mt.title("Population Growth in Top 10 Country's")
    mt.show()


def rank():
    x = df["Country/Territory"].head(10)
    y = df["Rank"].head(10)
    
    mt.figure(figsize=(10,10))
    mt.bar(x,y)
    mt.xlabel("Country/Territory")
    mt.ylabel("Rank of Country")
    mt.title("Distribution of Rank of Country in Population")
    mt.show()

while True:
    choice = input("Enter a Choice :\n1 = World Population Percentage\n2 = Indian Population in Year Wise\n3 = Population Growth in Top 10 Country's\n4 = Rank of Country in Population\n").strip()
    if(choice == '0'):
        print("Good Bye!")
        break
    choices = list(set(choice.split()))
    for choice in choices:
        if(choice == '1'):
            country()
        elif(choice == '2'):
            population_year_find()
        elif(choice == '3'):
            growth()
        elif(choice == '4'):
            rank()

        else:
            print()
            print("----------------------------------------------")
            print("Please enter a valid Choice")
            print("Exit a program to press a ' 0 ' ")
            print("----------------------------------------------")


