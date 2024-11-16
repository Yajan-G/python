from azure.iot.hub import IoTHubRegistryManager
import json
from time import sleep


deviceConnectionString = "HostName=koili-iot-staging.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=9u82CA6igMe4GjfkutU6E9iXtx8g333lTAIoTAImFc4="

registry_manager = IoTHubRegistryManager.from_connection_string(deviceConnectionString)

json_msg = {}
json_msg['broadcast_type'] = 1
json_msg['money'] = 100
json_msg['lang_Id'] = 0
json_msg['print_msg']= "<LS>0</LS> <CENTER> <LOGO> rintest </LOGO> </CENTER> \r\n   <FH> Koili 100 </FH>  \r\n\r\n DATE: %s  \r\n  <CENTER> <FS> SALE \r\n NPR %s \r\n APPROVED</FS> </CENTER>  \r\n\r\n payment initiator       <RIGHT>    NQR</RIGHT> \r\n Initiator ID    <RIGHT> +977984*******</RIGHT>\r\n \r\n APPROVAL CODE  <RIGHT>CIPS-39324730434</RIGHT> \r\n  <QR>https://koili.com.np/</QR>\r\n \r\n\r\n"
for i in range(1,5):
	json_msg['money'] = i * 10
	ret = registry_manager.send_c2d_message("MD23135", json.dumps(json_msg))
	print(ret)
	sleep(5)


