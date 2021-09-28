---
title: Database-First Approach to Entity Framework Core
tags: .Net, Entity Framework
author: Mark Haines
date: 9/28/2021
---
Test change
Test2

Entity Framework maps models in a .Net project to tables in a SQL database, allowing us to manipulate the database from within our .Net app.

There are two approaches to setting up an EF Core project: 
1) Create the database and tables first. Then use EF Core to scaffold the database and generate the models and database context.
2) Write the models and database context first in C#. Then use EF Core to migrate the database.

For this project, I will use the database-first approach. There are two reasons for this. One, I find that it's faster to write the SQL query than to write the C# models. But more importantly, it saves a lot of work to have Entity generate the database context, which manages the connection to the database.


## Steps
1. Create SQL database and tables
2. Create a new ASP.NET Core project
3. Install EF Core packages
4. Scaffold the database
5. Set up DbContext service in Startup.cs
6. Create database controller


### Install EF Core packages



Open the NuGet package manager