# combien first digit and last digit
# sum them up
import re

def main():
    total_sum = 0
    file_path = './input.txt'
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming findFirstAndLastNumber returns a number
            res = findFirstAndLastNumber(line)
            total_sum += res

    print(total_sum)
# def edgeTest():
#     print(findFirstAndLastNumber(''))

def test():
    print(findFirstAndLastNumber('eightnine12ten'))

def determine_number_or_spelling(match):
    if match.isdigit():
        return int(match), "Number"
    elif match.lower() in {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'}:
        return int(match.lower()), "Spelling"
    else:
        return None, "Unknown"
    


def findFirstAndLastNumber(input_line):
    # Find all integers in the string
    digit_matches = re.findall(r'\d+', input_line)
    spelling_matches = re.findall(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten)\b', input_line, re.IGNORECASE)

    all_matches = digit_matches + spelling_matches
    
    print(all_matches, 'all')


    if all_matches:
        # Extract the first and last integers
        first_number = int(all_matches[0])
        if(determine_number_or_spelling(all_matches[0]) == "Number"):
            first_number = int(all_matches[0][0])

        last_number = int(all_matches[-1])
        
        if(determine_number_or_spelling(all_matches[0]) == "Number"):
            last_number = int(all_matches[-1][-1])

        combined_number = str(first_number) + str(last_number)
        print(combined_number)
        return int(combined_number)

test()