def salary_chart() -> str:
    return """
    {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Salary of Employee by Join Date'
    },
    subtitle: {
        text: 'Brought to you by the analytics department.'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date of Joining'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        name: {
            nameDescription: [['Martha', 'Stewart'], ['Blah', 'Yah']]
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Salary'
        },
        labels: {
            format: '${value}'
        },
        accessibility: {
            rangeDescription: 'Range: 1980 to 2018.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '${point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Salary',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
    """


def age_chart() -> str:
    return """
    {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Age of Employee by Year Joined'
    },
    subtitle: {
        text: 'Brought to you by the analytics department.'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Year of Joining'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 1980 to 2017'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Age'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 21 to 60.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Age',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
    """


def pie_chart() -> str:
    return NotImplemented
