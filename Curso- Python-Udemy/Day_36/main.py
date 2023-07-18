from datetime import datetime
import smtplib
import requests

dt = datetime.now()
week_day = dt.weekday()

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
COMPANY_NAME = "tesla"
STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = "apikey"
FNC = "TIME_SERIES_DAILY_ADJUSTED"
INTERVAL = "60min"
stock_params = {
    "function":FNC,
    "symbol":STOCK_NAME,
    "interval":INTERVAL,
    "apikey":API_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "apikey"
NEWS_ORDER = "publishedAt"
NEWS_LANG = "en"
news_params = {
    "q":COMPANY_NAME, #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    "sortBy":NEWS_ORDER,
    "language":NEWS_LANG,
    "apiKey":NEWS_API_KEY,
}
# --------------------------------- Stock Data --------------------------------
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()
# --------------------------------- News Data --------------------------------
news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
# --------------------------------- Vars --------------------------------
last_day_list = data["Meta Data"]["3. Last Refreshed"].split("-")
if week_day == 5 or week_day == 6:
    print("Weekends dont have stock market data.\nClosing the program now...")
    exit()
elif week_day == 0 :
    last_day_list[2] = int(last_day_list[2]) - 3
else:
    last_day_list[2] = int(last_day_list[2]) - 1
yesterday_date = data["Meta Data"]["3. Last Refreshed"]
before_yesterday_date = "-".join(str(x) for x in last_day_list)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_close = float(data["Time Series (Daily)"][yesterday_date]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_close = float(data["Time Series (Daily)"][before_yesterday_date]["4. close"])

# #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(before_yesterday_close - yesterday_close)

# #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
result_percent = float(((yesterday_close - before_yesterday_close) * 100) / before_yesterday_close)


## STEP 2: https://newsapi.org/ 
articles = news_data["articles"][0:4] #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.

artcl_list = [] #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
if result_percent > 3 : #TODO 5. - If percentage is greater than number then print("Get News").
    for i in range(len(articles)):
        title = articles[i]["title"].upper()
        date = articles[i]["publishedAt"]
        desc = articles[i]["description"]
        text = (f"{STOCK_NAME}: 🔺 {result_percent:.2f}%\nHeadline: {title} - {date}\nBrief: {desc}\n").encode("utf-8")
        artcl_list.append(text)
elif result_percent < 3 : #TODO 5. - If percentage is lower than number then print("Get News").
    for i in range(len(articles)):
        title = articles[i]["title"].upper()
        date = articles[i]["publishedAt"]
        desc = articles[i]["description"]
        text = (f"{STOCK_NAME}: 🔻 {result_percent:.2f}%\nHeadline: {title} - {date}\nBrief: {desc}\n").encode("utf-8")
        artcl_list.append(text)


#to send a separate message with each article's title and description to your phone number. 
#TODO 9. - Send each article as a separate message via Twilio. 
def send_msg(msg):
    my_email = "user@email.com"
    my_password = "password"
    dest_email = "dest_user@email.com"
    email_msg = f"Subject:Stock Market News Message\n\n{msg}"
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=dest_email, msg=email_msg)

for i in range(len(artcl_list)-1):
    send_msg(artcl_list[i])
    print("Sent e-mail!!!")