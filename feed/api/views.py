from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from.serializers import FeedSerializer
from feed.models import Feed

from django.db.models import F

class FeedList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedAPIList(APIView):
    permission_classes = (IsAuthenticated,)
  
    def get(self, request, format=None):
        feed = Feed.objects.all()
        serializer = FeedSerializer(feed, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedAPIDetail(APIView):
    permission_classes = (IsAuthenticated,)
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
