# Import python packages
import streamlit as st
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)
#from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(":apple: Uncle Yer's Fruits Details :apple:")
st.write(
  """Enter fruit name and root depth code below.
  """
)

# Get the current credentials
cnx = st.connection("snowflake")
session = cnx.session()

fn = st.text_input('Fruit Name:')
rdc = st.selectbox('Root_Deph:',('S','M','D'))
if st.button('Submit'):
    #st.write('Fruit Name entered is ' + fn)
    #st.write('Root Depth Code chosen is ' + rdc)
    sql_insert = 'insert into garden_plants.fruits.fruit_details select \''+fn+'\',\''+rdc+'\''
    #st.write(sql_insert)
    result=session.sql(sql_insert)
    st.write(result)
