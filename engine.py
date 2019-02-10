# -*- encoding: utf-8 -*-

# imports
import pandas as pd
from re import fullmatch
# imports

# Variables

# Variables

# Classes


class Validation():
    @classmethod
    def validatethis(cls, name, kind):
        if(kind == "name"):
            cls.validatename(name)
        elif(kind == "email"):
            cls.validateemail(name)
        elif(kind == "address"):
            cls.validateaddress(name)
        elif (kind == "cpf"):
            cls.validatecpf(name)
        elif(kind=="telephone"):
            cls.validatetelephone(name)
    @staticmethod
    def validatename(name):
        try:
            assert(fullmatch(r'[a-zA-Z]+', name) is not None)
        except:
            if(name == ""):
                raise Exception("Nome Vazio.")
            raise Exception("{} não é um nome válido, apenas a-zA-Z permitido para manter compatibilidade.".format(name))

    @staticmethod
    def validateemail(name):
        try:
            assert(fullmatch(r'.*@.*\..*', name) is not None)
        except:
            raise Exception("{} é um email inválido, formato aceito: nome@dominio.com(.br)".format(name))

    @staticmethod
    def validateaddress(name):
        try:
            assert(fullmatch(r'[a-zA-Z\.,]+', name) is not None)
        except:
            raise Exception("{} é um endereço inválido, apenas letras, números, vírgulas e ponto aceitos, escreva o nome "
                            "completo.".format(name))

    @staticmethod
    def validatecpf(name):
        try:
            assert(fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', name) is not None or fullmatch(r'\d{11}', name) is not None)
        except:
            raise Exception("{} é um cpf inválido, formatos aceitos: xxx.xxx.xxx-xx ou xxxxxxxxxxx onde x é um inteiro.".format(name))

    @staticmethod
    def validatetelephone(name):
        try:
            assert(fullmatch(r'\d{8,9}',name) is not None or fullmatch(r'\d{4,5}-\d{4}', name) is not None)
        except:
            raise Exception("{} é um número invalido, formatos aceitos: xxxxx-xxxx ou (x)xxxxxxxx onde x é um inteiro".format(name))

    @staticmethod
    def validatevalue(name):
        try:
            assert(fullmatch(r'R\$\d+\.\d+,\d+', name))
        except:
            raise Exception("{} é uma quantitade inválida, formato aceito: R$xx.xx,xx".format(name))


class Pessoa():
    def __init__(self, nome, email, telefone, cpf):
        """
        todos os parametros são passados como string.
        :param nome:
        :param email:
        :param telefone:
        :param cpf:
        """
        campos = [nome,email,telefone,cpf]
        validar = ["name","email","telephone","cpf"]
        for campo in range(len(campos)):
            Validation.validatethis(campos[campo],validar[campo])
        self.instance = pd.DataFrame([[nome, email, telefone]], columns=["Nome", "Email", "Telefone"], index=[cpf])
        self.instance.index.names = ["CPF"]

    def __str__(self):
        return self.instance.__str__()


class Funcionario(Pessoa):
    def __init__(self, nome, email, telefone, cpf, salario, **kwargs):
        super().__init__(nome, email, telefone, cpf)
        self.instance["Salário"] = salario
        cargosvalidos = ["Presidente", "Médico", "Técnico", "Preparador", "Motorista", "Cozinheiro", "Advogado", "Jogador"]
        if("cargo" in kwargs):
            if kwargs["cargo"] not in cargosvalidos:
                raise Exception("{} é um cargo inválido".format(kwargs["cargo"]))

        for key in kwargs:
            self.instance[key] = kwargs[key]


class Socio(Pessoa):
    def __init__(self, nome, email, telefone, cpf, endereco, valor, tipo, situ):
        super().__init__(nome, email, telefone, cpf)
        self.instance["Contribuição"] = valor
        self.instance["Classe"] = tipo
        self.instance["Situação"] = situ
        self.instance["Endereço"] = endereco


class Recurso():
    def __init__(self, nome, disponivel):
        self.nome = nome
        self.disponivel = disponivel
        self.instance = pd.DataFrame([[disponivel]], columns=["Disponibilidade"], index=[nome])
        self.instance.index.names = ["Nome"]

    def get(self, campo):
        if(campo in self.instance.columns):
            return self.instance[campo]
        else:
            return None

    def set(self, campo, valor):
        if(campo in self.instance.columns):
            self.instance[campo] = valor
        else:
            return False
        return True

    def __str__(self):
        return self.instance.__str__()


class Estadio(Recurso):
    def __init__(self, nome, disponivel, capacidade, banheiros, lanchonetes):
        super().__init__(nome, disponivel)
        self.instance["capacidade"] = capacidade
        self.instance["banheiros"] = banheiros
        self.instance["lanchonetes"] = lanchonetes


class Centro(Recurso):
    def __init__(self, nome, disponivel, dormitorios):
        super().__init__(nome, disponivel)
        self.instance["dormitorios"] = dormitorios

# Classes

# Functions

# Functions

# Main


def main():
    print(Funcionario("wykthor", "a@a.a", "9999-9999", "00000000000", "30", cargo="Técnico"))
    return None


# Main


if __name__ == "__main__":
    main()


