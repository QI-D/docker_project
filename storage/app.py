import connexion
import datetime
import json
import yaml
import logging
import logging.config

from connexion import NoContent
from base import Base
from expense import Expense
from user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS

with open('app_config.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

database=app_config['datastore']

DB_ENGINE= create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(database['user'],database['password'],database['hostname'],database['port'],database['db']))
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)


def placeOrder(body):

    trace_id = body['trace_id']
    session = DB_SESSION()

    expense = Expense(body['order_id'],
                      body['item_id'],
                      body['item_name'],
                      body['quantity'],
                      body['price'],
                      body['timestamp'],
                      trace_id)

    session.add(expense)

    session.commit()
    session.close()

    logger.info(f'Stored event expenseEvent with a trace id of {trace_id}')

    return NoContent, 201

def getExpense(timestamp):

    session = DB_SESSION()
    timestamp_datetime = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    expenses = session.query(Expense).filter(Expense.date_created >= timestamp_datetime)

    results_list = []
    for expense in expenses:
        results_list.append(expense.to_dict())
    print(results_list)

    session.close()
    logger.info("Query for get expenses after %s returns %d results" % (timestamp, len(results_list)))

    return results_list, 200

def get_user(username):
    session = DB_SESSION()
    readings = session.query(User).filter(User.username == username)
    result=[]
    for i in readings:
        result.append(i.to_dict())
    session.close()
    
    if len(result) == 0:
        return "user doesn't exist"
    else:
        return result, 200

def write_user(body):

    session = DB_SESSION()
    print(body)
    user = User(  
            body['username'],
            body['password'],
            )

    session.add(user)

    session.commit()
    session.close()

    return NoContent, 201


app = connexion.FlaskApp(__name__, specification_dir='')
CORS(app.app, resources={r"*": {"origins": "*", "headers": "*"}})
app.add_api("openapi.yml", strict_validation=True, validate_responses=True)

with open('log_config.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger('basicLogger')

if __name__ == "__main__":
    app.run(port=8090)
