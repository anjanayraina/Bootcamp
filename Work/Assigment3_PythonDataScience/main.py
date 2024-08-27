import pandas as pd

df = pd.read_csv('Sample_bank_data (1) (1).csv')

median_age = df['Age'].median()
avg_balance_loan_above_1000 = df[df['LoanAmount'] > 1000]['AccountBalance'].mean()
rejected_loans_count = df[df['LoanStatus'] == 'Rejected'].shape[0]

female_customers_low_balance = df[(df['Gender'] == 'Female') & (df['AccountBalance'] < 3000)][['CustomerName', 'Branch']]
customers_balance_range = df[(df['AccountBalance'].between(3000, 10000)) & (df['CreditScore'] < 600)]

total_loan_by_gender = df.groupby('Gender')['LoanAmount'].sum()
avg_credit_score_by_account_type = df.groupby('AccountType')['CreditScore'].mean()

loan_status_count = df['LoanStatus'].value_counts()
avg_balance_approved = df[df['LoanStatus'] == 'Approved']['AccountBalance'].mean()

avg_loan_30_40 = df[(df['Age'] >= 30) & (df['Age'] <= 40)]['LoanAmount'].mean()
age_group_rejected = df[df['LoanStatus'] == 'Rejected'].groupby(pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 70, 80])).size()

lowest_avg_loan_branch = df.groupby('Branch')['LoanAmount'].mean().idxmin()
loan_approval_percentage_by_branch = df[df['LoanStatus'] == 'Approved'].groupby('Branch').size() / df.groupby('Branch').size() * 100


loan_distribution_high_credit = df[df['CreditScore'] > 750]['LoanAmount']
lowest_credit_score_customer = df.loc[df['CreditScore'].idxmin()][['CustomerName', 'Branch']]


df['BalanceCategory'] = pd.cut(df['AccountBalance'], bins=[0, 3000, 7000, df['AccountBalance'].max()], labels=['Low', 'Medium', 'High'])
customer_segments = df['BalanceCategory'].value_counts()
highest_avg_loan_status = df.groupby('LoanStatus')['LoanAmount'].mean().idxmax()


missing_values = df.isnull().sum().idxmax()
credit_score_outliers = df[df['CreditScore'] > df['CreditScore'].quantile(0.99)]

print("Median Age:", median_age)
print("Average Account Balance for Loans > $1000:", avg_balance_loan_above_1000)
print("Rejected Loan Applications Count:", rejected_loans_count)
print("Female Customers with Balance < $3000:\n", female_customers_low_balance)
print("Customers with Balance between $3000 and $10000 and Credit Score < 600:\n", customers_balance_range)
print("Total Loan Amount by Gender:\n", total_loan_by_gender)
print("Average Credit Score by Account Type:\n", avg_credit_score_by_account_type)
print("Loan Status Count:\n", loan_status_count)
print("Average Balance of Approved Loans:", avg_balance_approved)
print("Average Loan Amount for Age 30-40:", avg_loan_30_40)
print("Age Group with Most Rejected Loans:", age_group_rejected.idxmax())
print("Branch with Lowest Average Loan Amount:", lowest_avg_loan_branch)
print("Loan Approval Percentage by Branch:\n", loan_approval_percentage_by_branch)
print("Loan Distribution for Credit Scores > 750:\n", loan_distribution_high_credit.describe())
print("Customer with Lowest Credit Score:\n", lowest_credit_score_customer)
print("Customer Segments by Account Balance:\n", customer_segments)
print("Loan Status with Highest Average Loan Amount:", highest_avg_loan_status)
print("Column with Most Missing Values:", missing_values)
print("Credit Score Outliers:\n", credit_score_outliers.describe())
