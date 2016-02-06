# Trick

* Write x a number with 7 digits x = abcdef.
* The biggest sum of digits we can get is pow(9, 5) * 7 = 413,343 that has only 6 digits
* Therefore the numbers x that verify x = sum( pow(x, 5) for x in digits(x) ) has a maximum of 6 digits and is less or
equal to pow(9, 5) * 6 = 354,294
* Hence, we need only to look for numbers between 2 (convention) and 999,999 (= 1,000,000 - 1)