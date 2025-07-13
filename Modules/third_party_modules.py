# Third party modules in python :- 

'''
Third-party modules are Python libraries or packages developed by others (not built into Python) that you can install separately to add more functionality to your programs.

They are not included by default, but you can easily install them using pip, Python's package manager.
'''


'''
Why Use Third-Party Modules ? 

Add powerful features quickly (e.g., data analysis, web development, APIs)
Save time by using pre-written and optimized code
Access large communities and frequent updates
'''


# How to Install Third-Party Modules :- 
'''
pip install module_name

Example :- 
pip install numpy
'''



# Example of popular third party module :- 
'''
| Module                     | Description                                                     |
| -------------------------- | --------------------------------------------------------------- |
| **`numpy`**                | Numerical operations and arrays                                 |
| **`pandas`**               | Data analysis and manipulation                                  |
| **`matplotlib`**           | Plotting and data visualization                                 |
| **`requests`**             | Send HTTP requests (e.g., fetch web data)                       |
| **`flask`**                | Lightweight web framework                                       |
| **`django`**               | Full-featured web framework                                     |
| **`beautifulsoup4`**       | Web scraping HTML/XML                                           |
| **`openpyxl`**             | Read/write Excel files                                          |
| **`pygame`**               | Game development                                                |
| **`scikit-learn`**         | Machine learning                                                |
| **`tensorflow` / `torch`** | Deep learning                                                   |
| **`tkinter`** *(built-in)* | GUI development *(Note: technically built-in, not third-party)* |
'''



import pandas as pd

# Create a simple DataFrame (like a table)
data = {
    'Name': ['Karan', 'Anjali', 'yash'],
    'Marks': [85, 92, 78]
}

df = pd.DataFrame(data)

# Display the data
print("Student Data:\n", df)

# Calculate average marks
average = df['Marks'].mean()
print("\nAverage Marks:", average)

