"""
Examples of widget types

dict(type='date', name='date2', default='2012/03/15', label='Bogus2:',
     min="1893/01/01"), # Comes back to python as yyyy-mm-dd

"""
# Association of plots
data = {'plots': [
    {'label': 'Daily', 'options': [
        {'id': "108", 'mw': True,
         "label": "Accumulated Station Departures of Precipitation/GDD/SDD"},
        {'id': "11", 'label': "ASOS/AWOS Daily Min/Max Dew Point for a Year"},
        {'id': "94",
         "label": "Bias of 24 Hour High+Low Computation by Hour"},
        {'id': "96",
         "label": "Bias of 24 Hour Precipitation Computation by Hour"},
        {'id': "82",
         'label': "Calendar of Daily Observations from Automated Stations"},
        {'id': "32", 'label': "Daily Temperature Departures for One Year",
         'mw': True},
        {'id': "21",
         'label': "Change in NCDC 81 Daily Climatology over X Days"},
        {'id': "91", 'mw': True,
         "label": "Consecutative Day Statistics of High+Low Temps / Precip"},
        {'id': "66", 'mw': True,
         "label": ("Consecutative Days with High/Low Temp "
                   "Above/Below Threshold")},
        {'id': "31", 'mw': True,
         'label': "Extreme Jumps or Dips in High Temperature over X days"},
        {'id': "7", 'mw': True,
         'label': "Growing Degree Day Periods for One Year by Planting Date"},
        {'id': "61",
         'label': ("High/Low Temp above/below avg OR dry streaks "
                   "by NWS CLI Sites")},
        {'id': "19", 'mw': True,
         'label': "Histogram of Daily High/Low Temperatures"},
        {'id': "35", 'label': "Histogram of X Hour Temperature Changes"},
        {'id': "60", 'label': ("Hourly Temperature Frequencies "
                               "Above/Below Threshold")},
        {'id': "86", 'mw': True, 'label': "IEM Daily Reanalysis Plots"},
        {'id': "34", 'mw': True,
         'label': "Max Stretch of Days with High/Low Above/Below Threshold"},
        {'id': "26",
         'label': "Min Daily Low after 1 July / Max Daily High before 1 July"},
        {'id': "5", 'mw': True,
         'label': "Minimum Daily Temperature Range"},
        {'id': "126",
         'label': "Mixing Ratio Climatology and Yearly Timeseries Plot"},
        {'id': "84", 'mw': True,
         'label': "MRMS Q3 Estimated Precipitation (multiday summaries too)"},
        {'id': "22", 'mw': True,
         'label': ("Percentage of Years within Temperature Range "
                   "from Averages")},
        {'id': "83", 'mw': True,
         'label': ("Period Averages or Totals of X days around a "
                   "given day of the year")},
        {'id': "107", 'mw': True,
         'label': ("Period Statistics of Temp/Precip for a date period "
                   "each year")},
        {'id': "97", 'mw': True,
         "label": "Period Statistics for an Exact Stretch of Days"},
        {'id': "43",
         'label': "Recent (Past 2-3 Days) Timeseries (Meteogram)"},
        {'id': "62", 'mw': True,
         'label': "Snow Depth"},
        {'id': "38", 'mw': True,
         'label': "Solar Radiation Estimates from NARR"},
        {'id': "25", 'mw': True,
         'label': "Spread of Daily High and Low Temperatures"},
        {'id': "4", 'mw': True,
         'label': "State Areal Coverage of Precip Intensity over X Days"},
        {'id': "89", 'mw': True,
         'label': "State Areal Coverage/Efficiency of Precipitation"},
        {'id': "81", 'mw': True,
         'label': "Standard Deviation of Daily Temperatures"},
        {'id': "28", 'mw': True,
         'label': "Trailing Number of Days Precipitation Total Rank"},
        {'id': "132", 'mw': True,
         'label': "Top 10 Precip/Temperature Values by Month/Seaseon"},
    ]},
    {'label': 'Monthly', 'options': [
        {'id': "130", 'mw': True,
         'label': "Average High/Low Temperature with/without Snowcover"},
        {'id': "71", 'label': "Average Wind Speed and Direction for Month"},
        {'id': "125", 'mw': True,
         'label': "Climatological Maps of Annual/Monthly Averages"},
        {'id': "1", 'mw': True,
         'label': "Comparison of Multi-Month Totals/Averages"},
        {'id': "55", 'label': "Daily Climatology Comparison"},
        {'id': "17", 'label': "Daily High/Low Temps with Climatology"},
        {'id': "129", 'mw': True,
         'label': "Daily Observation Percentiles/Frequencies by Month"},
        {'id': "15", 'mw': True,
         'label': "Daily Temperature Change Frequencies by Month"},
        {'id': "98", 'mw': True,
         'label': "Day of Month Frequency of meeting temp/precip threshold"},
        {'id': '65', 'mw': True,
         'label': 'Day of the Month with the coldest/warmest temperature'},
        {'id': "29",
         'label': "Frequency of Hourly Temperature within Range by Month"},
        {'id': "9", 'mw': True, 'label': ("Growing Degree Day Climatology "
                                          "and Daily Values for one Year")},
        {'id': "2", 'mw': True,
         'label': "Month Precipitation v Month Growing Degree Day Departures"},
        {'id': "57", 'mw': True,
         'label': "Monthly Precipitation/Temperature Records"},
        {'id': "95", 'mw': True,
         'label': "Monthly Precipitation/Temperature with El Nino Indices"},
        {'id': "24", 'mw': True,
         'label': "Monthly Precipitation/Temperature Climate District Ranks"},
        {'id': "3", 'mw': True,
         'label': "Monthly Precipitation/Temperature Statistics by Year"},
        {'id': "6", 'mw': True,
         'label': "Monthly Precipitation/Temperature Distributions"},
        {'id': "42",
         'label': "Hourly Temperature Streaks Above/Below Threshold"},
        {'id': "85",
         'label': "Hourly Temperature Frequencies by Month"},
        {'id': "8", 'mw': True,
         'label': "Monthly Precipitation Reliability"},
        {'id': "23", 'mw': True,
         'label': "Monthly Station Departures + El Nino 3.4 Index"},
        {'id': "36", 'mw': True,
         'label': "Month warmer than other Month for Year"},
        {'id': "58", 'mw': True,
         'label': ("One Day's Precipitation Greater than X percentage "
                   "of Monthly Total")},
        {'id': "41", 'mw': True,
         'label': ("Quantile / Quantile Plot of Daily Temperatures "
                   "for Two Months")},
        {'id': "20", 'label': "Hours of Precipitation by Month"},
        {'id': "47", 'mw': True,
         'label': "Snowfall vs Precipitation Total for a Month"},
        {'id': "39", 'mw': True,
         'label': "Scenarios for this month besting some previous month"},
    ]},
    {'label': 'Yearly', 'options': [
        {'id': "76",
         'label': "Average Dew Point by Year or Season"},
        {'id': "125", 'mw': True,
         'label': "Climatological Maps of Annual/Monthly Averages"},
        {'id': "128", 'mw': True,
         'label': "Comparison of Yearly Summaries between two stations"},
        {'id': "99", 'label': "Daily High + Low Temperatures with Departures",
         'mw': True},
        {'id': "12", 'mw': True,
         'label': "Days per year and first/latest date above given threshold"},
        {'id': "74", 'mw': True,
         'label': ("Days per year by season or year with temperature "
                   "above/below threshold")},
        {'id': "13", 'mw': True,
         'label': "End/Start Date of Summer (warmest 91 day period) per Year"},
        {'id': "27", 'mw': True,
         'label': "First Fall Temp Below Threshold (First Freeze/Frost)"},
        {'id': "53", 'label': ("Hourly Frequency of Temperature within "
                               "Certain Ranges")},
        {'id': "10", 'mw': True,
         'label': ("Last Spring and First Fall Date "
                   "above/below given threshold")},
        {'id': '64', 'mw': True,
         'label': 'Last or First Snowfall of Each Winter Season'},
        {'id': "33", 'mw': True, 'label': "Maximum Low Temperature Drop"},
        {'id': "105", 'mw': True,
         'label': "Maximum Period between Precipitation Amounts"},
        {'id': "46", 'label': "Minimum Wind Chill Temperature"},
        {'id': "30", 'mw': True, 'label': "Monthly Temperature Range"},
        {'id': "44", 'label': "NWS Office Accumulated SVR+TOR Warnings"},
        {'id': "69", 'mw': True,
         'label': "Percentage of Days each Year Above Average"},
        {'id': "77", 'mw': True,
         'label': "Period between Last and First High Temperature for Year"},
        {'id': "75", 'mw': True,
         'label': "Precipitation Totals by Season/Year"},
        {'id': "63", 'mw': True,
         'label': "Records Set by Year (Max High / Min Low)"},
        {'id': "103", 'mw': True,
         'label': "Step Ups in High Temp / Step Downs in Low Temp by Year"},
        {'id': "100", 'mw': True,
         'label': "Temperature / Precipitation Statistics by Year"},
        {'id': "104", 'mw': True,
         'label': "Trailing X day temp/precip departures (weather cycling)"},
        {'id': "14", 'mw': True,
         'label': "Yearly Precipitation Contributions by Daily Totals"},
    ]},
    {'label': 'METAR ASOS Special Plots', 'options': [
        {'id': "78",
         'label': ("Average Dew Point/RH% by Air Temperature "
                   "by Month or Season or Year")},
        {'id': "79",
         'label': ("Average Dew Point by Wind Direction "
                   "by Month or Season or Year")},
        {'id': "40",
         'label': "Cloud Amount and Level Timeseries for One Month"},
        {'id': "88",
         'label': "Cloudiness Impact on Hourly Temperatures"},
        {'id': "59",
         'label': "Daily u and v Wind Component Climatologies"},
        {'id': "54",
         'label': ("Difference between morning low "
                   "or afternoon high temperature between two sites")},
        {'id': "87",
         'label': ("Frequency of METAR Code (Thunder, etc) "
                   "by week by hour")},
        {'id': "131",
         'label': ("Frequency of Overcast Clouds by Air Temperature "
                   "by month/season")},
        {'id': "93", 'label': "Heat Index Hourly Histogram"},
        {'id': "106",
         'label': "Hourly temp distributions on days exceeding temperature"},
        {'id': "18", 'label': "Long term temperature time series"},
        {'id': "45", 'label': "Monthly Frequency of Overcast Conditions"},
        {'id': "67",
         'label': "Monthly Frequency of Wind Speeds by Air Temperature"},
        {'id': "37",
         'label': "MOS Forecasted Temperature Ranges + Observations"},
        {'id': "16", 'label': "Wind Rose when specified criterion is meet"},
    ]},
    {'label': 'NASS Quickstats (USDA Crop Statistics)', 'options': [
        {'id': "127",
         'label': ("Crop Progress by Year")},
    ]},
    {'label': 'NWS Warning Plots', 'options': [
        {'id': "92",
         'label': "Days since Last Watch/Warning/Advisory by WFO"},
        {'id': "72",
         'label': "Frequency of Issuance time for Watch/Warning/Advisories"},
        {'id': "52",
         'label': "Gaant Chart of WFO Issued Watch/Warning/Advisories"},
        {'id': "102",
         'label': "Local Storm Report Source Type Ranks by Year"},
        {'id': "44",
         'label': "NWS Office Accumulated Warning/Warning/Advisories by Year"},
        {'id': "68",
         'label': "Number of Distinct Phenomena/Significance VTEC per Year"},
        {'id': "73",
         'label': "Number of Watch/Warning/Advisories Issued per Year"},
        {'id': "70",
         'label': "Period between First and Last VTEC Product Each Year"},
        {'id': "48", 'label': "Time of Day Frequency for Given Warning / UGC"},
        {'id': "80",
         'label': "Time Duration of a Watch/Warning/Advisory for a UGC"},
        {'id': "101",
         'label': "Top 25 Most Frequent VTEC Products by Office/NWS"},
        {'id': "56", 'label': "Weekly Frequency of a Watch/Warning/Advisory"},
        {'id': "109",
         'label': "WFO VTEC Event Counts for a Given Period (map)"},
        {'id': "90",
         'label': "UGC Statistics for Watch/Warning/Advisory by state/wfo"},
    ]},
    {'label': 'Sustainable Corn Project Plots', 'options': [
        {'id': "49", 'mw': True,
         'label': "Two Day Precipitation Total Frequencies"},
        {'id': "50", 'mw': True,
         'label': "Frequency of Measurable Daily Precipitation"},
        {'id': "51", 'mw': True,
         'label': "Frequency of No Daily Precipitation over 7 Days"},
    ]},
]}
