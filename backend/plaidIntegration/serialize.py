from rest_framework import serializers
from .models import plaidUser
from flask import Flask 
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode

app = Flask(__name__)

class plaidUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = plaidUser
        fields = ('name', 'email', 'token', 'access_token')
