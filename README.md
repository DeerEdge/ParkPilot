# ParkPilot

```
create table PARK_NAMES
(
    ID             SERIAL
        primary key,
    NAME           VARCHAR(200)  not null,
    DESCRIPTION    VARCHAR(2000) not null,
    STATE          VARCHAR(50)   not null,
    CITY           VARCHAR(50)   not null,
    TYPE           VARCHAR(50)   not null,
    WEBSITE        VARCHAR(500),
    LATITUDE       NUMERIC(11, 8),
    LONGITUDE      NUMERIC(11, 8),
    IMAGE_LINK_SRC VARCHAR(50000)
);
```
