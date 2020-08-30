import logging
logging.basicConfig(level=logging.DEBUG)
def squared_threes():
 return_value = []
 # YOUR CODE GOES HERE
 return_value = [value**2 for value in range(0,100,3)]
 # END SHOULDNT GO BEYOND HERE
 return return_value
if __name__ == "__main__":
 for x in squared_threes():
      logging.debug(x)
