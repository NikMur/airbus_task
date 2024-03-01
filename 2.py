# Retrieve a list of filenames of test images
test_files =[f for f in os.listdir(test_image_dir) ]
# Create a DataFrame 
submission_df = pd.DataFrame({'ImageId':test_files})
# Add a column for encoded pixel predictions , default value - None
submission_df['EncodedPixels']=None
# Display the first few rows of the DataFrame
submission_df.head()