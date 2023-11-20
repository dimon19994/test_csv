CREATE TABLE data
(
    id         SERIAL                   NOT NULL PRIMARY KEY,
    category   TEXT                     NOT NULL,
    first_name TEXT                     NOT NULL,
    last_name  TEXT                     NOT NULL,
    email      TEXT                     NOT NULL,
    gender     TEXT                     NOT NULL,
    birth_date TIMESTAMP WITH TIME ZONE NOT NULL
);

CREATE INDEX data_category ON data (category);
CREATE INDEX data_birth_date ON data (birth_date);
