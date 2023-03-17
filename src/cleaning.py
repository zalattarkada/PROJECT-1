import pandas as pd
import re
def rename_columns (df):
    '''quitamos los espacios que pueda haber en los nombres de las columnas (en especial el de 'Sex ') y los ponemos en mayuscula'''
    space = {i: i.rstrip() for i in df.columns}
    df = df.rename(columns=space)
    df.columns
    return df.rename(columns=lambda x: x.lower())


def cohesive_activities(activity_str):
    '''Esta función crea valores más cohesivos cogiendo los gerundios de las actividades ya presentes en la lista '''
    
    activity_str = activity_str.lower()
    activities = {
        'swim': 'Swimming',
        'surf': 'Surfing',
        'bath': 'Swimming',
        'div': 'Diving',
        'snork': 'Snorkeling',
        'padd': 'Paddle boarding',
        'play': 'Swimming',
        'wad': 'Wading',
        'body': 'Body boarding',
        'stand': 'Standing',
        'kite': 'Kiteboarding',
        'boog': 'Boogie boarding',
        'kayak': 'Kayaking',
        'spear': 'Spearfishing',
        "Fishing": 'Fishing',
        'net': 'Fishing'
    }
    for keyword, activity in activities.items():
        if re.search(keyword, activity_str):
            return activity
    return activity_str.capwords(activity_str)

#df['activity'] = df['activity'].apply(cohesive_activities)


def time_day(time_str):
    '''Esta función elimina todos los valores que no siguen el formato horario de 00h00 y transforma las horas en franjas horarias'''
    if ':' in time_str:
        hour = int(time_str.split(':')[0])
        if 'PM' in time_str.upper() and hour != 12:
            hour += 12
    else:
        hour = int(time_str.split('h')[0])

    if hour >= 5 and hour < 12:
        return 'Morning'
    elif hour >= 12 and hour < 17:
        return 'Afternoon'
    elif hour >= 17 and hour < 21:
        return 'Evening'
    else:
        return 'Night'

# creamos una nueva columna con las franjas horarias 
#df['time of the day'] = df['time'].apply(time_day)

# eliminamos la columna de time
##df.drop(['time'], axis=1, inplace= True)

def clean_hours(time_str):
    regex = re.compile(r'^\d{1,2}h\d{2}$')
    df = df[df['time'].str.match(regex)]
