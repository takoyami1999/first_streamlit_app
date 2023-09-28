import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

#Title of the Diner
streamlit.title('MY PARENTS NEW HEALTHY DINER!')

#Menu
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

#Smoothie
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Data
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Option to Pick Fruits
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Data Visualization
streamlit.dataframe(fruits_to_show)

#response api
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#function
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#Display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

#input for fruit_choice
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
                    
  else:
  #normalize api response to a database
      back_from_function = get_fruityvice_data (fruit_choice)
      streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

#stop
streamlit.stop()

#streamlit connect
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_rows)

#input fruit
fruit_choice = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding ', fruit_choice)

#insert to table
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
