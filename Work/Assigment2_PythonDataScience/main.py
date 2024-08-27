import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('Sample_bank_data (1).csv')

plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=[20, 30, 40, 50, 60, 70, 80], edgecolor='black')
plt.title('Customer Age Range Analysis')
plt.xlabel('Age Range')
plt.ylabel('Number of Customers')
plt.savefig('age_range_analysis.png')

loan_status_by_gender = pd.crosstab(df['Gender'], df['LoanStatus'])
loan_status_by_gender.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Loan Status by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Loans')
plt.savefig('loan_status_by_gender.png')

account_type_counts = df['AccountType'].value_counts().reset_index()
account_type_counts.columns = ['AccountType', 'Count']
fig = px.pie(account_type_counts, names='AccountType', values='Count', hole=0.3, title='Account Type Distribution')
fig.write_image('account_type_distribution.png')

fig = px.scatter(df, x='CreditScore', y='LoanAmount', trendline='ols', title='Loan Amount by Credit Score')
fig.write_image('loan_amount_by_credit_score.png')

loan_approval_by_branch = df[df['LoanStatus'] == 'Approved'].groupby('Branch').size() / df.groupby('Branch').size()
loan_approval_by_branch = loan_approval_by_branch.reset_index(name='ApprovalRate')
fig = px.bar(loan_approval_by_branch, x='ApprovalRate', y='Branch', orientation='h', title='Loan Approval Rate by Branch')
fig.write_image('loan_approval_by_branch.png')

df['AgeGroup'] = pd.cut(df['Age'], bins=[20, 30, 40, 50, 60, 70, 80], labels=['20-30', '31-40', '41-50', '51-60', '61-70', '71-80'])
fig = px.box(df, x='AgeGroup', y='CreditScore', title='Credit Score Distribution by Age Group')
fig.write_image('credit_score_by_age_group.png')

fig = px.scatter(df, x='AccountBalance', y='LoanAmount', size='LoanAmount', title='Account Balance vs. Loan Amount')
fig.write_image('account_balance_vs_loan_amount.png')

avg_loan_by_branch = df.groupby('Branch')['LoanAmount'].mean().reset_index()
fig = px.line(avg_loan_by_branch, x='Branch', y='LoanAmount', title='Average Loan Amount by Branch')
fig.write_image('avg_loan_by_branch.png')

fig = go.Figure()
for status in df['LoanStatus'].unique():
    fig.add_trace(go.Histogram(x=df[df['LoanStatus'] == status]['Age'], name=status))
fig.update_layout(barmode='overlay', title='Age Distribution by Loan Status')
fig.update_traces(opacity=0.75)
fig.write_image('age_distribution_by_loan_status.png')

fig = px.violin(df, x='AccountType', y='CreditScore', box=True, title='Credit Score Distribution Across Account Types')
fig.write_image('credit_score_across_account_types.png')
