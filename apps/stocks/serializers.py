from rest_framework import serializers


class OptionGrantsSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    start_date = serializers.DateField()
    cliff_months = serializers.IntegerField()
    duration_months = serializers.IntegerField()

    class Meta:
        fields = ['quantity', 'start_date', 'cliff_months', 'duration_months']
    
class CompanyValuationsSerializer(serializers.Serializer):
    price = serializers.DecimalField(decimal_places=2, max_digits=10)
    valuation_date = serializers.DateField()

    class Meta:
        fields = ['price', 'valuation_date']

class VestedEquityValueSerializer(serializers.Serializer):
    option_grants = OptionGrantsSerializer()
    company_valuations = CompanyValuationsSerializer(many=True)

    class Meta:
        fields = ['option_grants', 'company_valuations']
