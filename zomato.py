import streamlit as st
import plotly.express as px
import pandas as pd
st.title("Zomato_data_analysis")
zomato_data=pd.read_csv(r"zomato.csv", encoding="latin-1")
st.write(zomato_data.head(10))
group_by_city=zomato_data.groupby("City").count()

data_online=group_by_city.sort_values("Has Online delivery",ascending=False).head(20)

x=group_by_city.index



# group_by_city

fig1=px.bar(data_online,y=['Has Table booking'],x=data_online.index,title="How many table booking count")
st.plotly_chart(fig1)
fig2=px.bar(data_online,y=['Has Online delivery'],x=data_online.index,title="Count of online Dilivery in Top city")
st.plotly_chart(fig2)
grouped_by_rating=zomato_data.groupby(['Restaurant Name','Rating text']).agg({"Rating text":"count"})

df=grouped_by_rating



df=df.rename({"Rating text":"Rating_text_count"},axis=1)

df=df.reset_index()

# fig3=px.bar(df.sort_values(by=["Rating_text_count",'Restaurant Name'],ascending=False).head(30),x="Rating_text_count",y=['Restaurant Name'],color="Rating text")
# st.plotly_chart(fig3)
fig4= px.bar(
    df.sort_values(by=["Rating_text_count", 'Restaurant Name'], ascending=False).head(30),
    x="Rating_text_count",
    y='Restaurant Name',
    color='Rating text',
)

st.plotly_chart(fig4)
df=zomato_data.groupby(["Longitude","Latitude"]).count()

df.reset_index(inplace=True)

df=df.sort_values("Has Table booking",inplace=False)
# df

# import plotly.express as px

# Assuming 'df' is your DataFrame with 'longitude', 'latitude', and 'count_delivery' columns
fig5= px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    size="Has Table booking",
    color="Has Table booking",
    size_max=100,
    zoom=10,
    mapbox_style="open-street-map",
    title="TABLE BOOKING",
    labels={'Has Table booking': 'Count of Delivery'},
)

st.plotly_chart(fig5)
new_df=grouped_by_rating=zomato_data.groupby(['Restaurant Name','Rating text',"Longitude","Latitude"]).agg({"Rating text":"count"})

new_df=new_df.rename({"Rating text":"rating_count_text"},axis=1)
new_df=new_df.reset_index()

# new_df

# Assuming 'df' is your DataFrame with 'longitude', 'latitude', and 'count_delivery' columns
fig6 = px.scatter_mapbox(
    new_df,
    lat="Latitude",
    lon="Longitude",
    size="rating_count_text",
    color="Rating text",
    size_max=50,
    zoom=10,
    mapbox_style="open-street-map",
    title="RATING_COUNT_TEXT VS RANTING COUNT",
    labels={'rating_count_text': 'Count of Delivery'},
)

st.plotly_chart(fig6)

fig7 = px.scatter_mapbox(
    zomato_data,
    lat="Latitude",
    lon="Longitude",
    size="Average Cost for two",
    color="Rating text",
    size_max=100,
    zoom=1,
    mapbox_style="open-street-map",
    title="AVG COST PRICE VS RATING TEXT",
    labels={'rating_count_text': 'Count of Delivery'},
)

st.plotly_chart(fig7)
