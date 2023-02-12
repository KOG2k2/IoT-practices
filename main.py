import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_AI import *

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"];
AIO_USERNAME = "Rumin2k2";
AIO_KEY = "aio_Ntml66e0OaDztrJ43u7VvS8rsNEb";

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
    print("Nhan du lieu:" + payload + " feed id:" + feed_id);

client = MQTTClient(AIO_USERNAME, AIO_KEY);
client.on_connect = connected;
client.on_disconnect = disconnected;
client.on_message = message;
client.on_subscribe = subscribe;
client.connect();
client.loop_background();

counter = 10;
sensor_type = 0;
AI_counter = 5;
AI_result = "";
previous_result = "";
 
while True:
    counter = counter - 1;
    if counter <= 0:
        counter = 10;
        print("Random data is published");
        if sensor_type == 0:
            print("temp =")
            temp = random.randint(10,20);
            client.publish("cambien1", temp);
            sensor_type = 1
        elif sensor_type == 1:
            print("humid = ")
            humi = random.randint(50,70);
            client.publish("cambien2", humi);
            sensor_type = 2
        elif sensor_type == 2:
            print("light = ");
            light = random.randint(100, 500);
            client.publish("cambien3", light);
            sensor_type = 0;
            
    AI_counter = AI_counter - 1;
    if AI_counter <= 0:
        AI_counter = 5;
        previous_result = AI_result;
        AI_result = image_detector();  
        if previous_result != AI_result:
            print("AI output: ", AI_result); 
            client.publish("AI", AI_result);
    time.sleep(1);