import logging
from flask import request
from functools import wraps


def handle_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        app_logger = logging.getLogger("app_logger")
        try:
            # Try to decode json data
            request.get_json()
            result = func(*args, **kwargs)

            # Log info
            app_logger.info({"path": request.full_path})
            return {
                "code": 200,
                "data": result,
            }
        except Exception as error:
            # Log error
            app_logger.error({"error": str(error)})
            return {
                "code": 500,
                "error_message": "INTERNAL ERROR",
            }

    return wrapper
