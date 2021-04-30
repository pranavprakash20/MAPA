import wikipedia

statement = "iphone"
results = wikipedia.summary(statement, sentences=3)
print(results)