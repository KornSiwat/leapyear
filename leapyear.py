def is_leapyear(year: int)-> bool:
    is_centuryyear_divisible_by_400 = is_centuryyear(year) and year % 400 == 0
    is_divisible_by_4 = year % 4 == 0
    
    return is_centuryyear_divisible_by_400 or is_divisible_by_4

def is_centuryyear(year:int)-> bool:
    is_divisible_by_100 =  year % 100 == 0
    
    return is_divisible_by_100