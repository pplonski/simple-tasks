from rest_framework import serializers
import tasks.models as models
import cerberus

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        read_only_fields = ('id', 'state', 'result', 'task_id', 'created_by')
        fields = ('params', 'id', 'state', 'result', 'task_id', 'created_by', 'parent_organization')
        extra_kwargs = {
            'parent_organization': {'write_only': True}
        }

    def validate_params(self, params):
        if params is None or params == '':
            raise serializers.ValidationError("Params cannot be empty")

        schema = {'arg1': {'type': 'integer', 'required': True},
                  'arg2': {'type': 'integer', 'required': True}}
        validator = cerberus.Validator(schema)

        if not validator.validate(params):
            raise serializers.ValidationError(validator.errors)
        return params
