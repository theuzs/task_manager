from core.models import Funcionario, Produto, Venda, Atividade
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class InsereFuncionarioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao'
        ]


# FORMULÁRIO DE INCLUSÃO DE Produtos
# -------------------------------------------

class InsereProdutoForm(forms.ModelForm):
    descricao = forms.CharField(
        label='Descrição',
        required=True,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Produto

        # Campos que estarão no form
        fields = [
            'nome',
            'descricao',
            'preco'
        ]


# FORMULÁRIO DE INCLUSÃO DE Vendas
# -------------------------------------------

class InsereVendaForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Venda

        # Campos que estarão no form
        fields = [
            'funcionario',
            'produto'
        ]

# FORMULÁRIO DE INCLUSÃO DE ATIVIDADES
# -------------------------------------------

class InsereAtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = [
            'funcionario',
            'titulo',
            'descricao',
            'data', 
            'status'
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[('pendente', 'Pendente'), ('concluida', 'Concluída')]),
        }

    def __init__(self, *args, **kwargs):
        super(InsereAtividadeForm, self).__init__(*args, **kwargs)
        # Personalizações adicionais podem ser feitas aqui, como
        # restringir a lista de funcionários disponíveis.
