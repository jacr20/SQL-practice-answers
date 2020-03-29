from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()

# Construct a reference to the "chicago_crime" dataset
dataset_ref = client.dataset("chicago_crime", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# List all the tables in the "hacker_news" dataset
tables = list(client.list_tables(dataset))

# Print names of all tables in the dataset (there are four!)
for table in tables:
    print(table.table_id)
num_tables = len(tables)
print(num_tables)

#create a pointer to a specific table:
# Construct a reference to the "full" table
table_ref = dataset_ref.table("crime")

# API request - fetch the table
table = client.get_table(table_ref)

# Now investigate the schema of the 'Full' table made reference to:
table.schema

table_ref = dataset_ref.table("crime")

# API request - fetch the table
table = client.get_table(table_ref)

client.list_rows(table, max_results=5).to_dataframe()
