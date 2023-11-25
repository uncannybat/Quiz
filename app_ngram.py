
import streamlit as st
from nltk import ngrams
from nltk.tokenize import word_tokenize


def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

def main():
    st.title("N-gram Generator")

    
    text_input = st.text_area("Enter Text:", "")

   
    n = st.slider("Select the order of N-gram:", 1, 5, 2)

    
    if st.button("Generate N-grams"):
        if text_input:
           
            n_grams = generate_ngrams(text_input, n)

           
            st.subheader(f"{n}-grams:")
            for gram in n_grams:
                st.write(gram)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
