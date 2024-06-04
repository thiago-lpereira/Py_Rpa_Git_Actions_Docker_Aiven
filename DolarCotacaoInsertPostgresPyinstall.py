from  selenium import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService  # noqa

from selenium.webdriver.common.by import By

# opt = webdriver.ChromeOptions()
# opt.arguments.append("headless")
# Setup chrome driver
options = webdriver.EdgeOptions() 
options = options.add_argument("--headless")
driver = webdriver.Edge(options=options,service=EdgeService(EdgeChromiumDriverManager().install()))

# Navigate to the url
driver.get('https://www.bloomberg.com/quote/USDBRL:CUR')

# Find element by Class Name
elements = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[5]/div/main/div/div[1]/div[4]/div[2]/time")
elements1 = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[5]/div/main/div/div[1]/div[4]/div[1]/div[1]")


for e,y in zip(elements,elements1):
    print(e.text)
    lines = e.text.split('\n')
    brl_line = lines[0]
    # brl_lina = lines[2]

    # Splitting the BRL line by spaces and retrieving the second element which contains the value
    # brl_value = brl_line.split()[0]
    time = brl_line.split()[0] #Tempo
    
    data = brl_line.split()[3] #Data

    #Tratamento de DATE
    data3var = data.split('/')
    datamonvar = data3var[0]
    datadayvar = data3var[1]
    datayearvar = data3var[2]
    #Tratamento de DATE.year + DATE.month + DATE.day
    data1var = str("'"+datadayvar+'-'+datamonvar+'-'+ datayearvar+"'")

    #Tratamento de TIME
    time2var = time.split(':')
    timehoravar = time2var[0]
    timeminutovar = time2var[1]
    #Tratamento de TIME.hora
    timehoravar = int(timehoravar) +1
    timehoravar = str(timehoravar)
    #Tratamento de TIME.hora + TIME.minuto
    time1var = str(timehoravar +':' +timeminutovar+ ':00')
    

    #Dolar
    lines = y.text.split('\n')
    dolar_cotacao = str(lines[0])
    dolar_cotacao = dolar_cotacao[:4]
    
import psycopg2

# establishing the connection
conn = psycopg2.connect(
	database="defaultdb",
	user='avnadmin',
	password='AVNS_5bFezDwoFSmpZoYY0pM',
	host='pg-dadc362-thiagolevi2007-5833.e.aivencloud.com',
	port='28522'
)

# creating a cursor object
cursor = conn.cursor()


# list that contain records to be inserted into table
data = [(data1var,time1var, dolar_cotacao)]

# inserting record into employee table
for d in data:
	cursor.execute("call inserir_cotacao_dolar(%s,%s,%s)", d)


# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()

    

    
    # data = data.replace([])


    # hora = brl_lina.split('EDT')[0]
    # brl_value = brl_value.replace(',','.')





# Close the driver
driver.quit()
# importing psycopg2 module
