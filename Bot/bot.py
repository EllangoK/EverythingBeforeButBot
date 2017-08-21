import praw
import re

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("ArkunEnterprises")
pizza = 'pizza'


for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search(" but " or ", but " , comment.body, re.IGNORECASE):
            comment.reply("test reply please ignore")
            print(pizza)
            

