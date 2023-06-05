from rest_framework import serializers
from api.models import Company, Employee

#create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    # company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())  
    class Meta:
        model=Employee
        fields="__all__"