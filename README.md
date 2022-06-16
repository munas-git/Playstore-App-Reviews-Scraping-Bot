# Playstore-App-Reviews-Scraping-Bot
Simple bot that scrapes the review and ratings data of app specified on Google Play Store
#### Before attempting to scrape data
- You must have the selenium driver for google chrome installed
- You have to include the path of the driver on your local machine
- You have to enter the app name in the space provided before running the script.
- You can adjust the "number of calls". This tells the script how many times to trigger the JS data loading function. More loads = More data and longer process time.

### Hit run and watch the scraper do its magic. It also saves the app reviews in csv format as 'app name'.csv
### You should ignore any error messages like "DevTools listening on...."
- "dns_config_service_win.cc(509)] Failed to read DnsConfig." Simply means your system is not connected to the internet.
- In situation where the script fails to load completely, it means the wait time was too short and page content did not fully load. To solve this, simply increase wait time in "time.sleep(_)". Adjust the time in seconds to your desired time.
