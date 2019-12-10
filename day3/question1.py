from index import getData, getResult

data = getData()
result = getResult(data["firstWire"], data["secondWire"])
print("Manhattan Distance: ", result["manhattanDistance"])
