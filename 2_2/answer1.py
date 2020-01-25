
def gengo(year):
    if year < 1868:
        gengo_name = ""
        gengo_year = ""
    elif year < 1912:
        gengo_name = "明治"
        gengo_year = year - 1867
    elif year < 1926:
        gengo_name = "大正"
        gengo_year = year - 1911
    elif year < 1989:
        gengo_name = "昭和"
        gengo_year = year - 1925
    elif year < 2019:
        gengo_name = "平成"
        gengo_year = year - 1988
    else:
        gengo_name = "令和"
        gengo_year = year - 2018

    # 最初の年は「元年」と表記するので、表示を変更する
    if gengo_year == 1:
        gengo_year = "元"
    return f"{gengo_name}{gengo_year}年"

print(gengo(2020))