from datetime import datetime

def generate_years_list():
    years = []
    for year in range(datetime.now().year, datetime.now().year + 5):
        years.append((year, year))
    return years