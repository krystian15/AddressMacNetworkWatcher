import datetime
import time
import ciso8601
from datetime import datetime


def get_current_date_timestamp() -> int:
    return int(time.mktime(ciso8601.parse_datetime(datetime.today().strftime('%Y-%m-%d')).timetuple()))


def is_new_day(prev_timestamp: int) -> bool:
    return  bool(get_current_date_timestamp() != prev_timestamp)
