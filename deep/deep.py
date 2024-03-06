print("What is the Answer to the Great Question of Life, the Universe, and Everything?")
resp = input("").strip()
if resp == "42" or resp.lower() == "forty two" or resp.lower() == "forty-two":
    print("Yes")
else:
    print("No")