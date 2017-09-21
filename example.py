import logging

from pymongo import MongoClient
from arrow import Arrow

import plnxgrabber


def get_db(name):
    client = MongoClient('localhost:27017')
    db = client[name]
    return db


def main():
    logging.basicConfig(filename='plnxgrabber.log',
                        filemode='w',
                        format='%(asctime)s - %(name)s - %(funcName)s() - %(levelname)s - %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S',
                        level=logging.DEBUG)

    db = get_db('TradeHistory')
    grabber = plnxgrabber.Grabber(db)

    try:
        # Collect every USDT_* pair starting from September 1st
        grabber.row('(USDT_+)', from_ts=Arrow(2017, 9, 1, 0, 0, 0).timestamp, drop=True)
    except Exception as e:
        logging.exception(e)
    # Show advanced information on stored pairs
    grabber.mongo.db_long_info()

if __name__ == '__main__':
    main()
