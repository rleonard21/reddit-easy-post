# Reddit Easy Post Bot!

### About
There have been a few threads in /r/redditdev regarding an easy way to automatically submit a post
at a given time. This is a simple Python script to cover that need!

### Setup
 
#### Dependencies
This script uses Python 3.6 and has only one dependency: PRAW. This is the API Wrapper used for interfacing with
the Reddit API. It can be installed with pip:
```commandline
$ pip3 install praw
```


More information about installing PRAW can be found here:
http://praw.readthedocs.io/en/latest/getting_started/installation.html


#### Configuration
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


#### Client ID and Client Secret
In order to make your account access the Reddit API, it must be a developer account. 
This can be done by going into account preferences, then click apps. This panel should allow you 
to create a bot for the account and get the ID and Secret. 
A good guide can be found here:

http://progur.com/2016/09/how-to-create-reddit-bot-using-praw4#registering-the-bot

#### Submission Content!
This script uses the supplied `content.txt` file for the content of the submission. Edit
this file in your favorite text editor. Remember, Reddit's posts use Markdown for formatting!
Plenty of information about can be found online. 
The first line of this file will be the title of the post. Anything after that is the content
of the submission! Here's an example `content.txt` file to help:
```buildoutcfg
Hello world!
This is the body of your submission. Anything following the 
first line of this file will be included in your post. Have fun!
```
Here the title will be `Hello world!` and the body will be `This is the body...` and everything
after that. 

### Cron Installation
This script is intended to run on a Linux (or Mac) based computer using the crontab service. This can easily be accomplished using a Desktop, Raspberry Pi, or a service such as Amazon AWS. 

Open a terminal and clone this repository into your working directory:

```commandline
$ git clone https://github.com/rleonard21/reddit-easy-post.git
```

Then edit your crontab by running the following command:
```commandline
$ crontab -e
```
When the crontab file opens in the text editor, enter the following at the bottom:

```commandline
min hr day mon dow python3 /full/path/post-cron.py
```

Where `min`, `hr`, `day`, `mon`, and `dow` represent the time at which to run the script. 
How to set up the time will not be explained here, as it is covered in
many other resources:
http://www.adminschoice.com/crontab-quick-reference

Once this is setup on crontab, the Reddit account will post by itself at the specific intervals!

### Cron Alternative
Something that I've found useful a few times is the ability to post only once at a certain time. 
This can be done using the `at` tool in Linux. Installation is as such:
```commandline
$ sudo apt-get install at
```
And setting up the one-time post is just as easy:
```commandline
$ echo "python3 /full/path/post-cron.py" | at 9:00AM
```
A good walkthrough of `at` can be found here: 
https://tecadmin.net/one-time-task-scheduling-using-at-commad-in-linux/

### Modifying the Post Content
If you setup the script and wanted it to post something different, all that needs to be done is to modify the material inside of `content.txt`. 
When the bot posts next, it will use the updated content in the file. 
