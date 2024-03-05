#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 404:
            return 0
        results = response.json().get("data")
        return results.get("subscribers")
    except requests.exceptions.RequestException as e:
        return 0
    except ValueError as e:
        return 0
    except KeyError as e:
        return 0
    except Exception as e:
        return 0
