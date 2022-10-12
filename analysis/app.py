from datetime import datetime
import requests
import connexion
from connexion import NoContent
from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient
import pymongo
import yaml


def init_scheduler():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(populate_stats, 'interval', seconds=app_config['scheduler']['period_sec'])
    sched.start()

def get_database():
   CONNECTION_STRING = app_config['datastore']['connectionstring']
   client = MongoClient(CONNECTION_STRING)

   return client['orders']

def get_stats():
    curr_time = datetime.now()
    print(f"curr_time : {curr_time}")
    curr_time_str = curr_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    dbname = get_database()
    collection_name = dbname[app_config['datastore']['db']]
    result = list(collection_name.find().sort('last_updated',pymongo.DESCENDING))
    if len(result) == 0:
        return curr_time_str
    result_dict = {
        "total_price": result[0]["total_price"],
        "total_quantity": result[0]["total_quantity"],
        "last_updated": result[0]["last_updated"]
    }
    return result_dict

def write_data(data):
    dbname = get_database()
    collection_name = dbname[app_config['datastore']['db']]
    stats={
        "total_price": data['total_price'],
        "total_quantity": data['total_quantity'],
        "last_updated": data['last_updated']
    }
    collection_name.insert_one(stats)
    return 

def calculate_data(data):
    stats={
        "total_price":0,
        "total_quantity":0
    }
    if len(data) == 0:
        return stats

    total_price=0
    total_quantity=0
    for i in data:
        print(f"i in data {i}")
        total_price += float(i['price'])
        total_quantity += int(i["quantity"])

    stats['total_price'] = total_price
    stats['total_quantity'] = total_quantity
    return stats

def populate_stats():
    """ Periodically update stats """

    last_update=get_stats()["last_updated"]

    raw_data = requests.get(app_config['mysql']['url']+f"?timestamp={last_update}")
    processed_data = calculate_data(raw_data.json())

    mongo_data ={
        "total_price": processed_data['total_price'],
        "total_quantity": processed_data['total_quantity'],
        "last_updated": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    write_data(mongo_data)
    print(f"data insert{mongo_data}")


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yml", validate_responses=True)

with open('app_config.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

if __name__ == "__main__":
    init_scheduler()
    app.run(port=8100)