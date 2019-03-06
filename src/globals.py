"""
This module contains all global variables.

------------------------------------------------------------------------
TODO: Remove test ROOT_DIR

"""


SCENARIO_CODES = {
    'business_as_usual_5%': '5BAU',
    'concentrated_20%': '20CONC',
    'dispersed_20%': '20DISP',
    'targeted_35%': '35TRGT'
}
FORECAST_CODES = {
    'actual': 'Pwr1HB',
    'forecast_one_hour': 'FcstHA',
    'forecast_four_hour': 'Fcst4HA',
    'forecast_six_hour': 'Fcst6HA',
    'forecast_one_day': 'FcstDA'
}

# ROOT_DIR = 'data'
ROOT_DIR = 'data/test'
PERIOD_DIRS = ['2008-2010']
SCENARIO_DIRS = [
    SCENARIO_CODES['business_as_usual_5%'],
    SCENARIO_CODES['concentrated_20%'],
    SCENARIO_CODES['dispersed_20%'],
    SCENARIO_CODES['targeted_35%']
]
FORECAST_DIRS = [
    FORECAST_CODES['actual'],
    FORECAST_CODES['forecast_one_hour'],
    FORECAST_CODES['forecast_four_hour'],
    FORECAST_CODES['forecast_six_hour'],
    FORECAST_CODES['forecast_one_day']
]
