
def gengo(year):
    gengo_start_dict = {"明治":1868, "大正":1912, "昭和":1926, "平成":1989, "令和":2019}
    base_year = next(iter(gengo_start_dict.values()))
    gengo_name = ""
    if year < base_year:
        return "江戸時代以前には対応していません"
    for next_gengo_name in gengo_start_dict:
        if year < gengo_start_dict[next_gengo_name]:
            year_count = year_count_calc(year, base_year)
            return f"{gengo_name}{year_count}年"
        else:
            base_year = gengo_start_dict[next_gengo_name]
            gengo_name = next_gengo_name
        if gengo_name == list(gengo_start_dict.items())[-1][0]:
            year_count = year_count_calc(year, gengo_start_dict[gengo_name])
            return f"{gengo_name}{year_count}年"

def year_count_calc(end, start):
    year_count = end - start + 1
    if year_count == 1:
        year_count = "元"
    return year_count


print(gengo(2020))