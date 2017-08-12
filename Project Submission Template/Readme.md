## Description

The primary motivation of Build Peoria is to connect citizens to their built environment for the purposes of transparent information dissemination, make traversing roads, sidewalks, and bike trails in the City come with ease, voice their ‘gripes,’ and help City staff prioritize possible future infrastructure improvements.

This application is developed by the Urban Unicorn LLC.

## Screenshots

If possible, provide a couple screenshots of your project. You can use a tool like https://monosnap.com/welcome or https://droplr.com to take a screenshot. Animated gifs are also welcome.

## Data/APIs used

We only used a subset of the provided data just to keep things simple. However, we did transform the data and merge them into one set in `website\db.sqlite3` inside of the table 'peoria_project'
We merged and transformed the data into a table that has latitude, longitude, type, description, and filename.

Type is construction type:

    PV = Pavement projects
    BK = bike path projects
    TC = trashcans
    RA = Ramps
    SW = sidewalks

Latitude and longitude are the centroids of the project if they are not already point values
    
Filename is the geojson filename of the source data.

id is just the primary key.

*To run the application:*

`git clone https://github.com/urban-unicorns/peoriacivichackathon2017`

`cd website`

`python manage.py runserver`

## Dependencies

+ Python 3+
+ Django
+ geopy
+ git


## Team Members

+ [Ry Whittington](https://github.com/orgs/urban-unicorns/people/rwhitt2049)
+ [Austin Aldag](https://github.com/orgs/urban-unicorns/people/ama296)
+ [Ryan Rigato](https://github.com/orgs/urban-unicorns/people/rrigato)
+ [Balmes Tejeda](https://github.com/orgs/urban-unicorns/people/BalmesTejeda)
+ [Nghi Nguyen](https://github.com/orgs/urban-unicorns/people/mnghinguyen)
+ [Chris Nebergall](https://github.com/orgs/urban-unicorns/people/topher96)
