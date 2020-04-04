from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from .forms import CarForm
import requests
# Create your views here.

#BASE_URL = "https://www.olx.pl/motoryzacja/samochody/"
#FILTER_URL = "?search%5Bfilter_float_price%3Afrom%5D={}&search%5Bfilter_float_price%3Ato%5D={}&search%5Bfilter_enum_petrol%5D%5B0%5D={}&search%5Bfilter_enum_transmission%5D%5B0%5D={}"
#BRAND = "volkswagen"
#MODEL = "tiguan"
#MODEL_URL = "{}/{}/".format(BRAND,MODEL)
#PRICE_FROM = 45000 
#PRICE_TO =  65000
#PETROL = "diesel"
#SHIFT = "manual"



def getDataOLX(name,model,year_from,year_to,petrol):
    BASE_URL = "https://www.olx.pl/motoryzacja/samochody/"
    FILTER_URL = "?search%5Bfilter_float_price%3Afrom%5D={}&search%5Bfilter_float_price%3Ato%5D={}&search%5Bfilter_enum_petrol%5D%5B0%5D={}&search%5Bfilter_enum_transmission%5D%5B0%5D={}"
    BRAND = name
    MODEL = model
    MODEL_URL = "{}/{}/".format(name,model)
    PRICE_FROM = 45000 
    PRICE_TO =  65000
    PETROL = petrol
    SHIFT = "manual"

    URL = BASE_URL + MODEL_URL + FILTER_URL.format(PRICE_FROM,PRICE_TO,PETROL,SHIFT)
    FINAL_URL = URL.lower()

    response = requests.get(FINAL_URL)
    data_cars = response.text
    soup = BeautifulSoup(data_cars, features='html.parser')
    cars_listings = soup.find_all('td',{'class':'offer'})

    car_list = []

    for cars in cars_listings:
        if cars.find('img', {'class':'fleft'}) is None:
            print("www.olx.pl")
        else:
            #print(cars.find('img', {'class':'fleft'}).get('alt'))
            car_name = cars.find('img', {'class':'fleft'}).get('alt')

        if cars.find('img',{'class':'fleft'}) is None:
            print("www.olx.pl")
        else:
            #print(cars.find('img',{'class':'fleft'}).get('src'))
            car_img = cars.find('img',{'class':'fleft'}).get('src')

        if cars.find(class_='space inlblk rel') is None:
            print("www.olx.pl")
        else:
            #print(cars.find(class_='space inlblk rel').find(class_='price').text)
            car_price = cars.find(class_='space inlblk rel').find(class_='price').text

        if cars.find('td') is None:
            car_url = "www.olx.pl"
        elif cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}) is None : 
            car_url = "www.olx.pl"
        else :
            #print(cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href'))
            car_url = cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href')
            #print(cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href'))
        car_list.append((car_name,car_price,car_url, car_img))
        #print(car_list)
    return car_list
    


def home(request):

    
    return render(request, 'scrapping/base.html')


def search(request):
    BASE_URL = "https://www.olx.pl/motoryzacja/samochody/"
    FILTER_URL = "?search%5Bfilter_float_price%3Afrom%5D={}&search%5Bfilter_float_price%3Ato%5D={}&search%5Bfilter_enum_petrol%5D%5B0%5D={}&search%5Bfilter_enum_transmission%5D%5B0%5D={}"
    BRAND = 'Seat'
    MODEL = 'Leon'
    MODEL_URL = "{}/{}/".format(BRAND,MODEL)
    PRICE_FROM = 0 
    PRICE_TO =  150000
    PETROL = 'diesel'
    SHIFT = "manual"

    URL = BASE_URL + MODEL_URL + FILTER_URL.format(PRICE_FROM,PRICE_TO,PETROL,SHIFT)
    FINAL_URL = URL.lower()

    response = requests.get(FINAL_URL)
    data_cars = response.text
    soup = BeautifulSoup(data_cars, features='html.parser')
    cars_listings = soup.find_all('td',{'class':'offer'})

    car_list = []

    for cars in cars_listings:
        if cars.find('img', {'class':'fleft'}) is None:
            print("www.olx.pl")
        else:
            #print(cars.find('img', {'class':'fleft'}).get('alt'))
            car_name = cars.find('img', {'class':'fleft'}).get('alt')

        if cars.find('img',{'class':'fleft'}) is None:
            print("www.olx.pl")
        else:
            print(cars.find('img',{'class':'fleft'}).get('src'))
            #car_img = cars.find('img',{'class':'fleft'}).get('src')
            #car_img = "C:/Users/HP/Downloads/tire.png"

        if cars.find(class_='space inlblk rel') is None:
            print("www.olx.pl")
        else:
            #print(cars.find(class_='space inlblk rel').find(class_='price').text)
            car_price = cars.find(class_='space inlblk rel').find(class_='price').text

        if cars.find('td') is None:
            car_url = "www.olx.pl"
        elif cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}) is None : 
            car_url = "www.olx.pl"
        else :
            #print(cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href'))
            car_url = cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href')
            #print(cars.find('td').find('a',{'class':'thumb vtop inlblk rel tdnone linkWithHash scale4 detailsLink'}).get('href'))
        car_list.append((car_name,car_price,car_url))
        
    #print(car_list)
    return render(request, 'scrapping/search.html', {'car_list': car_list})