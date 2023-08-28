import json

input_file_path = '../jikan-metadata.json'
new_data_file_path = '../newData.json'
output_file_path = 'jikan-data.json'

# Load the JSON data from the input file
with open(new_data_file_path, 'r') as input_file:
    data = json.load(input_file)

roman_to_value = {
    "null": 1,
    "I": 1,
    "II": 0.9,
    "III": 0.85,
    "IV": 0.75,
    "V": 0.65
}

freq_map = {}

filtered_data = []

for item in data:
    tier = item.get("Tier")  # Use .get() to avoid KeyError
    mint = item.get("Mint")

    if tier is not None and tier != "null":
        filtered_item = {
            "Mint": mint,
            "Tier": roman_to_value.get(tier, 1)  # Default to 1 if tier not in roman_to_value
        }

        freq_map[tier] = freq_map.get(tier, 0) + 1
        filtered_data.append(filtered_item)

# Write the filtered data to the output JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(filtered_data, output_file, indent=4)

def sum_freq_map(freq_map):
    total_sum = 0
    for value in freq_map.values():
        total_sum += value
    return total_sum

print("Filtered data has been written to", output_file_path)
print("------------")
print("Final Counts")
print(freq_map)
# print(sum_freq_map(freq_map))