# Import Libraries
import pandas as pd
from datetime import time, datetime, timedelta, date
import openpyxl

# Create dataframes from the daily report files
#   Dataframes based on Merchant Name/ID (MID) 
#       Restaurant  Data-Name       Merchant ID
#       Hachi-Ko    HACHI-KO        ZXJSAY8VNH38Y
#       Cafe Darte  CAFFE Dâ€™ARTE  3KQAXWG8WK961
#       La Pisa     LA PISA         60CH9N5ZRRQX1
hachi_mid = 'ZXJSAY8VNH38Y'
cafe_darte_mid = '3KQAXWG8WK961'
la_pisa_mid = '60CH9N5ZRRQX1'

# report_file_path = "C:\\Users\\kevin\\Downloads\\" + //(today's date)// <- need to figure out how to make the below filepath format
    # ex: "C:\\Users\\kevin\\Downloads\\DailyReport-AllStores_2020-08-12_2020-08-12.csv"

test_path = "C:\\Users\\kevin\\Downloads\\DailyReport-AllStores_2020-08-12_2020-08-12.csv"

concourse_df = pd.read_csv(test_path)

# print(concourse_df.columns)
hachi_df = concourse_df[concourse_df['Merchant ID'] == hachi_mid]
cafe_darte_df = concourse_df[concourse_df['Merchant ID'] == cafe_darte_mid]
la_pisa_df = concourse_df[concourse_df['Merchant ID'] == la_pisa_mid]

shops = [
        hachi_df,           # i == 0
        cafe_darte_df,      # i == 1
        la_pisa_df          # i == 2
        ]

for i in range(len(shops)):
    discount_10 = 0             # 10% discount for SeaTac general employees
    discount_40 = 0             # 40% discount for concourse employees
    discount_100 = 0            # 100% discount for managers
    discount_count = 0          # count of discounts given out 

    net_1 = 0                   # net sale amount without tax
    # net_2 = net_1 + tax
    # net_3 = net_2
    tax_total = 0               # total tax charged
    tips_total = 0

    cash_total = 0              # total amount tendered in CASH
    credit_card_total = 0       # total amount tendered by CARD
    visa_total = 0              
    mastercard_total = 0
    amex_total = 0
    disc_total = 0
    
    american_vouch = 0          # Vouchers for each airline
    southwest_vouch = 0
    hawaiian_vouch = 0
    northwest_vouch = 0
    delta_vouch = 0
    alaska_vouch = 0
    misc_vouch = 0              # vouchers that are Misc, spirit, or jet-blue
    gift_certificate = 0



    # Based on value of 'i', place stats into respective worksheet in Cash&Sales excel file.

    pass