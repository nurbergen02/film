from rest_framework import serializers
from .models import Movi, ProductReview, Rating
from django.contrib.auth import get_user_model

user = get_user_model()


class ProductListSerializer(serializers.ModelSerializer):
    """
        Класс для перевода типов данных Python в json формат
    """

    class Meta:
        """
            Класс для передачи дополнительных данных
        """
        model = Movi
        # fields = ('id','title', 'price', 'status')
        exclude = ("description", "image", "created_at")
        # fields = '__all__'
        # fields = ('title','status','description','price','image')


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movi
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(ProductDetailSerializer, self).to_representation(instance)
        representation['reviews'] = ProductReviewSerializer(
            ProductReview.objects.filter(product=instance.id),
            many=True
        ).data
        return representation


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta(ProductDetailSerializer.Meta):
        pass

    def validate_price(self, price):
        if price < 100:
            raise serializers.ValidationError('Цена не может быть отрицательной и меньше 100')
        return price


class ProductReviewSerializer(serializers.ModelSerializer):
    product_title = serializers.SerializerMethodField("get_product_title")

    def get_product_title(self, product_review):
        title = product_review.product.title
        return title

    class Meta:
        model = ProductReview
        fields = "__all__"

    def validate_product(self, product):
        if self.Meta.model.objects.filter(product=product).exists() == True:
            raise serializers.ValidationError('Вы уже оставляли отзыв на данных продукт')
        return product

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                'Рейтинг должен быть от 1 до 5'
            )
        return rating

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if not request.user.is_anonymous:
            representation["author"] = request.user.email
        return representation


# райтинг
class RatingSerializer(serializers.ModelSerializer):
    post_title = serializers.SerializerMethodField("get_post_title")

    class Meta:
        model = Rating
        # fields = 'all'
        exclude = ('author',)

    def get_post_title(self, rating):
        title = rating.post.title
        return title

    def validate_rating(self, rating):
        if rating not in range(1, 11):
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        return rating

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        # print(dir(instance) ,'Hellooooooo')
        if not request.user.is_anonymous:
            representation['author'] = request.user.email

        return representation
