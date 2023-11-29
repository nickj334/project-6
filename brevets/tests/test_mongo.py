

import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


from pymongo import MongoClient
import nose
from mongo import test_insert, test_fetch
import arrow

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

db = client.test_inputs
collection = db.test_lists

# Defining constant variable for time
TIME1 = "2023-07-01T00:00"

# Defining begin time as arrow object
BEGIN_TIME = arrow.get(TIME1)

# Creating global variables for test rows and test brevet distance
BREVET_DIST = "500"
ROW1 = { 'km': 100,
        'open_time': begin_time.shift(minutes=+60),
        'close_time': begin_time.shift(minutes=+65)}
ROW2 = { 'km': 200,
         'open_time': begin_time.shift(minutes=+120),
         'close_time': begin_time.shift(minutes=+125)}
ROW3 = { 'km': 300,
         'open_time': begin_time.shift(minutes=+180),
         'close_time': begin_time.shift(minutes=+185)}
ROWS = [ROW1, ROW2, ROW3]


# Testing the insertion of data into the database
def insert_test():
    _id = insert_attempt(BEGIN_TIME, BREVET_DIST, ROWS)
    assert isinstance(_id, str)

# Testing the fetching of data from database
def fetch_test():
    result = fetch_attempt()
    assert result[0] == BEGIN_TIME
    assert result[1] == BREVET_DIST
    assert result[2][0] == ROW1
    assert result[2][1] == ROW2
    assert result[2][2] == ROW3

