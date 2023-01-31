from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json
from polls.serializers import ResultsSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getResults(request, question_id):
    results = ResultsSerializer.get_results(request, question_id)
    json_data = json.dumps(results)
    return Response(json.loads(json_data))

