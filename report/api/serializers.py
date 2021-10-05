from rest_framework import serializers
from report.models import Report, Category

class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'