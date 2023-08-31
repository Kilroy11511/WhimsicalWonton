import streamlit as st
import pandas as pd
import plotly.express as px

#look for more information here https://docs.streamlit.io/library/cheatsheet
# ---------------------------------------------------------------------
# Try to transfer over the colab EDA into here
# - copy pasting any data cleaning steps 
# - copy pasting graphs
# - doing a "st.plotly_chart(fig)" to display on our streamlit
# - add analysis using some st.____ function


#adding title
st.title("Hello World")

#add an initial description / introduction here
st.write("The S&P ESG risk rating is a data-set made by Pritish Dugar, and provided by Sustainalytics. It is a recent search on how ESG ratings and companie sectors are related to each other. This valuable source of research will lead us to understand how important some factors are to different economic sectors such as environmental impact, company’s governance structure and controversies associated with the company’s ESG practices. Our analysis will tell us of which sector is improverished, hence more prominancy will be given it once known about.")

#meet the team
#each person write a small biography here, with information like school,
#interests, why you joined AI Camp

st.text("Hi! My name is Thomas and I was the Instructor of the Whimsical Wontons. I am in my 4th year of college at Winona State University. I like to play board games and work out. I joined AI Camp because I believe in it's goals and mission to change the norm of teaching and learning.")

st.text('My name is Dylan. Im going into my last year of highschool. I joined AI camp to learn about coding and develop skills I could use down the line. I like playing sports and hiking. ')

st.text('My name is Siwar, and I am 17. I joined AI camp for a gist to inquire more on coding languages and data analytics. I have the summer off, so new informarion has its benefice, and I can tell it was worth it.')

#begin the eda
df = pd.read_csv('SP 500 ESG Risk Ratings.csv')

columns_to_drop = ['Address', 'Description', 'Symbol']
df.drop(columns_to_drop, axis=1, inplace=True)
df.dropna(inplace=True)

def replaceComma(s):
  if isinstance(s, str):
    return s.replace(",", "")
  else: 
    return s


df['Full Time Employees'] = df['Full Time Employees'].apply(replaceComma).astype('int64')

def removePerText(s):

    out = ""

    for char in s: #for every character in the string
        if char.isnumeric():
            out += char

    return out

df['ESG Risk Percentile'] = df['ESG Risk Percentile'].apply(removePerText).astype('int32')
st.dataframe(df.head())

df_corr = df.corr(numeric_only=True)
fig = px.imshow(df_corr)
st.plotly_chart(fig)

fig = px.sunburst(df, path=["Sector", "Industry"], title="Breakdown of Industries Within each Sector")
st.plotly_chart(fig)
st.text('This graph is a sunburst chart. Sunburst charts specialize in showing how something can be broken down by multiple categories. In this case, we are breaking down the number of companies in the S&P 500 into sectors, and then further breaking down those sectors into industries as you look from the inside of the graph out. The sector with the most companies is the Financial Services sector with 49, and the largest industry in that is the Asset Management industry.')
fig = px.box(df,x="Sector", y="Total ESG Risk score", title="Overview of Sector's Total ESG Risk Score")
fig = px.box(df,x="Sector", y="Total ESG Risk score", title="Overview of Sector's Total ESG Risk Score")
st.plotly_chart(fig)
s
fig = px.density_heatmap(df,'Sector','Total ESG Risk score',color_continuous_scale='ylorrd', title = 'ESG Risk Similarites Within Sectors' )
st.plotly_chart(fig)
st.text('')
fig = px.density_heatmap(df,'Sector','Controversy Score',color_continuous_scale='ylorrd')
st.plotly_chart(fig)

fig = px.density_heatmap(df,'Sector','Social Risk Score',color_continuous_scale='ylorrd' )
st.plotly_chart(fig)

fig = px.density_heatmap(df,'Sector','Environment Risk Score',color_continuous_scale='ylorrd' )
st.plotly_chart(fig)

fig = px.density_heatmap(df,'Sector','Governance Risk Score',color_continuous_scale='ylorrd' ) #
st.plotly_chart(fig)

fig = px.box(df, x="Sector", y='ESG Risk Percentile', points = 'all', title = 'ESG Risk Percetiles With Outliers') #try swapping x and y here for a more "traditional" box plot look
st.plotly_chart(fig)

fig = px.histogram(df, 'Full Time Employees', 'Social Risk Score', histfunc='avg') #turn into average?
st.plotly_chart(fig)

fig = px.violin(df, x="ESG Risk Level", y="ESG Risk Percentile", points='all')
st.plotly_chart(fig)