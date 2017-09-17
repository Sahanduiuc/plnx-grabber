import logging

import arrow
from poloniex import Poloniex
from pymongo import MongoClient

import plnxgrabber


def get_db(name):
    client = MongoClient('localhost:27017')
    db = client[name]
    return db


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(funcName)s() - %(levelname)s - %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S',
                        level=logging.DEBUG)

    polo = Poloniex()
    db = get_db('TradeHistory')
    grabber = plnxgrabber.Grabber(polo, db)

    # Fetch 5 minutes
    start_ts = arrow.Arrow(2017, 9, 1, 0, 0, 0).timestamp
    # start_id = 7821708
    end_ts = arrow.Arrow(2017, 9, 1, 0, 5, 0).timestamp
    # end_id = 7821761

    grabber.one('USDT_BTC', start_ts=start_ts, end_ts=end_ts, overwrite=True)


if __name__ == '__main__':
    main()
