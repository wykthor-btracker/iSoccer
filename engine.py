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
        return self.instance


class Funcionario(Pessoa):
    def __init__(self, nome, email, telefone, cpf, salario, **kwargs):
        super().__init__(nome, email, telefone, cpf)
        self.instance["Salário"] = salario
        for key in kwargs:
            self.instance[key] = kwargs[key]
# Classes

# Functions

# Functions

# Main


def main(*args, **kwargs):
    print(Funcionario("wykthor","a@a.a","9999-9999","00000000000","30",cargo="Prefeito").instance)
    return None


# Main


if __name__ == "__main__":
    main()


