import time
import streamlit as st
from Setup import setup
from Style import style

# on_click function for the submit button
def submit():
    # Check if the 'name' and 'issue' fields are filled
    if not st.session_state['name'] or not st.session_state['issue']:
        st.warning('Please fill in both the Name and Issue fields.')
        st.session_state['form_submitted'] = False
    else:
        # Set the form submitted state to True
        st.session_state['form_submitted'] = True
        # Reset the form fields
        st.session_state['name'] = ''
        st.session_state['email'] = ''
        st.session_state['issue'] = ''

# Render the form 
def report_an_issue():
    st.title('Report An Issue')
    st.write('Please fill out the form below to report an issue.')

    with st.form(key='report_issue_form'):
        st.text_input(
            label='Name',
            help='Enter your name',
            placeholder='John Doe',
            max_chars=50,
            key='name'
        )
        st.text_input(
            label='Email (Optional)',
            help='Enter your email if you wish to be contacted regarding the issue.',
            placeholder="johndoe@joe.com",
            max_chars=50,
            key='email'
        )
        st.text_area(
            label='Describe the issue',
            max_chars=500,
            help='Please provide a detailed description of the issue you are facing.',
            placeholder='Issue Description...',
            key='issue'
        )
        st.form_submit_button('Submit', on_click=submit)

    # Display the submission message below the form
    if 'form_submitted' not in st.session_state:
        st.session_state['form_submitted'] = False

    if st.session_state['form_submitted']:
        with st.spinner('Submitting your issue...'):
            time.sleep(1)
            st.success('Issue Submitted!')
            st.session_state['form_submitted'] = False

# run the page
setup(title="Report An Issue", sidebar="expanded")
report_an_issue()
style()
