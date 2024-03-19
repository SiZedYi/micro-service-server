import random
import string
import os
import py_eureka_client.eureka_client as eureka_client

server_port = 8000

def eureka_init():
    if os.environ.get("RUN_MAIN"):
        eureka_client.init(eureka_server="http://localhost:8761",
                        app_name="user_service",
                        instance_port=server_port,
                        instance_id=("DJANGO:user_service:" + str(server_port)))
        print("Eureka client is running")


def stop_eureka():
    if os.environ.get("RUN_MAIN"):
        eureka_client.stop()
        print("Stopping Eureka client")