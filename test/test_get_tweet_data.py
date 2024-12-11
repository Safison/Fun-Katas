from src.get_tweet_data import get_tweet_data

def test_My_awesome_tweet_return_0_16():
    input_tweet = "My awesome tweet"
    expect = { 'tags': [], 'mentions': [], 'tag_count': 0, 'mention_count': 0, 'length': 16 }
    result = get_tweet_data(input_tweet)
    assert result == expect

def test_My_awesome_tweet_to_northcoders():
    input_tweet = "My awesome tweet to @northcoders"
    expect = {'tags': [], 'mentions': ['@northcoders'], 'tag_count': 0, 'mention_count': 1, 'length': 32} 

    result = get_tweet_data(input_tweet)
    assert result == expect

def test_My_awesome_tweet_about_coding():
    input_tweet = "My awesome tweet about #coding"
    expect = {'tags': ['#coding'], 'mentions': [],'tag_count': 1, 'mention_count': 0, 'length': 30}
    result = get_tweet_data(input_tweet)
    assert result == expect
def test_My_awesome_tweet_about_Hash_coding_at_northcoders():
    input_tweet = "My awesome tweet about #coding to @northcoders"
    expect = {'tags': ['#coding'], 'mentions': ['@northcoders'], 
   'tag_count': 1, 'mention_count': 1, 'length': 46}
    result = get_tweet_data(input_tweet)
    assert result == expect

def test_Iam_hash_coding_with_at_northcoders_I_love_hash_coding_and_at_northcoders():
    input_tweet = "I am #coding with @northcoders I love #coding and @northcoders"
    expect= {'tags': ['#coding'], 'mentions': ['@northcoders'], 
   'tag_count': 1, 'mention_count': 1, 'length': 62}
    result=get_tweet_data(input_tweet)
    assert result == expect