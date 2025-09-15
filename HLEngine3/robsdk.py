import requests
import json


class RobSDK:

    def robot_position(self, payload, rob_url):
        feedback = requests.post(rob_url, json=payload)
        return feedback.json()
