# List of deal values (sales pipeline)
deal_values = [1200, 3000, 500, 8000]

# Indexing (fundamental concept)
print(deal_values[0])    # first deal
print(deal_values[-1])   # last deal

# Slicing (foundation for time-based analysis)
print(deal_values[0:2])  # first two deals
print(deal_values[1:])   # from the second deal onward
print(deal_values[:3])   # up to the third deal

# Mutability (critical for data manipulation)
deal_values[1] = 3500
print(deal_values)

# Essential list methods
deal_values.append(2000)   # add a new deal
deal_values.remove(500)    # remove a canceled deal
deal_values.sort()         # sort deal values

# Built-in functions frequently used in data analysis
print(len(deal_values))   # number of deals
print(sum(deal_values))   # total value
print(max(deal_values))   # highest deal
print(min(deal_values))   # lowest deal

# Real-world sales pipeline example
pipeline = [5000, 12000, 8000, 3000, 15000]

total_pipeline = sum(pipeline)
average_deal = total_pipeline / len(pipeline)

print("Total pipeline value:", total_pipeline)
print("Average deal size:", average_deal)
