from rest_framework import serializers  
from django.db.models import Q
from goods.models import Goods,GoodsCategory,IndexAd,Banner,GoodsImage,GoodsCategoryBrand
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image=serializers.ImageField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Goods.objects.create(**validated_data)
class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"
class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"
class CategorySerializer(serializers.ModelSerializer):
    sub_cat=CategorySerializer2(many=True)#sub_cat的变量名与models当中的related_name="sub_cat"一致
    class Meta:
        model = GoodsCategory
        fields = "__all__"
class GoodsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=GoodsImage
        fields=("image",)

class GoodsSerializer(serializers.ModelSerializer):
        category=CategorySerializer()
        images=GoodsImageSerializer(many=True)
        class Meta:
            model = Goods
            fields = "__all__"#('name', 'click_num', 'market_price', 'add_time')
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"
class IndexCategorySerialiizer(serializers.ModelSerializer):
    brands=BrandSerializer(many=True)
    goods=serializers.SerializerMethodField()
    sub_cat=CategorySerializer2(many=True)
    ad_goods=serializers.SerializerMethodField()


    def get_ad_goods(self,obj):
        goods={}
        ad_goods=IndexAd.objects.filter(category_id=obj.id)
        if ad_goods:
            good_ins=ad_goods[0].goods
            goods_json=GoodsSerializer(good_ins,many=False,context={'request':self.context['request']}).data
            #context={'request':self.context['request']}自定义的serializer加上这个才会自动添加域名
            return goods_json




    def get_goods(self,obj):
        all_goods=Goods.objects.filter(Q(category_id=obj.id)|
                               Q(category__parent_category_id=obj.id)|
                               Q(category__parent_category__parent_category_id=obj.id))
        goods_serializer=GoodsSerializer(all_goods,many=True,context={'request':self.context['request']})
        return goods_serializer.data
    class Meta:
        model = GoodsCategory
        fields = "__all__"
