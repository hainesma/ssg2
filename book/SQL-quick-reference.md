# SQL Quick Reference

### Creating a database

    CREATE DATABASE DbName;

### Creating a table

    CREATE TABLE TableName (
        Id INT PRIMARY KEY IDENTITY(1,1),
        Column1 NVARCHAR(20),
        Column2 NVARCHAR(20),
        Column3 NVARCHAR(20)
    )

### Adding entries into a table

    INSERT INTO TableName 
    VALUES
    ('Column1 value', 'Column2 value', 'Column3 value'),
    