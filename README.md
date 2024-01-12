### Identifying Repeatable Tranactions:

Naive Approach:

- An assumption that can be made about the transactions is that transactions with similar amounts will likely be related and therefore can be grouped to determine if they have any cadence to their timestamps
- If we group transactions by amount we can find the time delta between transactions and check if there are any common time deltas which is an indicator of recurring transactions
- Time based:
    - On a regular cadence, e.g. monthly or weekly or daily or at a specific timing
    - If time based and reliant on business days then a regular cadence might need to take into account holidays or weekends, but this can be a later consideration


### Running the application
Use the following command: 
poetry run flask --app recurring_app/app run