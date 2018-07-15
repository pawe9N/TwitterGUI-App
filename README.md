# TwitterGUI-App
TwitterGUI App was created for purpose of learning python, twitter API (python-twitter library) and PyQt5.

## Description of application
This app shows twitter profile in window without assistance of browser. You can watch your tweets and tweets of people you follow, add new tweets or send messages to other users.

## Getting Started

If you want to use this program, you have to download all files of this repository.
Then you should install all requirements which you can see in requirements.txt. 
To install it you should use the following pip command in your console: 
```python
pip install -r /path/to/requirements.txt
```
After that you have to create keys_class.py file in classes directory and input the following code with your keys there:

```python
class Keys:
	def __init__(self):
		self.consumer_key = "Input your consumer key"
		self.consumer_secret = "Input your consumer secret key"
		self.access_token = "Input your access token key"
		self.access_secret = "Input your access secret key"
```

After that you will can open an application with your personal twitter account.

## Little demo with Gifs

- Starting the application
<img src="https://i.imgur.com/C9catMz.gif">

- Choosing my account
<img src="https://i.imgur.com/m5gPhzF.gif">

- Showing data (tweets, my tweets, photos, messages to me, messages from me, following, followers, favourites)
<img src="https://i.imgur.com/QEjYOMk.gif">

- Posting a new tweet with instant switching to "My Tweets" page
<img src="https://i.imgur.com/mOJLGhp.gif">

- Sending a message to users (in this example to myself) with instant switching to "Messages From Me" page
<img src="https://i.imgur.com/DBYhRUB.gif">

- What if you will not have an internet connection?
<img src="https://i.imgur.com/yFPMNNo.gif">
