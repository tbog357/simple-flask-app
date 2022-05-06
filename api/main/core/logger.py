import logging
import json


class JsonLoggingFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def format(self, record: logging.LogRecord):
        dict_record = {
            "message": record.msg,
            "time": record.created,
            "level": record.levelname,
            "file": record.filename,
            "func": record.funcName,
            "module": record.pathname,
        }
        record.msg = json.dumps(dict_record, sort_keys=True)
        return super().format(record)


