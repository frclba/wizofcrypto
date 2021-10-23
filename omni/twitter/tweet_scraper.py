from snscrape.modules import twitter

def search_from_specific_user(user):
    maxTweets = 100

    # Creating list to append tweet data to
    tweets_list1 = []
    print('here')
    for i, tweet in enumerate(twitter.TwitterSearchScraper('from:{}'.format(user)).get_items()):
        if i > maxTweets:
            break
        without_mentions = tweet.content.split("@", 1)[0]
        without_links = without_mentions.split("https://", 1)[0]
        tweets_list1.append([without_links])

    return tweets_list1
    # TODO ->     https://stackoverflow.com/a/41786472

def search_from_search_query(search_query):
    tweets_list2 = []
    for i, tweet in enumerate(twitter.TwitterSearchScraper(search_query).get_items()):
        if i > 500:
            break
        tweets_list2.append(
            [tweet.date, tweet.id, tweet.content, tweet.user.username])

    # TODO 2 -> https://stackoverflow.com/a/66310138