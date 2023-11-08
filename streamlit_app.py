import openai
import streamlit as st

# Set up your OpenAI API key
api_key = st.secrets["openai"]["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"]
openai.api_key = api_key

# Define a function to interact with the chatbot
def chat_with_bot():
    st.title("Travel Itinerary Chatbot")
    st.sidebar.write("Chat with the chatbot to plan your travel itinerary")

    # Initialize conversation history using session state
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input:
            # Append user input to the conversation history
            st.session_state.conversation.append(f"You: {user_input}")

            # Call the ChatGPT API to generate a response
            response = openai.Completion.create(
                engine="davinci",
                prompt="\n".join(st.session_state.conversation),
                max_tokens=50  # Adjust as needed
            )

            # Get the bot's reply from the API response
            bot_reply = response.choices[0].text

            # Append the bot's reply to the conversation history
            st.session_state.conversation.append(f"Chatbot: {bot_reply}")

    # Display the entire conversation
    st.subheader("Chat History")
    for message in st.session_state.conversation:
        st.write(message)

if __name__ == "__main__":
    chat_with_bot()
