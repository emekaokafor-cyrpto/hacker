import streamlit as st

# 1. Define the Dictionary Data
nigerian_dict = {
    "Yoruba": {
        "Ekaabo": "Welcome",
        "Ose": "Thank you / Thanks",
        "Beni": "Yes",
        "Rara": "No",
        "Bawo ni": "How are you?"
    },
    "Hausa": {
        "Sannu": "Hello / Hi",
        "Na gode": "Thank you",
        "Eh": "Yes",
        "A'a": "No",
        "Ina kwana": "Good morning"
    },
    "Igbo": {
        "Nnoo": "Welcome",
        "Daalu": "Thank you",
        "Ee": "Yes",
        "Mba": "No",
        "Kedu": "How are you?"
    },
    "Efik": {
        "Mesiere": "Good morning",
        "Sosongo": "Thank you",
        "Idem mfo?": "How are you?",
        "Iiyii": "No",
        "Ami mmoyom": "I want"
    },
    "Kanuri": {
        "Sanda": "Greetings / Hello",
        "Amana": "Trust / Reliability",
        "Beni": "Yes",
        "A'a": "No",
        "Wunye": "I (Self)"
    }
}

# 2. Streamlit UI Layout
st.title("🇳🇬 Mini Nigerian Language Dictionary")
st.write("Select a language and a word to see its English meaning.")

st.set_page_config(page_title="Emeka dictionary", page_icon="🇳🇬")

# Language Selection
language = st.selectbox("Choose a Language", list(nigerian_dict.keys()))

# Word Selection based on chosen language
if language:
    words = list(nigerian_dict[language].keys())
    selected_word = st.selectbox(f"Select a {language} word", words)

    # Display the Result
    meaning = nigerian_dict[language][selected_word]
    st.success(f"The English meaning of '**{selected_word}**' is: **{meaning}**")

# Sidebar info
st.sidebar.header("About")
st.sidebar.info("This app features 5 major Nigerian languages: Yoruba, Hausa, Igbo, Efik, and Kanuri.")
