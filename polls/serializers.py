from rest_framework import serializers
from .models import Choice


class ResultsSerializer(serializers.Serializer):
    choice = serializers.SerializerMethodField()

    def get_results(self, question_id):
        choices = Choice.objects.filter(question_id=question_id)

        results = []
        for choice in choices:
            results.append({
                'id': choice.id,
                'choice_text': choice.choice_text,
                'votes': choice.votes
            })

        return results
