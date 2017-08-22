import praw
import re

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("ArkunEnterprises")
pizza = 'pizza'


for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search(" but " or ", but " and not "Everything before but doesn't count", comment.body, re.IGNORECASE):
            comment.reply("Everything before but doesn't count. \n\n You meant this: \n\n >" + comment.body)
            print(pizza)
            

