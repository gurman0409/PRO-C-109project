import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")

reading_score_list = df["reading score"].to_list()

reading_score_mean = statistics.mean(reading_score_list)

reading_score_median = statistics.median(reading_score_list)

reading_score_mode = statistics.mode(reading_score_list)

print("Mean of the data is ->" , reading_score_mean)
print("Median of the data is ->" , reading_score_median)
print("Mode of the data is ->" , reading_score_mode)

reading_score_std_deviation = statistics.stdev(reading_score_list)

reading_score_first_std_deviation_start, reading_score_first_std_deviation_end = reading_score_mean-reading_score_std_deviation, reading_score_mean+reading_score_std_deviation
reading_score_second_std_deviation_start, reading_score_second_std_deviation_end = reading_score_mean-(2*reading_score_std_deviation), reading_score_mean+(2*reading_score_std_deviation)
reading_score_third_std_deviation_start, reading_score_third_std_deviation_end = reading_score_mean-(3*reading_score_std_deviation), reading_score_mean+(3*reading_score_std_deviation)

reading_score_list_of_data_within_1_std_deviation = [result for result in reading_score_list if result > reading_score_first_std_deviation_start and result < reading_score_first_std_deviation_end]
reading_score_list_of_data_within_2_std_deviation = [result for result in reading_score_list if result > reading_score_second_std_deviation_start and result < reading_score_second_std_deviation_end]
reading_score_list_of_data_within_3_std_deviation = [result for result in reading_score_list if result > reading_score_third_std_deviation_start and result < reading_score_third_std_deviation_end]

print("{}% of data for reading score lies within 1 standard deviation".format(len(reading_score_list_of_data_within_1_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for reading score lies within 2 standard deviations".format(len(reading_score_list_of_data_within_2_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for reading score lies within 3 standard deviations".format(len(reading_score_list_of_data_within_3_std_deviation)*100.0/len(reading_score_list)))