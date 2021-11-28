import uuid
from datetime import datetime
import configparser

def create_log_message(msg):
    return {
        'uuid':  uuid.uuid4().hex,
        'is_consumed': False,
        'topic': msg['topic'],
        'published_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'content_format': msg['content_format'],
        'content': msg['content']
    }

def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_publish_message(data):
    return {
        'uuid':  uuid.uuid4().hex,
        'topic': data['topic'],
        'content_format': data['content_format'],
        'content': data['content']
    }


def get_connect_headers(sid, environ):
    return {
        'topic': environ['HTTP_TOPIC'],
        'output_format': environ['HTTP_OUTPUT_FORMAT'],
        'sid': sid
    }

def get_db_config():
    config = configparser.ConfigParser()
    config.read('simple-async-mq-server/database/db_config.ini')
    return config['database']
