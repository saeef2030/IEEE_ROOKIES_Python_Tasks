"""
as round() is a built in  function that rounds to the nearest even integer number
(float point number from the decimal value to the closest multiple of 10)
so 6.5 rounded to 6 & 3.5 to 4 & (6-4=2) then (2==3)will give false
"""
print(round(6.5)-round(3.5) == 3)