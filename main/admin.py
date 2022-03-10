from django.contrib import admin
from .models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)

admin.site.register(Brand)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','color_bg')
admin.site.register(Color,ColorAdmin)

admin.site.register(Size)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Categories,CategoriesAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','brand','color','size','status','is_featured')
    list_editable = ('status','is_featured')
admin.site.register(Product,ProductAdmin)

#product attribute

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag','product','price','color','size',)
admin.site.register(ProductAttribute,ProductAttributeAdmin)

# order
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('user','total_amt','paid_status','order_dt')
admin.site.register(CartOrder,CartOrderAdmin)

# order items
class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no','item','image_tag','qty','price','total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)

# product review
class ProductReviewAdmin(admin.ModelAdmin):
	list_display=('user','product','review_text','get_review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)