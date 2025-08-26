from django.contrib import admin

# Register your models here.
from .models import Member, Settings, Payment, MemberActivityLog

class MemberAdmin(admin.ModelAdmin):
    actions = None
    list_display = ("memberNumber", "name", "lastname", "dni", "home", "isActive")
    list_display_links = ("memberNumber", "name", "lastname", "dni", "home", "isActive")
    search_fields = ("name", "lastname", "dni", "memberNumber")  # buscador arriba
    list_filter = ("isActive", "sex")
    # list_display = ("memberNumber", "name", "lastname", "dni", "sex", "memberDischargeDate")
    def get_fields(self, request, obj=None):
        if obj:  # si obj existe → estamos editando
            return ( "memberNumber","isActive", "name", "lastname", "dni", "home", "birthdate", "memberRegistrationDate", "email", "phone", "celular","sex" ,"observations")
        else:  # si obj es None → estamos creando
            return ( "memberNumber", "name", "lastname", "dni", "home", "birthdate", "memberRegistrationDate", "email", "phone", "celular","sex" ,"observations")
    def get_readonly_fields(self, request, obj=None):
      if obj:  # obj existe → estamos editando
          return ("memberRegistrationDate",)  # solo lectura al editar
      return ()  # al crear, no es de solo lectur

admin.site.register(Member, MemberAdmin)

class SettingsAdmin(admin.ModelAdmin):
    actions = None
    list_display = ("paymentAmount",)
    # # Evitar que se agreguen nuevos registros
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Settings, SettingsAdmin)


def actualPaymentAmount():
    settings = Settings.objects.first()
    if settings:
        return settings.paymentAmount
    return 0  # fallback si no hay registro  


class PaymentAdmin(admin.ModelAdmin):
    actions = None
    list_filter = ("month", "method")  # filtros que aparecen a la derecha
    list_display = ("member__memberNumber", "member__name", "member__lastname", "month", "amount", "date", "method")
    list_display_links = ("member__memberNumber", "member__name", "member__lastname", "month", "amount", "date", "method")
    search_fields = ('member__name', 'member__lastname', 'member__dni')
    autocomplete_fields = ("member",)  # buscador arriba
    
    def member__memberNumber(self, obj):
        return obj.member.memberNumber
    member__memberNumber.short_description = "Número de Socio"

    def member__name(self, obj):
        return obj.member.name
    member__name.short_description = "Nombre"

    def member__lastname(self, obj):
        return obj.member.lastname
    member__lastname.short_description = "Apellido"
    
    def get_changeform_initial_data(self, request):
        """
        Se ejecuta cuando se abre el formulario de "Añadir".
        """
        initial = super().get_changeform_initial_data(request)

        settings = Settings.objects.first()
        if settings:
            initial['amount'] = settings.paymentAmount  # 👈 valor inicial en admin

        return initial

admin.site.register(Payment, PaymentAdmin)

class MemberActivityLogAdmin(admin.ModelAdmin):
    actions = None
    list_display = ("member_memberNumber", "member_name", "member_lastname", "activity", "date")
    list_filter = ("activity", "date")  # filtros que aparecen a la derecha
    search_fields = ('member__name', 'member__lastname', 'member__dni', "member__memberNumber")
    
    def member_memberNumber(self, obj):
        return obj.member.memberNumber
    member_memberNumber.short_description = "Número de Socio"

    def member_name(self, obj):
        return obj.member.name
    member_name.short_description = "Nombre"

    def member_lastname(self, obj):
        return obj.member.lastname
    member_lastname.short_description = "Apellido"
    
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj = ...):
        return False
admin.site.register(MemberActivityLog, MemberActivityLogAdmin)
    