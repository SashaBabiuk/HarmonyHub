CREATE DATABASE harmonyHub;
USE harmonyHub;
CREATE TABLE person (
    user_id integer  NOT NULL,
    username varchar(50)  NOT NULL,
    email varchar(50)  NOT NULL,
    password varchar(50)  NOT NULL,
    registration_date  date  NOT NULL,
    type_id integer NOT NULL,
    settings_id integer  NOT NULL,
    user_favorite_artist integer  NOT NULL,
    user_favorite_group integer  NOT NULL,
    PRIMARY KEY (user_id)
) ;

CREATE TABLE image (
    image_id integer  NOT NULL,
    image_type varchar(25)  NOT NULL,
    image  blob  NOT NULL,
    image_size varchar(25)  NOT NULL,
    image_ctgy varchar(25)  NOT NULL,
    image_name varchar(50)  NOT NULL,
    song_song_id integer  NOT NULL,
    PRIMARY KEY (image_id)
) ;