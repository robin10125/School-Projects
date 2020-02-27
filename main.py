from catalogue import CountryCatalogue
countryData = "text.txt"
continentData = "continent.txt"

data = CountryCatalogue(countryData, continentData)

data.setPopulationOfCountry("A",20)
data.setAreaOfCountry("A",1)
data.addCountry("Country",15,20,"OC")
data.deleteCountry("B")
data.printCountryCatalogue()

print("test", data.getCountriesByContinent("SA"))
print("test2", data.filterCountriesByPopDensity(0,100))

data.saveCountryCatalogue("newtextfile.txt")

print(data.countryFinder("A"))

