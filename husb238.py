def main(i2c):
    pd_output = [0, 0, 0]
    try:
        i2c.writeto(0x8, b'\x00')
        pd_response = i2c.readfrom(0x8, 8)
        
        pd_voltage = [5, 9, 12, 15, 18, 20]
        pd_current = [0.5, 0.7, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5,
                      2.75, 3, 3.25, 3.5, 4, 4.5, 5]    

        max_index = -1
        for i in range(2, 8):
            if pd_response[i] & 0b10000000:
                max_index = i

        if max_index != -1:
            voltage = pd_voltage[max_index - 2]
            current = pd_current[pd_response[max_index] & 0b00001111]
            pd_output = [voltage, current, voltage * current]

    except:
        pass

    return pd_output
