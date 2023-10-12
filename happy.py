import unittest 
  
class TestStringMethods(unittest.TestCase): 
    def test_negative_or_positive(self): 
        wordValue = "Sad"
        outputValue = "Happy"
   
        self.assertEqual(wordValue, outputValue) 
  
if __name__ == '__main__': 
    unittest.main()