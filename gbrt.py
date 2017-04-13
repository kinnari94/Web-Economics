#import graphlab module
import graphlab as gl

#read training data CSV to variable 'data'
data = gl.SFrame.read_csv('train.csv', verbose=False)

#read validation data CSV to variable 'testdata'
testdata = gl.SFrame.read_csv('validation.csv', verbose=False)

#create logisic regression classifier from chosen features
#data = train.csv
#click is target

model = gl.boosted_trees_regression.create(data, target='click', features=[ 'slotheight', 'slotwidth' ,'advertiser','city','hour'],max_iterations=20, validation_set=None)


#predict the PCTR values against the validation dataset,
#testdata = validation.csv
#values = predicted values

values = model.predict(testdata)


#test model prediction, prints first 5 rows
print values.head(5)


#add values as a column
#values = values from the prediction
#newdata is the new variable for this new Sframe
#testdata is our validation dataset

newdata = testdata.add_column(values, name='PCTR_GBRT')


#SAVING
newdata.save('validationprediction1.csv', format='csv')


