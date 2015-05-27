import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
    North, 6.47, 4.03
    Yorkshire, 6.13, 3.76
    Northeast, 6.19, 3.77
    East Midlands, 4.89, 3.34
    West Midlands, 5.63, 3.47
    East Anglia, 4.52, 2.92
    Southeast, 5.89, 3.20
    Southwest, 4.79, 2.71
    Wales, 5.27, 3.53
    Scotland, 6.08, 4.51
    Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(", ") for i in data]
column_names = data[0]
data_rows = data[1:]
df = pd.DataFrame(data_rows, columns = column_names)

#Generate dataframes of type float:
df["Alcohol"] = df["Alcohol"].astype(float)
df["Tobacco"] = df["Tobacco"].astype(float)

#Calculate descriptive stats for Alcohol data:
etoh_mean = df["Alcohol"].mean()
etoh_median = df["Alcohol"].median()
etoh_mode = stats.mode(df["Alcohol"])[0][0]
etoh_range = max(df["Alcohol"]) - min(df["Alcohol"])
etoh_variance = df["Alcohol"].var()
etoh_stdev = df["Alcohol"].std()
etoh_list = [etoh_mean, etoh_median,etoh_mode,etoh_range,etoh_variance,etoh_stdev]

#Calculate descriptiv stats for Tobacco data:
tb_mean = df["Tobacco"].mean()
tb_median = df["Tobacco"].median()
tb_mode = stats.mode(df["Tobacco"])[0][0]
tb_range = max(df["Tobacco"]) - min(df["Tobacco"])
tb_variance = df["Tobacco"].var()
tb_stdev = df["Tobacco"].std()
tb_list = [tb_mean, tb_median, tb_mode, tb_range, tb_variance, tb_stdev]

#Print stats:
data_type = ("Ethanol", "Tobacco")
statistic_type = ("mean", "median", "mode", "range", "variance", "standard deviation")
#Print output:
print "Python stats.py"
for index, statistic_name in enumerate(statistic_type):
    print "The {stat} for Ethanol is {data}".format(stat = statistic_name, data = etoh_list[index])
    print "The {stat} for Tobacco is {data}".format(stat = statistic_name, data = tb_list[index])




