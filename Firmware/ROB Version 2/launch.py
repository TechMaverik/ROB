import socket
import ujson
import configurations
from wifi_con import WifiCon
from motion_planner import MotionPlanner

WifiCon().connect()


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

    if method == "POST" and path == "/rob/move/":
        data = parse_json_from_request(request)
        if data:
            response_data = {
                "success": True,
                "received": data,
                "message": "Move command received and processed",
            }
            response = configurations.OK_HEADER + ujson.dumps(response_data)
            MotionPlanner().move_robot(delay=0.001, payload=data)
        else:
            response = configurations.BAD_HEADER + ujson.dumps(
                {"error": "Invalid JSON"}
            )

    elif method == "GET" and path == "/":
        response_data = {
            "device": "Rob Robotic Arm",
            "version": 2.0,
            "status": "Ready",
        }
        response = configurations.OK_HEADER + ujson.dumps(response_data)

    else:
        response = configurations.BAD_HEADER + ujson.dumps(
            {"error": "Unsupported method or path"}
        )

    cl.send(response)
    cl.close()
