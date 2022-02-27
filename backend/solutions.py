def burgers(tons):
    return int(tons*500)

def flights(tons): #flights from London to New York
    return int(tons/2.7)+1

def trees(tons): #trees cut down//need to plant x trees to offset 
    return int(tons/1.2)+1

def drive(tons):
    return 1000*tons*9*2.4
  
def light(tons): #a 100w light bulb would need to burn for this many years 
    return int(tons/0.75)


def cars(tons): #equivalent weight in cars
    return int(tons/1.36)+1



def totalFootprint(elements):
    carbon = 0

    costs = {'ada': 0, 'btc':114, 'eth': 44, 'doge': 7.8, 'bch': 3.4, 'ltc': 3.2, 'etc': 1.7, 'xmr': 1, 'bsv': 0.5, 'dash': 0.5, 'zec': 0.5, 'sol': 0, 'xrp': 0}
    marketCaps =  {'ada':1, 'btc': 737, 'eth': 328, 'doge': 0.46, 'bch': 4.1, 'ltc': 0.7, 'etc': 0.4, 'xmr': 0.1, 'bsv': 0.073, 'dash': 0.141, 'zec': 0.163, 'sol': 1, 'xrp': 1} #in trillion


    
    for elem in elements:
        coin = elem[0]
        value = elem[2]

        marketShare = value/(marketCaps[coin]*10**9)
        carbonFoot = marketShare * costs[coin]

        carbon += carbonFoot 
    

    #200 eth, 200btc, 200doge

    
    return(carbon*233000)

#print(totalFootprint([['btc', 0.05, 1966], ['eth', 1, 2788], ['doge', 1, 1276]]))


def comparisions(tons):
    li = []
    li.append("eating "+ str(burgers(tons))+ " cheeseburgers")
    li.append("a 100kW light bulb burning for "+ str(light(tons))+ " years")
    li.append("taking "+ str(flights(tons))+ " flights from London to New York.")

    return li

def sol(tons):
    li = []

    li.append("plant "+ str(trees(tons))+" trees")
    li.append("donate "+ str(int(35*tons/12)+1)+ "$ per month to Biochar or a similar carbon-removing charity.")

    return li

def out(elem):
    tons = totalFootprint(elem)
    return (comparisions(tons), sol(tons), tons)


