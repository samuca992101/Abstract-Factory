from abc import ABC, abstractmethod

class Cabecalho(ABC):
    @abstractmethod
    def gerar_cabecalho(self) -> str:
        pass

class Conteudo(ABC):
    @abstractmethod
    def gerar_conteudo(self) -> str:
        pass

class Rodape(ABC):
    @abstractmethod
    def gerar_rodape(self) -> str:
        pass

class CabecalhoPDF(Cabecalho):
    def gerar_cabecalho(self) -> str:
        return "Cabeçalho do PDF"

class ConteudoPDF(Conteudo):
    def gerar_conteudo(self) -> str:
        return "Conteúdo do PDF"

class RodapePDF(Rodape):
    def gerar_rodape(self) -> str:
        return "Rodapé do PDF"

class CabecalhoDOCX(Cabecalho):
    def gerar_cabecalho(self) -> str:
        return "Cabeçalho do DOCX"

class ConteudoDOCX(Conteudo):
    def gerar_conteudo(self) -> str:
        return "Conteúdo do DOCX"

class RodapeDOCX(Rodape):
    def gerar_rodape(self) -> str:
        return "Rodapé do DOCX"

class CabecalhoExcel(Cabecalho):
    def gerar_cabecalho(self) -> str:
        return "Cabeçalho do EXCEL"
    
class ConteudoExcel(Conteudo):
    def gerar_conteudo(self) -> str:
        return "Conteudo do EXCEL"

class RodapeExcel(Rodape):
    def gerar_rodape(self) -> str:
        return "Rodape do EXCEL"

class CabecalhoCsv(Cabecalho):
    def gerar_cabecalho(self) -> str:
        return "Cabecalho do CSV"

class ConteudoCsv(Conteudo):
    def gerar_conteudo(self) -> str:
        return "Conteudo do CSV"

class RodapeCsv(Rodape):
    def gerar_rodape(self) -> str:
        return "Rodape do CSV"

class FabricaRelatorio(ABC):
    @abstractmethod
    def criar_cabecalho(self) -> Cabecalho:
        pass

    @abstractmethod
    def criar_conteudo(self) -> Conteudo:
        pass

    @abstractmethod
    def criar_rodape(self) -> Rodape:
        pass

class FabricaRelatorioPDF(FabricaRelatorio):
    def criar_cabecalho(self) -> Cabecalho:
        return CabecalhoPDF()
    def criar_conteudo(self) -> Conteudo:
        return ConteudoPDF()
    def criar_rodape(self) -> Rodape:
        return RodapePDF()
    
class FabricaRelatorioEXCEL(FabricaRelatorio):
    def criar_cabecalho(self) -> Cabecalho:
        return CabecalhoExcel()
    def criar_conteudo(self) -> Conteudo:
        return ConteudoExcel()
    def criar_rodape(self) -> Rodape:
        return RodapeExcel()
    
class FabricaRelatorioCSV(FabricaRelatorio):
    def criar_cabecalho(self) -> Cabecalho:
        return CabecalhoCsv()
    def criar_conteudo(self) -> Conteudo:
        return ConteudoCsv()
    def criar_rodape(self) -> Rodape:
        return RodapeCsv()

class FabricaRelatorioDOCX(FabricaRelatorio):
    def criar_cabecalho(self) -> Cabecalho:
        return CabecalhoDOCX()
    def criar_conteudo(self) -> Conteudo:
        return ConteudoDOCX()
    def criar_rodape(self) -> Rodape:
        return RodapeDOCX()
