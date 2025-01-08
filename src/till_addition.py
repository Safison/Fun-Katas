
def till_addition(till):
    sum = 0
    for coin in till:
        if 'p' in coin:
            coin = coin.rstrip('p')
            coin = int(coin)
            coin = coin / 100
            sum += coin
        elif '£' in coin:
            coin = coin.lstrip('£')
            coin = int(coin)
            sum += coin
    return '£' + str(sum)
