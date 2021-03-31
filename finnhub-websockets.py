import json
import datetime
import websocket
from elasticsearch import Elasticsearch

es = Elasticsearch(
    cloud_id="finnhub-websockets-demo:d2VzdGV1cm9wZS5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJGZhNjcxMThjZjdhYjQyZTc5MTc2NDNiNjdhMTYzYTBhJGY3YjE0NmNlZjQ0NDQ3Nzc5Y2ZiNTJmYzM4YzEwZTJi",
    http_auth=("elastic", "UJWZc4pPDvYxLV770h62OVrQ"),
)

def on_message(ws, message):

    message_json = json.loads(message)
    message_json["@timestamp"] = datetime.datetime.utcnow().isoformat()
    res = es.index(index="websockets-data", body=message_json)
    print(message_json)

def on_error(ws, error):

    print(error)

def on_close(ws):

    print("### closed ###")

def on_open(ws):

    #ws.send('{"type":"subscribe","symbol":"COMMON:AAPL"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:ETHUSDT"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:AVAXUSDT"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:EGLDUSDT"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


if __name__ == "__main__":

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c0fallv48v6snrib6k0g",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
