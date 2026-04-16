-- Insert files from folder into database as tables
-- This script creates tables based on CSV files in the directory

-- Example: Load CSV files using BULK INSERT (SQL Server) or LOAD DATA (MySQL)
-- Adjust syntax based on your database system

-- For SQL Server:

create TABLE time_series_stats (
    id INT PRIMARY KEY,
    timestamp DATETIME,
    value FLOAT
);
BULK INSERT [dbo].[time_series_stats]
FROM '/Users/gauravkumardani/Documents/ml-code-samples/handson-ml3/fraud/time_series_stats.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

-- For PostgreSQL:
-- COPY table_name FROM '/path/to/file.csv' WITH (FORMAT csv, HEADER);

-- For MySQL:
-- LOAD DATA INFILE '/path/to/file.csv' INTO TABLE table_name FIELDS TERMINATED BY ',';