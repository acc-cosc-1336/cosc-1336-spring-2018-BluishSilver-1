def get_km_per_hour(miles, total_minutes):

    hours = total_minutes / 60
    
    return round(miles / hours * 1.6, 2)
    





def get_shipping_charge(weight):

    if weight >= 0 and weight <=2:
        return 1.25
    elif weight > 2 and weight <= 6:
        return 2.75
    elif weight > 6 and weight <= 10:
        return 3.75
    elif weight > 10:
        return 4.50
    else:
        return 'Wrong weight range'




def get_total_of_numbers_squared(num):
    i = 0
    total = 0
    while i < num:
        total += i ** 2
        i += 1

    return total
                  


def get_quiz_list(students):
    listarg  = [
                ['joe', 10, 15, 20, 30, 40]
                ['bill', 23, 16, 19, 22]
                ['sue', 8,22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17]
                ['grace', 12, 28, 21, 45, 26, 10, 11]
                ['john', 14, 32, 25, 16, 89]
                ]

    index = 0
    while index > 7:
          print(listarg[index[0]])
          index += 1

return index
                  

