cities = {
    'CO': 'Denver',
    'CA': 'Los Angeles'
}

states = {
    'Colorado': 'CO',
    'California': 'CA'
}

countries = {
    'United States of America': 'USA'
}

countries['Canada'] = 'CA'

print('CO has:', cities['CO'])

print('Colorado is abbreviated as:',states['Colorado'])

print('California has:', cities[states['California']])