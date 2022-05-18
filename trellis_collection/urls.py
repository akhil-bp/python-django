from django.urls import path
from .views import CollectionsCreate, CollectionsList,CollectionDetail,CollectionrequestFilter,CollectionAgentFilter,CollectionCountStatus,CollectionAgentMarkUsReady
urlpatterns = [
    
    path("api/createcollection/", CollectionsCreate.as_view(), name="create-collection"),
    path("api/getallcollection/", CollectionsList.as_view(), name="list-collection"),
    path('api/getcollectiondetail/<int:pk>/', CollectionDetail.as_view(),name='collection-detail'),
    path('api/getclientcollection/', CollectionrequestFilter.as_view(),name="client-filter"),
    path('api/getagentcollection/', CollectionAgentFilter.as_view(),name="agent-filter"),
    path('api/agentcollectionmarkusready/', CollectionAgentMarkUsReady.as_view(),name="agent-filter"),
    path('api/getcollectionstatus/<int:pk>/', CollectionCountStatus.as_view(),name="collection-status"),
    

]