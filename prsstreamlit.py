import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def gather_student_preferences():
    st.title("Project Recommendation System")

    # Using Streamlit's text input and select box widgets for user inputs
    knowledge_level = st.selectbox("Your level of knowledge in technology:", ["Beginner", "Intermediate", "Advanced"])
    domain_of_interest = st.text_input("Your domain of interest:")
    technology_preference = st.text_input("List your technology preferences (e.g., Python, IoT, Machine Learning): ")
    relevant_fields = st.text_input("Relevant fields of interest:")
    goal_objective = st.text_input("Your goal/objective:")

    return {
        'Knowledge Level': knowledge_level,
        'Domain of Interest': domain_of_interest,
        'Technology Preference': technology_preference,
        'Relevant Fields of Interest': relevant_fields,
        'Goal/Objective': goal_objective
    }

def encode_student_preferences(student_preferences, project_features):
    encoded_preferences = {feature: 0 for feature in project_features}

    # Mapping knowledge level, domain of interest, technology preference, and relevant fields of interest
    # Adjust these mappings to ensure they align with the features in your project dataset
    feature_mappings = {
        'Knowledge Level': 'Complexity Level_',
        'Domain of Interest': 'Domain_',
        'Technology Preference': 'Technology Stack_',
        'Relevant Fields of Interest': 'Field_',
        'Goal/Objective': 'Goal_'
    }

    for pref_category, feature_prefix in feature_mappings.items():
        selected_option = student_preferences[pref_category]
        feature_name = f"{feature_prefix}{selected_option}"

        # Only add the feature if it exists in the project features
        if feature_name in encoded_preferences:
            encoded_preferences[feature_name] = 1

    return encoded_preferences

def main():
    st.title("Project Recommendation System")

    # Define options for each dropdown
    knowledge_level_options = ["Beginner", "Intermediate", "Advanced"]
    domain_of_interest_options = ["IoT", "Cybersecurity", "Web Development", "Data Science", "AI", "Mobile App Development", "Cloud Computing", "Game Development", "Machine Learning", "Blockchain"]
    technology_preference_options = ["Python", "Java", "JavaScript", "C#", "C++", "Ruby", "Go", "Swift", "Kotlin", "PHP"]
    relevant_fields_options = ["Creative Arts", "Marketing & Advertising", "Finance & Economics", "Healthcare & Medicine", "Education & Training", "Engineering & Manufacturing", "Environmental Science", "Legal & Policy", "Social Sciences", "Entertainment & Media"]
    goal_objective_options = ["Learning new skills", "Starting a career", "Personal project", "Academic research", "Gaining domain expertise"]

    # Dropdowns for user input
    knowledge_level = st.selectbox("Your level of knowledge in technology:", knowledge_level_options)
    domain_of_interest = st.selectbox("Your domain of interest:", domain_of_interest_options)
    technology_preference = st.selectbox("Your technology preference:", technology_preference_options)
    relevant_fields = st.selectbox("Relevant fields of interest:", relevant_fields_options)
    goal_objective = st.selectbox("Your goal/objective:", goal_objective_options)

    # Submit button
    if st.button('Submit'):
        # Once the button is pressed, process the inputs
        student_preferences = {
            'Knowledge Level': knowledge_level,
            'Domain of Interest': domain_of_interest,
            'Technology Preference': technology_preference,
            'Relevant Fields of Interest': relevant_fields,
            'Goal/Objective': goal_objective
        }
        # Encode student preferences
        encoded_preferences = encode_student_preferences(student_preferences, project_features)

        # Convert encoded preferences to DataFrame
        encoded_preferences_df = pd.DataFrame([encoded_preferences])

        # Calculate cosine similarity and get top projects
        similarity_scores = cosine_similarity(encoded_preferences_df, final_projects_df[project_features])
        flattened_similarity_scores = similarity_scores.flatten()
        similarity_scores_df = pd.DataFrame({'Similarity Score': flattened_similarity_scores, 'Project ID': final_projects_df['Project ID'], 'Project Name': final_projects_df['Project Name']})
        top_matching_projects = similarity_scores_df.sort_values(by='Similarity Score', ascending=False).head(5)

        # Display the recommended projects
        st.write("Top Matching Projects:")
        st.table(top_matching_projects)


# Load your preprocessed project dataset
# Ensure you have the path to your dataset correctly specified
final_projects_df = pd.read_csv("C:/Users/Joshua Ilangovan/OneDrive/Documents/Project Recommendation System/2nd-preprocessed_dataset.csv")
project_features = final_projects_df.columns.drop(['Project ID', 'Project Name'], errors='ignore')

if __name__ == "__main__":
    main()