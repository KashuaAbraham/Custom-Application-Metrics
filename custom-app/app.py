from prometheus_client import start_http_server, Summary, Counter, Gauge
import random
import time

# Create metrics to track
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNTER = Counter('request_count', 'Number of requests')
IN_PROGRESS = Gauge('in_progress_requests', 'Number of requests in progress')

# Decorate function with metric
@REQUEST_TIME.time()
def process_request():
    IN_PROGRESS.inc()
    REQUEST_COUNTER.inc()
    time.sleep(random.random())
    IN_PROGRESS.dec()

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request()
