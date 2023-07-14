import datetime
import json
import uuid
from pathlib import Path

import requests

# from ..time.time_zone import get_current_date, get_yesterday_date

url = "https://clariti-health.com/rest/clariti/estimateapi/"
username = "hitechhealth4928"
password = "GD5_BJXpNj3Kp86%"

# today_date = get_current_date(tz = 'Asia/Kolkata')
# yesterday_date = get_yesterday_date(tz = 'Asia/Kolkata')
# target_date = yesterday_date
target_date = "2022-08-03" #On Monday we set it manually...but have to be automated

extracted_data_dir = Path("/home/ubuntu/tesing/extracted_data")
extracted_data_file_name = "all-in-one_v4.json"
extracted_data_file_path = extracted_data_dir / target_date / extracted_data_file_name

ocr_data_path = '/home/ubuntu/Extracted-data/all_patients_' + target_date + '.json'

api_request_response_dir = Path("/home/ubuntu/output/api_request_response_data")
api_request_response_file_name = "api_" + target_date + ".json"
api_request_response_file_path = api_request_response_dir / api_request_response_file_name


def get_response(output_file='api_response_file', **context):
  ti = context['task_instance']
  data = ti.xcom_pull(task_ids='process_files')
  with open('/home/ubuntu/src/utils/api_utils/server_inputV2_TEST.json', 'r') as f:
    json_data = json.load(f)

  get_payload = lambda v: {'Payload': {'Message': json_data['Message'], 'Patient': v, 'Errors': json_data['Errors']}}

  payload_response = {k: get_payload(v) for k, v in data.items()}

  for _, payload in payload_response.items():
    resp = requests.post(url,  json = payload['Payload'], auth = (username, password))
    payload['Response'] = json.loads(resp.text)

  with open(output_file, 'w') as f:
    json.dump(payload_response, f)

from prefect import task


# @task()
def get_response_vijay(data, output_file='api_response_file'):

  with open('/home/ubuntu/src/utils/api_utils/server_inputV2_TEST.json', 'r') as f:
    json_data = json.load(f)

  get_payload = lambda v: {'Payload': {'Message': json_data['Message'], 'Patient': v, 'Errors': json_data['Errors']}}

  payload_response = {k: get_payload(v) for k, v in data.items()}
  
  for _, payload in payload_response.items():
    # print(json.dumps(payload, indent = 4), "\n")
    payload['Payload']['Message']['createdatetimeutc'] = str(datetime.datetime.now())
    payload['Payload']['Message']['messageid'] = str(uuid.uuid4())
    # print(json.dumps(payload, indent = 4), "\n")    
    resp = requests.post(url,  json = payload['Payload'], auth = (username, password))    
    payload['Response'] = json.loads(resp.text)  

  with open(output_file, 'w') as f:
    print ("Dumping the API responses")
    json.dump(payload_response, f)

if __name__ == '__main__':
  # target_date = '2022-05-09'
  # extracted_data_file_path = extracted_data_dir + target_date + '/all-in-one_v4.json'
  with open(ocr_data_path, 'r') as f: #Insert the full path of json objects file here
    print (f'\n -----------------target_date: {target_date} ------------------\n')
    print("Opened json file \n")
    data = json.load(f)
    # print(data)    
    get_response_vijay(data, api_request_response_file_path)
    # get_response_vijay.run(data, api_request_response_file_path)
