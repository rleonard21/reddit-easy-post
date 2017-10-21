# Reddit Easy Post Bot!

### About
There have been a few threads in /r/redditdev regarding an easy way to automatically submit a post
at a given time. This is a simple Python script to cover that need!

### Setup
Using this program is rather simple. 
##### Dependencies
This script has only one dependency: PRAW. This is the API Wrapper used for interfacing with
the Reddit API. It can be installed with pip:

`pip3 install praw`

More information about installing PRAW can be found here:
http://praw.readthedocs.io/en/latest/getting_started/installation.html

##### Configuration
Most of the work is done in the `config.txt` file. 
This script uses a configuration file to determine the account credentials. The contents of
the `config.txt` file are as follows:
```
username=       <-- the username of the account
password=       <-- the password for that account
client-id=      <-- the "client id" for the Reddit account
client-secret=  <-- the "client secret" associated with the Reddit account
subreddit=      <-- the subreddit where the post should go
```
A quick note here: Fields such as `username` and `subreddit` do not include the common
slashes. For example, the username should be `username` instead of `/u/username`, and the 
subreddit should be like `redditdev` rather than `/r/redditdev`.

##### Client ID and Client Secret
In order to make your account access the Reddit API, it must be a developer account. 
This can be done by going into account preferences, then click apps. This panel should allow you 
to create a bot for the account and get the ID and Secret. 
A good guide can be found here:
http://progur.com/2016/09/how-to-create-reddit-bot-using-praw4#registering-the-bot





### Installation
This script runs on any Linux (or mac) based computer using the crontab service. 

Open a terminal and clone this repository into your working directory:

`git clone https://github.com/rleonard21/reddit-easy-post.git`

Then edit your crontab by running the following command:

`crontab -e`

When the crontab file opens in the text editor, enter the following at the bottom:

`min hr day mon dow python3 /path/to/directory/post-cron.py`

Where `min`, `hr`, `day`, `mon`, and `dow` represent the time at which to run the script. 
How to set up the time will not be explained here, as it is covered in
many other resources:
http://www.adminschoice.com/crontab-quick-reference

Once this is setup on crontab, the Reddit account will post by itself at the specific intervals!