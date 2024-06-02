# Playlist Data Management API

This project is a Django-based RESTful API for managing playlist data. It provides endpoints for loading playlist data from a JSON file, fetching playlist details, and updating star ratings.

## Technologies Used

- Django: A high-level Python web framework for building web applications.
- Django Rest Framework (DRF): A powerful and flexible toolkit for building Web APIs in Django.

<pre>

viv_takehome/
│
├── api_manager/
│ ├── migrations/
├── data/
│ │   └── playlist.json
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── urls.py
│ └── views.py
├── manage.py
└── viv_takehome/
├──-- init.py
├──---settings.py
├──-- urls.py
└──-- wsgi.py

</pre>

- `api_manager/`: Django app containing models, views, serializers, and URL configurations.
- `playlist.json`: JSON file containing playlist data.
- `manage.py`: Django's command-line utility for administrative tasks.
- `viv_takehome/`: Django project directory containing project settings and URL configurations.

## Database Used

This project uses the default SQLite database provided by Django for simplicity. It can be changed based on requirements.

## API Endpoint Details

- **Load Playlist Data**: `POST /v1/preprocess/load-playlist-data/`
  - Description: Endpoint for loading playlist data from the JSON file into the database.
- **Fetch all Playlist Detail**: `GET /v1/api/playlist-data`
  - Description: Endpoint for fetching all playlist details.
  - Method: GET
  - Parameters:
    - `page`: Page number
    - `page_size`: Number of items per page
- **Fetch Playlist Detail**: `GET /v1/api/playlist-data/field`
  - Description: Endpoint for fetching playlist details based on the a field,currently only takes title.
  - Method: GET
  - Query Param:
    - `title`: Title of the playlist
- **Update Star Rating**: `PATCH /v1/api/playlist-data/field`
  - Description: Endpoint for updating the star rating of a playlist based on a field, currently supported title.
  - Method: PATCH
  - Query Param:
    - `title`: Title of the playlist
  - Request Body:
    - `star_rating`: Star rating value to be updated


## Installing Requirements

1. Navigate to the project directory:

cd viv_takehome

2. Install the required packages using pip:

pip install -r requirements.txt

## Running the Server

1. Ensure you are in the project directory:

cd viv_takehome

2. Run the Django development server:
    python manage.py runserver

It will run on 8000 as default port