# ParkPilot

```
create table PARK_NAMES
(
    ID             SERIAL
        primary key,
    NAME           VARCHAR(200),
    DESCRIPTION    VARCHAR(2000),
    STATE          VARCHAR(50),
    CITY           VARCHAR(50),
    TYPE           VARCHAR(50),
    WEBSITE        VARCHAR(500),
    LATITUDE       NUMERIC(11, 8),
    LONGITUDE      NUMERIC(11, 8),
    IMAGE_LINK_SRC VARCHAR(50000)
);
```
