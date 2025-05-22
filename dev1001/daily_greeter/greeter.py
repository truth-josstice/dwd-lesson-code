import datetime as d
import random as r

today = d.datetime.today().strftime("%Y-%m-%d")
print(f'Today is: {today}')

greetings = ['Good morning starshine, the earth says hello!', 'Gooooooooood morning Vietnam!!!', 'Wakey wakey eggs \'n\' bakey!', 'It\'s always 12pm somewhere!', 'Sometimes a sleep-in is good for the soul!', 'Rise and grind baybay!!!!!!']
print(f'A little message for your morning: {r.choice(greetings)}')