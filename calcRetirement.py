import calendar


def retirement(birthYear):
    if birthYear <= 1937:
        return 65, 0
    elif birthYear == 1938:
        return 65, 2
    elif birthYear == 1939:
        return 65, 4
    elif birthYear == 1940:
        return 65, 6
    elif birthYear == 1941:
        return 65, 8
    elif birthYear == 1942:
        return 65, 10
    elif 1943 <= birthYear <= 1954:
        return 66, 0
    elif birthYear == 1955:
        return 66, 2
    elif birthYear == 1956:
        return 66, 4
    elif birthYear == 1957:
        return 66, 6
    elif birthYear == 1958:
        return 66, 8
    elif birthYear == 1959:
        return 66, 10
    elif birthYear < 0:
        return -1
    elif birthYear > 2019:
        return -1
    else:
        return 67, 0


def calculate_retirement_date(birth_year, birth_month, age_years, age_months):
    year = birth_year + age_years
    month = birth_month + age_months

    if month > 12:
        year += 1
        month -= 12
    else:
        return year, calendar.month_name[month]


