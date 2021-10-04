import pandas as pd
import os


excel_covid_df = pd.read_excel('covid_19_india.xlsx')

parent_dir = (os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
output_dir = os.path.join(parent_dir, "output_csv_files")
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

# a. Extract confirmed cases by state wise for each day.
state_date_wise_file = os.path.join(output_dir, "State_Date_Wise_Confirmed_Cases.csv")
excel_covid_df.groupby(["State", "Date"])["Confirmed"].sum().to_csv(state_date_wise_file)

# b. Create a report of total deaths state wise in the descending order
state_wise_deaths_file = os.path.join(output_dir, "State_Wise_Deaths_Descending.csv")
excel_covid_df.groupby("State")["Deaths"].sum().sort_values(ascending=False).to_csv(state_wise_deaths_file)

# c. Create a report of consolidated data for all states by month
all_state_month_wise_file = os.path.join(output_dir, "All_States_Month_Wise_Consolidation.csv")

excel_covid_df["Date"] = pd.to_datetime(excel_covid_df['Date'])

excel_covid_df[["ConfirmedIndianNational",
                "ConfirmedForeignNational"]] = excel_covid_df[["ConfirmedIndianNational",
                                                               "ConfirmedForeignNational"]].replace('-',0)
excel_covid_df.groupby([excel_covid_df["Date"].dt.strftime('%B'),
                        "State"])[["ConfirmedIndianNational",
                                   "ConfirmedForeignNational", "Cured",
                                   "Deaths", "Confirmed"]].sum().to_csv(all_state_month_wise_file)

print("Output CSV files generated in : " + str(output_dir))
