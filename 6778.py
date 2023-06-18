# 6778

number_of_antenna = int(input())
number_of_eyes = int(input())


if number_of_antenna >= 3 and number_of_eyes <= 4:
    print('TroyMartian')

if number_of_antenna <= 6 and number_of_eyes >= 2:
    print('VladSaturnian')

if number_of_antenna <=2 and number_of_eyes <= 3:
    print('GraemeMercurian')


