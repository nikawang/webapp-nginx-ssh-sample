from flask import Flask, jsonify
import os
import logging
import json

app = Flask(__name__)

@app.route('/env')
def env():
    env_vars = dict(os.environ)
    env_v = jsonify(env_vars)
    env_v_str = json.dumps(env_vars)
    logger = logging.getLogger('my_logger')
    logger.info(env_v_str)
    return env_v

if __name__ == '__main__':
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)

    # 创建一个handler，用于将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 定义handler输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(file_handler)
    logger.addHandler(console_handler) 
    logger.info("App started")
    app.run(host='0.0.0.0', port=80)

