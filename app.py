import requests
import random
import time
import logging
from configparser import ConfigParser

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("goblinmine.log"),
        logging.StreamHandler()
    ]
)

config = ConfigParser()
config.read("config.ini")

SECRET = str(config.get("AUTH", "SECRET"))

MIN_WAIT = 8*3600
MAX_WAIT = 11*3600

URL_COLLECT = 'https://backend.mun-team.ru/api/coins/collect'
URL_SUBMIT = 'https://backend.mun-team.ru/api/coins/submit'
HEADERS_COLLECT = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': SECRET,
    'Connection': 'keep-alive',
    'Host': 'backend.mun-team.ru',
    'Origin': 'https://frontend.mun-team.ru',
    'Referer': 'https://frontend.mun-team.ru/',
    'Sec-Ch-Ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
HEADERS_SUBMIT = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': SECRET,
    'Connection': 'keep-alive',
    'Content-Length': '18',
    'Content-Type': 'application/json',
    'Host': 'backend.mun-team.ru',
    'Origin': 'https://frontend.mun-team.ru',
    'Referer': 'https://frontend.mun-team.ru/',
    'Sec-Ch-Ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
DATA_SUBMIT = {"option_ids": [1]}

def main():
    while True:
        try:
            response_collect = requests.get(URL_COLLECT, headers=HEADERS_COLLECT)
            if response_collect.status_code == 200:
                text_collect = response_collect.text
                logging.info("Success! Claim executed successfully.")
                logging.info(f"Data: {text_collect}")
                if '"Да"' in text_collect:
                    response_submit = requests.post(URL_SUBMIT, headers=HEADERS_SUBMIT)
                    if response_submit.status_code == 200:
                        text_submit = response_submit.text
                        logging.info("Success! The question was answered.")
                        logging.info(f"Data: {text_submit}")
            else:
                logging.warning(f"Request failed with status code {response.status_code}: {response.text}")
            sleep_time = random.randint(MIN_WAIT, MAX_WAIT)
            logging.info(f"Sleeping for {sleep_time} seconds...")
            time.sleep(sleep_time)
        except requests.RequestException as e:
            logging.error(f"Network error: {e}")
            logging.info("Sleeping for 12 hours before retry...")
            time.sleep(43200)
        logging.info("- "*16)

if __name__ == "__main__":
    main()
