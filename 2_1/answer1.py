def is_leap_year(year):
    # 下2桁が4の倍数であれば閏年、下2桁が00の場合は全体が400の倍数であれば閏年
    if str(year)[2:] == "00":
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if int(str(year)[2:]) % 4 == 0:
            return True
        else:
            return False

for i in range(2000, 2101):
    print(f"{str(i)} {str(is_leap_year(i))}")