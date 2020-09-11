"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2
import pandas as pd

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    nsfg.CleanFemResp(df)
    return df


def ReadFemPreg(dct_file='2002FemPreg.dct',
                dat_file='2002FemPreg.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    return df

def validatePregNum(resp):
    preg = ReadFemPreg()

    pregmap = nsfg.MakePregMap(preg)

    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = pregmap[caseid]
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum);
            return False

    return True

def ReadFirstPregnancies(preg):
    first_pregs = preg[preg.pregnum==1]
    return first_pregs

def ReadEstoniaFile(file_name='ess9csee.sas7bdat'):
    sasdt = pd.read_sas(file_name)
    return sasdt

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()
    #print(validatePregNum(resp))

    preg = ReadFemPreg()
    first_pregs = ReadFirstPregnancies(preg)
    print(first_pregs.preglen.value_counts())

    #est = ReadEstoniaFile()
    #print(est)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
