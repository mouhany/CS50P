grocery = {}

while True:
    try:
        item = input().upper().strip()
        if item not in grocery:  
            # Initialize item's quantity in grocery
            grocery[item] = 1
        else:  
            # Update item's quantity
            grocery[item] = grocery[item] + 1
    except EOFError:
        sorted_dict = dict(sorted(list(grocery.items())))
        for item in sorted_dict:
            print(sorted_dict[item], item, sep=" ")
        break
    except KeyError:
        pass