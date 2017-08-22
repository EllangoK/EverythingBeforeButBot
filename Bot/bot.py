import praw
import re
import pdb
import os
import time
import sys

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
                if re.search(" but " or ", but ", comment.body, re.IGNORECASE):
                    fixed_comment = re.split("but", comment.body, flags=re.IGNORECASE)[0]
                    x = fixed_comment
                    if x.endswith(', '):
                        x = x[:-1]
                        x = x[:-1]
                    comment.reply('Everything before **but** doesn\'t count. \n\n You mean \n\n >' + x + "\n\n Instead of \n\n >" + comment.body)
                    posts_replied_to.append(comment.id)
                    print ("s")
                    with open("posts_replied_to.txt", "w") as f:
                        for post_id in posts_replied_to:
                            f.write(post_id + "\n")


doStuff()