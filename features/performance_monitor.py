import time
import logging

logging.basicConfig(level=logging.INFO)

def monitor_response_time(func):
    """Decorator to log function response time."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Response time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

# @monitor_response_time
# def sample_function():
#     time.sleep(1)
#     return "Done"

# if __name__ == "__main__":
#     result = sample_function()
#     print(result)