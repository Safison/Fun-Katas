
def get_tweet_data(tweet):
    tweet_list=tweet.split(' ')
    tweet_length=len(tweet)
    tags_count=0
    tag_word=''
    mention_word=''
    mention_count=0
    tweet_dict={}
    tag_list=[]
    mention_list=[]
    for i in range(len(tweet_list)):
        if tweet_list[i].startswith('#'):
            
            if tweet_list[i] not in tag_list:
                tags_count += 1
                tag_word = tweet_list[i]
                tag_list.append(tag_word)
        elif tweet_list[i].startswith('@'):
            
            if tweet_list[i] not in mention_list:
                mention_count += 1
                mention_word = tweet_list[i]
                mention_list.append(mention_word)
    tweet_dict["tags"]=tag_list
    tweet_dict["mentions"]=mention_list
    tweet_dict["tag_count"]=tags_count
    tweet_dict["mention_count"]=mention_count
    tweet_dict["length"]=tweet_length

    return tweet_dict