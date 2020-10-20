import os
import json
import requests


def main():
    filename = "last-ip.json"
    last_ip = get_last_ip(filename)
    current_ip = get_external_ip()
    print(last_ip)
    print(current_ip)
    if current_ip != last_ip:
        print("New IP")

        save_ip(current_ip, filename)
    else:
        print("Same IP")    


def get_last_ip(filename:str) -> str:
    if not os.path.isfile(filename):
        return "0.0.0.0"
    with open(filename) as json_file:
        data = json.load(json_file)
        return data['last_ip']


def save_ip(ip:str, filename:str):
    with open(filename, 'w') as json_file:
        json.dump({'last_ip': ip}, json_file)


def get_external_ip() -> str:
    # See https://stackoverflow.com/a/36205547
    return requests.get("https://api.ipify.org").text


if __name__ == '__main__':
    main()
