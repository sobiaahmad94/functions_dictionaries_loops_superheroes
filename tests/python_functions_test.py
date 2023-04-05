from src.python_functions_practice import *

# import calendar
import unittest


class TestPythonFunctionPractice(unittest.TestCase):

  def test_return_10(self):
      return_10_result = return_10()
      self.assertEqual( 10, return_10_result )

  def test_add(self):
      add_result = add( 1, 2 )
      self.assertEqual( 3, add_result )

  def test_subtract(self):
      subtract_result = subtract( 10, 5 )
      self.assertEqual( 5, subtract_result )

  def test_multiply(self):
      multiply_result = multiply( 4, 2 )
      self.assertEqual( 8, multiply_result )

  def test_divide(self):
      divide_result = divide( 10, 2 )
      self.assertEqual( 5, divide_result )

  def test_length_of_string(self):
      test_string = "A string of length 21"
      string_length = length_of_string( test_string )
      self.assertEqual( 21, string_length )

  def test_join_string(self):
      string_1 = "Mary had a little lamb, "
      string_2 = "its fleece was white as snow"
      joined_string = join_string( string_1, string_2 )
      self.assertEqual( "Mary had a little lamb, its fleece was white as snow", joined_string )

  def test_add_string_as_number(self):
      add_result = add_string_as_number( "1", "2" )
      self.assertEqual( 3, add_result )

# result number_to_full_month_name - create one function
# which gives the result 1 for January, 3 for March
# and 9 for September
  def test_number_to_full_name__month_1(self):
      result = number_to_full_month_name( 1 )
      self.assertEqual( "January", result )

#   @unittest.skip("delete this line to run the test")
  def test_number_to_full_name__month_3(self):
      result = number_to_full_month_name( 3 )
      self.assertEqual( "March", result )

#   @unittest.skip("delete this line to run the test")
  def test_number_to_full_name__month_9(self):
      result = number_to_full_month_name( 9 )
      self.assertEqual( "September", result )

#   @unittest.skip("delete this line to run the test")
  def test_number_to_short_month_name__month_1(self):
      first_month_string = number_to_short_month_name( 1 )
      self.assertEqual( "Jan", first_month_string )

#   @unittest.skip("delete this line to run the test")
  def test_number_to_short_month_name__month_4(self):
      fourth_month_string = number_to_short_month_name( 4 )
      self.assertEqual( "Apr", fourth_month_string )

#   @unittest.skip("delete this line to run the test")
  def test_number_to_short_month_name__month_10(self):
      tenth_month_string = number_to_short_month_name( 10 )
      self.assertEqual( "Oct", tenth_month_string )

  #Further

  #Given the length of a side of a cube calculate the volume
  @unittest.skip("delete this line to run the test")
  def test_volume_of_cube(self):
    #add test code here
    pass

  #Given a String, return the String reversed
  @unittest.skip("delete this line to run the test")
  def test_reverse_string(self):
    #add test code here
    pass

  #Given a value in farenheit, convert this into celsius.
  @unittest.skip("delete this line to run the test")
  def test_fahrenheit_to_celsius(self):
    #add test code here
    pass

# My own examples

# A) Calculating superhero aliases 

#   @unittest.skip("delete this line to run the test")
def test_superhero_aliases(self):
    superhero_alias_name = get_superhero_alias("Spider-Man")
    self.assertEqual( "Spider-Man", superhero_alias_name )

def test_get_superhero_superpowers(self):
    superhero_name = get_superhero_superpowers("Spider-Man")
    self.assertEqual( "Spider-Man", superhero_name)



if __name__ == '__main__':
    unittest.main()
