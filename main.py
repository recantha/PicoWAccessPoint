import socket
import network
import tinyweb
from machine import Pin
from utime import sleep

# Define SSID and password for the access point
ssid = "PicoW"
password = "123456789"

# Define an access point, name it and then make it active
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

# Wait until it is active
while ap.active == False:
    pass

print("Access point active")
# Print out IP information
print(ap.ifconfig())

# Define on-board LED
led = Pin("LED", Pin.OUT)

# Start up a tiny web server
app = tinyweb.webserver()

# Serve a simple Hello World! response when / is called
# and turn the LED on/off using toggle()
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page
    await response.send('<html><body><h1>Hello, world!</h1></body></html>\n')
    
    led.toggle()

# Run the web server as the sole process
app.run(host="0.0.0.0", port=80)
