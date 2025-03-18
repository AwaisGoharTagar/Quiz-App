import streamlit as st
import random

# Streamlit app setup
st.markdown("<h1 style='text-align: center;'>🧠 Quiz Game</h1>", unsafe_allow_html=True)

# Ask for user's name
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

st.session_state.user_name = st.text_input("Enter your name:", st.session_state.user_name)

if not st.session_state.user_name:
    st.warning("Please enter your name to start the quiz.")
    st.stop()

# Question bank with 100+ questions
questions = {
    "General Knowledge": [
        {"question": "What is the capital of France?", "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"], "answer": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A) Mars", "B) Jupiter", "C) Saturn", "D) Venus"], "answer": "A"},
        {"question": "What is the largest ocean?", "options": ["A) Atlantic", "B) Pacific", "C) Indian", "D) Arctic"], "answer": "B"},
        {"question": "Which language has the most speakers?", "options": ["A) English", "B) Spanish", "C) Mandarin", "D) Hindi"], "answer": "C"},
        {"question": "Who wrote 'Hamlet'?", "options": ["A) Shakespeare", "B) Dickens", "C) Tolstoy", "D) Austen"], "answer": "A"},
        {"question": "Who painted the Mona Lisa?", "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"], "answer": "C"},
        {"question": "Which country invented pizza?", "options": ["A) France", "B) Italy", "C) USA", "D) Greece"], "answer": "B"},
    ],
    "Science": [
        {"question": "What is the chemical symbol for water?", "options": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"], "answer": "B"},
        {"question": "What gas do plants absorb?", "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"], "answer": "B"},
        {"question": "What is the powerhouse of the cell?", "options": ["A) Nucleus", "B) Mitochondria", "C) Ribosome", "D) Cytoplasm"], "answer": "B"},
        {"question": "How many bones are in the human body?", "options": ["A) 206", "B) 205", "C) 210", "D) 201"], "answer": "A"},
        {"question": "Which planet has the most moons?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"], "answer": "D"},
        {"question": "What is the hardest natural substance on Earth?", "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"], "answer": "C"},
        {"question": "What type of energy is produced by the Sun?", "options": ["A) Nuclear", "B) Solar", "C) Geothermal", "D) Chemical"], "answer": "B"},
    ],
    "History": [
        {"question": "Who discovered America?", "options": ["A) Columbus", "B) Magellan", "C) Cook", "D) Marco Polo"], "answer": "A"},
        {"question": "Who was the first U.S. President?", "options": ["A) Lincoln", "B) Washington", "C) Jefferson", "D) Adams"], "answer": "B"},
        {"question": "What year did World War II end?", "options": ["A) 1942", "B) 1945", "C) 1950", "D) 1939"], "answer": "B"},
        {"question": "Which empire built the Great Wall of China?", "options": ["A) Roman", "B) Mongol", "C) Qing", "D) Ming"], "answer": "D"},
        {"question": "Which war was fought between the North and South regions of the United States?", "options": ["A) World War I", "B) Civil War", "C) Korean War", "D) Vietnam War"], "answer": "B"},
        {"question": "Who was the first emperor of China?", "options": ["A) Qin Shi Huang", "B) Kublai Khan", "C) Sun Yat-sen", "D) Confucius"], "answer": "A"},
    ],
    "Sports": [
        {"question": "How many players are in a soccer team?", "options": ["A) 10", "B) 11", "C) 12", "D) 9"], "answer": "B"},
        {"question": "Which country won the 2018 FIFA World Cup?", "options": ["A) Germany", "B) Brazil", "C) France", "D) Argentina"], "answer": "C"},
        {"question": "What is the national sport of Japan?", "options": ["A) Karate", "B) Judo", "C) Sumo Wrestling", "D) Baseball"], "answer": "C"},
        {"question": "How many rings are in the Olympic logo?", "options": ["A) 4", "B) 5", "C) 6", "D) 7"], "answer": "B"},
        {"question": "Which sport uses a shuttlecock?", "options": ["A) Tennis", "B) Squash", "C) Badminton", "D) Volleyball"], "answer": "C"},
        {"question": "How many holes are there in a standard golf course?", "options": ["A) 9", "B) 12", "C) 18", "D) 21"], "answer": "C"},
    ],
    "Technology": [
        {"question": "Who is the CEO of Tesla?", "options": ["A) Jeff Bezos", "B) Bill Gates", "C) Elon Musk", "D) Mark Zuckerberg"], "answer": "C"},
        {"question": "What does HTML stand for?", "options": ["A) Hyper Text Markup Language", "B) High Tech Modern Language", "C) Hyperlink Transfer Machine Language", "D) Hyper Text Management Language"], "answer": "A"},
        {"question": "What is the most used programming language?", "options": ["A) Python", "B) JavaScript", "C) C++", "D) Java"], "answer": "B"},
        {"question": "Which company made the first iPhone?", "options": ["A) Samsung", "B) Google", "C) Apple", "D) Nokia"], "answer": "C"},
        {"question": "Which company created the Windows operating system?", "options": ["A) Apple", "B) Google", "C) Microsoft", "D) IBM"], "answer": "C"},
        {"question": "What is the name of the AI assistant in iPhones?", "options": ["A) Alexa", "B) Siri", "C) Google Assistant", "D) Cortana"], "answer": "B"},
    ],
    "Geography": [
        {"question": "What is the longest river in the world?", "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"], "answer": "B"},
        {"question": "Which country has the most natural lakes?", "options": ["A) Canada", "B) USA", "C) Russia", "D) India"], "answer": "A"},
        {"question": "What is the smallest country in the world?", "options": ["A) Vatican City", "B) Monaco", "C) San Marino", "D) Liechtenstein"], "answer": "A"},
        {"question": "Which desert is the largest?", "options": ["A) Sahara", "B) Arctic", "C) Gobi", "D) Kalahari"], "answer": "B"},
    ],
    "Entertainment": [
        {"question": "Who played Iron Man in the Marvel movies?", "options": ["A) Chris Evans", "B) Robert Downey Jr.", "C) Chris Hemsworth", "D) Mark Ruffalo"], "answer": "B"},
        {"question": "Which movie won the Best Picture Oscar in 2020?", "options": ["A) 1917", "B) Joker", "C) Parasite", "D) Once Upon a Time in Hollywood"], "answer": "C"},
        {"question": "Who is the King of Pop?", "options": ["A) Prince", "B) Elvis Presley", "C) Michael Jackson", "D) Justin Timberlake"], "answer": "C"},
    ],
}

# Get all questions and shuffle
all_questions = [q for category in questions.values() for q in category]
random.shuffle(all_questions)

# Session state to track quiz progress
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.shuffled_questions = all_questions[:len(all_questions)]

# Show Questions
if st.session_state.current_question < len(st.session_state.shuffled_questions):
    q = st.session_state.shuffled_questions[st.session_state.current_question]

    st.subheader(f"Question {st.session_state.current_question + 1}")
    st.write(q["question"])
    user_answer = st.radio("Choose an option:", q["options"], index=None, key=f"q{st.session_state.current_question}")

    if st.button("Submit Answer"):
        correct_answer = q["answer"]

        if user_answer and user_answer.startswith(correct_answer):
            st.success("✅ Correct! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is {correct_answer}.")

        st.session_state.current_question += 1
        st.rerun()

# Final Score
if st.session_state.current_question >= len(st.session_state.shuffled_questions):
    st.subheader(f"🎯 Quiz Completed, {st.session_state.user_name}!")
    st.write(f"**{st.session_state.user_name}, your final score is: {st.session_state.score}/{len(all_questions)}**")
    
    if st.button("Play Again 🔄"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.shuffled_questions = all_questions[:len(all_questions)]
        st.rerun()
