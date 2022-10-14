import datetime
import time
import zipfile
from datetime import timedelta
from io import BytesIO

import pandas as pd
import pytz
import requests

base_single_url_oasis = "http://oasis.caiso.com/oasisapi/SingleZip"
base_group_url_oasis = "http://oasis.caiso.com/oasisapi/GroupZip"

fetch_all = 0

node_id = "NCMETER_1_N001"
market_run_id = "DAM"
queryname = "PRC_LMP"
version = "1"
result_format = "6"


start_time = datetime.datetime(2021, 1, 1)
end_time = datetime.datetime(2021, 1, 2)

# Using American los angeles time
local = pytz.timezone("America/Los_Angeles")

oasis_request_time_format = "%Y%m%dT%H:%M-0000"

start_time = (
    local.localize(start_time, is_dst=None)
    .astimezone(pytz.utc)
    .strftime(oasis_request_time_format)
)
end_time = (
    local.localize(end_time, is_dst=None)
    .astimezone(pytz.utc)
    .strftime(oasis_request_time_format)
)

if fetch_all == 0:
    par = {
        "queryname": queryname,
        "startdatetime": start_time,
        "enddatetime": end_time,
        "version": version,
        "market_run_id": market_run_id,
        "node": node_id,
        "resultformat": result_format,
    }
else:
    par = {
        "queryname": queryname,
        "startdatetime": start_time,
        "enddatetime": end_time,
        "version": version,
        "market_run_id": market_run_id,
        "resultformat": result_format,
        "grp_type": "ALL",
    }

proxies = {
  'http': 'http://127.0.0.1:10818',
  'https': 'http://127.0.0.1:10828',
}

r = requests.get(base_single_url_oasis, params=par, proxies=proxies)
content = r.content
status = r.status_code
print(status)
zf = zipfile.ZipFile(BytesIO(r.content))

try:
    df = pd.read_csv(zf.open(zipfile.ZipFile.namelist(zf)[0]))
    zf.close()

    df = df[df["LMP_TYPE"] == "LMP"]

    df = df.sort_values("INTERVALSTARTTIME_GMT")
    df.reset_index()
    file_name = start_time + "_LMP.csv"

    df.to_csv(file_name)
    print(file_name + " saved")

except pd.errors.ParserError:
    print("parsing error, retring...")
