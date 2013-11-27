#!/usr/bin/python

import praw
import webbrowser

def redditsearch(query, r):
    search = r.search_reddit_names(query)
    for subs in search:
        print "Searching Subreddit %s" % subs
    submissions = r.get_subreddit(str(subs)).get_hot(limit='1')
    print type(submissions)
    #for item in submissions:
    #print "The title is %s" % submissions.title
    #print "The URL is %s" % submissions.url
    #print "The subreddit is %s" % submissions.subreddit



def randomreddit(r):
    print "Searching Random Reddit"
    randomsub = r.get_random_subreddit()
    random = r.get_random_submission(subreddit=randomsub)
    print "The title is %s." % random.title
    print "The URL is %s." % random.url
    print "The subreddit is %s." % random.subreddit

def main():
    """Setting parameters needed for script"""
    user_agent = ("TestBot no such user found github.com/archey")
    r = praw.Reddit(user_agent=user_agent)
    query = raw_input("Please input search terms" + " ")
    print "Searching Reddit for %s, as requested" % query
    redditsearch(query,r)
    #content = redditsubmissions(subs,r) 
    randomreddit(r)
if __name__ == "__main__":
    main()
