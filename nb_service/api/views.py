from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from nb_service import models
from nb_service import filtersets
from . import serializers

class ICViewSet(NetBoxModelViewSet):
    queryset = models.IC.objects.all()
    serializer_class = serializers.ICSerializer
    filterset_class = filtersets.ICFilter


class ServiceViewSet(NetBoxModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

class ApplicationViewSet(NetBoxModelViewSet):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

class RelationViewSet(NetBoxModelViewSet):
    queryset = models.Relation.objects.all()
    serializer_class = serializers.RelationSerializer

    @action(detail=False, methods=['get'], url_path='graph')
    def graph(self, request):
        """
        Returns service relationships in Grafana Node Graph format

        Returns:
            {
                "nodes": [{"id": "...", "title": "...", ...}],
                "edges": [{"id": "...", "source": "...", "target": "...", "mainStat": "..."}]
            }
        """
        # Collect unique services from all relations
        nodes = {}
        edges = []

        relations = models.Relation.objects.all()

        for rel in relations:
            # Add source service node
            source_id = str(rel.source.service.id)
            if source_id not in nodes:
                nodes[source_id] = {
                    "id": source_id,
                    "title": rel.source.service.name,
                    "subTitle": "Service",
                    "mainStat": "",
                    "arc__success": 0.5,
                    "arc__errors": 0,
                    "detail__role": "service"
                }

            # Add destination service node
            dest_id = str(rel.destination.service.id)
            if dest_id not in nodes:
                nodes[dest_id] = {
                    "id": dest_id,
                    "title": rel.destination.service.name,
                    "subTitle": "Service",
                    "mainStat": "",
                    "arc__success": 0.5,
                    "arc__errors": 0,
                    "detail__role": "service"
                }

            # Add edge
            edges.append({
                "id": str(rel.id),
                "source": source_id,
                "target": dest_id,
                "mainStat": rel.link_text or "connected",
                "detail__relationship": rel.link_text or ""
            })

        return Response({
            "nodes": list(nodes.values()),
            "edges": edges
        })

class PenTestViewSet(NetBoxModelViewSet):
    queryset = models.PenTest.objects.all()
    serializer_class = serializers.PenTestSerializer


class GrafanaNodeGraphView(APIView):
    """
    Dedicated API endpoint for Grafana Node Graph visualization
    Returns service relationships in Grafana-compatible format
    """
    permission_classes = []  # Public endpoint

    def get(self, request):
        # Collect unique services from all relations
        nodes = {}
        edges = []

        relations = models.Relation.objects.all()

        for rel in relations:
            # Add source service node
            source_id = str(rel.source.service.id)
            if source_id not in nodes:
                nodes[source_id] = {
                    "id": source_id,
                    "title": rel.source.service.name,
                    "subTitle": "Service",
                    "mainStat": "",
                    "arc__success": 0.5,
                    "arc__errors": 0,
                    "detail__role": "service"
                }

            # Add destination service node
            dest_id = str(rel.destination.service.id)
            if dest_id not in nodes:
                nodes[dest_id] = {
                    "id": dest_id,
                    "title": rel.destination.service.name,
                    "subTitle": "Service",
                    "mainStat": "",
                    "arc__success": 0.5,
                    "arc__errors": 0,
                    "detail__role": "service"
                }

            # Add edge
            edges.append({
                "id": str(rel.id),
                "source": source_id,
                "target": dest_id,
                "mainStat": rel.link_text or "connected",
                "detail__relationship": rel.link_text or ""
            })

        return Response({
            "nodes": list(nodes.values()),
            "edges": edges
        })