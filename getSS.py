import pandas as pd

# The URL to your online Excel file (must be a direct link)
url = 'https://hwdsbonca-my.sharepoint.com/:x:/g/personal/dwgreen_hwdsb_on_ca/IQAUGhfI6JYKQ5pgEw7MQ7OeAeLzgA9uesAkp0DfeUlVhfk?e=L1jGZu&nav=MTVfezg4QjA1Mzg5LTMyN0QtNDM2OS04MjMyLUVDMDUzNTJDMEQxMH0'

try:
    # Use pandas read_excel to load the data from the URL
    df = pd.read_excel(url)
    
    # Display the first few rows of the DataFrame
    print(df.head())
    
    # You can now perform data analysis or manipulation on the DataFrame (df)

except Exception as e:
    print(f"An error occurred: {e}")
    print("Ensure the URL is a direct link to the file and that the file is publicly accessible.")
