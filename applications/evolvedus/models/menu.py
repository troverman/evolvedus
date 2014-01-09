################################################################
####menu.py#####################################################
################################################################

################################
####title#######################
################################  
if request.function == 'index':
    response.title = 'evurdd urrs'
else:
    response.title = request.function

################################
####meta########################
################################ 
response.meta.author = 'Trevor Overman'
response.meta.description = 'evolved us'
response.meta.keywords = 'evolved'
response.meta.generator = 'evolved'

################################
####analytics###################
################################ 
response.google_analytics_id = 'UA-22491760-14'
