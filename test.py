# userResult = 'Xin chao {}, sinh o {}'.format(event['name'], event['place'])

d1 = '2023-12-22'

a = d1.split("-")
day = int(a[2])
month = int(a[1])

hsign = ['Capricornus', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpius', 'Sagittarius']

zodiac = ''

if month == 1:
    if day <= 19:
        zodiac = hsign[0]
    else:
        zodiac = hsign[1]
        
elif month == 2:
    if day <= 18:
        zodiac = hsign[1]
    else:
        zodiac = hsign[2]

elif month == 3:
    if day <= 20:
        zodiac = hsign[2]
    else:
        zodiac = hsign[3]

elif month == 4:
    if day <= 19:
        zodiac = hsign[3]
    else:
        zodiac = hsign[4]

elif month == 5:
    if day <= 20:
        zodiac = hsign[4]
    else:
        zodiac = hsign[5]

elif month == 6:
    if day <= 21:
        zodiac = hsign[5]
    else:
        zodiac = hsign[6]

elif month == 7:
    if day <= 22:
        zodiac = hsign[6]
    else:
        zodiac = hsign[7]

elif month == 8:
    if day <= 22:
        zodiac = hsign[7]
    else:
        zodiac = hsign[8]
        
elif month == 9:
    if day <= 22:
        zodiac = hsign[8]
    else:
        zodiac = hsign[9]

elif month == 10:
    if day <= 23:
        zodiac = hsign[9]
    else:
        zodiac = hsign[10]

elif month == 11:
    if day <= 21:
        zodiac = hsign[10]
    else:
        zodiac = hsign[11]

elif month == 12:
    if day <= 21:
        zodiac = hsign[11]
    else:
        zodiac = hsign[0]

print(zodiac)