import requests
import sys

try:
    r = requests.get("http://localhost:8080/health", timeout=3)
    if r.status_code == 200:
        print("Service is healthy")
        sys.exit(0)
    else:
        print("System unhealty")
        sys.exit(1)
except Exception as e:
    print("Health check failed: ", e)
    sys.exit(1)
