import json

from s_appearance_health import aah
from s_character import crt
from s_career import job
from s_relationship import rlt
from s_suitable_works import suw
from s_suitable_partners import sup

def lambda_handler(event, context):
    # TODO implement
    name = event['name']
    date = event['date']
    time = event['time']
    place = event['place']
    
    a = date.split("-")
    day = int(a[2])
    month = int(a[1])
    dateFixed = a[2] + '/' + a[1] + '/' + a[0]
    
    hsign = ['Capricornus', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpius', 'Sagittarius']
    
    zodiac = ''
    appearance = ''
    character = ''
    career = ''
    relationship = ''
    suworks = ''
    supns = ''
    
    if month == 1:
        if day <= 19:
            zodiac = hsign[0]
            appearance = aah[0]
            character = crt[0]
            career = job[0]
            relationship = rlt[0]
            suworks = suw[0]
            supns = sup[0]
        else:
            zodiac = hsign[1]
            appearance = aah[1]
            character = crt[1]
            career = job[1]
            relationship = rlt[1]
            suworks = suw[1]
            supns = sup[1]
            
    elif month == 2:
        if day <= 18:
            zodiac = hsign[1]
            appearance = aah[1]
            character = crt[1]
            career = job[1]
            relationship = rlt[1]
            suworks = suw[1]
            supns = sup[1]
        else:
            zodiac = hsign[2]
            appearance = aah[2]
            character = crt[2]
            career = job[2]
            relationship = rlt[2]
            suworks = suw[2]
            supns = sup[2]
    
    elif month == 3:
        if day <= 20:
            zodiac = hsign[2]
            appearance = aah[2]
            character = crt[2]
            career = job[2]
            relationship = rlt[2]
            suworks = suw[2]
            supns = sup[2]
        else:
            zodiac = hsign[3]
            appearance = aah[3]
            character = crt[3]
            career = job[3]
            relationship = rlt[3]
            suworks = suw[3]
            supns = sup[3]
    
    elif month == 4:
        if day <= 19:
            zodiac = hsign[3]
            appearance = aah[3]
            character = crt[3]
            career = job[3]
            relationship = rlt[3]
            suworks = suw[3]
            supns = sup[3]
        else:
            zodiac = hsign[4]
            appearance = aah[4]
            character = crt[4]
            career = job[4]
            relationship = rlt[4]
            suworks = suw[4]
            supns = sup[4]
    
    elif month == 5:
        if day <= 20:
            zodiac = hsign[4]
            appearance = aah[4]
            character = crt[4]
            career = job[4]
            relationship = rlt[4]
            suworks = suw[4]
            supns = sup[4]
        else:
            zodiac = hsign[5]
            appearance = aah[5]
            character = crt[5]
            career = job[5]
            relationship = rlt[5]
            suworks = suw[5]
            supns = sup[5]
    
    elif month == 6:
        if day <= 21:
            zodiac = hsign[5]
            appearance = aah[5]
            character = crt[5]
            career = job[5]
            relationship = rlt[5]
            suworks = suw[5]
            supns = sup[5]
        else:
            zodiac = hsign[6]
            appearance = aah[6]
            character = crt[6]
            career = job[6]
            relationship = rlt[6]
            suworks = suw[6]
            supns = sup[6]
    
    elif month == 7:
        if day <= 22:
            zodiac = hsign[6]
            appearance = aah[6]
            character = crt[6]
            career = job[6]
            relationship = rlt[6]
            suworks = suw[6]
            supns = sup[6]
        else:
            zodiac = hsign[7]
            appearance = aah[7]
            character = crt[7]
            career = job[7]
            relationship = rlt[7]
            suworks = suw[7]
            supns = sup[7]
    
    elif month == 8:
        if day <= 22:
            zodiac = hsign[7]
            appearance = aah[7]
            character = crt[7]
            career = job[7]
            relationship = rlt[7]
            suworks = suw[7]
            supns = sup[7]
        else:
            zodiac = hsign[8]
            appearance = aah[8]
            character = crt[8]
            career = job[8]
            relationship = rlt[8]
            suworks = suw[8]
            supns = sup[8]
            
    elif month == 9:
        if day <= 22:
            zodiac = hsign[8]
            appearance = aah[8]
            character = crt[8]
            career = job[8]
            relationship = rlt[8]
            suworks = suw[8]
            supns = sup[8]
        else:
            zodiac = hsign[9]
            appearance = aah[9]
            character = crt[9]
            career = job[9]
            relationship = rlt[9]
            suworks = suw[9]
            supns = sup[9]
    
    elif month == 10:
        if day <= 23:
            zodiac = hsign[9]
            appearance = aah[9]
            character = crt[9]
            career = job[9]
            relationship = rlt[9]
            suworks = suw[9]
            supns = sup[9]
        else:
            zodiac = hsign[10]
            appearance = aah[10]
            character = crt[10]
            career = job[10]
            relationship = rlt[10]
            suworks = suw[10]
            supns = sup[10]
    
    elif month == 11:
        if day <= 21:
            zodiac = hsign[10]
            appearance = aah[10]
            character = crt[10]
            career = job[10]
            relationship = rlt[10]
            suworks = suw[10]
            supns = sup[10]
        else:
            zodiac = hsign[11]
            appearance = aah[11]
            character = crt[11]
            career = job[11]
            relationship = rlt[11]
            suworks = suw[11]
            supns = sup[11]
    
    elif month == 12:
        if day <= 21:
            zodiac = hsign[11]
            appearance = aah[11]
            character = crt[11]
            career = job[11]
            relationship = rlt[11]
            suworks = suw[11]
            supns = sup[11]
        else:
            zodiac = hsign[0]
            appearance = aah[0]
            character = crt[0]
            career = job[0]
            relationship = rlt[0]
            suworks = suw[0]
            supns = sup[0]
    
    
    return {
        'statusCode': 200,
        'name': name,
        'date': dateFixed,
        'time': time,
        'place': place,
        'zodiac': zodiac,
        'appearance': appearance,
        'character': character,
        'career': career,
        'relationship': relationship,
        'suworks': suworks,
        'supns': supns
    }
