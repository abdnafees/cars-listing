# Cars Listing

Cars Listing Take Home Project for Backend Engineering Mentorship

This is a Django based assignment. We have created a base project for you to work from. You are free to vary from our original base if you would like to. We provide it with the intention of providing a common base for all candidates to work from and to hopefully save you a bit of time.

We encourage you to use the Django Rest Framework for developing your API. This is a framework that we use extensively at Cars listing, and it provides some nice functionality out of the box. [Django Rest Framwork](https://www.django-rest-framework.org/)


## What to Build
We would like you to build an API that can be used to query some information about cars.
Sample data is provided in the `data` folder.
We have provided the stub for a Django command to import the data. Finish writing this code.
You should use Django's ORM to model the data and store it in a local database.
Then, utilize the Django Rest Framework to provide an API to query the models.
A very basic API design here would simply return all of the data available.
You can choose to improve and refine this very basic API design, and we encourage you to do so.
This will give us an opportunity to see how you approach API design.
If you are running out of time, you can outline how you would have done things differently given more time.


## How Will This Be Evaluated
We will use this project as our basis for our evaluation of your coding skill level as it relates to our team.
To do this, we will review your code with an eye for the following:

- Design Choices - choice of functionality, readability, maintainability, extendability, appropriate use of language/framework features
- Does it work as outlined
- Testing - have you considered how you'd test your code?
- Documentation - have you provided context around decisions and assumptions that you have made?
- Polish - have you produced something that would be ready to go into a production system?
  if not, have you clearly stated what would be needed to get from where it is to that level of polish?

## Time Expectations
We know you are busy and likely have other commitments in your life, so we don't want to take too much of your time.
We don't expect you to spend more than 2 hours working on this project. That being said, if you choose to put more or
less time into it for whatever reason, that is your choice. Feel free to indicate in your notes below if you worked on
this for a different amount of time and we will keep that in mind while evaluating the project. You can also provide us
with additional context if you would like to. Additionally, we have left a spot below for you to note. If you have ideas 
for pieces that you would have done differently or additional things you would have implemented if you had more time, 
you can indicate those in your notes below as well, and we will use those as part of the evaluation. For example, if you 
would have tested more, you can describe the tests that you would have written, and just provide 1 or 2 actual implemented
tests.

## Public Forks
We encourage you to try this project without looking at the solutions others may have posted. This will give the most
honest representation of your abilities and skills. However, we also recognize that day-to-day programming often involves 
looking at solutions others have provided and iterating on them. Being able to pick out the best parts and truly 
understand them well enough to make good choices about what to copy and what to pass on by is a skill in and of itself. 
As such, if you do end up referencing someone else's work and building upon it, we ask that you note that as a comment. 
Provide a link to the source so we can see the original work and any modifications that you chose to make. 

## Setup Instructions
1. Fork this repository and clone to your local environment.
1. Install a version of Python 3 if you do not already have one. We recommend Python 3.8 or newer.
1. You can use the built-in virtual environment creation within Python to create a sandboxed set of package installs. 
   If you already have a preferred method of virtualenv creation, feel free to proceed with your own method. 
   `python -m venv env`    
1. You will need to activate your virtual environment each time you want to work on your project. 
   Run the `activate` script within the `env/bin` folder that was generated.
1. We have provided a `requirements.txt` file you can use to install the necessary packages.
   With your virtualenv activated run: `pip install -r requirements.txt`
1. To run the django server run `python manage.py runserver`
1. To run the data import command run `python manage.py populate_cars`
1. You are now setup and ready to start coding. 


# Your Notes

## Time Spent
Approximately 5 hours were spent on the completion of this project. Time breakdown w.r.t the subtask:

Subtask | Restructuring repo and Dockerizing | Analysing data, creating Car model and implementing populate_cars.py | Adding Serizalizer and Views for Listing cars and performing CRUD operations on Home model | Adding Unittests | Documentation 
--- | --- | --- | --- |--- |--- 
Hours spent | 1 | 2 | 1 | 0.5 | 0.5 

## Assumptions
* Since the task requirement and project was initially setup for read-only users, listing cars feature work fine.
Create, Update and Delete operations are added but doesn't work as it would require setting up authentication process.
* As the code could be made production ready, instead of using virtual environment, the repository is restructured and dockerized.

## Next Steps

### Features
* Setting authentication and authorization process to allow users to perform complete CRUD operations on home instances.
* Update List API to enhance filtering options. For instance, users should be able to search according to range of MPG, Displacement and Horsepower as well by weight.
* Add pagination to List API endpoint to limit the number of results per page

### Testing
* Add tests for all crud operations and cover more scenarios for each endpoint

## How to Use

### Project Setup
1. Follow the instructions on https://docs.docker.com/install/ to install docker
2. Follow the instructions on https://docs.docker.com/compose/install/ to install docker compose
3. Create a `.env` file under *carslisting* directory and copy the contents from `.env.sample` in it. Contact the developer for credentials.
4. From the project root, `cd carslistings` and run the following command to start the application server: 
        `sudo docker compose up --build`
5. docker-compose will run entrypoint.sh that handles model migrations as well as running `populate_cars` script to populate `Car` table using `data/data.csv` 
6. The app will run locally at http://127.0.0.1:8000

### Interacting with API endpoints
In your browser, try the following URLs:

#### List All Homes
GET `http://127.0.0.1:8001/api/list-all-cars/`

