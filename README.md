#Plotly-data-CSV
This project will display concluded results in form of interactive dashboard.

*system requirenments*

```
python>=3.8
pandas==1.3.3
plotly==5.3.1
```

## setting up environments and running program ##
* Please ``cd`` into directory where you downloaded repository.
ex.. ```cd home/rashmi_projects```
 

* firing up environment and install packages run this command subsquently. 
```make install``` and after that `make dev`


* at this point you are in virtual environment which has all dependancies needed.


* Please run ``make customer_data`` to get output for new_customers made and total_customers made by each company over the period of time.


* Run ``make sales_data`` to get output of how company performed each day on basis of revenue and total revenue over the period of time.


* This 2 command mentioned abover should open chrome local browser to open plots.

### Conditions and Considerations for the Program ###

* This project takes consideration of new_customers made each day and total_customer for particular company at given time. This is done by utilizing set data structure in python.


* And the sales each day is considered to be total_revenue nminus refunded_money at given day.


* The results as CSV can be seen in ``csv_files`` folder and screenshot of plotly output can be seen in ``graph_pics`` folder of repo.
