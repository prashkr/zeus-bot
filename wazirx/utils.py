from utils.orderbook import Entry


def transform_raw_orderbook(raw_orderbook):
    bids = []
    asks = []
    for p, q in raw_orderbook['bids']:
        bids.append(Entry(p, q))

    for p, q in raw_orderbook['asks']:
        asks.append(Entry(p, q))

    return {
        'bids': bids,
        'asks': asks
    }
