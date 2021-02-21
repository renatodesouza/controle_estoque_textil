from django.db import models


class Representante(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField('E-mail')
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Representante'
        verbose_name_plural = 'Representantes'


class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField('E-mail')
    telefone = models.CharField(max_length=30)
    site = models.CharField('Site', max_length=50)
    representante = models.ForeignKey(Representante, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


class Tecido(models.Model):
    KILOS = 'KG'
    METROS = 'MT'

    TIPO_DE_MEDIDA = [
        (KILOS, 'Kg'),
        (METROS, 'MT')
    ]

    nome = models.CharField(max_length=50)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    rendimento = models.FloatField('Rendimento')
    estampa = models.BooleanField('Estampado', default=False)
    estampa_exclusiva = models.BooleanField('Estampa Exclusiva', default=False)
    
    medida = models.CharField('Unidade Medida', max_length=2, choices=TIPO_DE_MEDIDA, default='METROS')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tecído'
        verbose_name_plural = 'Tecídos'


class Pedido(models.Model):
    tecido = models.ForeignKey(Tecido, on_delete=models.PROTECT)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    representante = models.ForeignKey(Representante, on_delete=models.PROTECT)
    quantidade = models.FloatField('Quantidade')
    data_compra = models.DateField('Data da Compra')
    data_entrega = models.DateField('Data da entrega')

    def __str__(self):
        return self.tecido.nome

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    
