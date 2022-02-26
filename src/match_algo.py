import numpy as np
import pandas as pd


def rate_job(job_skillsets, job_ptraits, curated_job_listings):

    df = pd.DataFrame(curated_job_listings)
    #get rankings of skillsets
    #get rankings of personality traits

    #search for occurance of words in curated_job_listings

    #feed weightage (by ranking) as value 0-1, occurance as range
    #example_1 = [.9 for _ in range(5)] + [.84 for _ in range(4)] + [.52 for _ in range(2)]


    return final_job_listing


def lse(L):
    return np.log(sum(map(np.exp, L)))