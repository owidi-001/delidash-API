from rest_framework.schemas import AutoSchema
import coreapi
import coreschema


class RegistrationSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.upper() == "POST":
            extra_fields = [
                coreapi.Field(
                    "name", required=True, location="form", schema=coreschema.String()
                ),
                coreapi.Field(
                    "email", required=True, location="form", schema=coreschema.String()
                ),
                coreapi.Field(
                    "phone_number",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        pattern=r"\+254\w{9}",
                        description="must start with 07... eg 07 xxxx xxxx",
                    ),
                ),
                coreapi.Field("password", required=True, location="form"),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class UserLoginSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        fields = [
            coreapi.Field("email", required=True, location="form"),
            coreapi.Field("password", required=True, location="form"),
        ]
        manual_fields = super().get_manual_fields(path, method)
        return fields + manual_fields


class ProfileSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.upper() in ["PATCH"]:
            extra_fields = [
                coreapi.Field(
                    "name", required=False, location="form", schema=coreschema.String()
                ),
                # coreapi.Field(
                #     "email", required=False, location="form", schema=coreschema.String()
                # ),
                # coreapi.Field(
                #     "phone_number",
                #     required=False,
                #     location="form",
                #     schema=coreschema.String(
                #         pattern=r"\+254\w{9}",
                #         description="must start with 07... eg 07 xxxx xxxx",
                #     ),
                # )
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields



"""
For changing current user password
"""
class ChangePasswordSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = [
            coreapi.Field("old_password", required=True, location="form"),
            coreapi.Field("new_password", required=True, location="form"),
        ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


"""
For resetting password/Forgot password
"""
class ResetPasswordSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = [
            coreapi.Field("email", required=True, location="form"),
        ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields