# Playstore-App-Reviews-Scraping-Bot
Simple bot that scrapes the review and ratings data of app specified on Google Play Store
#### Before attempting to scrape data
- You should have the reqiuired libraries
- You must have the appropriate selenium driver for google chrome installed
- You have to include/adjust the path to the driver on your local machine
- You have to enter the app name in the space provided before running the script.
- You can adjust the "number of calls". This tells the script how many times to trigger the JS data loading function. More loads = More data and longer process time.

## Other things to note.
- You should ignore any error messages like "DevTools listening on...."
- "dns_config_service_win.cc(509)] Failed to read DnsConfig." Simply means your system is not connected to the internet.
- In an event where the bot crashes after you receive the "Exercise patience as this may take up to 10 minutes or more." message, it means you have a slow network and need to adjust the WAIT_TIME to suit network speed.
- It saves the app reviews in csv format as 'app name_reviews'.csv
---
## This bot was not built to break any laws of any sort. I built it to scrap data for my Call of Duty Mobile ML/NLP project. It can and will be used to scrape app reviews for other projects.
--- 
