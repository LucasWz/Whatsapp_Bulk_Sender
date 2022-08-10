# WhatsApp Bulk Sender

## About the project

I'm too lazy to copy-paste 50 messages. So, I tried various chrome extensions for sending bulk messages in WhatsApp. **I don't trust them to protect my personal data** and some of them don't work as expected or are paid service. Result, I tried to do it my way with **Python and Selenium**.

After a couple of hours, here is the result. A lot to improve, but it works just fine for my purpose:  **Sending automated messages with a picture to a bunch of french folks and keep track of sending messages.**

This is a personal and educational project, **use it carefully and avoid spaming your contacts**. I take **no responsability if your phone number is blocked by WhatsApp.** 

Feel free to comment or contribute 👍

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
   1. Duplicated the `TEMPLATE` folder and rename it as you pleased. Into the folder :
   2. Paste your message to send in the `message.txt`file ;
   3. Paste your picture and rename it as `picture.png` (or .jpg or .gif) ;
   4. Paste your phone numbers and names in the `contacts.csv` file. **Warning**: Keep the column headers as they are and be sure that every phone number are formatted with international phone prefix as +33XXXXXX (France). `Saved Name` are facultative.
   5. Write the paths in the `config.yml` file. The pictures path needs to be an absolute one. Finally, find your chrome profile data directory. You can rename the `default` part with an other name if you please. Examples can be found in the `config.yml` file.
3. **Run in command** line the `src/main.py` file and input your folder name.
4. The first time, you will have to **scan the QR code** with your phone. (For the next time, if you use the same chrome profile -see `config.yml`- you will not have to do this again)
5. The chrome browser will show up, and **the magic will begin**. When the process completes, the browser exists and you will find a `tracking.csv` file containing your contact informations plus a column `Sent` to check if the message was sent and the `Time` it was achieved (or not).

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
