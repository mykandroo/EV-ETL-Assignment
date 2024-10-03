This repository is created as a public repository for an ETL project. It contains the zip file that includes all the files including .db, instructions in PDF format, Python script, and output expected in .csv format. Additionally, Python script and CSV file are uploaded directly for easy access.

Data (.db) Background:
  Company XYZ held a promo sale for their signature items named: x,y,z. Sales are at an all-time high, but they want to create a marketing strategy to target age groups of people by looking at total quantities purchased.
  They then created a database with these business rules:
    ● A sales receipt can have multiple items in an order.
    ● For every order, the clerk records all quantities for all items, including items not bought (which they denote with quantity=NULL).
    ● Each customer can do multiple sales transactions, and has his/her age stored in a database.

Python script has the following parts:
  1. Connecting to .db file.
  2a. Getting the result using SQL.
  2b. Getting the result using Pandas.
  3. Extracting the result to .csv.

Requirements:
  - Python should be installed and IDE should be used to run selection.
  - .db file should be save in local folder.

Instructions in Running the script:
  1. Update the location and filename of the .db in the upper part of the script.
  2. Run this and import the necessary libraries.
  3. Create a connection to the .db file by running the next part.
  4. Choose the preferred script if by SQL or Pandas and run it.
  5. Lastly, run the last part to save the result to .csv in your local folder where the .db file is in.


For any questions, reach out to mike.andrew@rocketmail.com.
