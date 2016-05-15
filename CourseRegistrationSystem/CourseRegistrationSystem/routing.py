from channels.routing import route
from Registration.consumers import ws_message
channel_routing = [
    route("websocket.receive", ws_message),
    # route("http.request", "Registration.consumers.http_consumer"),
]
