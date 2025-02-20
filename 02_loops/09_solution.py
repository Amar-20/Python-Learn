#unique item checker, print if any of the item is duplicate.

item=['apple','banana','mango','apple','berry']
unique_item=set()
for i in item:
    if i in unique_item:
        print('Duplicate:', i)
        break
    unique_item.add(i)