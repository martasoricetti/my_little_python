from final_software import RelationalDataProcessor, RelationalQueryProcessor
from final_software import TriplestoreDataProcessor, TriplestoreQueryProcessor
from final_software import GenericQueryProcessor

# first create the relational
# database using the related source data
rel_path = "publications.db"
rel_dp = RelationalDataProcessor()
rel_dp.setDbPath(rel_path)
rel_dp.uploadData("relational_publications.csv")
rel_dp.uploadData("relational_other_data.json")

# Then, create the RDF triplestore (remember first to run the
# Blazegraph instance) using the related source data
grp_endpoint ="http://192.168.131.1:9999/blazegraph/sparql" #use your Blazegraph service URL + "/sparql"
grp_dp = TriplestoreDataProcessor()
grp_dp.setEndpointUrl(grp_endpoint)
#grp_dp.uploadData("graph_publications.csv")
#grp_dp.uploadData("graph_other_data.json")

# In the next passage, create the query processors for both
# the databases, using the related classes
rel_qp = RelationalQueryProcessor()
rel_qp.setDbPath(rel_path) 
grp_qp = TriplestoreQueryProcessor()
grp_qp.setEndpointUrl( grp_endpoint)


# Finally, create a generic query processor for asking
# about data
generic = GenericQueryProcessor()
generic.addQueryProcessor(rel_qp)
generic.addQueryProcessor(grp_qp)


#now you can execute all the methods of the GenericQueryProcessor (use print)
print(generic.getPublicationInVenue("issn:1588-2861"))
#for x in generic.getPublicationsPublishedInYear("2016"):
    #print(x.getIds())
    
print(generic.getPublicationsPublishedInYear("2016"))

print(generic.getDistinctPublisherOfPublications(['doi:10.1007/s11192-018-2705-y', 'doi:10.1080/2157930x.2018.1439293']))
