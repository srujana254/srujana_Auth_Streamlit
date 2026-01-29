import streamlit as st

# header
st.header("Hello,I am Srujana")

# Title
st.title("title")

# Subheader
st.subheader("subheader")

# text method to display information
st.text("Text")

# markdown (used to draw lines)
st.markdown("----------------------------------------------------------------------")
st.markdown("### this is Markdown")
st.markdown("**Bold Text**")
st.markdown("*Italic Text*")
st.markdown(" - item 1 \n - item 2\n - item 3")
st.markdown("<h3 style='color:red'>Red Text</h3>", unsafe_allow_html=True)

# write (Most fexible function (text,numbers,.ists,dicts,dataframes))
st.write("write method")
st.write([1, 2, 34, 5])

# caption
st.caption("This is a caption")

# code
st.code(
    """
        def add(a,b):
          return a+b
        """,
    language="python",
)

# latex
st.latex(r""" a^2 + b^2 = c^2 """)

# divider
st.divider()

# button
if st.button("Click Me"):
    st.write("Button Clicked")
    st.success("Success Message")
    st.balloons()
    st.snow()
else:
    st.write("Button Not Clicked")
    st.error("Connection Error")

# text input
user_input = st.text_input("Enter your name")
# st.write("User Input:", user_input)
# st.write(f"Hello,{user_input}!")
if user_input == "":
    st.warning("Please enter your name")
elif not user_input.isalpha():
    st.error("Name should contain only alphabets")
else:
    st.success(f"Hello, {user_input}!")
# multi text
multi_text = st.text_area("Enter multiple lines of text")
st.write("Multi-line Text:", multi_text)

# checkbox
if st.checkbox("Show/Hide"):
    st.write("Checkbox is checked")

# radio button
status = st.radio("Select your status", ("Active", "Inactive"))
st.write("Status:", status)

st.divider()

# select box
city = st.selectbox(
    "Select your city", ("HYD", "New York", "Los Angeles", "Chicago", "Houston")
)
st.write("City:", city)

st.divider()

# multiselect
fruits = st.multiselect(
    "Select your favorite fruits", ("Apple", "Banana", "Mango", "Orange", "Grapes")
)
st.write("Fruits:", fruits)

st.divider()

# slider
age = st.slider("Select your age", 0, 100, 25)  # min:0, max:100, default:25
st.write("Age:", age)

st.divider()

# file uploader
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.success("File uploaded successfully")
    st.write("Filename:", uploaded_file.name)

st.divider()

# form method to create a form and form_submit_button
with st.form("my_forma"):
    st.write("Inside the form")
    name = st.text_input("Enter your name")
    submitted = st.form_submit_button("Submit")
if submitted:
    st.success(f"Hello, {name}!")


st.divider()

# login
with st.form("login_form"):
    st.write("Login Form")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_submitted = st.form_submit_button("Login")
if login_submitted:
    st.success(f"Welcome, {username}!")

st.divider()

# columns method to create columns
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is column 1")
with col3:
    st.header("Column 3")
    st.write("This is column 3")
with col2:
    st.header("Column 2")
    st.write("This is column 2")

st.divider()

# CONTAINERS
with st.container():
    st.header("Container Example")
    st.write("This is inside the container")
    with st.form("continer_form"):
        st.write("Form inside container")
        data = st.text_input("Enter some data")
        container_submitted = st.form_submit_button("Submit Data")
    if container_submitted:
        st.success(f"You entered: {data}")

st.divider()

# table
data = {
    "Name": ["Anurag", "Sumit", "Rohit"],
    "Age": [21, 22, 20],
    "Course": ["B.Tech", "M.Tech", "BBA"],
}
st.table(data)

st.divider()

# sidebar
st.sidebar.title("Menu")
option = st.sidebar.radio("Go to", ["Home", "About", "Contact"])
st.sidebar.write("You selected:", option)


st.divider()


# cache method to store the data
@st.cache_data
def LOAD_DATA():
    return [1, 2, 3, 4, 5]


data = LOAD_DATA()
st.write("Cached Data:", data)
