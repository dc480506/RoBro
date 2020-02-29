import pickle
some_list = [[1,2,3],[4,56]]

#store data inside "some_file.p"
pickle.dump( some_list, open( "some_file.p", "wb" ) )

#load data from "some_file.p"
other_list= pickle.load( open( "some_file.p", "rb" ) )
print(other_list)