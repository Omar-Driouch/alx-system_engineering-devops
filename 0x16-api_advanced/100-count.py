#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and
returns a list containing the titles of all
hot articles for a given subreddit
"""


import praw

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if not subreddit:
        return

    # Initialize Reddit instance
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='YOUR_USER_AGENT'
    )

    # Fetch hot articles from the subreddit
    try:
        subreddit_obj = reddit.subreddit(subreddit)
        hot_articles = subreddit_obj.hot(limit=100, params={'after': after})
    except praw.exceptions.Redirect:
        print("Invalid subreddit or no results found.")
        return

    for submission in hot_articles:
        # Get the next page of submissions if there's more
        after = submission.fullname
        count_words(subreddit, word_list, after, counts)

        # Parse title and count occurrences of keywords
        title_words = submission.title.lower().split()
        for word in word_list:
            word = word.lower()
            if word in title_words:
                counts[word] = counts.get(word, 0) + title_words.count(word)

    # If it's the initial call, print the results
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")