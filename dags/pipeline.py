from airflow.decorators import dag, task

@dag (
    schedule=None,
    catchup=False
)
def my_dag():
    
    print("Hello World")
    
my_dag()