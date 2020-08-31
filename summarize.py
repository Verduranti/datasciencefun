import boto3
from botocore import UNSIGNED
from botocore.config import Config
import pandas as pd

# Utility function stolen from somewhere else in my libary of code
def bytes_2_human_readable(number_of_bytes):
    if number_of_bytes < 0:
        raise ValueError("!!! number_of_bytes can't be smaller than 0 !!!")

    step_to_greater_unit = 1024.

    number_of_bytes = float(number_of_bytes)
    unit = 'bytes'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'KB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'MB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'GB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'TB'

    precision = 1
    number_of_bytes = round(number_of_bytes, precision)

    return str(number_of_bytes) + ' ' + unit


# Public S3 buckets must be accessed with 'unsigned' requests
s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))

dataset = s3.Bucket('mozbi-sr-data-science')
# Don't pull data down without knowing something about it.
# Like how much of your cellular data it will absorb or whether it will fit in memory
for obj in dataset.objects.all():
    print(obj.key, obj.last_modified, bytes_2_human_readable(obj.size))

# Grab the files since they're not so big and just store them locally
# s3.Bucket('mozbi-sr-data-science').download_file('data/moz_customer_data_train.csv', 'train.csv')
# s3.Bucket('mozbi-sr-data-science').download_file('data/moz_customer_data_test.csv', 'test.csv')


train_df = pd.read_csv('./train.csv', parse_dates=True)
test_df = pd.read_csv('./test.csv', parse_dates=True)

# It is clear from the initial review of the data we will need to take some hygiene steps
# Data hygiene steps:
# 1. Industry types consolidated



