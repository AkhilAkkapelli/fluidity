from fluidity_tools import stat_parser
from numpy import zeros, arange, fromfile, ones, shape

def readstat_3d(filename="random_walk_agents.detectors", prefix='Steve_', do_padding=True):
    s = stat_parser(filename)

    last_locations_error = zeros((3,100))
    for i in range(100):
        n = i + 1
        padding = ''
        if(do_padding):
            if(n<100):
                padding = '0'
                if(n<10):
                    padding ='00'
        last_locations_error[0,i] = s[prefix+padding+str(n)]['position'][0][-1]
        last_locations_error[1,i] = s[prefix+padding+str(n)]['position'][1][-1]
        last_locations_error[2,i] = s[prefix+padding+str(n)]['position'][2][-1]
    X = fromfile('Xvals.txt',sep=' ')
    Y = fromfile('Yvals.txt',sep=' ')
    Z = 0.5*ones(shape(X))
    last_locations_error[0,:] = last_locations_error[0,:] - X
    last_locations_error[1,:] = last_locations_error[1,:] - Y
    last_locations_error[2,:] = last_locations_error[2,:] - Z 
    return last_locations_error

def initial_location_error(filename="random_walk_agents.detectors", prefix='Steve_', do_padding=True):
    """ Similar to readstat_3d, but calculating the distance to the initial position, 
        so we can check that the detectors have not been moved.
    """
    s = stat_parser(filename)

    first_locations_error = zeros((3,100))
    for i in range(100):
        n = i + 1
        padding = ''
        if(do_padding):
            if(n<100):
                padding = '0'
                if(n<10):
                    padding ='00'
        first_locations_error[0,i] = s[prefix+padding+str(n)]['position'][0][-1]
        first_locations_error[1,i] = s[prefix+padding+str(n)]['position'][1][-1]
        first_locations_error[2,i] = s[prefix+padding+str(n)]['position'][2][-1]

    x = 0.5+0.25*arange(0,100.)/100.
    y = zeros(100) + 0.5
    z = zeros(100) + 0.5
    first_locations_error[0,:] = first_locations_error[0,:] - x
    first_locations_error[1,:] = first_locations_error[1,:] - y
    first_locations_error[2,:] = first_locations_error[2,:] - z 
    return first_locations_error

