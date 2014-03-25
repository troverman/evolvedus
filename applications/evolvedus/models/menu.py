################################################################
####menu.py#####################################################
################################################################

################################
####title#######################
################################  
if request.function == 'index':
    response.title = 'evolved us'
else:
    response.title = request.function

################################
####meta########################
################################ 
response.meta.author = 'Trevor Overman'
response.meta.description = 'evolved us'
response.meta.keywords = 'evolved'
response.meta.generator = 'evolved'

