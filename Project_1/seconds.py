
import phonenumbers
from phonenumbers import geocoder, carrier

# Парсинг номера телефону
x = phonenumbers.parse('+380 97 207 9224')

# Отримання назви оператора
Carrier = carrier.name_for_number(x, 'en')

# Отримання опису регіону
Region = geocoder.description_for_number(x, 'en')

# Спроба отримати назву міста
citi = geocoder.description_for_number(x, "en")

print("Carrier:", Carrier)
print("Region:", Region)
print("City:", citi if citi else "Місто не визначено")