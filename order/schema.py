import coreschema
from rest_framework.schemas import AutoSchema, ManualSchema
import coreapi


class OrderSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.upper() == "POST":
            extra_fields = [
                coreapi.Field("delivery_address", required=True, location="form",
                              schema=coreschema.Object(required=True, description="Order location to be saved")),
            ]

        if method.upper() == "Patch":
            extra_fields = [
                coreapi.Field("id", required=False, location="form",
                              schema=coreschema.Integer(description="Order id to be updated")),
                coreapi.Field("status", required=False, location="form",
                              schema=coreschema.String(description="Order status update")),
                coreapi.Field("quantity", required=False, location="form",
                              schema=coreschema.String(description="Order quantity update")),                            
                coreapi.Field("note", required=False, location="form",
                              schema=coreschema.Object(required=False, description="Note object to be updated")),
            ]

        if method.upper() == "DELETE":
            extra_fields = [
                coreapi.Field("id", required=False, location="form",
                              schema=coreschema.Integer(description="Order id to be deleted")),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields