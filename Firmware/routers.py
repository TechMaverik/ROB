import socket
import ujson
import time
import configurations
from wifi_con import WifiCon
from motion_planner import MotionPlanner

WifiCon().connect()
MotionPlanner().set_default_position()


def parse_json_from_request(request):
    try:
        body = request.split("\r\n\r\n", 1)[1].strip()
        return ujson.loads(body)
    except:
        return None


addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

while True:
    cl, addr = s.accept()
    request = cl.recv(2048).decode()
    try:
        method, path, _ = request.split(" ", 2)
    except ValueError:
        continue

    if method == "POST" and path == "/router/move/":
        data = parse_json_from_request(request)
        if data:
            response_data = {
                "success": True,
                "received": data,
                "message": "Move command received and processed",
            }
            response = configurations.OK_HEADER + ujson.dumps(response_data)
            MotionPlanner().software_feedback_control_system(final_position=data)
        else:
            response = configurations.BAD_HEADER + ujson.dumps(
                {"error": "Invalid JSON"}
            )
    else:
        response = configurations.BAD_HEADER + ujson.dumps(
            {"error": "Unsupported method or path"}
        )

    cl.send(response)
    cl.close()
