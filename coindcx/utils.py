from utils.orderbook import Entry


def transform_raw_orderbook(raw_orderbook):
    new_bids = []
    new_asks = []
    bids, asks = raw_orderbook['bids'], raw_orderbook['asks']
    for p, q in bids.items():
        new_bids.append(Entry(p, q))

    for p, q in asks.items():
        new_asks.append(Entry(p, q))

    new_bids = sorted(new_bids, key=lambda e: e.price, reverse=True)
    new_asks = sorted(new_asks, key=lambda e: e.price)

    return {
        'bids': new_bids,
        'asks': new_asks
    }
