import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv
from datetime import date
from selenium.webdriver.common.by import By

def hotel_scraping(city,start_date,end_date):
    city = "Bangalore"
    start_date = "31-01-2024"
    end_date = "01-02-2024"

    csv_file = open(f"{city}_hotels_{start_date}_{end_date}.csv",'w',newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([city,"date of checking: "+str(date.today())])
    csv_writer.writerow(["",""])
    csv_writer.writerow(['name','price'])

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
    hotel_url = f"https://www.thomascook.in/hotels/srp?id=DC231&search=Bangalore,%20IN&ci=31-01-2024&co=01-02-2024&searchType=city&room=1&starRating=&package=&R1=2_0"
    driver.get(hotel_url)
    time.sleep(20)

    start = time.time()

    # will be used in the while loop
    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
        # this command scrolls the window starting from
        # the pixel value stored in the initialScroll 
        # variable to the pixel value stored at the
        # finalScroll variable
        initialScroll = finalScroll
        finalScroll += 1000

        # we will stop the script for 3 seconds so that 
        # the data can load
        time.sleep(3)
        # You can change it as per your needs and internet speed

        end = time.time()

        # We will scroll for 20 seconds.
        # You can change it as per your needs and internet speed
        scrolling_time = 80
        if round(end - start) > scrolling_time:
            break


    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find_all('div', class_="col-md-12 col-sm-12 col-12 hotel-search-list" )
    for ele in text:
        name = ele.find('a', class_="cursor-pointer" ).text
        price = ele.find('span',{"data-bind":"attr:{'id':'hotelPrice_'+$data.hotelKey}"}).text.replace(" ","")
        
        print(name + " " + price)
        csv_writer.writerow([name,price])
        
    csv_file.close()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
url = f"https://www.thomascook.in/hotels"
driver.get(url)
time.sleep(20)

# driver.find_element(By.XPATH,"//input[@tabindex='1']").click()
# time.sleep(5)
