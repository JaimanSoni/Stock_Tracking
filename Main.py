import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime
from flask import Flask, render_template, redirect, request
counter = 0
app = Flask(__name__)
date = datetime.now()

urls = ["https://www.moneycontrol.com/india/stockpricequote/infrastructure-general/texmacorailengineering/TRE", "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/centralbankindia/CBO01", "https://www.moneycontrol.com/india/stockpricequote/sugar/kotharisugarschemicals/KSC", "https://www.moneycontrol.com/india/stockpricequote/carbon-black/pcbl/PCB01", "https://www.moneycontrol.com/india/stockpricequote/engines/greavescotton/GC20", "https://www.moneycontrol.com/india/stockpricequote/paper/pudumjeepaperproductslimited/PPP04", "https://www.moneycontrol.com/india/stockpricequote/finance-term-lending/sbicardspaymentservices/SCP02", "https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/reliancepower/RP", "https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/suzlonenergy/SE17"]
sharePrices =[1, 2, 3, 4, 5, 6, 7, 8, 9]
numberOfSharesPurchased = [500, 400, 400, 100, 100, 500, 19, 500, 4000]
originalSharePrice = [44, 23, 36, 114, 128, 38, 755, 140, 4]
shareNames = ["Texmaco Rail", "Central Bank", "Kothari Sugar", "PCBL", "Greaves Cotton", "Padamji Paper", "SBI Cards", "R Power", "Suzlon"]
@app.route("/")
def addPrices():

    for j in range(len(urls)):
        url = urls[j]
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        a = soup.find("div", id = "nsecp")
        sharePrices[j] = a.text
        

    path2 = os.path.join(os.getcwd(), "Prices.csv")
    with open(path2, "a") as f:
        f.write("\n")
        j = 0
        for i in sharePrices:
            if j == 5:
                f.write(i + ",")
            else:
                f.write(i + ",")
            j+=1
        f.write(str(date))
    return render_template("index.html", sharePrices = sharePrices, shareNames = shareNames, originalSharePrice = originalSharePrice, numberOfSharesPurchased = numberOfSharesPurchased)

# @app.route("/addnew")
# def addStock():
#     global counter
#     counter = 0
#     return render_template("addnew.html")

# @app.route("/home", methods = ["GET", "POST"])
# def home():
#     numberOfSharesPurchased.append(request.form.get("number"))

#     global counter
#     if counter == 0:
#         counter += 1
#         return render_template("index.html", sharePrices = sharePrices, shareNames = shareNames, originalSharePrice = originalSharePrice, numberOfSharesPurchased = numberOfSharesPurchased)
#     else:
#         counter = 0
#         return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)