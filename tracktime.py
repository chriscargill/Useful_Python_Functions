"""
Track how long it takes for a function to execute.
"""

from datetime import datetime
import os
import time

# Proper way of passing arguements to decorators. Use a wrapper function that gathers the args and kwargs
def TrackTime(func):
    """ A decorator that logs to a file in the ./logs/ folder the time it took to complete the work inside of the decorator."""
    
    def wrapper(*params, **k_params):
        try:
            start_time = datetime.now()
            try:
                decoratedFunc = func(*params, **k_params) # Still need to figure out how to get this function errors to bubble up
            except Exception as e1:
                pass
            end_time = datetime.now()
            took_time = end_time - start_time
            directory = os.path.dirname(os.path.abspath(func.__module__))
            directory = f"{directory}/logs/"
            if not os.path.exists(f"{directory}"):
                os.makedirs(f"{directory}")
            log_file = open(f"{directory}{func.__name__}_success.log", "a")
            log_file.write(f"{time.ctime()}: {func.__name__}({params},{k_params}) completed in {took_time}. Value Returned: {decoratedFunc}\n")
            log_file.close()
        except Exception as e:
            directory = os.path.dirname(os.path.abspath(func.__module__))
            directory = f"{directory}/logs/"
            if not os.path.exists(f"{directory}"):
                os.makedirs(f"{directory}")
            log_file = open(f"{directory}{func.__name__}_error.log", "a")
            log_file.write(f"{time.ctime()}: Error with {func.__name__}({params},{k_params}); ERROR: {str(e)}.\n")
            log_file.close()

    return wrapper
