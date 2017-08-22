import praw
import re
import pdb
import os
import time

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("ArkunEnterprises")
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

def doStuff():
    for comment in subreddit.stream.comments():
        if comment.id not in posts_replied_to:
            if comment.author != "EverythingBeforeBut":
                if re.search(" but " or ", but " and not "Everything before but doesn't count", comment.body, re.IGNORECASE):
                    comment.reply('Everything before but doesn\'t count. \n\n You meant this: \n\n >' + comment.body)
                    posts_replied_to.append(comment.id)
                    with open("posts_replied_to.txt", "w") as f:
                        for post_id in posts_replied_to:
                            f.write(post_id + "\n")
                        print ("s")
