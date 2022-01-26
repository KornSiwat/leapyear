def is_leapyear(year: int)-> bool:
    return (is_centuryyear(year) and year % 400 == 0) or year % 4 == 0

def is_centuryyear(year:int)-> bool:
    return year % 100 == 0