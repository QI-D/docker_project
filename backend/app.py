import connexion
import datetime
import json
import swagger_ui_bundle
import yaml
import logging
import logging.config
import uuid
import requests

from connexion import NoContent
from flask_cors import CORS


def placeOrder(body):
    trace_id = str(uuid.uuid4())
    body["trace_id"] = trace_id

    headers = {"content-type": "application/json"}
    response = requests.post(app_config['expenseEvent']['url'], json=body, headers=headers)
    logging.info(f'Reveived event expenseEvent request with a trace id of {trace_id}')
    logging.info(f'Returned event expenseEvent response {trace_id} with status {response.status_code}')

    return NoContent, 201


app = connexion.FlaskApp(__name__, specification_dir='')
CORS(app.app, resources={r"*": {"origins": "*", "headers": "*"}})
app.add_api("openapi.yml", strict_validation=True, validate_responses=True)

with open('app_config.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

with open('log_config.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)

logger = logging.getLogger('basicLogger')

if __name__ == "__main__":
    app.run(port=8080)
