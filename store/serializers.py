from rest_framework import serializers
from .models import Categories, Coupons, Roles, Profile, Products

class CategoriesSerializer(serializers.ModelSerializer):
	children = serializers.SerializerMethodField()

	class Meta:
		model = Categories
		fields = ['id', 'name', 'slug', 'description', 'parent', 'active', 'created_at', 'updated_at', 'children']
		read_only_fields = ['slug', 'created_at', 'updated_at', 'children']

	def get_children(self, obj):
		if obj.children.exists():
			return CategoriesSerializer(obj.children.all(), many=True).data
		return []

class CouponsSerializer(serializers.ModelSerializer):
    is_valid = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Coupons
        fields = [
            'id',
            'code',
            'description',
            'coupon_type',
            'discount_value',
            'active',
            'valid_from',
            'valid_to',
            'usage_limit',
            'used_count',
            'created_at',
            'updated_at',
            'is_valid',
        ]
        read_only_fields = ['used_count', 'created_at', 'updated_at', 'is_valid']

    def get_is_valid(self, obj):
        return obj.is_valid()

class RolesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Roles
		fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Show username/email instead of ID
    role = RolesSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Roles.objects.all(), source='role', write_only=True, allow_null=True, required=False
    )

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'role',
            'role_id',
            'phone_number',
            'profile_image',
            'date_of_birth',
            'gender',
            'address_line1',
            'address_line2',
            'city',
            'state',
            'postal_code',
            'country',
            'email_verified',
            'phone_verified',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

class ProductsSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(), many=True, write_only=True, source='categories')

    class Meta:
        model = Products
        fields = [
            'id',
            'code',
            'name',
            'slug',
            'categories',      # nested read-only
            'category_ids',    # write-only for input
            'description',
            'price',
            'discount_price',
            'stock',
            'active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']