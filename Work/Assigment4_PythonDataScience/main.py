import pandas as pd

df = pd.read_csv('Sample_bank_data (1) (2).csv')

average_age = df['Age'].mean()
total_loan_amount = df['LoanAmount'].sum()
approved_loans_count = df[df['LoanStatus'] == 'Approved'].shape[0]

high_credit_customers = df[df['CreditScore'] > 700][['CustomerName', 'Branch']]
approved_customers_high_balance = df[(df['AccountBalance'] > 5000) & (df['LoanStatus'] == 'Approved')]

average_balance_by_account_type = df.groupby('AccountType')['AccountBalance'].mean()
total_loan_by_branch = df.groupby('Branch')['LoanAmount'].sum()

loan_status_percentage = df['LoanStatus'].value_counts(normalize=True) * 100
avg_credit_score_pending = df[df['LoanStatus'] == 'Pending']['CreditScore'].mean()

age_loan_correlation = df[['Age', 'LoanAmount']].corr().loc['Age', 'LoanAmount']
age_group_highest_loan = df.groupby(pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 70, 80]))['LoanAmount'].mean().idxmax()

highest_avg_balance_branch = df.groupby('Branch')['AccountBalance'].mean().idxmax()
avg_loan_by_branch = df.groupby('Branch')['LoanAmount'].mean()

highest_credit_score = df['CreditScore'].max()
customer_with_highest_credit_score = df[df['CreditScore'] == highest_credit_score][['CustomerName', 'Branch']]

approved_loan_credit_score_distribution = df[df['LoanStatus'] == 'Approved']['CreditScore']

loan_status_count = df['LoanStatus'].value_counts()
fig1 = loan_status_count.plot(kind='bar', title='Number of Customers by Loan Status')
fig1.get_figure().savefig('loan_status_distribution.png')

fig2 = df.plot.scatter(x='AccountBalance', y='LoanAmount', title='Account Balance vs. Loan Amount')
fig2.get_figure().savefig('account_balance_vs_loan_amount.png')

customer_segments = df.groupby(['AccountType', 'LoanStatus']).size()
highest_avg_loan_account_type = df.groupby('AccountType')['LoanAmount'].mean().idxmax()

missing_data = df.isnull().sum().idxmax()
outliers_account_balance = df[(df['AccountBalance'] > df['AccountBalance'].quantile(0.99)) | (df['AccountBalance'] < df['AccountBalance'].quantile(0.01))]
outliers_loan_amount = df[(df['LoanAmount'] > df['LoanAmount'].quantile(0.99)) | (df['LoanAmount'] < df['LoanAmount'].quantile(0.01))]

print(average_age)
print(total_loan_amount)
print(approved_loans_count)
print(high_credit_customers)
print(approved_customers_high_balance)
print(average_balance_by_account_type)
print(total_loan_by_branch)
print(loan_status_percentage)
print(avg_credit_score_pending)
print(age_loan_correlation)
print(age_group_highest_loan)
print(highest_avg_balance_branch)
print(avg_loan_by_branch)
print(highest_credit_score)
print(customer_with_highest_credit_score)
print(approved_loan_credit_score_distribution.describe())
print(customer_segments)
print(highest_avg_loan_account_type)
print(missing_data)
print(outliers_account_balance.describe())
print(outliers_loan_amount.describe())
