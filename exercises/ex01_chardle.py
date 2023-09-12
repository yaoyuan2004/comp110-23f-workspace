"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730713746"
x: str = input("Enter a 5-character word:")
if len(x) != 5:
    exit("Word must contain 5 characters")
y: str = input("Enter a single character:")
print("Searching for", y ,"in" ,x)

index: int = 0
times: int = 0
for letter in x:
    index = index+1
    if letter == y:
        print(y, "found at index",index)
        times = times+1
if times == 0:
    print ("No instances of", y ,"found in", x)
else:
    print(times, "instances of", y, "found in", x)