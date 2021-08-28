import unittest
from test_fizzbuzz import callClassFunction

class TestSuperFizzBuzz(unittest.TestCase):
    #FizzBuzz
    def test_give_15_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(15),"FizzBuzz", "FizzBuzz")

    def test_give_30_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(30),"FizzBuzz", "FizzBuzz")

    def test_give_45_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(45),"FizzBuzz", "FizzBuzz")

    def test_give_60_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(60),"FizzBuzz", "FizzBuzz")

    def test_give_75_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(75),"FizzBuzz", "FizzBuzz")

    def test_give_90_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(90),"FizzBuzz", "FizzBuzz")

    def test_give_105_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(105),"FizzBuzz", "FizzBuzz")

    def test_give_120_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(120),"FizzBuzz", "FizzBuzz")

    def test_give_135_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(135),"FizzBuzz", "FizzBuzz")

    def test_give_150_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(150),"FizzBuzz", "FizzBuzz")
    
    def test_give_9990_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9990),"FizzBuzz", "FizzBuzz")

    def test_give_7770_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(7770),"FizzBuzz", "FizzBuzz")

    def test_give_6660_Should_be_FizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(6660),"FizzBuzz", "FizzBuzz")

    #FizzFizzBuzzBuzz
    def test_give_225_Should_be_FizzFizzBuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(225),"FizzFizzBuzzBuzz", "FizzFizzBuzzBuzz")

    def test_give_450_Should_be_FizzFizzBuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(450),"FizzFizzBuzzBuzz", "FizzFizzBuzzBuzz")

    def test_give_2025_Should_be_FizzFizzBuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(2025),"FizzFizzBuzzBuzz", "FizzFizzBuzzBuzz")

    def test_give_2250_Should_be_FizzFizzBuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(2250),"FizzFizzBuzzBuzz", "FizzFizzBuzzBuzz")

    def test_give_5625_Should_be_FizzFizzBuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(5625),"FizzFizzBuzzBuzz", "FizzFizzBuzzBuzz")

    #FizzFizz
    def test_give_9_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9),"FizzFizz", "FizzFizz")

    def test_give_18_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(18),"FizzFizz", "FizzFizz")

    def test_give_27_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(27),"FizzFizz", "FizzFizz")

    def test_give_36_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(36),"FizzFizz", "FizzFizz")

    def test_give_54_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(54),"FizzFizz", "FizzFizz")

    def test_give_63_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(63),"FizzFizz", "FizzFizz")

    def test_give_72_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(72),"FizzFizz", "FizzFizz")

    def test_give_81_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(81),"FizzFizz", "FizzFizz")

    def test_give_99_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(99),"FizzFizz", "FizzFizz")
    
    def test_give_999_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(999),"FizzFizz", "FizzFizz")
   
    def test_give_9999_Should_be_FizzFizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9999),"FizzFizz", "FizzFizz")

    # #BuzzBuzz
    def test_give_25_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(25),"BuzzBuzz", "BuzzBuzz")

    def test_give_100_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(100),"BuzzBuzz", "BuzzBuzz")

    def test_give_125_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(125),"BuzzBuzz", "BuzzBuzz")

    def test_give_175_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(175),"BuzzBuzz", "BuzzBuzz")

    def test_give_200_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(200),"BuzzBuzz", "BuzzBuzz")

    def test_give_250_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(250),"BuzzBuzz", "BuzzBuzz")

    def test_give_275_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(275),"BuzzBuzz", "BuzzBuzz")

    def test_give_325_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(325),"BuzzBuzz", "BuzzBuzz")

    def test_give_350_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(350),"BuzzBuzz", "BuzzBuzz")
    

    def test_give_4450_Should_be_BuzzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(4450),"BuzzBuzz", "BuzzBuzz")

    #FIZZ
    def test_give_3_Should_be_Fizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(3),"Fizz", "Fizz")

    def test_give_6_Should_be_Fizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(6),"Fizz", "Fizz")
        
    def test_give_12_Should_be_Fizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(12),"Fizz", "Fizz")

    def test_give_9996_Should_be_Fizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9996),"Fizz", "Fizz")

    def test_give_9993_Should_be_Fizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9993),"Fizz", "Fizz")
    
    def test_give_123_Should_be_Fizz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(123),"Fizz", "Fizz")
    

    #BUZZ
    def test_give_5_Should_be_BUZZ(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(5),"Buzz", "Buzz")
    
    def test_give_10_Should_be_BUZZ(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(10),"Buzz", "Buzz")

    def test_give_35_Should_be_BUZZ(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(35),"Buzz", "Buzz")

    def test_give_40_Should_be_BUZZ(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(40),"Buzz", "Buzz")
    
    def test_give_55_Should_be_BUZZ(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(55),"Buzz", "Buzz")

    def test_give_9995_Should_be_BUZZ(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9995),"Buzz", "Buzz")
    
    

    #NoFizzBuzz
    def test_give_1_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(1),"NoFizzBuzz", "NoFizzBuzz")

    def test_give_2_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(2),"NoFizzBuzz", "NoFizzBuzz")

    def test_give_9998_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9998),"NoFizzBuzz", "NoFizzBuzz")

    def test_give_9997_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9997),"NoFizzBuzz", "NoFizzBuzz")

    def test_give_9994_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9994),"NoFizzBuzz", "NoFizzBuzz")
    
    def test_give_9932_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(9932),"NoFizzBuzz", "NoFizzBuzz")

    def test_give_62_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(62),"NoFizzBuzz", "NoFizzBuzz")

    def test_give_53_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(53),"NoFizzBuzz", "NoFizzBuzz")
    
    def test_give_262_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(262),"NoFizzBuzz", "NoFizzBuzz")
    
    def test_give_331_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(331),"NoFizzBuzz", "NoFizzBuzz")
    
    def test_give_884_Should_be_NoFizzBuzz(self):
        result = callClassFunction().callfizzbuzz()
        self.assertEqual(result.result(884),"NoFizzBuzz", "NoFizzBuzz")
    

if __name__ == '__main__':
    unittest.main()
