day_count = int(input("Enter the count of the day\n> "))

if day_count > 0 and day_count < 94:
    print("بهار -- Spring")
elif day_count > 93 and day_count < 187:
    print("تابستان -- Summer")
elif day_count > 186 and day_count < 277:
    print("پاییز -- Fall")
else:
    print("زمستان -- Winter")
