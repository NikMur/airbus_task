# airbus_task

Description of solution file code!

First I import necessary python libraries, including os for file operations and pandas for data manipulation.
Than i define pathes for images directories:
train_image_dir is constructed using os.path.join() to connect the base directory with the directory containing training images, '../input/airbus-ship-detection/train_v2'.
Similarly, test_image_dir is connected using os.path.join() with the directory containing test images, '../input/airbus-ship-detection/test_v2'.

Than I use os.listdir(test_image_dir) to retrieve a list of filenames of test images present in the specified directory, and then
iterate over the filenames and store them in the test_files list.

A pandas DataFrame, submission_df, is created with the column 'ImageId' initialized with the filenames of test images.
I add another column 'EncodedPixels' to store the predicted segmentation masks for ships. Initially, all values are set to None.
Than I print the total number of images in the test dataset using an f-string with the len() function to get the length of the test_files list.
and The first few rows of the submission_df DataFrame using the head().
Finally, the DataFrame is saved to a CSV file 'submission.csv'.
