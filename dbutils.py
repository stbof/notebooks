# Databricks notebook source
# MAGIC %md 
# MAGIC # DBUtils New Notebook

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------

dbutils.widgets.help()

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/databricks-datasets"))

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/"))

# COMMAND ----------


