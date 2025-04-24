import streamlit as st
import wikipedia

st.set_page_config(page_title="Wikipedia Q&A", page_icon="📚")

st.title("📚 Wikipedia Q&A")
st.write("Ask any question and get a summary from Wikipedia.")

query = st.text_input("Enter your query", "")

if query:
    try:
        page = wikipedia.page(query)
        st.subheader(f"📖 {page.title}")
        st.write(page.summary[:1000] + "...")
        st.markdown(f"[🔗 View Full Article]({page.url})")
    except wikipedia.exceptions.DisambiguationError as e:
        st.warning("Your query returned multiple results. Be more specific.")
        st.write("**Suggestions:**")
        st.write(e.options)
    except wikipedia.exceptions.PageError:
        st.error("Page not found. Try a different query.")
    except Exception as ex:
        st.error(f"An error occurred: {ex}")
