from errno import EMLINK
import math


cost_of_house = 800000
house_downpayement = 0.25 * cost_of_house
house_loan_duration = 6 * 12
house_interest = 0.07 / 12

cost_of_car = 60000
car_loan_duration = 1 * 12
car_interest = 0.12 / 12

amount = 100000
duration = 10 * 12
interest = 0.09 / 12


def emi_calculator(principal, duration, interest, downpayement=0):
    loan_amount = principal - downpayement
    try:
        emi = (
            loan_amount
            * interest
            * ((1 + interest) ** duration)
            / ((1 + interest) ** duration - 1)
        )
    except ZeroDivisionError:
        emi = loan_amount / duration

    return math.ceil(emi)


house_emi = emi_calculator(
    cost_of_house, house_loan_duration, house_interest, house_downpayement
)
car_emi = emi_calculator(cost_of_car, car_loan_duration, car_interest)

total_emi = house_emi + car_emi
print(
    f"Shaun has to pay {total_emi} every month with {house_emi} for house and {car_emi} for car"
)

total_interest = (
    emi_calculator(amount, duration, interest) * duration
    - emi_calculator(amount, duration, 0) * duration
)

print(total_interest)
