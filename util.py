import math, pygame, settings, sys, numpy

def greysacle(red: int=None, green: int=None, blue: int=None, red_mult: float=0.3, green_mult: float=0.6, blue_mult: float=0.1):
    output = ()

    if red is not None:
        output += ((red * red_mult), )
    else:
        output += (0, )

    if green is not None:
        output += ((green * green_mult), )
    else:
        output += (0, )

    if blue is not None:
        output += ((blue * blue_mult), )
    else:
        output += (0, )


    return output if output != () else None

def brightness(red: int=0, green: int=0, blue: int=0):
    '''
    returns the sum of its 1st, 2nd and 3rd arguments.
    '''
    try:
        return red + green + blue
    except TypeError:
        print (f"Error: Red ({red}), Green ({green}) and Blue ({blue}) must all be compatible datatypes!")
        if settings.sys_traceback_quit:
            sys.exit()

def euclid_distance(x: int=1, y: int=1, Tx: int=1, Ty: int=1):
    return math.sqrt((x - Tx) ** 2 + (y - Ty) ** 2)

def quantize(value, levels: int=10):
    value = numpy.clip(value, 0, 255)

    step_jump = 255 // (levels - 1)
    steps = [(x * step_jump) for x in range(levels)]
    closest = min(steps, key=lambda x: abs(x - value))
    return closest
