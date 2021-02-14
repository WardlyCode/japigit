import urllib.request
import json


def getStockData(stock):
    url= "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+stock+"&apikey=GXKBT94AVIQWCVIB"

    connection = urllib.request.urlopen(url)
    responseString = connection.read().decode()

    return responseString
    
#print(getStockData('ntdoy'))

def main():
    outputFile = open("japi.out", "w")

    print('Enter stock symbol or quit:')
    stock = input()

    while stock != 'quit':
        data = getStockData(stock)

        print(data)
        print(' ')

        dictionary = json.loads(data)

        quote = dictionary['Global Quote']

        entry = 'The current price of ' + stock + ' is: ' + quote['05. price']
        outputFile.write(entry)
        outputFile.write("\n")

        print('The current price of ' + stock + ' is: ' + quote['05. price'])
        print(' ')


        print('Enter stock symbol or quit:')
        stock = input()

main()