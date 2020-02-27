from country import Country
class CountryCatalogue:
#I am Robin Hylands.  This is my assignment 4 part 2.

    def __init__(self, data, continents):
        self._countryData = open(data, "r")
        self._continentData = open(continents, "r")
        self._countryCat = {}
        self._cDictionary = {}
        #these are the data structues that will be used throughout the program.

        _countryLines = self._countryData.readlines()
        _continentLines = self._continentData.readlines()

        del _countryLines[0]
        del _continentLines[0]
        #This deletes title of data columns, which is not needed.

        for indCountries in _continentLines:
            countryValues = indCountries.split(",")
            self._cDictionary[countryValues[0]] = countryValues[1]
        #This builds the cDictionary dictionary.

        for indLines in _countryLines:
            countryElements = indLines.split("|")
            country = Country(countryElements[0])
            country.setPopulation(int(countryElements[1]))
            country.setArea(float(countryElements[2]))
            _name = country.getName()
            if _name in self._cDictionary:
                country.setContinent(self._cDictionary[_name])
            else:
                country.setContinent("No continent data for this country. \n")

            self._countryCat[countryElements[0]] = country
        #This sets the values of the country object, and adds it to the dictionary.

        self._countryData.close()
        self._continentData.close()


    def countryFinder(self, countryName):
        if countryName in self._countryCat:
            return self._countryCat[countryName]
        else:
            return None


    def setPopulationOfCountry(self, countryName, newPop):
        if countryName in self._countryCat:
            self._countryCat[countryName].setPopulation(newPop)
            return True
        else:
            return False


    def setAreaOfCountry(self, countryName, newArea):
        if countryName in self._countryCat:
            self._countryCat[countryName].setArea(newArea)
            return True
        else:
            return False


    def addCountry(self, countryName, pop, area, continent):
        if countryName in self._countryCat and countryName in self._cDictionary:
            return False
        elif countryName in self._countryCat:
            self._cDictionary[countryName] = continent
            return True
        else:
            newCountry = Country(countryName)
            newCountry.setPopulation(pop)
            newCountry.setArea(area)
            newCountry.setContinent(continent)
            self._countryCat[countryName] = newCountry
            if countryName not in self._cDictionary:
                self._cDictionary[countryName] = continent
            return True
        #This builds a country object from the parameters, and appends it to the list in cDictionary.


    def deleteCountry(self, countryName):
        if countryName in self._countryCat:
            del self._countryCat[countryName]
        if countryName in self._cDictionary:
            del self._cDictionary[countryName]


    def printCountryCatalogue(self):
        print(self._countryCat)


    def getCountriesByContinent(self, continent):
        _countryList = []
        for elements in self._cDictionary:
            if self._cDictionary[elements] == continent + "\n":
                _countryList.append(elements)
        if len(_countryList) == 0:
            return False
        else:
            return _countryList


    def filterCountriesByPopDensity(self, low, high):
        _countryList =[]
        for item in self._countryCat:
            countryPop = self._countryCat[item].getPopDensity()
            if low <= countryPop <= high:
                _countryList.append([item, countryPop])
        return sorted(_countryList, key = lambda x: x[1])
    #This iterates through countryCat and checks the population density.
    # If it is within the range, it appends it to a new list, and returns a sorted version of that list.


    def saveCountryCatalogue(self, filename):
        _countryList = []
        for countryNames in self._countryCat:
            countries = self._countryCat[countryNames]
                
            _name = countries.getName()
            _continent = countries.getContinent()
            _pop = str(countries.getPopulation())
            _area = str(countries.getArea())
            _popDensity = str(countries.getPopDensity())

            if _continent == None:
                _continent = "No continent data.  Try deleting and re-adding this country with continent data."

            countryData = _name + "|" + _continent + "|" + _pop + "|" + _area + "|" + _popDensity
            _countryList.append(countryData)

        _countryList = sorted(countryList)
        # This formats the data, and appends it to a list, which is then sorted.

        file = open(filename, "w")
        _count = 0
        for elements in _countryList:
            file.write(elements + "\n")
            _count += 1
        file.close()
        if _count == 0:
            _count = -1
        return _count

