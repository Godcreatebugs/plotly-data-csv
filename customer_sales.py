import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv('customer_data.csv')
def sales_count(company_name:str):
    df.sort_values(by='customer_created_at')
    df['customer_created_at'] = pd.to_datetime(df['customer_created_at']).dt.strftime('%Y-%m-%d')
    df['dates'] = pd.Series(pd.date_range('20170328',periods=1680)).dt.strftime('%Y-%m-%d')
    customer_sales=[]

    for date in df[df['dates'].notnull()].dates:
        mask = (df['customer_created_at'] == date) & (df['company_id']== company_name)
        cols = df.loc[mask]
        #convert column to a series and append to customers_sales list
        sales_list = cols['customer_total_spent']
        refund_total = cols[cols['status']=='refunded'].customer_total_spent
        total_spent = sales_list.sum() - refund_total.sum()
        customer_sales.append(total_spent)
    new_field = f'{company_name}_sales_made_on_date'
    df[new_field] =  pd.Series(customer_sales)

    #make total customers as new column in data frame
    df.loc[0,'total_spent_'+company_name] = df.loc[0,new_field]
    for i in range(1,1681):
        df.loc[i,'total_spent_'+company_name] = df.loc[i-1,'total_spent_'+company_name] + df.loc[i,new_field]
    return df

def plot_graphs():
    df2=sales_count("Jim's Gym Supplies")
    df3=sales_count("John's Boardgame Shop")
    last_df=sales_count("Mary's Christmas Store")
    last_df.to_csv('company_sales.csv')

    new_df = pd.read_csv('company_sales.csv')
    fig = make_subplots(rows=3,cols=2,start_cell='bottom-left',
                    subplot_titles=("Jim's sales_day","Jim's total_sales","John's sales_day","John's total_sales","Mary's sales_day","Mary's total_sales"))

#adding subplots
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["Jim's Gym Supplies_sales_made_on_date"]),row=1,col=1)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["John's Boardgame Shop_sales_made_on_date"]),row=2,col=1)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["Mary's Christmas Store_sales_made_on_date"]),row=3,col=1)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["total_spent_Jim's Gym Supplies"]),row=1,col=2)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["total_spent_John's Boardgame Shop"]),row=2,col=2)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["total_spent_Mary's Christmas Store"]),row=3,col=2)
    fig.show()

if __name__=='__main__':
    plot_graphs()
