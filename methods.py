
def dayOfWeek(date_str):
    '''Date format 2025-11-23'''
    from datetime import datetime

    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # Get day of the week
    day_of_week = date_obj.strftime("%A")
    return day_of_week