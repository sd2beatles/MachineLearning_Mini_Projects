from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.model_selection import GridSearchCV
from datetime import datetime
from airflow.operators.bash import BashOperator

defaeult_args={
    'start_date':datetime(2021,4,19)
}


def preprocessing_data():
    data=pd.read_csv("/home/david/Downloads/diamond.csv")
    if 'Unnamed: 0' in data.columns:
        data.drop('Unnamed: 0',axis=1,inplace=True)
    data=pd.get_dummies(data.rename({'Carat':'carat'},axis=1))
    data.to_csv("/home/david/Downloads/diamond_dummies.csv")
    


def best_params(model):
    data=pd.read_csv("/home/david/Downloads/diamond_dummies.csv")
    if 'Unnamed: 0' in data.columns:
        data.drop('Unnamed: 0',axis=1,inplace=True)
    
    X_features,y_target=data.drop("price",axis=1),data.loc[:,"price"]
    if model=='ridge':
        model_name,params=Ridge(),{'alpha':[0.05,0.1,1,5,8,10,12,15,20]}
    elif model=='lasso':
        model_name,params=Lasso(),{'alpha':[0.001,0.005,0.008,0.05,0.1,0.5,1,5,10]}
        
    grid_model=GridSearchCV(model_name,param_grid=params,scoring='neg_mean_squared_error',cv=5)
    grid_model.fit(X_features,y_target)
    rmse=np.sqrt(-1*grid_model.best_score_)
    return (grid_model.best_params_,rmse)

with DAG("x_com_dag",schedule_interval="@daily",default_args=defaeult_args,catchup=False) as dag:
    preprocessing=PythonOperator(
        task_id="preprocessing_data",
        python_callable=preprocessing_data
    )

    interval=BashOperator(
        task_id='taking_interval',
        bash_command='sleep 3',
        do_xcom_push=False
    )

    with TaskGroup("parapmeter_processing") as prameter_processing:
        training_model_ridge=PythonOperator(
            task_id="grid_search_ridge",
            python_callable=best_params,
            op_kwargs={'model':'ridge'}
            )

        training_model_lasso=PythonOperator(
            task_id="grid_search_lasso",
            python_callable=best_params,
            op_kwargs={'model':'lasso'}
        )
    preprocessing >> interval >> prameter_processing

