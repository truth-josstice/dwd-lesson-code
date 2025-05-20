# map() Exercises
#
# Exercise 1
# ----------
# You have a list of product prices.
# Use `map` and a lambda to create a new list where each price
# has a 20% tax added to it (price * 1.20).
# Remember to format the output nicely if you can
# (e.g., to two decimal places, but the core is the map).

prices = [10.99, 5.49, 20.00]
tax = 1.2
total_prices = map(lambda price: price * tax, prices)
tp_formatted = ['$' + '%.2f' % elem for elem in total_prices ]

print(f'Total prices: {tp_formatted}')

# Exercise 2
# ----------
# Given a list of scores, use map() to get a list of the grade level for each score.
#
# HD if >=90
# D if >=80
# C if >=70
# P if >=50
# F if <50

scores = [85, 92, 78, 60, 42, 95, 70, 53]

def score_to_grade(score):
    if score in range(0, 100):
        if score >= 90:
            return 'HD'
        elif score >=80:
            return 'D'
        elif score >= 70:
            return 'C'
        elif score >= 50:
            return 'P'
        else:
            return 'F'
    else:
        return 'Invalid score value'
    
grades = map(score_to_grade, scores)

print(scores)
print(f'{list(grades)}')