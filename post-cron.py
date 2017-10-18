import praw
import datetime
import os.path

# open the config file as read-only
input_file = open('config.txt', 'r')
config_settings = input_file.readlines()
input_file.close()

# make sure all of the configuration fields have been filled except for the submission time related
 # ones, which don't matter for this crontab-based script
for config in config_settings:
    if config[-2:] == '=\n' and config[:10] != 'submission':
        raise('Error: Configuration field left blank!')


# begin parsing the information from the configuration file into usable variables
# note the '.rstrip()' method being called on each string - this removes any newlines
username = config_settings[0][9:].rstrip()
password = config_settings[1][9:].rstrip()

client_id = config_settings[2][10:].rstrip()
client_secret = config_settings[3][14:].rstrip()

subreddit = config_settings[4][10:].rstrip()
submission_title = config_settings[8][17:].rstrip()
submission_text = config_settings[9][16:].rstrip()


# open/create a log file to dump whether the scrip was successful or not
if os.path.isfile('log.txt'):
    log_file = open('log.txt', 'a')

else:
    # create the file if it doesn't exist
    log_file = open('log.txt', 'a')
    log_file.write('Log Generated: ' + str(datetime.datetime.now()) + "\n==========================================\n")


try:
    # login to reddit...
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, username=username,
                         user_agent="User")

    # create an instance of the subreddit class and submit the post!
    target_subreddit = reddit.subreddit(subreddit)
    target_subreddit.submit(title=submission_title, selftext=submission_text, url=None, resubmit=True, send_replies=True)

    # output to the logfile
    log_file.write(str(datetime.datetime.now()) + '  :  Success\n')

except Exception as err:
    # if something went wrong with reddit, put the exception in the log file
    log_file.write(str(datetime.datetime.now()) + '  :  Failure: ' + str(type(err)) + '\n')

