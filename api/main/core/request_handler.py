from flask import request
from functools import wraps


def handle_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Try to decode json data
            request.get_json()
            result = func(*args, **kwargs)
            return {
                "code": 200,
                "data": result,
            }
        except Exception as error:
            # TODO: log this error
            return {
                "code": 500,
                "error_message": "INTERNAL ERROR",
            }

    return wrapper
