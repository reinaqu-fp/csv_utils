# -*- coding: utf-8 -*-
'''
Created on 22 oct 2021

@author: reinaqu_2
'''
import csv_joiner 

def main():
    csv_joiner.une_columnas_csvs("../data/hoteles.csv", "../data/hotels.csv", "../data/hoteles_joined.csv",
                                      encoding_1="utf-8", 
                                      encoding_2="utf-8")

if __name__=="__main__":
    main()