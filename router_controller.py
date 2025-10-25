import socketio
import threading
import time

# Create a SocketIO client to connect to each region server
regions = {
    "asia": "http://127.0.0.1:5001",
    "europe": "http://127.0.0.1:5002",
    "us": "http://127.0.0.1:5003"
}

clients = {}
current_region = 0
region_keys = list(regions.keys())

# Connect to each region server
def connect_regions():
    for region, url in regions.items():
        sio = socketio.Client()

        @sio.event
        def connect():
            print(f"✅ Connected to region {region}")

        @sio.on('message')
        def handle_message(data):
            print(f"[{region.upper()}] {data}")

        sio.connect(url)
        clients[region] = sio
        time.sleep(1)

# Simulate load balancing by routing messages round-robin
def route_message(msg):
    global current_region
    region = region_keys[current_region]
    clients[region].send(f"[ROUTED to {region}] {msg}")
    current_region = (current_region + 1) % len(region_keys)

if __name__ == "__main__":
    print("🌐 Router Controller started...")
    connect_regions()

    while True:
        msg = input("Enter a message to route (or 'quit'): ")
        if msg.lower() == "quit":
            break
        route_message(msg)
