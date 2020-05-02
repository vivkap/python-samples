
# coding: utf-8

# In[4]:


from influxdb import InfluxDBClient


# In[6]:


client = InfluxDBClient(host='192.168.99.100', port=8086)


# In[9]:


client.get_list_database()


# In[10]:


client.switch_database('secondsdb')


# In[11]:


client.get_list_measurements()


# In[12]:


client.query('select * from cpuUsage')


# In[19]:


import os, pandas as pd
os.chdir(r'C:\Users\Akshay\csvandtext')


# In[17]:


os.getcwd()


# In[20]:


df = pd.read_csv('HR_Data.csv', header=0)


# In[21]:


for row_index,row in df.iterrows():
    tags=row[0]
    field_value=row[8]
    json_body = [
        {
        "measurement": "HR_Data",
        "tags": {
            "Reference":tags
                },
        "fields": {
            "value" : field_value
               }
     }
    ]
    print(json_body)
    client.write_points(json_body)
    


# In[22]:


client.get_list_measurements()


# In[23]:


client.query('select * from HR_Data')

