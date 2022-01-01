import phonenumbers
from phonenumbers import geocoder

phone = input('Numero: ')

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_numbers, 'pt'))

