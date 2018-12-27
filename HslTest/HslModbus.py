import HslCommunication as hsl
import time

print(time.asctime( time.localtime(time.time()) ))
busTcpClient=hsl.ModbusTcpNet("192.168.1.195")

readf=busTcpClient.ReadFloat("100").IsSuccess

print(readf)
print(time.asctime( time.localtime(time.time()) ))