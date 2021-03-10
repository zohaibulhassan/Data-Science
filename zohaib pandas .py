#!/usr/bin/env python
# coding: utf-8

# In[103]:


import numpy as np
import pandas as pd
students = {'name': ["Ali", "Faraz", "Kamran", "Faizan", "Nasir", "Asad", "Danish"],
            'Age': [20,21,24,21,20,23, np.nan],
            'Python': [89,49,78,96,100,78, 80],
            'Numpy': [78.87, 34, 89,75,95,85,65],
            'Pandas': [40,75,85,48,60,89, 96]}
data = pd.DataFrame (students)
data


# In[104]:


data.dropna ()


# In[105]:


data


# In[106]:


data.fillna ({'Age': data ['Age']. mean(), 'Python': 0})


# In[107]:


data['Obtained Marks'] = data['Python']+ data['Numpy']+ data['Pandas']
data


# In[108]:


data['Total Marks'] = '300' 
data


# In[109]:


data['Result'] = ["pass" if a >= 200 else "fail" for a in data['Obtained Marks']]
data


# In[110]:


data['Precentage'] = (data['Obtained Marks'] *100)/300
data


# In[111]:


data['Precentage'] = round(data['Precentage'])
data


# In[112]:


data['Grade'] = ["A+" if a>=80
                 else "A" if a>= 70
                 else "B" if a>=60
                 else "Fail"
                 for a in data['Precentage']]
data


# In[113]:


data['Age'] = fillna({'Age': data ['Age']. mean()})


# In[ ]:


data.fillna({'Age':data['Age'].mean()})
data


# In[114]:


data.fillna ({'Age': data ['Age']. mean()},inplace = True) # for permenent update


# In[115]:


data


# In[116]:


data['Result2'] = [(py,np,pd) for py,np,pd in zip(data['Python'],data['Numpy'],data['Pandas'])]


# In[117]:


data


# In[118]:


data['Subject Wise Result'] = ["pass" if(py>=70 and np>=70 and pd>=70)
                   else "Fail"
                   for py,np,pd in zip(data['Python'],data['Numpy'],data['Pandas'])]


# In[119]:


data


# In[120]:


data['overall Result'] = data['Result']


# In[121]:


data


# In[122]:


data.drop(columns='overall Result',inplace = True)
data


# In[123]:


fail = data['Subject Wise Result'] == "Fail"
data[fail]


# In[124]:


Pass = data['Subject Wise Result'] == "pass"
data[Pass]


# In[125]:


gradeA = data['Grade'] == "A+"
data[gradeA]


# In[126]:


data


# In[145]:


data[data['Python']== data['Python'].max()]


# In[147]:


data[data['Python']== data['Python'].max()]


# In[151]:


data[(data['Python'] <80) & (data['Numpy'] < 80)]


# In[ ]:




