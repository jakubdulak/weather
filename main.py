import pyttsx3  #Importuje bibliotekę text to speech
import requests #Importuje bibliotekę requests

#Zbiera podstawowe dane o użytkowniku
user = input("Przedstaw się: ")
city = input("Wprowadź nazwę miasta: ")

#Połączenie z API Open Weather Map
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d58bdf12ce646a164f95527270b52127&units=metric"

#Z wykorzystaniem biblioteki requests imoprtuje dane z API
dane = requests.get(url)

#Zdefiniowanie formatu w jakim mają być prezentowane dane
pogoda = dane.json()

#Wyodrębnienie z pobranych danych informacji o temperaturze z zaokrągleniem do jednego miejsca po przecinku
temp = round(pogoda["main"]["temp"],1)

#Zainicjalizowanie oraz ustawienie syntezatora TTS
engine = pyttsx3.init()
engine.setProperty('rate', 200)

#Określenie informacji jakie ma wypowiedzieć syntezator
engine.say("Cześć"+user+"aktualnie temperatura w mieście"+city+"to"+str(temp)+"°C")
if str(temp) < '5': #zdefiniowanie odpowiedzi w zależności od pobranych danych
    engine.say("Ubierz się ciepło !"+user)
else:
    engine.say("Nie jest aż tak zimno")
engine.runAndWait() #Wywołanie syntezatora