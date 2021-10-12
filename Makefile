install:
	\python3 -m pip install --user --upgrade pip --ignore-installed --no-cache-dir;\
	\python3 -m pip install --user virtualenv --ignore-installed --no-cache-dir;\

dev:requirements.txt
	\python3 -m venv venv;\
	\source ./venv/bin/activate;\
	\pip3 install --upgrade setuptools;\
	\pip3 install numpy;\
	\pip3 install cython;\
	\python3 -m pip install -r requirements.txt --ignore-installed --no-cache-dir;\

customer_data:
	\. ./venv/bin/activate;\
	\python3 customer_addition.py;\

sales_data :
	\. ./venv/bin/activate;\
	\python3 customer_sales.py;\

clean:
	\rm -rf venv\