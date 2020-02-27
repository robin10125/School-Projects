class Country:
#I am Robin Hylands, this is my assignment 4 part 1.

    def __init__ (self, name):
        self._name = name
        self._pop = None
        self._area = None
        self._continent = None
    #Initializes object variables

    def getName(self):
        return self._name


    def getPopulation(self):
        return self._pop


    def getArea(self):
        return self._area


    def getContinent(self):
        return self._continent


    def setPopulation(self, population):
        self._pop = population


    def setArea(self,area):
        self._area = area


    def setContinent(self, continent):
        self._continent = continent


    def getPopDensity(self):
        if self._pop and self._area != None:
            popDensity = float(self._pop / self._area)
            roundPopDensity = round(popDensity * 100) / 100
            return roundPopDensity
        else:
            return "Not enough data for calculating population density.  " \
                   "Try deleting this country and re-adding it with the area and population in the parameter"
    #Finds population density, and if not enough data is present for that calculation, it returns a string suggesting to add that data

    
    def __repr__(self):
        return str(self._name + "(population:" + str(self._pop) + ", size:" + str(self._area) + ") in " + str(self._continent)) 
    
    
