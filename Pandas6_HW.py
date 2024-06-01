#  Problem 1 : Delete Duplicate Emails 


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id',inplace=True)
    person.drop_duplicates(['email'], inplace=True)



# Problem 2 : The Number of Rich Customers


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store['amount'] > 500]
    richCount = len(set(df['customer_id']))
    return pd.DataFrame([richCount], Columns=['rich_count'])