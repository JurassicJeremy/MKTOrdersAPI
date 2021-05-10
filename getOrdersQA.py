import requests
import json
import os

# The below API are for MarketTime's QA DB
# Update MFRID in URLs in lines 48 and 76
# Update API Key in lines 14 and 124

# URL to retrieve count of new orders
countURL = "https://api.reptimeqa.com/reptime/public/api/orders/export/c/count"

payload = {}
headers = {
    # API Key provided by MarketTime
    "x-api-key": "ENTER IN API KEY"
}
# GET API to obtain count of new orders
responseCount = requests.request("GET", countURL, headers=headers, data=payload)
count = json.loads(responseCount.text)

if apiKey in apiKey.txt:

    while True:

        print("*" * 25)
        print("What would you like to do?")
        print("*" * 25)
        print("c = Get New Order Count")
        print("d = Download Data File")
        print("v = View Raw Order Data")
        print("u = Update Order Status")
        print("q = Quit")
        print("*" * 25)
        answerMenu = input(":")

        if answerMenu == "c":

            # Currently functional, but need to wildcard search for response, not sure how to do that yet.
            # if ":1" in responseCount.text:
            while count['response'] == 0:
                print("There are no new orders, please check again later.\n")
                break

            if ":1" in responseCount.text:
                print('\nYou have', count['response'], 'new order(s), would you like to download them?\n')

                answer = input("Type y for yes, n for no: ", )

                if answer == "y":
                    detailsURL = "https://api.reptimeqa.com/reptime/public/api/orders/export/MFRID/open"

                    # GET API to obtain new order details
                    response = requests.request("GET", detailsURL, headers=headers, data=payload)
                    results = response.json()
                    print("Your orders have been marked as RECEIVED.\n")

                if answer == "n":
                    print("Thank you, see you later!")

        if answerMenu == "d":
            # Creates TXT file, and adds API response to file
            with open("apiResults1.txt", "w") as file:
                file.write(json.dumps(results))
                print("File Opened")
                os.startfile("apiResults1.txt")

        if answerMenu == "v":
            # Prints raw json data of new orders
            print("Here is the raw data:\n", response.content)

        if answerMenu == "q":
            print("\nThank you, see you soon!")
            break

        if answerMenu == "u":

            # URL to update order status
            updateURL = "https://api.reptimeqa.com/reptime/public/api/import/MFRID/orders/{orderID}/status/update"
            updateID = input("Enter up to 5 IDs of the orders to be updated, separated by commas: " ).split(',')
            for x in updateID:
                replacedURL = updateURL.replace("{orderID}", x)
                # Can be enabled for testing purposes
                # print(replacedURL)

            print("Choose the desired status:")
            print("p = Pending")
            print("r = Processed")
            print("m = Modified")
            print("h = On Hold")
            print("s = Shipped")
            print("b = Backorder")
            print("c = Cancelled")
            print("o = complete")
            statusMenu = (input(":"))
            statusResult = ""
            replacedStatus = statusMenu.replace("", statusResult)

            if statusMenu == "p":
                statusResult = "Pending"

            if statusMenu == "r":
                statusResult = "Processed"

            if statusMenu == "m":
                statusResult = "Modified"

            if statusMenu == "h":
                statusResult = "On Hold"

            if statusMenu == "s":
                statusResult = "Shipped"

            if statusMenu == "b":
                statusResult = "Backorder"

            if statusMenu == "c":
                statusResult = "Cancelled"

            if statusMenu == "o":
                statusResult = "Complete"


            payload = statusResult
            headers = {
                "x-api-key": "ENTER IN API KEY",
                'Content-Type': 'text/plain',
            }

            for x in updateID:
                replacedURL = updateURL.replace("{orderID}", x)
                responseUpdate = requests.request("POST", replacedURL, headers=headers, data=payload)
                print("Order(s) have been updated to " + statusResult)

        else:
            print("Invalid choice, please choose again.")