
def main(i2c):

    pd_output = [0, 0, 0]
    try:
        i2c.writeto(0x8, b'\x00')
        pd_response = i2c.readfrom(0x8, 8)
        
        #print(', '.join('{:08b}'.format(byte) for byte in pd_response))
        byte_array = bytearray(pd_response)
        pd_voltage = [5, 9, 12, 15, 18, 20]
        pd_current = [0.5, 0.7, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5,
                      2.75, 3, 3.25, 3.5, 4, 4.5, 5]    
        available_voltage = []
        max_output = []
        x = []
        for i in range(2, 8):  
            byte = byte_array[i]
            if byte & 0b10000000:
                available_voltage.append(pd_voltage[i-2])
                x.append(i)
        
        max_output.append(pd_voltage[max(x)-2])
        max_output.append(pd_current[byte_array[max(x)] & 0b00001111])
        max_output.append(max_output[0]*max_output[1])

    except:
        return pd_output
    
    pd_output = max_output
    
    return pd_output

