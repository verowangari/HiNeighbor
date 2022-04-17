#### HiNeighbor
### Author

[Veronica Muriithi]

### Description
A Django web application that allows registered users to know about everything happening in their current neighborhoods. Members can also view business openings in their area.

![Screenreadme](https://user-images.githubusercontent.com/53782607/162088230-40298d9e-2bd2-49f1-a0ad-86cd0f319f0f.png)


![screenpost](https://user-images.githubusercontent.com/53782607/162088656-737740cd-44de-483a-bc7a-e20da8b9739b.png)


## Requirements
The user can perform the following functions:

-  A user can sign in with the application to start using.
-  A user can find a list of different businesses in their neighborhood.
-  A user can  view details of a single neighborhood.
-  A user can change their neighborhood when they decide to move out.
- A user can create posts that will be visible to everyone in the neighborhood.
- A user can find contact information for the health department and Police authorities near my neighborhood.


## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- cloudinary
- postgresql
- gunicorn
- django

## Technologies Used
- Python 3.8.10

- django-bootstrap3==21.2
- Django==4.0.3

## Project Setup Instructions
1) Git clone the repository 
```
https://github.com/verowangari/HiNeighbor.git
```
2. cd into  Neighbor
```
cd Neighbor
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate DB
```
py manage.py migrate
```
8. Run Application
```
py manage.py runserver
```

## Known Bugs
- There are no known bugs

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Contact Information 

If you have any question or contributions, please email me at [verowangari34@gmail.com]
© 2022 Veronica Muriithi