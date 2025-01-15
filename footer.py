import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Footer with LinkedIn and GitHub links
developer_email = 'rimeshcdry45@gmail.com'
def footer_page():    
    st.markdown("---")
    st.markdown("© 2025 Rimesh Chaudhary. All rights reserved.")
    st.markdown("🏠 House Price Prediction™ is a trademark of Rimesh Chaudhary.")
    st.markdown("### Connect with me:")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/rimesh-chaudhary/) | [GitHub](https://github.com/RimeshCdry/)")
    # Contact Information Section with form
    st.markdown("### Contact Information")
    st.markdown("If you have any questions or suggestions, feel free to reach out!")

    # Email form
    with st.form(key='contact_form'):
        email = st.text_input("Your Email Address")
        message = st.text_area("Your Message/Suggestions")
        submit_button = st.form_submit_button(label="Send Message")

        if submit_button:
            if email and message:
                # You can use an SMTP server to send an email, or use a service like SendGrid
                try:
                    # Setup your SMTP server
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    
                    # Log in to your email account (Replace with your own credentials)
                    server.login("your_email@gmail.com", "your_password")
                    
                    # Prepare the email
                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = f"{developer_email}"
                    msg['Subject'] = "Suggestion or Query from House Price Prediction App"
                    body = f"Message from {email}:\n\n{message}"
                    msg.attach(MIMEText(body, 'plain'))
                    
                    # Send email
                    server.sendmail(email, "your_email@gmail.com", msg.as_string())
                    server.quit()

                    # Inform the user
                    st.success("Your message has been sent successfully!")
                except Exception as e:
                    st.error(f"Error sending email: {e}")
            else:
                st.warning("Please provide both your email address and message.")
