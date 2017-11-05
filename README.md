# Udacity Project 3 - Logs Analysis

A simple Python project for Udacity's full-stack nanodegree program. The program connects to an SQL database, runs 3 queries, and prints
the results on the console.

## Download

The files for this program may be downloaded or cloned from https://github.com/cecilenguyen/LogsAnalysis.

Use the following command in the command terminal:

`$ git clone https://github.com/cecilenguyen/LogsAnalysis.git`

## System Requirements
Installation instructions can be found on their respective sites.

- [Python 3.6.3](https://www.python.org/downloads/) or later
- [Git](https://git-scm.com/downloads)
- [Vagrant](https://www.vagrantup.com)
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

## Quick Start

After downloading or cloning the program files, navigate to the directory folder.

`$ cd <C:\Directory\files\downloaded\to>`

Use the following command to see all files in directory:

`$ ls`

You should see all the following files: 
- README.md
- news.py
- news_output.txt
- newsdata.sql

**Environment set up**
Start Vagrant VM by running the command `vagrant up` and then log in using `vagrant ssh`

Then load the data using `psql -d news -f newsdata.sql`

**Run the program using the following command:**

`python3 news.py`

## The database
To explore the tables in the news database, run `psql -d news` and you will be able to directly run SQL commands in the terminal. 

The news database contains 3 tables with the following schemas: 
### Articles

| Column |           Type           |
|--------|--------------------------|
| author | integer                  |
| title  | text                     |
| slug   | text                     |
| lead   | text                     |
| body   | text                     |
| time   | timestamp with time zone |
| id     | integer                  |

### Authors
| Column |  Type   |                 
|--------|---------|
| name   | text    |
| bio    | text    |
| id     | integer |

### Log
| Column |           Type           |         
|--------|--------------------------|
| path   | text                     |
| ip     | inet                     | 
| method | text                     | 
| status | text                     | 
| time   | timestamp with time zone | 
| id     | integer                  |

## Copyright and License

news database provided by Udacity




