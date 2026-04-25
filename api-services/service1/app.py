from flask import Flask
import logging
import random

app = Flask(__name__)
logging.basicConfig(filename='service1.log', level=logging.INFO)

@app.route('/')
def home():
    val = random.randint(0, 100)
    logging.info(f'Home accessed, value={val}')
    return {"message": "Service1 running", "value": val}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
