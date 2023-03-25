from Adafruit_IO import MQTTClient
from uart import *

GETKEY = open("./key.txt", "r");
AIO_FEED_IDs = ["nutnhan1", "nutnhan2"];
AIO_USERNAME = GETKEY.readline().strip();
AIO_KEY = GETKEY.readline().strip();

def connected(client):
    print("Ket noi thanh cong");
    for topic in AIO_FEED_IDs:
        client.subscribe(topic);

def subscribe(client, userdata, mid, granted_qos):
    print("subscribe thanh cong");

def disconnected(client):
    print ("Ngat ket noi");
    sys.exit(1);
    
def message(client, feed_id, payload):
    print("Data From:" + feed_id + ":" + payload);
    
    if feed_id == "nutnhan1":
        if payload == 0:
            writeData("1");
        else:
            writeData("2");
            
    if feed_id == "nutnhan2":
        if payload == 0:
            writeData("3");
        else:
            writeData("4");
            
client = MQTTClient(AIO_USERNAME, AIO_KEY);
client.on_connect = connected;
client.on_disconnect = disconnected;
# client.on_message = message;
client.on_subscribe = subscribe;
client.connect();
client.loop_background();