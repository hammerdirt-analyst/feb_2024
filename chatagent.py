# litter_density_analysis.py
import streamlit as st
import openai
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Known locations
known_locations = [
    "Aare river basin",
    "Lake Geneva",
    "Lake Zurich",
    "Canton of Bern",
    "Lake Constance",
    # Add more locations as needed
]

# Function to generate a new narrative based on user input and a provided table
def generate_narrative_from_table(query, table):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    example_narrative = """
    Cluster analysis identified three distinct clusters with varying levels of litter density (pcs/m) and distinct land use characteristics. 
    Cluster 0, which includes 7 samples, has an average pcs/m of 0.235 and is primarily associated with high forest coverage (0.553) and lower building presence (0.162). 
    In contrast, Cluster 1, containing the majority of the samples (70), has a higher average pcs/m of 0.377. This cluster is characterized by a balance between undefined areas (0.536) and buildings (0.248). 
    Cluster 2, with 21 samples, exhibits the highest litter density at 1.405 pcs/m. This cluster is dominated by significant building coverage (0.586) and lower presence of undefined areas (0.119). 
    The public services feature remains low across all clusters, highlighting its minimal impact on litter density in this analysis.
    """
    
    prompt = (
        f"Generate a narrative summary for {query} based on the following table. Use the example narrative as a style guide:\n\n"
        f"{table.to_markdown()}\n\n"
        f"Example Narrative:\n{example_narrative}\n\n"
    )
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000
    )
    return response.choices[0].text.strip()

# Function to generate a table based on user query
def generate_table_for_query(query):
    # Dummy data for demonstration; replace with actual data retrieval logic
    data = {
        "clusters": [0, 1, 2],
        "samples": [7, 70, 21],
        "pcs/m": [0.235, 0.377, 1.405],
        "buildings": [0.162, 0.248, 0.586],
        "forest": [0.553, 0.199, 0.292],
        "undefined": [0.186, 0.536, 0.119],
        "public services": [0.002, 0.008, 0.039]
    }
    df = pd.DataFrame(data)
    return df

# Function to find location matches
def find_location_matches(user_input, locations):
    matches = [location for location in locations if location.lower() in user_input.lower()]
    return matches

# Generate multiple narratives for a query
def generate_narratives_for_query(query):
    narratives = []
    table = generate_table_for_query(query)
    
    for i in range(15):  # Generate 15 narratives
        narrative = generate_narrative_from_table(f"{query} aspect {i+1}", table)
        narratives.append(narrative)
    
    return narratives

# Compile multiple narratives into one text
def compile_narratives(narratives):
    return "\n\n".join(narratives)

# Generate a summary from multiple narratives
def generate_summary_from_narratives(narratives):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    compiled_narratives = compile_narratives(narratives)
    prompt = (
        f"Generate a comprehensive summary based on the following narratives:\n\n"
        f"{compiled_narratives}\n\n"
    )
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000
    )
    return response.choices[0].text.strip()

# Streamlit chat interface
st.title("Litter Density Analysis in Switzerland")
st.write("Ask me about litter density analysis, and I will provide detailed information.")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def get_response(user_input):
    matches = find_location_matches(user_input, known_locations)
    if matches:
        return f"We have information on the following locations: {', '.join(matches)}. Please choose one."
    else:
        query = user_input
        narratives = generate_narratives_for_query(query)
        summary = generate_summary_from_narratives(narratives)
        return f"Here is a summary of the results for {query}:\n\n{summary}"

user_input = st.text_input("You:", key='user_input')

if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    response = get_response(user_input)
    st.session_state['messages'].append({"role": "assistant", "content": response})

for message in st.session_state['messages']:
    st.write(f"{message['role']}: {message['content']}")
