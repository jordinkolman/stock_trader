# Summary: This module contains the user interface and logic for a console-based version of the stock manager program.
# Author: Jordin Kolman
# Date: 9/18/2022

from datetime import datetime
from stock_class import Stock, DailyData
from account_class import Traditional, Robo
from utilities import clear_screen, display_stock_chart
from os import path
import stock_data
import matplotlib.pyplot as plt
import csv


# Main Menu
def main_menu(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Stock Analyzer ---")
        print("1 - Manage Stocks (Add, Update, Delete, List)")
        print("2 - Add Daily Stock Data (Date, Price, Volume)")
        print("3 - Show Report")
        print("4 - Show Chart")
        print("5 - Manage Data (Save, Load, Retrieve)")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","5", "6","7","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Stock Analyzer ---")
            print("1 - Manage Stocks (Add, Update, Delete, List)")
            print("2 - Add Daily Stock Data (Date, Price, Volume)")
            print("3 - Show Report")
            print("4 - Show Chart")
            print("5 - Manage Data (Save, Load, Retrieve)")
            print("6 - Investor Type")
            print("7 - Load Data")
            print("0 - Exit Program")
            option = input("Enter Menu Option: ")
        if option == "1":
            manage_stocks(stock_list)
        elif option == "2":
            add_stock_data(stock_list)
        elif option == "3":
            display_report(stock_list)
        elif option == "4":
            display_chart(stock_list)
        elif option == "5":
            manage_data(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:
            clear_screen()
            print("Goodbye")

# Manage Stocks
def manage_stocks(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Stocks ---")
        print("1 - Add Stock")
        print("2 - Update Shares")
        print("3 - Delete Stock")
        print("4 - List Stocks")
        print("0 - Exit Manage Stocks")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("1 - Add Stock")
            print("2 - Update Shares")
            print("3 - Delete Stock")
            print("4 - List Stocks")
            print("0 - Exit Manage Stocks")
            option = input("Enter Menu Option: ")
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            update_shares(stock_list)
        elif option == "3":
            delete_stock(stock_list)
        elif option == "4":
            list_stocks(stock_list)
        else:
            print("Returning to Main Menu")

# Add new stock to track
def add_stock(stock_list):
    clear_screen()
    option = ""
    while option != "0":
        print("Add Stock --- ")
        symbol = input("Enter Ticker Symbol: ").upper()
        name = input("Enter Company Name: ")
        shares = float(input("Enter Number of Shares: "))
        new_stock = Stock(symbol, name, shares)
        stock_list.append(new_stock)
        option = input("Stock Added - Enter to Add Another Stock or 0 to Stop: ")

# Buy or Sell Shares Menu
def update_shares(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Update Shares ---")
        print("1 - Buy Shares")
        print("2 - Sell Shares")
        print("0 - Exit Update Shares")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Update Shares ---")
            print("1 - Buy Shares")
            print("2 - Sell Shares")
            print("0 - Exit Update Shares")
            option = input("Enter Menu Option: ")
        if option == "1":
            buy_stock(stock_list)
        elif option == "2":
            sell_stock(stock_list)
        elif option == "0":
            print("Returning to Main Menu")

# Buy Stocks (add to shares)
def buy_stock(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Sell Stocks (subtract from shares)
def sell_stock(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Remove stock and all daily data
def delete_stock(stock_list):
    clear_screen()
    print("Delete Stock ---")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("Which stock do you want to delete?:").upper()
    found = False
    i = 0
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
        i += 1
    if found == True:
        print("Deleted", symbol)
    else:
        print("Error: Symbol", symbol, "not found")
    _ = input("*** Press Enter to Continue ***")

# Get price and volume history from Yahoo! Finance using CSV import
def import_stock_csv(stock_list):
    print("\nAdd historical data to a stock in the stock list")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("Enter stock symbol: ").upper()
    filename = input("Enter the file name: ")
    for stock in stock_list:
        if stock.symbol == symbol:
            with open(filename, newline='')as stockdata:
                datareader = csv.reader(stockdata, delimiter=',')
                next(datareader)
                for row in datareader:
                    daily_data = DailyData(str(row[0]), float(row[4]), float(row[6]))
                    stock.add_data(daily_data)
    display_report(stock_list)

#Display report for All Stocks
def display_report(stock_list):
    print("Stock Report ---")
    for stock in stock_list:
        print("Report for: ", stock.symbol, stock.name)
        print("Shares: ", stock.shares)
        #variable initialization
        count = 0
        price_total = 0
        volume_total = 0
        lowPrice = 9999999.99
        highPrice = 0.0
        lowVolume = 9999999999
        highVolume = 0

        for daily_data in stock.DataList:
            count = count + 1
            price_total = price_total + daily_data.close
            volume_total = volume_total + daily_data.volume
            if daily_data.close < lowPrice:
                lowPrice = daily_data.close
            if daily_data.close > highPrice:
                highPrice = daily_data.close
            if daily_data.volume < lowVolume:
                lowVolume = daily_data.volume
            if daily_data.volume > highVolume:
                highVolume = daily_data.volume

            priceChange = highPrice - lowPrice
            print(daily_data.date, daily_data.close, daily_data.volume)

        if count > 0:
            print("Summary ---")
            print("Low Price: ${:,.2f}".format(lowPrice))
            print("High Price: ${:,.2f}".format(highPrice))
            print("Average Price: ${:,.2f}".format(price_total/count))
            print("Low Volume: {}".format(lowVolume))
            print("High Voume: {}".format(highVolume))
            print("Average volume: {:,.2f}".format(volume_total/count))
            print("Change in Price: ${:,.2f}".format(priceChange))
            print("Profit/Loss: ${:,.2f}".format(priceChange * stock.shares))
        else:
            print('**** No daily history')
        print("\n\n\n")
    print("---Report Complete---")
    _ = input("Prese Enter to continue")
# List stocks being tracked
def list_stocks(stock_list):
    clear_screen()
    print("Stock List ---")
    print("SYMBOL", " " * 7, "NAME", " " * 9, "SHARES")
    print("====================================")
    for stock in stock_list:
        print(stock.symbol, " " * (11-len(stock.symbol)), stock.name, " " * (17-len(stock.name)), stock.shares) 
    _ = input("*** Press Enter to Continue ***")

# Add Daily Stock Data
def add_stock_data(stock_list):
    clear_screen()
    print("Add Daily Stock Data ---")
    print("Stock List [", end="")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("Ready to add data for: ", symbol)
        print("Enter Data Seperated By Commas - DO NOT Use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date, float(price), float(volume))

            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("Data Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("*** Press Enter to Continue ***")

# Display Stock Chart
def display_stock_chart(stock_list, symbol):
    date = []
    price = []
    volume = []
    company = ""
    for stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)
    plt.plot(date, price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(company)
    plt.show()

# Display Chart
def display_chart(stock_list):
    clear_screen()
    print("Stock Chart---")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("Pick stock for a chart:").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        display_stock_chart(stock_list, current_stock.symbol)
    else:
        print("Error: Symbol", symbol, "not found")
    _ = input("*** Press Enter to Continue ***")

# Manage Data Menu
def manage_data(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Data ---")
        print("1 - Save Data to Database")
        print("2 - Load Data from Database")
        print("3 - Retrieve Data from Web")
        print("4 - Import from CSV File")
        print("0 - Exit Manage Data")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","5","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("1 - Save Data to Database")
            print("2 - Load Data from Database")
            print("3 - Retrieve Data from Web")
            print("4 - Import from CSV File")
            print("0 - Exit Manage Data")
            option = input("Enter Menu Option: ")
        if option == "1":
            stock_data.save_stock_data(stock_list)
            print("--- Data Saved to Database ---")
            _ = input("Press Enter to Continue")
        elif option == "2":
            stock_data.load_stock_data(stock_list)
            print("--- Data Loaded from Database ---")
            _ = input("Press Enter to Continue")
        elif option == "3":
            retrieve_from_web(stock_list)
            print("--- Data Retrieved from Yahoo! Finance ---")
            _ = input("Press Enter to Continue")
        elif option == "4":
            import_stock_csv(stock_list)
        else:
            print("Returning to Main Menu")

def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct= input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ",robo_acct.investment_return())
        print("\n\n")
        _ = input("Press Enter to Continue")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [",end="")
            for stock in stock_list:
                print(stock.symbol," ",end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
              if stock.symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock.shares += shares 
                temp_list.append(current_stock)
                print("Bought ",shares,"of",symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)


# Get stock price and volume history from Yahoo! Finance using Web Scraping
def retrieve_from_web(stock_list):
    clear_screen()
    print("*** This Module Under Construction ***")
    _ = input("*** Press Enter to Continue ***")

# Begin program
def main():
    #check for database, create if not exists
    if path.exists("stocks.db") == False:
        stock_data.create_database()
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()
