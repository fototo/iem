CREATE TABLE sm_daily (
  station char(5),
  valid date,
  TAir_C_Avg real,
  TAir_C_Max real,
  TAir_C_TMx timestamp with time zone,
  TAir_C_Min real,
  TAir_C_TMn timestamp with time zone,
  SlrMJ_Tot real,
  Rain_mm_Tot real,
  WS_mps_S_WVT real,
  WindDir_D1_WVT real,
  WindDir_SD1_WVT real,
  WS_mps_Max real,
  WS_mps_TMx timestamp with time zone,
  DailyET real,
  TSoil_C_Avg real,
  VWC_12_Avg real,
  VWC_24_Avg real,
  VWC_50_Avg real,
  EC12 real,
  EC24 real,
  EC50 real,
  T12_C_Avg real,
  T24_C_Avg real,
  T50_C_Avg real,
  PA real,
  PA_2 real,
  PA_3 real,
  T06_C_Avg real,
  VMW_06_Avg real
);
CREATE UNIQUE index sm_daily_idx on sm_daily(station, valid);
GRANT SELECT on sm_daily to nobody;

--- Soil Moisture Stations
CREATE TABLE sm_hourly (
  station char(5),
  valid timestamp with time zone,
  TAir_C_Avg real,
  RH real,
  SlrkW_Avg real,
  SlrMJ_Tot real,
  Rain_mm_Tot real,
  WS_mps_S_WVT real,
  WindDir_D1_WVT real,
  WindDir_SD1_WVT real,
  ETAlfalfa real,
  SolarRadCalc real,
  TSoil_C_Avg real,
  VWC_12_Avg real,
  VWC_24_Avg real,
  VWC_50_Avg real,
  EC12 real,
  EC24 real,
  EC50 real,
  T12_C_Avg real,
  T24_C_Avg real,
  T50_C_Avg real,
  PA real,
  PA_2 real,
  PA_3 real
);
CREATE UNIQUE index sm_hourly_idx on sm_hourly(station, valid);
GRANT SELECT on sm_hourly to nobody;


CREATE TABLE daily (
    station character varying(7),
    valid date,
    c11 real,
    c11_f character(1),
    c12 real,
    c12_f character(1),
    c20 real,
    c20_f character(1),
    c30 real,
    c30_f character(1),
    c40 real,
    c40_f character(1),
    c80 real,
    c80_f character(1),
    c90 real,
    c90_f character(1),
    c70 real,
    c70_f character(1),
    c110 real,
    c110_f character(1),
    c111 real,
    c111_f character(1),
    c509 real,
    c509_f character(1),
    c510 real,
    c510_f character(1),
    c1300 real,
    c1300_f character(1),
    c1301 real,
    c1301_f character(1),
    c900 real,
    c900_f character(1),
    c529 real,
    c529_f character(1),
    c530 real,
    c530_f character(1),
    c30h real,
    c30h_f character(1),
    c30l real,
    c30l_f character(1),
    c930 real,
    c930_f character(1)
);
CREATE UNIQUE INDEX daily_idx ON daily USING btree (station, valid);

CREATE TABLE hourly (
    station character varying(7),
    valid timestamp with time zone,
    c100 real,
    c100_f character(1),
    c200 real,
    c200_f character(1),
    c300 real,
    c300_f character(1),
    c400 real,
    c400_f character(1),
    c500 real,
    c500_f character(1),
    c600 real,
    c600_f character(1),
    c700 real,
    c700_f character(1),
    c800 real,
    c800_f character(1),
    c900 real,
    c900_f character(1)
);
CREATE UNIQUE INDEX hourly_idx ON hourly USING btree (station, valid);
