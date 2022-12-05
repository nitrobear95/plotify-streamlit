import streamlit as st
from PIL import Image
from style import get_css


## SITE CONFIG

# set the config for the page. App themes in .streamlit/config.toml

st.set_page_config(
            page_title="Plotify - create your story", # => Quick reference - Streamlit
            page_icon="../assets/plotify_logo.png",
            layout="centered", # wide
            initial_sidebar_state="expanded") # collapsed



st.markdown(get_css(), unsafe_allow_html=True)



## SIDEBAR

# Assets: Logo + headertext(plotify - create your story)

with st.sidebar.container():
    image = Image.open("assets/plotify_logocomplete.png")
    st.image(image, use_column_width=True) #, caption ='Plotify - create your story'



# Button 1 : Start API to return story with no prompts

if st.sidebar.button("I'M FEELING LUCKY"):
    # print is visible in the server output, not in the page
    st.write('lucky_story_selected')


# Input 1: Text Box: prompt to input short text, limit

input1 = st.sidebar.text_area('got the start of an idea?', height=150, max_chars = 150)


# Input 2: Radio buttons: choose genre

input2 = st.sidebar.radio('select your genre:',
                          ('Action 🤯',
                           'Comedy 🤣',
                           'Crime 👮🏽‍♀️',
                           'Drama 🎭',
                           'Fantasy 🚀',
                           'Horror 👻',
                           'Mystery 😵‍💫',
                           'Romance 😘',
                           'Young Adult 😎'))


# Button 2: Start API to return story with prompts + genre

if st.sidebar.button("GENERATE ME A STORY..."):
    # print is visible in the server output, not in the page
    st.write('prompts_story_selected')



## MAIN BODY

# Assets: borders top, right and bottom

# Assets: Headertext (your plotify-board)
image = Image.open("assets/plotify_pageheadertext.png")
st.image(image,  use_column_width=None)


# Output 1: Summary Text


# Output 2: TBC (Titles)
# Output 3: TBC (Topics)
# Output 4: TBC (Pictures)
# Output 5: TBC (MicroTwitter Story)
