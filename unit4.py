# Ryan Ge
# Rent a car
# September 27, 2016

def budget(period, mileage):

    """This function calculates the cost for the "budget" classification
       param period: integer, number of days of the rental
       param mileage: integer, the mileage during the rental
       return: float, the total cost of the rental"""

    return 40 * period + 0.25 * mileage

def daily(period, mileage):

    """This function calculates the cost for the "daily" classification
    param period: integer, number of days of the rental
    param mileage: integer, the mileage during the rental
    return: float, the total cost of the rental"""
    # base charge
    cost = 60 * period

    # mileage charge
    if mileage / period > 100:
        cost = cost + 0.25 * (mileage - 100 * period)
    return cost


def weekly(period, mileage):
    """This function calculates the cost for the "weekly" classification
    param period: integer, number of weeks of the rental
    param mileage: integer, the mileage during the rental
    return: float, the total cost of the rental"""
    # base charge
    cost = 190 * period

    # mileage charge
    if mileage / period > 900 and mileage / period <= 1500:
        cost = cost + 100 * period

    if mileage / period > 1500:
        cost = cost + 200 * period + 0.25 * (mileage - period * 1500)
    return cost


def main():

    """This function does the main operation
    return: it returns nothing"""

    # input the data
    code = input("Please input the classification code(B, D, or W):")
    period = int(input('Please input numbers of days for rental:'))
    odo_start = int(input('Please input the odometer reading at the start of the rental period'))
    odo_end = int(input('Please input the odometer reading at the end of the rental period:'))

    # decide the classification
    if code == 'B':
        cost = budget(period, odo_end - odo_start)
    elif code == 'D':
        cost = daily(period, odo_end - odo_start)
    elif code == 'W':
        cost = weekly(int((period + 6) / 7), odo_end - odo_start)

    # print the information and final result
    print('The classification code is ' + code)
    print('Days of rental: %d' % (period, ))
    print('Odometer reading at the start of the rental period: %d' % (odo_start, ))
    print('Odometer reading at the start of the rental period: %d' % (odo_end, ))
    print('Number of miles driven during the rental period: %d' % (odo_end - odo_start, ))
    print('Total bill for the rental: $%.2f' % (cost, ))

main()


    





