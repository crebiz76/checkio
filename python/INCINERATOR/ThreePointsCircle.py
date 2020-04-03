import math

def checkio(data):
    data = data.replace('(', '')
    data = data.replace(')', '')
    spoints = data.split(',')
    print(spoints)

    lpoints = []
    for i in spoints:
        lpoints.append(int(i))
    print(lpoints)

    ddots = {
	'x1':lpoints[0],
	'y1':lpoints[1],
	'x2':lpoints[2],
	'y2':lpoints[3],
	'x3':lpoints[4],
	'y3':lpoints[5]
    }
    print(ddots)

    tpoints = ((lpoints[0], lpoints[1]), (lpoints[2], lpoints[3]), (lpoints[4], lpoints[5]))
    print(tpoints)

    # for i in points:
    #     r = math.sqrt((3*x**2 -20*x + 3*y**2 -20*y + 44)/3)
    
    #replace this for solution
    return "" #"(x-{})^2+(y-{})^2={:0.2f}^2".format(a,b,r)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"