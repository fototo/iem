---=========================================================================
--- Storage of Management
---
CREATE TABLE management(
    updated varchar,
    irrigationmethod varchar,
    residuebiomassmoisture varchar,
    organicamendments varchar,
    cropyear varchar,
    irrigation varchar,
    comments varchar,
    residueplantingpercentage varchar,
    residueremoval varchar,
    residuetype varchar,
    residuehow varchar,
    uniqueid varchar,
    residuebiomassweight varchar,
    limeyear varchar,
    organicamendmentstext varchar,
    irrigationamount varchar
);
GRANT SELECT on management to nobody,apache;

--- Storage of Pesticides
---
CREATE TABLE pesticides(
    target8 varchar,
    reference varchar,
    crop varchar,
    valid varchar,
    operation varchar,
    target6 varchar,
    comments varchar,
    target10 varchar,
    adjuvant varchar,
    product4 varchar,
    product3 varchar,
    product2 varchar,
    product1 varchar,
    target1 varchar,
    method varchar,
    updated varchar,
    cropyear varchar,
    pressure varchar,
    uniqueid varchar,
    target9 varchar,
    timing varchar,
    target7 varchar,
    target4 varchar,
    target5 varchar,
    target2 varchar,
    target3 varchar,
    stage varchar,
    totalrate varchar,
    target6_2 varchar,
    rate4 varchar,
    rate3 varchar,
    rate2 varchar,
    rate1 varchar,
    rateunit4 varchar,
    justify varchar,
    rateunit1 varchar,
    rateunit3 varchar,
    rateunit2 varchar
);
GRANT SELECT on pesticides to nobody,apache;

--- Storage of Operations
---
CREATE TABLE operations(
    valid date,
    uniqueid varchar,
    updated varchar,
    operation varchar,
    stabilizername varchar,
    zinc varchar,
    stabilizerused varchar,
    manuremethod varchar,
    productrate varchar,
    manurerateunits varchar,
    fertilizerform varchar,
    nitrogen varchar,
    manurerate varchar,
    currentph varchar,
    potash varchar,
    limerate varchar,
    planthybrid varchar,
    comments varchar,
    plantrate varchar,
    manurecomposition varchar,
    manuresource varchar,
    neutralindex varchar,
    terminatemethod varchar,
    stabilizer varchar,
    cropyear int,
    potassium varchar,
    fertilizerformulation varchar,
    sulfur varchar,
    phosphorus varchar,
    fertilizerapptype varchar,
    plantrateunits varchar,
    targetph varchar,
    calcium varchar,
    depth varchar,
    phosphate varchar,
    biomassdate2 date,
    magnesium varchar,
    iron varchar,
    biomassdate1 date
);
GRANT SELECT on operations to nobody,apache;

--- ========================================================================
--- Storage of Soil Nitrate Data
---
CREATE TABLE soil_nitrate_data(
  site varchar(24),
  plotid varchar(24),
  depth varchar(24),
  varname varchar(24),
  year smallint,
  value varchar(32),
  updated timestamptz default now()
);

CREATE TABLE soil_nitrate_data_log(
  site varchar(24),
  plotid varchar(24),
  depth varchar(24),
  varname varchar(24),
  year smallint,
  value varchar(32),
  updated timestamptz default now()
);

CREATE OR REPLACE FUNCTION soil_nitrate_insert_before_F()
RETURNS TRIGGER
 AS $BODY$
DECLARE
    result INTEGER; 
BEGIN
    result = (select count(*) from soil_nitrate_data
                where site = new.site and plotid = new.plotid and
                varname = new.varname and year = new.year and
                depth = new.depth and
                (value = new.value or (value is null and new.value is null))
               );

	-- Data is duplication, no-op
    IF result = 1 THEN
        RETURN null;
    END IF;

    result = (select count(*) from soil_nitrate_data
                where site = new.site and plotid = new.plotid and
                varname = new.varname and year = new.year
                and depth = new.depth);

	-- Data is a new value!
    IF result = 1 THEN
    	UPDATE soil_nitrate_data SET value = new.value, updated = now()
    	WHERE site = new.site and plotid = new.plotid and
                varname = new.varname and year = new.year and
                depth = new.depth;
        INSERT into soil_nitrate_data_log SELECT * from soil_nitrate_data WHERE
        		site = new.site and plotid = new.plotid and
                varname = new.varname and year = new.year and depth = new.depth;
        RETURN null;
    END IF;

    INSERT into soil_nitrate_data_log (site, plotid, varname, year, depth, value)
    VALUES (new.site, new.plotid, new.varname, new.year, new.depth, new.value);

    -- The default branch is to return "NEW" which
    -- causes the original INSERT to go forward
    RETURN new;

END; $BODY$
LANGUAGE 'plpgsql' SECURITY DEFINER;

CREATE TRIGGER soil_nitrate_insert_before_T
   before insert
   ON soil_nitrate_data
   FOR EACH ROW
   EXECUTE PROCEDURE soil_nitrate_insert_before_F();
  
CREATE UNIQUE index soil_nitrate_data_idx on 
	soil_nitrate_data(site, plotid, varname, year, depth);
GRANT SELECT on soil_nitrate_data to nobody,apache;



--- ==========================================================================
--- Storage of Agronomic Data
---
CREATE TABLE agronomic_data(
  site varchar(24),
  plotid varchar(24),
  varname varchar(24),
  year smallint,
  value varchar(32),
  updated timestamptz default now()
);

CREATE TABLE agronomic_data_log(
  site varchar(24),
  plotid varchar(24),
  varname varchar(24),
  year smallint,
  value varchar(32),
  updated timestamptz default now()
);

CREATE OR REPLACE FUNCTION agronomic_insert_before_F()
RETURNS TRIGGER
 AS $BODY$
DECLARE
    result INTEGER; 
BEGIN
    result = (select count(*) from agronomic_data
                where site = new.site and plotid = new.plotid and
                varname = new.varname and year = new.year and
                (value = new.value or (value is null and new.value is null))
               );

	-- Data is duplication, no-op
    IF result = 1 THEN
        RETURN null;
    END IF;

    result = (select count(*) from agronomic_data
                where site = new.site and plotid = new.plotid and
                varname = new.varname and year = new.year);

	-- Data is a new value!
    IF result = 1 THEN
    	UPDATE agronomic_data SET value = new.value, updated = now()
    	WHERE site = new.site and plotid = new.plotid and
                varname = new.varname and year = new.year;
        INSERT into agronomic_data_log SELECT * from agronomic_data WHERE
        		site = new.site and plotid = new.plotid and
                varname = new.varname and year = new.year;
        RETURN null;
    END IF;

    INSERT into agronomic_data_log (site, plotid, varname, year, value)
    VALUES (new.site, new.plotid, new.varname, new.year, new.value);

    -- The default branch is to return "NEW" which
    -- causes the original INSERT to go forward
    RETURN new;

END; $BODY$
LANGUAGE 'plpgsql' SECURITY DEFINER;

CREATE TRIGGER agronomic_insert_before_T
   before insert
   ON agronomic_data
   FOR EACH ROW
   EXECUTE PROCEDURE agronomic_insert_before_F();
  
CREATE UNIQUE index agronomic_data_idx on 
	agronomic_data(site, plotid, varname, year);
GRANT SELECT on agronomic_data to nobody,apache;