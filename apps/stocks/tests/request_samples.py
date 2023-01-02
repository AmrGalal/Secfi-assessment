Plan4YearsWithCliffRequest = {
    "option_grants": {
        "quantity": 4800,
        "start_date": "01-01-2018",
        "cliff_months": 12,
        "duration_months": 48
    },
    "company_valuations": [
        {
            "price": 10.0,
            "valuation_date": "09-12-2017"
        }
    ]
}

Plan4YearsWithoutCliffRequest = {
    "option_grants": {
        "quantity": 4800,
        "start_date": "01-01-2018",
        "cliff_months": 0,
        "duration_months": 48
    },
    "company_valuations": [
        {
            "price": 10.0,
            "valuation_date": "09-12-2017"
        }
    ]
}

Plan2YearsWithCliffAndMultipleEvaluationsRequest = {
    "option_grants": {
        "quantity": 1200,
        "start_date": "01-01-2018",
        "cliff_months": 0,
        "duration_months": 12
    },
    "company_valuations": [
        {
            "price": 10.0,
            "valuation_date": "09-12-2017"
        },
        {
            "price": 20.0,
            "valuation_date": "12-12-2018"
        }
    ]
}