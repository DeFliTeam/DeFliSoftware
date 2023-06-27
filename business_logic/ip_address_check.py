import os
import socket
import time
import logging
import requests


class IpChecker:
    def __init__(self):
        self.current_ip_address = '0.0.0.0'
        try:
            self.current_ip_address = self.get_current_public_ip()
        except requests.exceptions.ConnectionError as e:
            print("No Internet. Please check you connection.")
        self.server_ip_address = '162.255.85.52'
        self.loop_flag = True
        self.logger = logging.getLogger("IPChecker")
        self.folder_path = os.path.dirname(os.path.abspath(__file__))
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S', filename=os.path.join(self.folder_path, r'change.log'),
                            filemode='w')

    @staticmethod
    def get_current_local_ip():
        return socket.gethostbyname(socket.gethostname())

    @staticmethod
    def get_current_public_ip():
        endpoint = 'https://ipinfo.io/json'
        response = requests.get(endpoint, verify=True)

        if response.status_code != 200:
            return 'Status:', response.status_code, 'Problem with the request. Exiting.'
            exit()

        data = response.json()

        return data['ip']

    def set_current_ip(self, ip):
        self.current_ip_address = ip

    def check_for_ip_change(self):
        while self.loop_flag:
            try:
                new_ip = self.get_current_public_ip()
            except requests.exceptions.ConnectionError as e:
                continue
            if self.current_ip_address != new_ip:
                self.current_ip_address = new_ip
                self.update_ip_address()
            time.sleep(10)

    def update_ip_address(self):
        command = f"sudo netcat {self.current_ip_address} 30002 | {self.server_ip_address} 30001"
        self.logger.debug(command)
        print(command)
        os.system(command)

    def start_for_ip_address(self, ip):
        self.set_current_ip(ip)
        self.update_ip_address()
        self.check_for_ip_change()

    def stop_checker(self):
        self.loop_flag = False
