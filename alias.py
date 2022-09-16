import sqlalchemy
import models

sql_select = sqlalchemy.select
sql_count = sqlalchemy.func.count
sql_sum = sqlalchemy.func.sum
sql_text = sqlalchemy.text

races_cols = models.races_table.c
drivers_cols = models.drivers_table.c
results_cols = models.results_table.c
circuits_cols = models.circuits_table.c
constructors_cols = models.constructors_table.c

races_select = models.races_table.select
drivers_select = models.drivers_table.select
results_select = models.results_table.select
circuits_select = models.circuits_table.select
constructors_select = models.constructors_table.select
