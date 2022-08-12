# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import random
import time

import psutil
from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest, Histogram, REGISTRY

logger = logging.getLogger(__name__)

app = Flask(__name__)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

number_of_requests = Counter(
    'number_of_requests',
    'The number of requests, its a counter so the value can increase or reset to zero.'
)

current_cpu_usage = Gauge(
    'current_pod_cpu_usage',
    'The current value of cpu usage, its a gauge so it can go up or down.',
    ['server_name']
)

PYTHON_REQUESTS_COUNTER = Counter("python_requests", "total requests")
PYTHON_FAILED_REQUESTS_COUNTER = Counter("python_failed_requests", "failed requests")
PYTHON_LATENCIES_HISTOGRAM = Histogram(
    "python_request_latency", "request latency by path"
)


@app.route('/metrics', methods=['GET'])
def get_data():
    """Returns all data as plaintext."""
    number_of_requests.inc()
    current_cpu_usage.labels('cpu_usage_sample').set(int(psutil.cpu_percent() * 10))
    return generate_latest(REGISTRY), 200


@app.route("/")
# [START monitoring_sli_metrics_prometheus_latency]
@PYTHON_LATENCIES_HISTOGRAM.time()
# [END monitoring_sli_metrics_prometheus_latency]
def homepage():
    # count request
    PYTHON_REQUESTS_COUNTER.inc()
    # fail 10% of the time
    if random.randint(0, 100) > 90:
        PYTHON_FAILED_REQUESTS_COUNTER.inc()
        # [END monitoring_sli_metrics_prometheus_counts]
        return ("error!", 500)
    else:
        random_delay = random.randint(0, 5000) / 1000
        # delay for a bit to vary latency measurement
        time.sleep(random_delay)
        return "home page"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
