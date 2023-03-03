#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

# Create the matrix
matrix = np.arange(1, 7).reshape((2, 3))

# Scale the matrix
scaled_matrix = np.multiply(matrix, 2)

print(matrix)

print(scaled_matrix)


# # b. Create a 3 by 3 identity matrix

# In[5]:


import numpy as np

# Create the identity matrix
identity_matrix = np.identity(3)

print(identity_matrix)


# #1c. To create a 1-D array called arry1 which contains elements ranging from zero to twenty-seven and then convert it to a 3-D array called arry2, we can use the arange and reshape functions:

# In[12]:


import numpy as np

# Create the 1-D array
arry1 = np.arange(27)

# Convert to a 3-D array
arry2 = arry1.reshape((3, 3, 3))

print(arry2)


# # d. Create two 2-D arrays with the first array containing elements from 1 to 6 and the second array containing elements from 7 to 12. Horizontally stack the two arrays together. Using the same set of arrays vertically stack the two arrays

# In[13]:


arr1 = np.arange(1, 7).reshape((2, 3))    # Create a 2x3 array with elements 1-6
arr2 = np.arange(7, 13).reshape((2, 3))   # Create a 2x3 array with elements 7-12
hstacked_arr = np.hstack((arr1, arr2))    # Horizontally stack the two arrays together
vstacked_arr = np.vstack((arr1, arr2))    # Vertically stack the two arrays together
print(hstacked_arr)
print(vstacked_arr)


# # e. Create an equally spaced sequence with a gap of 5 ranging from 0 to 100

# In[23]:


seq = np.arange(0, 101, 5)   # Create an array with values ranging from 0 to 100 with a step of 5
print(seq)


# # 2. Use various Functions associated with Pandas to answer the following questions.

# In[15]:


import pandas as pd


# In[16]:


student_names = ["Asun Patience", "Dassi Seth", "Tenu Stella", "Amevor Enoch", "Opoku Francis"]


# In[20]:


students = pd.DataFrame(student_names, columns=["Names"])
print(students)


# # b. Ghana Premier League Teams and their goals scored in their last five matches

# In[21]:


import pandas as pd


# In[49]:


team_names = ["Accra Hearts of Oak", "Asante kotoko", "Ashanti Gold sc", "Aduana Stars", "Medeama SC", "Ebusua Dwarfs", "WAFA SC", "Elmina Sharks", "Legon Citicies FC", "Bechem United", "Berekum Chelsea", "King Faisal Babes", "Inter Allies FC", "Great Olympics", "Liberty Professionals", "Karela United"]


# In[ ]:





# In[50]:


goals_dict={
    "Accra Hearts of Oak": [2, 3, 1, 1, 4],
  "Asante Kotoko": [1, 2, 0, 3, 2],
  "Ashanti Gold sc": [2, 0, 1, 2, 0],
  "Aduana Stars": [1, 2, 0, 0, 3],
  "Medeama SC": [1, 0, 1, 2, 0],
  "Ebusua Dwarfs": [0, 2, 0, 1, 1],
  "WAFA SC": [3, 1, 2, 3, 0],
  "Elmina Sharks": [1, 2, 1, 1, 0],
  "Legon Citicies FC": [0, 1, 1, 0, 0],
  "Bechem United": [1, 0, 0, 2, 2],
  "Berekum Chelsea": [2, 1, 2, 3, 1],
  "King Faisal Babes": [0, 1, 1, 1, 0],
  "Inter Allies Fc": [2, 3, 0, 1, 0],
  "Great Olympics": [1, 1, 1, 0, 0],
  "Liberty Professionals": [0, 2, 0, 1, 2],
  "Karela United": [2, 2, 1, 1, 1]
}


# In[51]:


teams = pd.DataFrame.from_dict(goals_dict, orient="index", columns=["match1", "match2", "match3", "match4", "match5"])


# In[52]:


teams['team_name'] = team_names


# In[53]:


teams.set_index('team_name', inplace=True)


# In[54]:


print(teams)


# #c.Write a program to create a DataFrame countries using a dictionary which stored country name, capitals, and populations of the country. Do this for West African Countries.

# In[55]:


import pandas as pd

# Create dictionary of West African Countries with their capitals and populations
countries_dict = {
    'Nigeria': ['Abuja', 206139587],
    'Ghana': ['Accra', 31072945],
    'Ivory Coast': ['Yamoussoukro', 26378275],
    'Senegal': ['Dakar', 16743930],
    'Mali': ['Bamako', 20250834],
    'Niger': ['Niamey', 24206636],
    'Burkina Faso': ['Ouagadougou', 20903273],
    'Guinea': ['Conakry', 13132792],
    'Benin': ['Porto-Novo', 12123200],
    'Togo': ['Lomé', 8278724],
    'Sierra Leone': ['Freetown', 8143385],
    'Liberia': ['Monrovia', 5057677],
    'Gambia': ['Banjul', 2347706],
    'Cape Verde': ['Praia', 549935],
}

# Convert dictionary to DataFrame
countries = pd.DataFrame.from_dict(countries_dict, orient='index', columns=['Capital', 'Population'])

# Display DataFrame
print(countries)


# # d.  A program capturing the provided dataset in python.

# In[57]:


#i.creating the given table
#names of the teams and the goals
import pandas as pd
Sno = [1, 2, 3, 4, 5, 6, 7]
team = ['Accra Hearts of Oak', 'Asante Kotoko', 'Ebusua Dwarfs', 'Sekondi Hassacas', 'Okwahu United', 'Tano Bofoakwa', 'BA United']
gf = [120,90,90,80,78,70,71]
ga = [35,55,60,43,39,50,55]
pts = [80,60,60,55,53,49,44]


# In[58]:


#assigning the headings to the table
teams_standing={'SNO':Sno, 'Teams':team, 'GF':gf, 'GA':ga, 'PTS':pts}


# In[59]:


#creating the dataframe
league_table = pd.DataFrame(teams_standing)
league_table


# In[60]:


#ii.b. teams that conceded less than 80 goals
league_table[league_table['GF']<80]


# In[61]:


#ii.c. teams that had less than 60 points
league_table[league_table['PTS']<60]


# In[62]:


#ii.a. teams that conceded more than 30 goals
league_table[league_table['GA']>30]


# In[ ]:




