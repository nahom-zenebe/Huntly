from jobspy import scrape_jobs
import pandas as pd


def scrape_all_jobs(search_term,location,sites,results_wanted):
    jobs = scrape_jobs(
        site_name=sites,
        search_term=search_term,
        location=location,
        results_wanted=results_wanted,
        hours_old=72  # last 3 days
    )

    return jobs