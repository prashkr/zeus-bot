class Entry:
    def __init__(self, price: str, quantity: str):
        self.price = float(price)
        self.quantity = float(quantity)

    def __str__(self):
        return f'(price: {self.price}, quantity: {self.quantity})'


class SpreadInfo:
    def __init__(self, lowest_ask, highest_bid):
        self.lowest_ask = lowest_ask
        self.highest_bid = highest_bid

    def get_spread(self):
        return self.lowest_ask.price - self.highest_bid.price

    def get_spread_prices(self):
        return self.lowest_ask.price, self.highest_bid.price

    def get_spread_entries(self):
        return self.lowest_ask, self.highest_bid


class Orderbook:
    def __init__(self, bids, asks):
        self.bids = bids
        self.asks = asks
        self.spread_info = SpreadInfo(lowest_ask=self.asks[0], highest_bid=self.bids[0])

    @property
    def spread(self):
        assert self.spread_info is not None, 'Spread is not initialized'
        return self.spread_info.get_spread()

    def get_spread_prices(self):
        return self.spread_info.get_spread_prices()
