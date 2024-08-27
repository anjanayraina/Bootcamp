import pandas as pd
import plotly.express as px

df = pd.read_csv('Sample_bank_data (1).csv')

fig = px.histogram(df, x='Age', nbins=20, title='Age Distribution')
fig.show()

fig = px.pie(df, names='Gender', title='Gender Distribution', hole=0.3)
fig.show()

avg_balance_by_account_type = df.groupby('AccountType')['AccountBalance'].mean().reset_index()
fig = px.bar(avg_balance_by_account_type, x='AccountType', y='AccountBalance', title='Average Account Balance by Account Type')
fig.show()

fig = px.box(df, x='LoanAmount', title='Loan Amount Distribution')
fig.show()

loan_status_counts = df['LoanStatus'].value_counts().reset_index()
loan_status_counts.columns = ['LoanStatus', 'Count']
fig = px.bar(loan_status_counts, x='LoanStatus', y='Count', title='Loan Status Distribution')
fig.show()

avg_credit_score_by_branch = df.groupby('Branch')['CreditScore'].mean().reset_index()
fig = px.bar(avg_credit_score_by_branch, x='Branch', y='CreditScore', title='Average Credit Score by Branch')
fig.show()

fig = px.box(df, x='AccountType', y='LoanAmount', title='Loan Amount by Account Type')
fig.show()

fig = px.scatter(df, x='Age', y='AccountBalance', title='Age vs. Account Balance')
fig.show()

total_balance_by_branch = df.groupby('Branch')['AccountBalance'].sum().reset_index()
fig = px.bar(total_balance_by_branch, x='Branch', y='AccountBalance', title='Total Account Balance by Branch')
fig.show()

fig = px.violin(df, x='LoanStatus', y='CreditScore', box=True, title='Credit Score vs. Loan Status')
fig.show()
