# -*- coding: utf-8 -*-
'''
Created on 22 oct 2021

@author: reinaqu_2
'''
import csv_extractor 

def main():
    columnas_a_extraer=['retweet_count', 'favorited','retweeted', 'created_at', 'in_reply_to_user_id_str']
    csv_extractor.extrae_columnas_csv("../data/tweets_all.csv", 
                                      "../data/tweets_cut.csv",
                                      columnas_a_extraer)

if __name__=="__main__":
    main()