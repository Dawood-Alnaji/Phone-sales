import numpy
import math


def Mobile(L):
    screen_size, battery_capacity, camera_quality = L

    if (4.5 > screen_size > 7):
        return -9999999999
    
    if (2000 > battery_capacity > 5000):
        return -9999999999
    
    if (8 > camera_quality > 108):
        return -9999999999

    estimated_price = 100 + (0.07 * screen_size) + (0.035 * battery_capacity) + (2.1 * camera_quality)

    if estimated_price > 500:
        return -9999999999

    popularity = 5.5* screen_size + 18.5* battery_capacity + 25.8 * camera_quality
    
    return -popularity

def Mobile1(L):
    screen_size, battery_capacity, camera_quality = L

    if (4.5 > screen_size > 7):
        return -9999999999
    
    if (2000 > battery_capacity > 5000):
        return -9999999999
    
    if (8 > camera_quality > 108):
        return -9999999999

    estimated_price = 100 + (0.07 * screen_size) + (0.035 * battery_capacity) + (2.1 * camera_quality)

    if estimated_price > 500:
        return -9999999999

    popularity = 159303.4861* screen_size + 550.0096* battery_capacity + 13397.5191* camera_quality

    if popularity<0:
        return -9999999999
    
    return -popularity




def getFunctionDetails(a):
    # [name, lb, ub, dim]
    param = {
        "Mobile": ["Mobile", [4.5, 2000, 8], [7, 5000, 108], 3],
        "Mobile1": ["Mobile1", [4.5, 2000, 8], [7, 5000, 108], 3]
    }
    return param.get(a, "nothing")
