# handler.py
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpld3

def main(event, context):
    
    PERF_DATA = pd.read_csv('https://res.cloudinary.com/harip/raw/upload/v1520830685/timeseries.csv')

    # Read column names and ignore Group column
    COL_NAMES = [colname for colname in PERF_DATA.columns.values if "Age_" in colname]

    # get average values for each column as a series
    AVG_VALUES = pd.Series([PERF_DATA[col_name].mean() for col_name in COL_NAMES])


    FIG, AX = plt.subplots(nrows=1, ncols=1)
    AVG = AX.twiny()

    # plot series
    AVG_VALUES.plot(kind='line', grid=True, ylim={0, 100})
    #plt.show()
    HTML=mpld3.fig_to_html(FIG)
    # print(HTML)
    return {
        'statusCode': '200',
        'body': HTML,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        } 
    }

if __name__ == "__main__":
    main('', '')