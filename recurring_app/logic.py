from recurring_app.data.transaction import Transaction 

def identify_recurring_transactions(transactions):
    sorted_transactions = sorted(transactions, key=lambda x: x.amount)
    print(sorted_transactions)
    groupedLists = group_by_amount(sorted_transactions)
    print(groupedLists)
    for group in groupedLists:
        # Iterate through transactions and find difference in time between each transaction and previous
        find_time_delta(group)
    return []


def group_by_amount(transactions):
    groupedLists = {}
    for transaction in transactions:
        if transaction.description not in groupedLists:
            groupedLists[transaction.description] = [transaction]
        else:
            groupedLists[transaction.description].append(transaction)
    return groupedLists

def find_time_delta(transactions):
    common_time_delta = {}
    # Current maximum
    current_max = 0
    for i in range(len(transactions)):
        if i >= 1:
            # Find time delta between each pair of transactions, and use this to detemine if there is a regularly occuring time delta
            time_difference_from_last = transactions[i].timestamp - transactions[i-1].timestamp 
            if common_time_delta[time_difference_from_last.total_seconds()] not in common_time_delta:
                common_time_delta[time_difference_from_last.total_seconds()] = 0
                # TODO: save the pair of transactions in tuple alongside the time delta
            else:
                common_time_delta[time_difference_from_last.total_seconds()] += 1
            if common_time_delta[time_difference_from_last.total_seconds()] > current_max:
                current_max = common_time_delta[time_difference_from_last.total_seconds()]
            # TODO: persist transactions in pairs and based on current max (most common time delta), return only the transactions that share this time delta (these are the recurring transactions)
    return []
        