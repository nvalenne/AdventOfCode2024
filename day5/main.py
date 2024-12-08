import re

"""
Extract the data from the input text file
    Returns: 
        - rules (list[str]): List of all rules
        - updates (list[str]): List of all updates
"""
def read_data():
    with open("input.txt", "r") as f:
        data = f.readlines()
        rule_order_pattern = "[0-9][0-9][|][0-9][0-9]"
        rules = []
        updates = []
        for line in data:
            if re.match(rule_order_pattern, line):
                rules.append(line.strip("\n").split("|"))
            else:
                updates.append(line.strip("\n"))
    f.close()

    return rules, updates


"""
Return a boolean which determines if the pages updates are in the right order
    Parameters:
        update (list[str]): list of pages for one update
    Return: Boolean
"""
def is_right_order(update, rules):
    pages_printed = []
    for page in update:
        for rule in rules:
            # If it breaks the rule
            print(rule)
            if page == rule[1] and rule[0] not in pages_printed:
                return False
            

    return True
            

"""
First part of the day 5
    Parameters:
        updates (list[str]): List of all updates
        rules (list[str]): List of all rules
    Return: Sum of the middle page number from correctly-ordered updates
"""
def first_part(updates, rules):
    result = 0
    for update in updates:
        update = update.split(",")
        rules_for_update = []
        for rule in rules:
            if rule[0] in update or rule[1] in update:
                rules_for_update.append(rule)
        if is_right_order(update, rules_for_update):
            print(update[len(update)//2])
            # result += update[len(update)//2]

    return result  
    

if __name__ == "__main__":
    rules, updates = read_data()
    print(f"First part: {first_part(updates, rules)}")
