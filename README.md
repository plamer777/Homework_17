## Homework 17 by using Flask, SQLAlchemy, RESTX and Marshmallow
This applications works with movie, director and genre tables from database by using SQLAlchemy package. There're different functions the application provides such as:

 - To get all movies
 - To get single movie by id 
 - To add new record in director and genre tables by provided json
 - To update records in director and genre tables by provided json
 - To delete any record in every table excepting movie
 ---
The project's structure:
 - schemas - classes to serialize and deserialize models
 - app - blueprints precesses /movies/, /directors/ and /genres/ routes'
 - configs - configuration file for Flask
 - dao - four DAOs to work with different tables in the database
 - tests - test files for API
 - data - JSON file to create the database
 - models - classes to work with SQLAlchemy
 - sources - there're Flask, SQLAlchemy and another instances in the file
 - utils - serving functions for tests and loading data
 - create_data.py - logic to create database by using JSON
 - requirements.txt - file with the project's dependencies
 - run.py - a main file to start the application
 - test.db - a database file
 - README.md - this file with app info
 ---
 The project was created in 03 November 2022 by Aleksey Mavrin
