import graphlab as gl
train_data = gl.SFrame.read_csv("E:\ML\Handwriting\\train.csv")

digit_classifier_v2 = gl.boosted_trees_classifier.create(train_data, "label", verbose=True)

#Load the Test Data:
test_data = gl.SFrame.read_csv('E:\ML\Handwriting\\test.csv')

#Classify the test data using the Model:
results = digit_classifier_v2.classify(test_data)

#Write the results to an output file.
f = open("C:\Users\joyeung\AppData\Local\Continuum\Anaconda\envs\dato-env\\v4results.csv", 'w')
results.print_rows(num_rows=28000, num_columns=1, output_file=f)
f.close()


