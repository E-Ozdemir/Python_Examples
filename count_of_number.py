def equal(a, b, c) :
    numbers = [a, b, c]
    result = numbers.count(max(numbers, key = numbers.count))
    if result > 1 : # bire esit demek tüm rakamlarin birbirinden büyük olmasi demek, o yüzden kosul > 1 seklinde yazildi.
        return result
    else :
        return 0

# same example with arbitrary numbers
def equal (*a) : # arbitrary numbers
    numbers = list(a)
    result = numbers.count(max(numbers, key = numbers.count)) # kac tekrarin oldugunu tespit ediyoruz
    if result > 1 :
        return result
    else :
        return 0    
 
equal(1,2,2,5,5,5,5)
