# WhatsApp Bulk Sender

## About the project

I'm too lazy to copy-paste 50 messages. So, I tried various chrome extensions for sending bulk messages in WhatsApp. **I don't trust them to protect my personal data** and some of them don't work as expected or are paid service. I also consider a bunch of other nice projects in GitHub but my secondary goal was to learn more about Selenium.

So, I tried to do it my way with **Python and Selenium**. After a couple of hours, here is the result. A lot to improve, but it works just fine for my purpose:  **Automate sending message with a picture to a bunch of folks and keep track of sent messages without having to scan QR code each time.**

Thanks for [Akjasim](https://github.com/akjasim/python-automation-selenium) and his youtube tutorials on Selenium. Also, consider to take a look at [alright](https://github.com/Kalebu/alright) library by Kalebu which is a nice WhatsApp wrapper of Selenium written in python.

What selenium will do to send the message : 

I. Whatsapp web : 
 1. Open Chrome Browser ; 
 2. Go to whatsapp web and wait for QR code to be completed ;
 
II. Loop trough sending messages with thumbnail : 
 1. Click the new chat button ; 
 2. Copy paste the number from the contacts.csv file in the search bar ; 
 3. Send Enter key to go to the first contact found ; 
 4. Click to the attachment button ; 
 5. Click to the picture button ; 
 6. Copy-paste the message into the picture caption ; 
 7. Click the send button ; 
 8. Clear the phone number ;

This is a personal and educational project, **use it carefully and avoid spaming your contacts**. I take **no responsability if your phone number is blocked by WhatsApp.** 

Feel free to contribute 👍

## Requirements

I developed this project under **Linux** Mint 19 with **chromium browser**. I used **Python 3.10** with **Selenium** as my main tool to scrape out WhatsApp. I didn't test other operating systems nor Python versions. Please find the `ENV.yml` to install all requiered packages.

## Features

* Multiple sending message  as caption (700 characters) with -only one- picture (png, jpg of gif);
* One time QR code checking;
* Validate the `contacts.csv` database:

  * if phone numbers have the country code (Currently, only french ones) and the right pattern (For other country codes, change the regex `pattern` variable in the `/src/modules/automate_whatsapp.py` file) or just comment the `test_contacts` function in `/src/main.py` file.
  * absence of duplicated or missing numbers;
  * your kept the column headers.
* Many randomized pauses during runtime to avoid being blocked ;

## Quickstart

1. Set up the **environment** with the `ENV.yml` file
2. Set up the **data** :
   1. Duplicated the `TEMPLATE` folder and rename it as you pleased. Then, into the folder :
   2. Paste your message to send in the `message.txt`file ;
   3. Paste your picture and rename it as `picture.png` (or .jpg or .gif) ;
   4. Paste your phone numbers and names in the `contacts.csv` file. **Warning**: Keep the column headers as they are and be sure that every phone number are formatted with international phone prefix as +33XXXXXX (France). `Saved Name` are facultative.
   5. Write the paths in the `TEMPLATE/config.yml` file. The pictures path needs to be an absolute one. Finally, find your chrome profile data directory. You can rename the `default` part with an other name if you please. Examples can be found in the `TEMPLATE/config.yml` file.
3. **Run in command** line the `src/main.py` file and input your folder name `python3 main.py` then input your data folder named previously `MY FOLDER`.
4. The first time, you will have to **scan the QR code** with your phone. (For the next time, if you use the same chrome profile -see `TEMPLATE/config.yml`- you will not have to do this again)
5. The chrome browser will show up, and **the magic will begin**. When the process completes, the browser exists and you will find a `tracking.csv` file containing your contact informations plus a `Sent` column to check if the message was sent and a `Time` column with sending time (or not).

## Improvements

* [ ] Bug fixing;
* [ ] Refactoring;
* [ ] Better exception handling;
* [ ] CLI Interface;
* [ ] Multiple choices for sending messages with or without attachments. Currently, it only supports sending messages as caption of one picture. (700 characters max.)
* [ ] Better use of sleep time and Selenium waits;
* [ ] Other web browser choices;
* [ ] Unit tests ;
* [ ] And more..
