# Import Libraries
import pandas as pd
from datetime import time, datetime, timedelta, date
import openpyxl
from decimal import *
# getcontext().prec = 2
# getcontext().rounding = ROUND_HALF_UP
with localcontext() as ctx:
    ctx.prec = 20
    ctx.rounding = ROUND_HALF_UP

# Create dataframes from the daily report files
#   Dataframes based on Merchant Name/ID (MID) 
#       Restaurant  Data-Name       Merchant ID
#       Hachi-Ko    HACHI-KO        ZXJSAY8VNH38Y
#       Cafe Darte  CAFFE Dâ€™ARTE  3KQAXWG8WK961
#       La Pisa     LA PISA         60CH9N5ZRRQX1
hachi_mid = 'ZXJSAY8VNH38Y'
# cafe_darte_mid = '3KQAXWG8WK961'
# la_pisa_mid = '60CH9N5ZRRQX1'

# report_file_path = "C:\\Users\\kevin\\Downloads\\" + //(today's date)// <- need to figure out how to make the below filepath format
    # ex: "C:\\Users\\kevin\\Downloads\\DailyReport-AllStores_2020-08-12_2020-08-12.csv"

test_path = "C:\\Users\\kevin\\Downloads\\DailyReport-AllStores_2020-08-12_2020-08-12.csv"

concourse_df = pd.read_csv(test_path)

# print(concourse_df.columns)
hachi_df = concourse_df[concourse_df['Merchant ID'] == hachi_mid]
# cafe_darte_df = concourse_df[concourse_df['Merchant ID'] == cafe_darte_mid]
# la_pisa_df = concourse_df[concourse_df['Merchant ID'] == la_pisa_mid]

shops = [
        hachi_df,           # i == 0
        # cafe_darte_df,      # i == 1
        # la_pisa_df          # i == 2
        ]

for i in range(len(shops)):
     # Lists from the dataframe we are interested in -
    order_payment_net = shops[i]['Order Payment Net'].to_list()
    # order_gross_amt = shops[i]['Order amount'].to_list()
    order_tax = shops[i]['Order Tax'].to_list()
    order_id = shops[i]['Order ID'].to_list()
    order_profit_for_disc = shops[i]['Order Profit'].to_list()
    
    payment_type = shops[i]['Payment Label'].to_list()
    card_type = shops[i]['Card Type'].to_list()
    tip_amt = shops[i]['Tip Amount'].to_list()

    discount_amt = shops[i]['Total Discount'].to_list()
    discount_name = shops[i]['Order Discount Names'].to_list()
    refund_amt = shops[i]['Order Refund'].to_list()
    refund_tax = shops[i]['Order Refund Tax'].to_list()


    # Counters/metrics for the Cash and Sales spreadsheet. 
    discount_10 = 0             # 10% discount for SeaTac general employees
    discount_15 = 0             # 15% discount for ???????
    discount_25 = 0             # 25% discount for ???????
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

    # loop through all the lines in each shops' list
    for k in range(len(order_payment_net)):
        #############################
        ######### Discounts #########
        ############################# Note: Can be evaluated independent of other variables
        discount_num = float(discount_amt[k])        

        if (discount_num != 0.0):
            discount_count += 1                     # increment discount number
            # print(discount_num)

            disc_level = int(discount_name[k])
            if disc_level == 100.0:    
                discount_num = Decimal(discount_amt[k])
            elif disc_level == 0.0:
                discount_num = Decimal((order_profit_for_disc[k]) * (10 / 100) / (1 - (10/100)))
            else:
                discount_num = Decimal((order_profit_for_disc[k]) * (disc_level / 100) / (1 - (disc_level/100)))

            discount_num_rounded = discount_num.quantize(Decimal('0.01'))
            print(discount_num_rounded)
            float(discount_num_rounded)

            if (disc_level == 100):                 # 100% manager discount case
                discount_100 += discount_num_rounded
            elif (disc_level == 40):                # 40% CC discount case
                discount_40 += discount_num_rounded
            elif (disc_level == 25):                # 25% ???? discount case
                discount_25 += discount_num_rounded
            elif (disc_level == 15):                # 15% ???? discount case
                discount_15 += discount_num_rounded
            else:                                   # 10% Seatac employee discount case
                discount_10 += discount_num_rounded
    print("Count of discounts: " + str(discount_count))
    print("Total discounts provided: " + str(discount_100 + discount_40 + discount_25 + discount_15 + discount_10))  
    ###################################
    ##### End of Discount Section #####
    ###################################
        
    pass
    