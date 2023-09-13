"""
Module to hold library functions.
"""

import polars as pl


def load_forest_percent_cover():
    path = r"https://raw.githubusercontent.com/dhavalpotdar/Gapminder-World-Data-Analysis/master/data/forest_coverage_percent.csv"
    return pl.read_csv(path)


def aged_15_24_employment_rate_percent():
    path = r"https://raw.githubusercontent.com/dhavalpotdar/Gapminder-World-Data-Analysis/master/data/aged_15_24_employment_rate_percent.csv"
    return pl.read_csv(path)


def hdi_human_development_index():
    path = r"https://github.com/dhavalpotdar/Gapminder-World-Data-Analysis/blob/master/data/hdi_human_development_index.csv"
    return pl.read_csv(path)


def income_per_person_gdppercapita_ppp_inflation_adjusted():
    path = r"https://raw.githubusercontent.com/dhavalpotdar/Gapminder-World-Data-Analysis/master/data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    return pl.read_csv(path)


def life_expectancy_years():
    path = r"https://raw.githubusercontent.com/dhavalpotdar/Gapminder-World-Data-Analysis/master/data/life_expectancy_years.csv"
    return pl.read_csv(path)


def literacy_rate_adult_total_percent_of_people_ages_15_and_above():
    path = r"https://raw.githubusercontent.com/dhavalpotdar/Gapminder-World-Data-Analysis/master/data/literacy_rate_adult_total_percent_of_people_ages_15_and_above.csv"
    return pl.read_csv(path)


def master():
    path = r"https://raw.githubusercontent.com/dhavalpotdar/Gapminder-World-Data-Analysis/master/data/master.csv"
    return pl.read_csv(path)


def population_density_per_square_km():
    path = r"https://raw.githubusercontent.com/dhavalpotdar/Gapminder-World-Data-Analysis/master/data/population_density_per_square_km.csv"
    return pl.read_csv(path)
