import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv('customer_data.csv')
def customer_count(company_name:str):
    df.sort_values(by='customer_created_at')
    df['customer_created_at'] = pd.to_datetime(df['customer_created_at']).dt.strftime('%Y-%m-%d')
    df['dates'] = pd.Series(pd.date_range('20170328',periods=1680)).dt.strftime('%Y-%m-%d')
    customers = set()
    customers_count=[]

    for date in df[df['dates'].notnull()].dates:
        mask = (df['customer_created_at'] == date) & (df['company_id']== company_name)
        cols = df.loc[mask]
        counter = 0
        for id in cols['customer_id']:
          if id not in customers:
            counter = counter + 1
            customers.add(id)
        customers_count.append(int(counter))
    new_field = f'{company_name}_customers_made_on_date'
    df[new_field] =  pd.Series(customers_count)

    #make total customers as new column in data frame
    df.loc[0,'total_customers_'+company_name] = df.loc[0,new_field]
    for i in range(1,1681):
        df.loc[i,'total_customers_'+company_name] = df.loc[i-1,'total_customers_'+company_name] + df.loc[i,new_field]
    return df

def plot_graphs():
    df2=customer_count("Jim's Gym Supplies")
    df3=customer_count("John's Boardgame Shop")
    last_df=customer_count("Mary's Christmas Store")
    last_df.to_csv('customer_add.csv')

    new_df = pd.read_csv('customer_add.csv')
    fig = make_subplots(rows=3,cols=2,start_cell='bottom-left',
                    subplot_titles=("Jim's new_customers_made","Jim's total_customer_count","John's new_customers_made","John's total_customer_count","Mary's new_customers_made","Mary's total_customer_count"))

#adding subplots
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["Jim's Gym Supplies_customers_made_on_date"]),row=1,col=1)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["John's Boardgame Shop_customers_made_on_date"]),row=2,col=1)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["Mary's Christmas Store_customers_made_on_date"]),row=3,col=1)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["total_customers_Jim's Gym Supplies"]),row=1,col=2)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["total_customers_John's Boardgame Shop"]),row=2,col=2)
    fig.add_trace(go.Scatter(x=new_df['dates'],y=new_df["total_customers_Mary's Christmas Store"]),row=3,col=2)
    fig.show()

if __name__=='__main__':
    plot_graphs()
