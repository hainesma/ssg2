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

### Adding rows to a table

    INSERT INTO TableName 
    VALUES
    ('Column1 value', 'Column2 value', 'Column3 value'),
    ('Column1 value', 'Column2 value', 'Column3 value')

To insert rows with only some of the values filled in, specify which columns the values are for after the name of the table.

    INSERT INTO TableName (Column1, Column3)
    VALUES
    ('Column1 value', 'Column3 value'),
    ('Column1 value', 'Column3 value')

### Deleting a row from a table

The `WHERE` keyword chooses a row or rows looking for where the specified column contains the specified value.

    DELETE FROM TableName
    WHERE Column1 = 'Column1 value'

### Updating a row

The `SET` keyword sets a new value for the specified column.

    UPDATE TableName
    SET Column3 = 'New Column3 value'
    WHERE Column1 = 'Column1 value' 

### Adding columns to a table

    ALTER TABLE TableName
    ADD Column4 NVARCHAR(20)

### Dropping an entire table

    DROP TABLE TableName