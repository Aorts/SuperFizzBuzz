class callClassFunction():
    def callfizzbuzz(self):
        fizzbuzzfunction = [
            FizzFizzBuzzBuzz(),  
            FizzBuzz(), 
            FizzFizz(),
            BuzzBuzz(), 
            Fizz(), 
            Buzz(), 
            NoFizzBuzz(), 
        ]
        return fizzfizzbuzzbuzz(fizzbuzzfunction)

class fizzfizzbuzzbuzz():
    def __init__(self,fizzbuzzfunction):
        self.fizzbuzzfunction = fizzbuzzfunction
    def result(self,n):
        for keepNum in self.fizzbuzzfunction:
            if keepNum.result(n):
                return keepNum.result(n)

class keepNum():
    def result(self,n):
        pass

class FizzBuzz(keepNum):
    def result(self,n):
        if n % 3 == 0 and n % 5 == 0 :
            #print("FizzBuzz")
            return "FizzBuzz"

class Fizz(keepNum):
    def result(self,n):
        if n % 3 == 0 :
            #print("Fizz")
            return "Fizz"

class Buzz(keepNum):
   def result(self,n):
        if n % 5 == 0 :
            #print("Buzz")
            return "Buzz"
class FizzFizz(keepNum):
    def result(self,n):
        if n % 9 == 0 :
            #print("FizzFizz")
            return "FizzFizz"

class BuzzBuzz(keepNum):
    def result(self,n):
        if n % 25 == 0 :
            #print("BuzzBuzz")
            return "BuzzBuzz"

class FizzFizzBuzzBuzz(keepNum):
    def result(self,n):
        if n % 9 == 0 and n % 25 == 0 :
            #print("FizzFizzBuzzBuzz")
            return "FizzFizzBuzzBuzz"

class NoFizzBuzz(keepNum):
    def  result(self,n):
        if n % 3 != 0 and n % 5 != 0 and n % 9 != 0 and n % 25 != 0:
            #print("NoFizzBuzz")

            return "NoFizzBuzz"



n = int(input("Input number : "))
if n in range(10000):
    result = callClassFunction().callfizzbuzz()
    print(result.result(n))
else:
    print("More than 10000")
