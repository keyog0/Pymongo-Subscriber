from pymongo_subscriber import PymongoSubscriber
import pandas as pd
import time
import datetime

mongo_reader = PymongoSubscriber(
    _id='admin',
    _password='admin',
    cluster_name='order',
    db_name='toppingtable',
    collection_name='order_list')

# while True :
last = mongo_reader.receive_last_one()
print(last['menu'])

data = {
    'menu':"Sweet_potato",
    'store':"100th store",
    'time':datetime.datetime.now(),
    'cpu_time':time.time()
}
mongo_reader.insert_one_mongo(data)
last = mongo_reader.receive_last_one()
mongo_reader.insert_one_mongo(data)
# mongo_reader.insert_one_mongo(data)

last = mongo_reader.receive_last_one()
print(last)
    # time.sleep(1)
    # st = time.time()
    # df = mongo_reader.receive_all()
    # print('df')

    # first = mongo_reader.receive_first_one()
    # last = mongo_reader.receive_last_one()
    # print('first')

    # print('last')
    # search = mongo_reader.receive_search(key='TOT_AMT',value='6900')
    # print(search)
    # print('fps :',1/(time.time()-st))