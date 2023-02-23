# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "bangalore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#     1. Write a program that asks user to enter a city name, and it should tell which country the city belongs to
#     2. Write a program that asks user to enter two cities, and it tells you if they both are in same country or not.
#         For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and
#         dhaka it should print "They don't belong to same country"
india = ['mumbai', 'bangalore', 'chennai', 'delhi']
pakistan = ['lahore', 'karachi', 'islamabad']
bangladesh = ['dhaka', 'khulna', 'islamabad']
city = input('Enter your city: ')
if city in india:
    print("The city is belongs to India")
elif city in pakistan:
    print('The city belongs to Pakistan')
else:
    print('The city belongs to Bangladesh')
#
city1 = input('Please enter the 1st city: ')
city2 = input('Please enter the 2nd city: ')
if city1 in india and city2 in india:
    print('They belongs to same country.')
elif city1 in pakistan and city2 in pakistan:
    print('They belongs to same country.')
elif city1 in bangladesh and city2 in bangladesh:
    print('They belongs to same country.')
else:
    print("They do not belongs to same country.")
    