# artist-intersection
Final project for CS3200

## Overview
ArtistIntersection is a sample database to be used on an art commission and marketplace website. It has been crafted around three personas: `Artists`, who can create listings for their artwork on the platform. `Collectors`, who can browse artist listings and create artwork requests. `Admins`, who can view sensitive information on user profiles and suspend Artists, prohibiting them from uploading any more artwork.

## REST API and Appsmith Implementation
We designed the current REST routes to provide data that we use in an AppSmith application. To facilitate this, our `GET` routes query the database based on the route provided. We will often rename and cherry-pick columns that we want to display to be more user-friendly. This data is then converted to python dictionary object which is serialized as JSON so that it can be easily sent and interpreted by appsmith widgets.

Our appsmith project also leverages `JSON` objects defined within their web editor, which allows us to execute multiple routes when information is submitted, as well as perform additional input validation against information retrieved from a route. This is useful for when we want to leverage a `POST` route which creates a new piece of art, where we also want to re-run the query which lists an Artists's works so that the new item will be reflected without requiring the user to refresh the page. Additionally during this process, we can query the suspended Artist list to ensure that the artist is allowed to create art before sending the `POST` request.


## Docker backend
Our program involves two containers that run locally, specified by the `docker-compose.yml` file. This file manages two docker containers: an alpine container running python which runs our API, and a mysql container that's used to run the mysql database. In order to create sample data for us to use in our website design, we have created a `create_db.sql` file. We mount the `db_bootstrap/` folder to the sql container's init directory, which ensures that the `create_db.sql` file will automatically be run and its tables will be present with data when the mysql container starts. The API communicates with the database using flask's `flaskext.mysql` module.

Secret management is accomplished through docker secrets. The passwords are stored in secrets within the `secrets` directory and their filepaths are specified within `docker-compose`. This automatically mounts the secret files within the `/run/secrets` directory of both containers.

Finally, we use an ngrok instance to allow our API to be accessible to the appsmith instance.

We have a demo of our program and appsmith application located [here]().
