import stats

# retrieve_data() -> list, list
def retrieve_data():
    file_out=open('Worldbank.txt','r')
    read=file_out.readlines()
    N=180
    l_fertility = []
    l_gdp = []
    for i in range(1,N+1):
        country=read[i]
        country=country.split()
        fert_rate=float(country[1])
        gdp=float(country[2])
        l_fertility+=[fert_rate]
        l_gdp+=[gdp]
    return l_fertility, l_gdp


def print_statistics(l_fertility, l_gdp):
    print('WORLD STATISTICS 2013')
    print('%%% Fertility %%%')
    print('Mean', stats.compute_mean(l_fertility))
    print('Median', stats.compute_median(l_fertility))
    print('Variance', stats.compute_variance(l_fertility))
    print('Std deviation', stats.compute_standard_deviation(l_fertility))
    print('%%% GDP %%%')
    print('Mean', stats.compute_mean(l_gdp))
    print('Median', stats.compute_median(l_gdp))
    print('Variance', stats.compute_variance(l_gdp))
    print('Std deviation', stats.compute_standard_deviation(l_gdp))


def main():
    l_fertility, l_gdp = retrieve_data()
    #print(l_fertility)
    #print(l_gdp)
    print_statistics(l_fertility, l_gdp)

main()
