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

st.write("Hi! My name is Thomas and I was the Instructor of the Whimsical Wontons. I am in my 4th year of college at Winona State University. I like to play board games and work out. I joined AI Camp because I believe in it's goals and mission to change the norm of teaching and learning.")

st.write('My name is Dylan. Im going into my last year of highschool. I joined AI camp to learn about coding and develop skills I could use down the line. I like playing sports and hiking. ')

st.write('My name is Siwar, and I am 17. I joined AI camp for a gist to inquire more on coding languages and data analytics. I have the summer off, so new informarion has its benefice, and I can tell it was worth it.')

#begin the eda
df = pd.read_csv('https://raw.githubusercontent.com/Kilroy11511/WhimsicalWonton/main/SP%20500%20ESG%20Risk%20Ratings.csv')

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
st.write('This graph is a sunburst chart. Sunburst charts specialize in showing how something can be broken down by multiple categories. In this case, we are breaking down the number of companies in the S&P 500 into sectors, and then further breaking down those sectors into industries as you look from the inside of the graph out. The sector with the most companies is the Financial Services sector with 49, and the largest industry in that is the Asset Management industry.')

fig = px.box(df,x="Sector", y="Total ESG Risk score", title="Overview of Sector's Total ESG Risk Score")
st.plotly_chart(fig)
st.write('Shown here is a box plot, comparing the distribution of Total ESG Risk scores to their respective sectors. With a box plot, we can easily see the maximum and minimum scores for each sector, as well as the median, Q1, Q3 and even outliers. The trends on the graph suggest that Real Estate consistently has the lowest risk scores, while the Energy sector has higher scores. The Consumer Defensive, Industrials, and Energy sectors all have a wide range, suggesting that the companies in their sectors have a wide range of using ESG and non-ESG practices.')

"""
fig = px.density_heatmap(df,'Sector','Total ESG Risk score',color_continuous_scale='ylorrd', title = 'ESG Risk Similarites Within Sectors' )
st.plotly_chart(fig)

fig = px.density_heatmap(df,'Sector','Controversy Score',color_continuous_scale='ylorrd')
st.plotly_chart(fig)

fig = px.density_heatmap(df,'Sector','Social Risk Score',color_continuous_scale='ylorrd' )
st.plotly_chart(fig)

fig = px.density_heatmap(df,'Sector','Environment Risk Score',color_continuous_scale='ylorrd' )
st.plotly_chart(fig)

fig = px.density_heatmap(df,'Sector','Governance Risk Score',color_continuous_scale='ylorrd' ) #
st.plotly_chart(fig)
"""

option: str = st.selectbox("Pick a column for the y-axis:", ('Total ESG Risk score', 'Controversy Score', 'Social Risk Score', 'Environment Risk Score', 'Governance Risk Score'))
fig = px.density_heatmap(df, x='Sector', y=option, color_continuous_scale='ylorrd' )
st.plotly_chart(fig)
st.write('This heatmap describes the similarities within sectors of ESG scores. From this we can see that many sectors have scores that reflect similarities between companies in the same sector. A takeaway from this could be that some sectors are more likely to have high ESG risks and it has less to do with specific companies.')


fig = px.box(df, x="Sector", y='ESG Risk Percentile', points = 'all', title = 'ESG Risk Percetiles With Outliers') #try swapping x and y here for a more "traditional" box plot look
st.plotly_chart(fig)
st.write('This box graph shows general trends of Risk percentiles based on Sectors. It also contains all companies as data points which allows for easy access of outlier data. The box graphs would suggest that certain sectors are similar in ESG percentiles while others are more likely to experience varience based on the individual company, but it can also be noted that some of the more varried sectors have less total companies to compare to making outliers skew the average ranges.')

fig = px.histogram(df, 'Full Time Employees', 'Social Risk Score', histfunc='avg') #turn into average?
st.plotly_chart(fig)
st.write('This graph is a histogram. It shows the frequency of full time employees in ratio to avg of social risk score. The aggregated bars emphasizes on the high avg of social risk score when full time employees are less present. However, it is inconsisitant when it goes up to 1.5M and then higher than 2M. In those cases, the avg of social risk score goes up tremendously. The graph of those two variables is inconsistant and can not be tied to a factor.')

fig = px.violin(df, x="ESG Risk Level", y="ESG Risk Percentile", points='all')
st.plotly_chart(fig)
st.write('The violin graph plots the ratio of ESG risk level over the ESG risk percentile, represented with oval kernels, denser in the middle and it narrows throughout the edges. It estimates that the higher the ESG risk level is, the higher ESG risk percentile escalates. Alternatively, the lower is the risk, the lesser is the percentile.')

#Conclusion
st.write('The data analyzed shows that ESG ratings and companies sectors are related, although that is not the only factor at play while calculating ratings. This information also shows certian sectors have tendencies towards higher or lower ESG scores while others are company specific. Based on this information the least at risk sectors are Realty and Technology while the most at risk sector would be Energy. Both Industrials and Consumer Defensive sectors have large variety within the sectors amoung ESG percentiles. The idea that companies in the same sector have similar ESG ratings is based on which sector you examine, which means some sectors are more volatile then others.')