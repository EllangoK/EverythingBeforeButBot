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
but = re.compile(' but ')

def doStuff():
    for comment in subreddit.stream.comments():
        if comment.id not in posts_replied_to:
            if comment.author != "EverythingBeforeBut" and "_youtubot_":
                if re.search(" but ", comment.body, re.IGNORECASE):
                    if re.search("\(", comment.body, re.IGNORECASE) and re.search("\)", comment.body, re.IGNORECASE):
                        comment2 = re.search('\(([^)]+)', comment.body)
                        for x in range(len(comment2)):
                            print (x)
                            parenthesis_comment = comment2[x]
                            if re.search(" but ", parenthesis_comment, re.IGNORECASE) == False:
                                break
                            else:
                                fixed_comment = re.split("but", comment.body, flags=re.IGNORECASE)[0]
                                x = fixed_comment
                                if x.endswith(', '):
                                    x = x[:-1]
                                    x = x[:-1]
                                #time.sleep(1200)
                                comment.reply('[Everything before the word **but** is horse shit.](https://www.youtube.com/watch?v=jIvYWUVB1Ig) \n\n **You mean** \n\n' + x + "\n\n **Instead of** \n\n" + comment.body)
                                posts_replied_to.append(comment.id)
                                print ("s")
                                with open("posts_replied_to.txt", "w") as f:
                                    for post_id in posts_replied_to:
                                        f.write(post_id + "\n")
                    else:
                        fixed_comment = re.split("but", comment.body, flags=re.IGNORECASE)[0]
                        x = fixed_comment
                        if x.endswith(', '):
                            x = x[:-1]
                            x = x[:-1]
                        #time.sleep(1200)
                        comment.reply('[Everything before the word **but** is horse shit.](https://www.youtube.com/watch?v=jIvYWUVB1Ig) \n\n **You mean** \n\n' + x + "\n\n **Instead of** \n\n" + comment.body)
                        posts_replied_to.append(comment.id)
                        print ("s")
                        with open("posts_replied_to.txt", "w") as f:
                            for post_id in posts_replied_to:
                                f.write(post_id + "\n")

doStuff()