create sequence SEQ_MEASUREMENTLOG
    minvalue 0
    maxvalue 9223372036854775807
    start with 1
    increment by 1
    cache 1;


CREATE TABLE MEASUREMENTLOG
(
    id              numeric(10)            NOT NULL,
    key             character varying(100) NOT NULL,
    datetime        TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    status          numeric(2) NOT NULL,

    CONSTRAINT MEASUREMENTLOG_pkey PRIMARY KEY (id)
);