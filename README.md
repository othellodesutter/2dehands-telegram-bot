# 2dehands-telegram-bot
Telegram bot that notifies the user when a new 2dehands listing that corresponds to their search was added to [2dehands](https://www.2dehands.be).

## Installation
The only requirement is having the *requests* library installed.

```bash
pip install requests
```

## Configuration
Make a new file in the main directory called *config.py* with the following structure:

```python
config = {
    'token': '',
    'chat_id': '',
    'url': 'for example https://www.2dehands.be/lrp/api/search?attributesByKey[]=Language%3Aall-languages&limit=100&offset=0&query=iphone&searchInTitleAndDescription=true&sortBy=SORT_INDEX&sortOrder=DECREASING&viewOptions=list-view'
}
```

To add a new bot on Telegram, start a conversation with [@BotFather](https://telegram.me/BotFather) and send the message `/newbot`. Choose the desired name of how you want your notifier to be called aswell as the desired username. Copy the token and paste it in the *config.py* file. 

To obtain the *chat_id* of the chat you want your bot to be in, add your freshly created bot to a group, send a message to this group starting with `/`, go to *api.telegram.org/bot`token`/getUpdates* and there you can get the *chat_id* ([I followed this guide](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)). 

Add in following url *https://www.2dehands.be/lrp/api/search?attributesByKey[]=Language%3Aall-languages&limit=100&offset=0&query= `the product you are looking for`&searchInTitleAndDescription=true&sortBy=SORT_INDEX&sortOrder=DECREASING&viewOptions=list-view*, the product you are looking for, copy the *url* and paste in into your *config.py* file.

## Usage
Start the bot by running the *script.py* file.
