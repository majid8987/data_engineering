lenght_string = ['milk','eggs','bread','butter','cheese','vegetables','fruits','chicken','rice']
C=[ls.upper() for ls in lenght_string]
longest_string = max(lenght_string)
shortest_string= min(lenght_string)

print(C)
print(longest_string)
print(shortest_string)
j= " ".join(lenght_string[0:10])
print(j)
