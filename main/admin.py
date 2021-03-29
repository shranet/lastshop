from django.contrib import admin
from .models import Unit, Category, PromoCode, Setting
from client.models import User


class UserAdmin(admin.ModelAdmin):
    # fields = [
    #     'username',
    #     'password',
    #     'first_name',
    #     'last_name'
    # ]

    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'date_joined',
        'is_staff',
        'is_superuser'
    ]

    class Meta:
        model = User


admin.site.register(User, UserAdmin)


def make_on_sidebar(modeladmin, request, queryset):
    queryset.update(on_sidebar=True)


def make_on_sidebar_false(modeladmin, request, queryset):
    queryset.update(on_sidebar=False)

make_on_sidebar.short_description = "Bosh sahifada chiqarish"
make_on_sidebar_false.short_description = "Bosh sahifadan olib tashlash"


class CategoryAdmin(admin.ModelAdmin):
    actions = [make_on_sidebar, make_on_sidebar_false]
    fields = [
        'parent',
        'name_uz',
        'name_ru',
        'on_sidebar',
        'on_sidebar_order'
    ]

    list_display = [
        'id',
        'name',
        'parent',
        'on_sidebar',
        'on_sidebar_order'
    ]

    def name(self, row):
        return row.name

    # def save_form(self, request, form, change):
    #     category = form.save(commit=False)
    #     category.admin = request.user
    #     # category.save()
    #
    #     return super().save_form(request, form, change)

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class UnitAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name_uz',
        'name_ru'
    ]

    class Meta:
        model = Unit


admin.site.register(Unit, UnitAdmin)


class SettingAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'value'
    ]

    class Meta:
        model = Setting

admin.site.register(Setting, SettingAdmin)
