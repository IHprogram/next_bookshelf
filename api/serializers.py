from rest_framework import serializers
# DjangoのデフォルトのUserモデルを利用
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # パスワードはwrite_only(入力できるが、readできない設定)と必須にする
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

        def create(self, validated_data):
            # Djangoに用意されているcreate_userメソッドを使って、
            # 新しくユーザーを作成(通常のserializerのcreateではパスワードが暗号化されないため)
            user = User.objects.create_user(**validated_data)
            return user