from .models import Collections
from .serializers import CollectionsSerializer
from rest_framework import generics,filters,views,response
import json
from .paginations import CustomPagination
# import logging
# logger = logging.getLogger('django-watchcollection')

class CollectionsCreate(generics.ListCreateAPIView):
    # API endpoint that allows creation of a new Collection  
    
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
    

class CollectionsList(generics.ListAPIView):
    # API endpoint that allows Collection to be viewed.
    
    
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['created']
    search_fields = ['agents', 'collection_title']
    pagination_class = CustomPagination
    



class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
    

class CollectionrequestFilter(generics.ListAPIView):
    serializer_class = CollectionsSerializer
    def get_queryset(self):
        print("self:",self.request.query_params)
        email = self.request.query_params.get('email')
       
        print("email:",email)
        queryset = Collections.objects.filter(clients__contains=[{"email":email}],mark_as_ready=True)        
        return queryset  
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['updated_at']
    search_fields = ['collection_title']

class CollectionAgentFilter(generics.ListAPIView):
    serializer_class = CollectionsSerializer
    def get_queryset(self):
        print("self:",self.request.query_params)
        email = self.request.query_params.get('email')
       
        print("email:",email)
        queryset = Collections.objects.filter(agents__contains=[{"email":email}])        
        return queryset  
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['collection_title']
    


class CollectionAgentMarkUsReady(generics.ListAPIView):
    serializer_class = CollectionsSerializer
    def get_queryset(self):
        email = self.request.query_params.get('email')
        queryset = Collections.objects.filter(agents__contains=[{"email":email}],mark_as_ready=True)        
        return queryset  
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['updated_at']
    search_fields = ['collection_title']
        
class CollectionCountStatus(views.APIView):
    
    def get_object(self, pk):
        print("self.kwargs['pk']:",pk)
        accepted,rejected,submitted,requested = 0,0,0,0      
        col_obj=Collections.objects.get(id=pk)
        for req in col_obj.requests['structure']['sections']:
            if(req['requests']):
                for reqs in req['requests']:
                    
                    if reqs['status'] == 'Accepted':
                        accepted=accepted+1
                    elif reqs['status'] == 'Rejected':
                        rejected=rejected+1
                    elif reqs['status'] == 'Submitted':
                        submitted=submitted+1
                    else:
                        requested=requested+1
                        
            if(req['sub_section']):
                for reqs in req['sub_section']:
                    for sub_reqs in req['requests']:
                        
                        if sub_reqs['status'] == 'Accepted':
                            accepted=accepted+1
                        elif sub_reqs['status'] == 'Rejected':
                            rejected=rejected+1
                        elif sub_reqs['status'] == 'Submitted':
                            submitted=submitted+1
                        else:
                            requested=requested+1

        return {'accepted':accepted,'rejected':rejected,'submitted':submitted,'requested':requested}
    
    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        return response.Response(queryset)