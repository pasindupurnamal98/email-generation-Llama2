import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import time

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    # Custom CSS for animations and styling
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    @keyframes pulse {
        0% { opacity: 0.6; }
        50% { opacity: 1; }
        100% { opacity: 0.6; }
    }
    
    .loading-text {
        animation: pulse 1.5s ease-in-out infinite;
        color: #1e3a8a;
        font-size: 1.2em;
        font-weight: 500;
    }
    
    @keyframes slideIn {
        from {
            transform: translateY(20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    .email-container {
        animation: slideIn 0.5s ease-out;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header with emoji and title
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center;'>📧 Cold Mail Generator</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666;'>Generate personalized cold emails from job postings</p>", unsafe_allow_html=True)
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Input section with better styling
    with st.container():
        st.markdown("### 🔗 Enter Job Posting URL")
        url_input = st.text_input("", value="https://boards.rooster.jobs/jobs/509285?source=linkedin", 
                                  placeholder="Paste the job posting URL here...")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submit_button = st.button("🚀 Generate Cold Email", use_container_width=True, type="primary")
    
    if submit_button:
        if not url_input:
            st.error("⚠️ Please enter a valid URL")
            return
            
        try:
            # Loading animation for fetching URL
            with st.spinner("🌐 Fetching job posting..."):
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                time.sleep(0.5)  # Small delay for better UX
            
            # Loading animation for portfolio
            with st.spinner("📁 Loading portfolio..."):
                portfolio.load_portfolio()
                time.sleep(0.5)
            
            # Loading animation for extracting jobs
            with st.spinner("🔍 Analyzing job requirements..."):
                jobs = llm.extract_jobs(data)
                time.sleep(0.5)
            
            if not jobs:
                st.warning("⚠️ No job information could be extracted from this URL")
                return
            
            # Process each job
            for idx, job in enumerate(jobs):
                st.markdown("---")
                
                # Display job info
                with st.expander(f"📋 Job Details #{idx + 1}", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**🏢 Role:** {job.get('role', 'N/A')}")
                        st.markdown(f"**📍 Location:** {job.get('location', 'N/A')}")
                    with col2:
                        st.markdown(f"**💼 Experience:** {job.get('experience', 'N/A')}")
                        skills = job.get('skills', [])
                        if skills:
                            st.markdown(f"**🛠️ Skills:** {', '.join(skills[:5])}{'...' if len(skills) > 5 else ''}")
                
                # Drafting animation
                progress_placeholder = st.empty()
                progress_bar = st.progress(0)
                
                # Animated drafting process
                drafting_steps = [
                    "🔍 Matching skills with portfolio...",
                    "📝 Drafting email introduction...",
                    "💡 Adding value propositions...",
                    "🎯 Personalizing content...",
                    "✨ Finalizing email..."
                ]
                
                for i, step in enumerate(drafting_steps):
                    progress_placeholder.markdown(f"<p class='loading-text'>{step}</p>", unsafe_allow_html=True)
                    progress_bar.progress((i + 1) / len(drafting_steps))
                    time.sleep(0.3)
                
                # Generate email
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                
                # Clear progress indicators
                progress_placeholder.empty()
                progress_bar.empty()
                
                # Display generated email with animation
                st.markdown("<div class='email-container'>", unsafe_allow_html=True)
                st.success("✅ Email generated successfully!")
                
                # Email display with copy button
                col1, col2 = st.columns([10, 1])
                with col1:
                    st.markdown("### 📧 Generated Cold Email")
                with col2:
                    if st.button("📋", key=f"copy_{idx}", help="Copy to clipboard"):
                        st.toast("Email copied to clipboard! 📋", icon="✅")
                
                # Display the email
                st.code(email, language='markdown')
                
                # Additional options
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🔄 Regenerate", key=f"regen_{idx}"):
                        st.rerun()
                with col2:
                    if st.button("💾 Save Draft", key=f"save_{idx}"):
                        st.toast("Draft saved! 💾", icon="✅")
                with col3:
                    if st.button("📤 Export", key=f"export_{idx}"):
                        st.download_button(
                            label="Download Email",
                            data=email,
                            file_name=f"cold_email_{idx}.txt",
                            mime="text/plain"
                        )
                
                st.markdown("</div>", unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"❌ An Error Occurred: {e}")
            with st.expander("🔍 Error Details"):
                st.code(str(e))
    
    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #888;'>Made with ❤️ using Streamlit & LangChain</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(
        layout="wide", 
        page_title="Cold Email Generator", 
        page_icon="📧",
        initial_sidebar_state="collapsed"
    )
    create_streamlit_app(chain, portfolio, clean_text)