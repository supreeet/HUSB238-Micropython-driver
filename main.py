import time
from machine import Pin, I2C
import husb238

i2c = I2C(1, scl=Pin(27), sda=Pin(26))


pd_output = husb238.main(i2c)
print(pd_output[0] , 'V,  ', pd_output[1] , 'A, ', pd_output[2] , 'W')
time.sleep_ms(248)

