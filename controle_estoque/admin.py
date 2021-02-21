from django.contrib import admin

from .models import Representante, Fornecedor, Tecido, Pedido

@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
    fieldssets = [
        ('Dados do Representante',      {'fields': ('nome', 'email', 'telefone')})
    ]

    list_display = ('id', 'nome', 'email', 'telefone')

    def representante(self, instance):
        return f'{instance.representante.nome}'


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados do Fornecedor',         {'fields': ('nome', 'email', 'telefone', 'site', 'representante')})
    ]

    list_display = ('id', 'nome', 'email', 'telefone', 'site', 'representante')

    def representante(self, instance):
        return f'{instance.representante.get_full_name}'


@admin.register(Tecido)
class TecidoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações do Tecído',           {'fields': ('nome', 'fornecedor', 'medida', 
                                                        'rendimento', 'estampa', 'estampa_exclusiva')})
    ]

    list_display = ('id', 'nome', 'fornecedor', 'medida', 'rendimento', 'estampa', 'estampa_exclusiva')

    def tecido(self, instance):
        return f'{instance.tecido.nome}'

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações do Pedido',           {'fields': ('tecido', 'fornecedor',
                                             'representante', 'quantidade', 'data_compra', 'data_entrega')})
    ]

    list_display = ('id', 'tecido', 'fornecedor', 'representante', 'quantidade', 'data_compra', 'data_entrega')

    def pedido(self, instance):
        return f'{instance.pedido.nome}'