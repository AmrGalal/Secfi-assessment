from dateutil.relativedelta import relativedelta   
from datetime import datetime

def get_monthly_shares(start_date, duration_months, quantity, cliff_durations):
    """
        Get the shares the user will have at every single month during the whole duration
    """
    current_date = datetime.strptime(start_date, '%d-%m-%Y').date()
    last_date = current_date + relativedelta(months=duration_months)
    monthly_increment = quantity/duration_months
    initial_value = 0
    response = []
    while current_date <= last_date:
        entry = {
            "date": current_date.strftime('%d-%m-%Y'),
            "total_value": initial_value
        }
        if cliff_durations:
            entry['total_value'] = 0
            cliff_durations -= 1
        initial_value += monthly_increment
        current_date += relativedelta(months=1)
        response.append(entry)
    
    return response

def get_last_price_for_share(company_valuations, share_date):
    """
        Get the price for the share at a specific time
    """
    result = company_valuations[0]["price"]
    for valuation in company_valuations:
        if valuation["valuation_date"] <= share_date:
            result = valuation["price"]
    return result

def calculate_monthly_valuations(company_valuations, monthly_shares):
    """
        Multiply each share with its price to get the valuation
    """
    for share in monthly_shares:
        share["total_value"] *= get_last_price_for_share(company_valuations, share["date"])
    return monthly_shares

def calculate_vested_equity_over_time(request_data):
    """
        Fetch the response needed for the endpoint
    """
    monthly_shares = get_monthly_shares(
        request_data['option_grants']['start_date'],
        request_data['option_grants']['duration_months'],
        request_data['option_grants']['quantity'],
        request_data['option_grants']['cliff_months']
    )
    company_valuations = sorted(
        request_data['company_valuations'],
        key=lambda d: d['valuation_date']
    )
    monthly_valuations = calculate_monthly_valuations(company_valuations, monthly_shares)
    return {
        "results": monthly_valuations
    }