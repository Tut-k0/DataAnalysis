import justpy as jp
import pandas as pd
from charts import salary_chart, age_chart, pie_chart

data = pd.read_csv('records.csv', parse_dates=['Date of Birth', 'Date of Joining',
                                               'Year of Joining'])
data_ordered = data.sort_values(by=['Date of Joining'])  # Ordering for the salary chart.
data_average = data.groupby(['Date of Joining']).median()
average_age = data_average.groupby(data_average.index.year).median()  # Aggregating for the age chart.

sc = salary_chart()
ac = age_chart()
pc = pie_chart()


def webapp():
    webpage = jp.QuasarPage()
    h1 = jp.QDiv(a=webpage, text="Chart Examples from CSV", classes="text-h3 text-center q-pb-sm")
    sc_hc = jp.HighCharts(a=webpage, options=sc)
    sc_hc.options.xAxis.categories = list(data_ordered['Date of Joining'].astype('str'))
    sc_hc.options.series[0].data = list(data_ordered['Salary'])
    ac_hc = jp.HighCharts(a=webpage, options=ac, classes="q-pt-md")
    ac_hc.options.xAxis.categories = list(average_age.index)
    ac_hc.options.series[0].data = list(average_age['Age in Yrs.'].round(0).astype('int'))
    #pc_hc = jp.HighCharts(a=webpage, options=pc)

    return webpage


jp.justpy(webapp)
