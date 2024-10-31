import unittest
from projeto import *
class TestFabricaRelatorio(unittest.TestCase):
    
    def test_fabrica_relatorio_pdf(self):
        fabrica = FabricaRelatorioPDF()
        self.assertEqual(fabrica.criar_cabecalho().gerar_cabecalho(), "Cabeçalho do PDF")
        self.assertEqual(fabrica.criar_conteudo().gerar_conteudo(), "Conteúdo do PDF")
        self.assertEqual(fabrica.criar_rodape().gerar_rodape(), "Rodapé do PDF")

    def test_fabrica_relatorio_docx(self):
        fabrica = FabricaRelatorioDOCX()
        self.assertEqual(fabrica.criar_cabecalho().gerar_cabecalho(), "Cabeçalho do DOCX")
        self.assertEqual(fabrica.criar_conteudo().gerar_conteudo(), "Conteúdo do DOCX")
        self.assertEqual(fabrica.criar_rodape().gerar_rodape(), "Rodapé do DOCX")

    def test_fabrica_relatorio_excel(self):
        fabrica = FabricaRelatorioEXCEL()
        self.assertEqual(fabrica.criar_cabecalho().gerar_cabecalho(), "Cabeçalho do EXCEL")
        self.assertEqual(fabrica.criar_conteudo().gerar_conteudo(), "Conteudo do EXCEL")
        self.assertEqual(fabrica.criar_rodape().gerar_rodape(), "Rodape do EXCEL")

    def test_fabrica_relatorio_csv(self):
        fabrica = FabricaRelatorioCSV()
        self.assertEqual(fabrica.criar_cabecalho().gerar_cabecalho(), "Cabecalho do CSV")
        self.assertEqual(fabrica.criar_conteudo().gerar_conteudo(), "Conteudo do CSV")
        self.assertEqual(fabrica.criar_rodape().gerar_rodape(), "Rodape do CSV")

if __name__ == "__main__":
    unittest.main()
