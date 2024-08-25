from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, mixins
from pymantic import sparql
import requests

# from rest_framework.permissions import IsAuthenticated
from .models import User
from django.http import Http404
from .serializers import CustomerSerializer
from django.contrib.auth.decorators import login_required


# Create your views here.
class Customers(APIView):

    def get_object(self):
        try:
            return User.objects.all()
        except User.DoesNotExist:
            return Http404

    def get(self, request):
        print(self.get_object())
        serializer = CustomerSerializer(self.get_object(), many=True)
        return Response(serializer.data)


# @login_required
# def customers(request):
#     queryset = User.objects.all()
#     context = {
#         "customers": queryset,
#     }
#     return render(request, "table/customers.html", context)


class CustomersViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer


class GraphView(APIView):
    def get(self, request):
        server = sparql.SPARQLServer("http://172.20.0.1:9999/blazegraph/sparql")
        server.update("load <file:///home/orbit/Downloads/freightm8/media/profile-pictures/olympics.ttl>")
        result = server.query("select * where { <http://blazegraph.com/blazegraph> ?p ?o }")

        for b in result["results"]["bindings"]:
            print("%s %s", b["p"]["value"], b["o"]["value"])
        return Response((b["p"]["value"], b["o"]["value"]) for b in result["results"]["bindings"])

    def post(self, request):

        namespace = request.data["namespace"]
        # properties = {
        #     "com.bigdata.namespace.testdb.spo.com.bigdata.btree.BTree.branchingFactor": 1024,
        #     "com.bigdata.rdf.store.AbstractTripleStore.textIndex": False,
        #     "com.bigdata.rdf.store.AbstractTripleStore.axiomsClass": "com.bigdata.rdf.axioms.NoAxioms",
        #     "com.bigdata.rdf.sail.isolatableIndices": False,
        #     "com.bigdata.rdf.sail.truthMaintenance": False,
        #     "com.bigdata.rdf.store.AbstractTripleStore.justify": False,
        #     "com.bigdata.rdf.sail.namespace": namespace,
        #     "com.bigdata.namespace.testdb.lex.com.bigdata.btree.BTree.branchingFactor": 400,
        #     "com.bigdata.rdf.store.AbstractTripleStore.quads": False,
        #     "com.bigdata.journal.Journal.groupCommit": False,
        #     "com.bigdata.rdf.store.AbstractTripleStore.geoSpatial": False,
        #     "com.bigdata.rdf.store.AbstractTripleStore.statementIdentifiers": False,
        # }
        properties = f"""
        com.bigdata.rdf.store.AbstractTripleStore.vocabularyClass=com.bigdata.rdf.vocab.core.BigdataCoreVocabulary_v20160317
com.bigdata.rdf.store.AbstractTripleStore.textIndex=true
com.bigdata.rdf.store.AbstractTripleStore.axiomsClass=com.bigdata.rdf.axioms.NoAxioms
com.bigdata.rdf.sail.isolatableIndices=false
com.bigdata.rdf.sail.truthMaintenance=false
com.bigdata.rdf.store.AbstractTripleStore.justify=false
com.bigdata.rdf.sail.namespace={namespace}
com.bigdata.rdf.store.AbstractTripleStore.quads=true
com.bigdata.namespace.quad.spo.com.bigdata.btree.BTree.branchingFactor=1024
com.bigdata.journal.Journal.groupCommit=false
com.bigdata.namespace.quad.lex.com.bigdata.btree.BTree.branchingFactor=400
com.bigdata.rdf.store.AbstractTripleStore.geoSpatial=false
com.bigdata.rdf.store.AbstractTripleStore.statementIdentifiers=false


        """

        headers = {"Content-Type": "text/plain;charset=iso-8859-1"}
        create_namespace_url = "http://172.20.0.1:9999/blazegraph/namespace"

        response = requests.post(create_namespace_url, headers=headers, data=properties, params={"name": namespace})
        print(response.content)
        if response.status_code == 201:
            print(f"Namespace '{namespace}' created successfully.")
            return Response(f"Namespace '{namespace}' created successfully.")
        else:
            print(f"Failed to create namespace {namespace}. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return Response({f"Failed to create namespace:Response: {response.text}"})
