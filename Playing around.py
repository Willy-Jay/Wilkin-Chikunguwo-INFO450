import logging
logging.basicConfig(level=logging.DEBUG)
numbers = list(range(1,6))
logging.debug (numbers)
even_numbers = list(range(2,11,2))
logging.debug (even_numbers)
odd_numbers = list(range(1,11,2))
logging.debug (odd_numbers)
squares = []
for value in range(1,11):
   squares.append( value ** 2)

logging.debug (squares)

squares = [value ** 2 for value in range (1,11)]
logging.debug (squares)

digits = squares
logging.debug (digits)

logging.debug (min(digits))
logging.debug (max(digits))
logging.debug (sum(digits))
