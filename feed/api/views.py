from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings

from.serializers import FeedSerializer
from feed.models import Feed

from django.db.models import F

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

class FeedList(generics.ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedDetail(generics.RetrieveAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedAPIList(APIView):
    permission_classes = (AllowAny,)
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request, format=None):
        feed = Feed.objects.all()
        page = self.paginate_queryset(feed)
        serializer = FeedSerializer(feed, many=True)

        return self.get_paginated_response(serializer.data)
  
    def post(self, request, format=None):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
         """
         Return a single page of results, or `None` if pagination is disabled.
         """
         if self.paginator is None:
             return None
         return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
         """
         Return a paginated style `Response` object for the given output data.
         """
         assert self.paginator is not None
         return self.paginator.get_paginated_response(data) 

class FeedAPIDetail(APIView):
    permission_classes = (AllowAny,)
    """
    Retrieve, update or delete a transformer instance
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Feed.objects.get(pk=pk)
        except Feed.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        feed = self.get_object(pk)
        
        counter, _ = Feed.objects.get_or_create(id = pk)
        counter.view = F('view')+1
        counter.save(update_fields=["view"])
        
        serializer = FeedSerializer(feed)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        feed = self.get_object(pk)
        serializer = FeedSerializer(feed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        feed = self.get_object(pk)
        serializer = FeedSerializer(feed,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        feed = self.get_object(pk)
        feed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
