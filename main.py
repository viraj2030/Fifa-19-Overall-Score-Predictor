import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go

X = pd.read_csv('streamlit_data.csv')
X.drop('Overall', inplace=True, axis=1)
raw_df = X.copy()
X.head()

st.title("""Fifa 19 Overall Rating Predictor""")
st.write('---')

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

Age = st.sidebar.slider('Age', X['Age'].min(), 40, 25)
Potential = st.sidebar.slider('Potential', 0, 100, 50)
Preferred_Foot = st.sidebar.selectbox('Preferred Foot', ('Right', 'Left'))
International_Reputation = st.sidebar.slider(
    'International Reputation', X['International Reputation'].min(), X['International Reputation'].max())
Weak_Foot = st.sidebar.slider(
    'Weak Foot', X['Weak Foot'].min(), X['Weak Foot'].max())
Skill_Moves = st.sidebar.slider(
    'Skill Moves', 1, 5)
Work_Rate = st.sidebar.selectbox('Work Rate', ('High / Low', 'High / Medium', 'High / High',
                                               'Medium / Low', 'Medium / Medium', 'Medium / High', 'Low / Low', 'Low / Medium', 'Low / High'))
Body_Type = st.sidebar.selectbox('Body Type', ('Messi', 'C. Ronaldo', 'Neymar', 'Normal', 'Lean', 'Stocky',
                                               'Shaqiri', 'Akinfenwa'))
Position = st.sidebar.selectbox('Position', ('RF', 'ST', 'LW', 'RCM', 'LF', 'RS', 'RCB', 'LCM', 'CB', 'LDM', 'CAM', 'CDM', 'LS',
                                             'LCB', 'RM', 'LM', 'LB', 'RDM', 'RW', 'CM', 'RB', 'RAM', 'CF', 'LAM', 'RWB', 'LWB'))
Weight_in_lbs = st.sidebar.slider(
    'Weight in lbs', X['Weight in lbs'].min(), 250)
Crossing = st.sidebar.slider(
    'Crossing', 0, 100, 50)
Finishing = st.sidebar.slider(
    'Finishing', 0, 100, 50)
HeadingAccuracy = st.sidebar.slider(
    'HeadingAccuracy', 0, 100, 50)
ShortPassing = st.sidebar.slider(
    'ShortPassing', 0, 100, 50)
Volleys = st.sidebar.slider(
    'Volleys', 0, 100, 50)
Dribbling = st.sidebar.slider(
    'Dribbling', 0, 100, 50)
Curve = st.sidebar.slider('Curve', 0, 100, 50)
FKAccuracy = st.sidebar.slider(
    'FKAccuracy', 0, 100, 50)
LongPassing = st.sidebar.slider(
    'LongPassing', 0, 100, 50)
BallControl = st.sidebar.slider(
    'BallControl', 0, 100, 50)
Acceleration = st.sidebar.slider(
    'Acceleration', 0, 100, 50)
Agility = st.sidebar.slider(
    'Agility', 0, 100, 50)
Balance = st.sidebar.slider(
    'Balance', 0, 100, 50)
ShotPower = st.sidebar.slider(
    'ShotPower', 0, 100, 50)
Jumping = st.sidebar.slider(
    'Jumping', 0, 100, 50)
Stamina = st.sidebar.slider(
    'Stamina', 0, 100, 50)
Strength = st.sidebar.slider(
    'Strength', 0, 100, 50)
LongShots = st.sidebar.slider(
    'LongShots', 0, 100, 50)
Aggression = st.sidebar.slider(
    'Aggression', 0, 100, 50)
Interceptions = st.sidebar.slider(
    'Interceptions', 0, 100, 50)
Positioning = st.sidebar.slider(
    'Positioning', 0, 100, 50)
Vision = st.sidebar.slider('Vision', 0, 100, 50)
Penalties = st.sidebar.slider(
    'Penalties', 0, 100, 50)
Composure = st.sidebar.slider(
    'Composure', 0, 100, 50)
GKDiving = st.sidebar.slider(
    'GKDiving', 0, 50)
GKHandling = st.sidebar.slider(
    'GKHandling', 0, 50)
GKKicking = st.sidebar.slider(
    'GKKicking', 0, 50)
GKPositioning = st.sidebar.slider(
    'GKPositioning', 0, 50)
GKReflexes = st.sidebar.slider(
    'GKReflexes', 0, 50)
Years_of_experience = st.sidebar.slider(
    'Years of experience', 0, 25)
Height_in_cm = st.sidebar.slider(
    'Height in cm', 150, 205, 170)
data = {'Age': Age,
        'Potential': Potential,
        'Preferred Foot': Preferred_Foot,
        'International Reputation': International_Reputation,
        'Weak Foot': Weak_Foot,
        'Skill Moves': Skill_Moves,
        'Work Rate': Work_Rate,
        'Body Type': Body_Type,
        'Position': Position,
        'Weight in lbs': Weight_in_lbs,
        'Crossing': Crossing,
        'Finishing': Finishing,
        'Heading Accuracy': HeadingAccuracy,
        'Short Passing': ShortPassing,
        'Volleys': Volleys,
        'Dribbling': Dribbling,
        'Curve': Curve,
        'FK Accuracy': FKAccuracy,
        'Long Passing': LongPassing,
        'Ball Control': BallControl,
        'Acceleration': Acceleration,
        'Agility': Agility,
        'Balance': Balance,
        'Shot Power': ShotPower,
        'Jumping': Jumping,
        'Stamina': Stamina,
        'Strength': Strength,
        'Long Shots': LongShots,
        'Aggression': Aggression,
        'Interceptions': Interceptions,
        'Positioning': Positioning,
        'Vision': Vision,
        'Penalties': Penalties,
        'Composure': Composure,
        'GK Diving': GKDiving,
        'GK Handling': GKHandling,
        'GK Kicking': GKKicking,
        'GK Positioning': GKPositioning,
        'GK Reflexes': GKReflexes,
        'Years of experience': Years_of_experience,
        'Height in cm': Height_in_cm}


features = pd.DataFrame(data, index=[0])


raw_df.rename(columns={'HeadingAccuracy': 'Heading Accuracy',
                       'ShortPassing': 'Short Passing',
                       'FKAccuracy': 'FK Accuracy',
                       'LongPassing': 'Long Passing',
                       'BallControl': 'Ball Control',
                       'LongShots': 'Long Shots',
                       'GKHandling': 'GK Handling',
                       'GKKicking': 'GK Kicking',
                       'GKPositioning': 'GK Positioning',
                       'ShotPower': 'Shot Power',
                       'GKDiving': 'GK Diving',
                       'GKReflexes': 'GK Reflexes'}, inplace=True)


df = pd.concat([features, raw_df], axis=0)


df = pd.get_dummies(df, drop_first=True)

df.drop('Work Rate_High/ High', axis=1, inplace=True)

df = df[:1]  # Selects only the first row (the user input data)


# Reads in saved classification model
load_clf = pickle.load(open('fifa_model.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df)


st.header('Overall player rating prediction: {}'.format(prediction[0].round(0)))


# Displays the user input features
#st.subheader('User Input features')
# st.write(df)

fifa_data_top_players = pd.read_csv('fifa 19 data.csv')

# fifa_data_top_players.columns
fifa_data_top_players = fifa_data_top_players[[
    'Name', 'Age', 'Nationality', 'Position', 'Club', 'Overall']]
fifa_data_top_players = fifa_data_top_players.sort_values(by='Overall', ascending=False)
fifa_data_top_players = fifa_data_top_players[:10]
# fifa_data_top_players

# fig = go.Figure(data=[go.Table(columnwidth=[400, 400, 400, 400, 400, 400],
#                               header=dict(values=list(fifa_data_top_players.columns),
#                                           fill_color='lightgrey',
#                                           align='left'),
#                               cells=dict(values=[fifa_data_top_players.Name, fifa_data_top_players.Age, fifa_data_top_players.Nationality, fifa_data_top_players.Club, fifa_data_top_players.Position, fifa_data_top_players.Overall],
#                                          fill_color='lavender',
#                                          align='left'))
#                  ])

# fig.show()
# st.write(fig)

feature_importance = pd.DataFrame(pd.Series(load_clf.feature_importances_, df.columns).nlargest(10))
feature_importance = feature_importance.rename(columns={0: 'Most important features'})
feature_importance = feature_importance.sort_values(by='Most important features')
st.subheader('The top 10 most important attributes to a players overall score')
fig_bar = st.bar_chart(feature_importance)

# Display top 10 players
st.subheader('Top 10 players in the world')
st.write(fifa_data_top_players)
