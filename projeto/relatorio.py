from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

pdf.add_page()

pdf.titulo("Relatório de Cursos de Graduação no Brasil")
pdf.sub_titulo("Distribuição de Vagas e Modalidades por Região")
pdf.imagem("capa.jpg", 40, 90, 130)  
pdf.ln(160)
pdf.linha_centralizada("Autor: Enzo Jesael. B. C. Ortiz")
pdf.linha_centralizada("Data: 8 de Setembro de 2024")

pdf.add_page()

pdf.titulo_base("Gráfico 1: Total de Vagas Autorizadas por Região")

pdf.paragrafo("O gráfico mostra a quantidade total de vagas autorizadas para cursos de graduação por região. É possível observar quais regiões concentram mais vagas, ajudando a identificar padrões de distribuição de oportunidades de ensino superior no Brasil.")
pdf.imagem("Gráfico_vagasporregiao.png", 30, 80, 150)
pdf.ln(120)

pdf.paragrafo("Com base neste gráfico, podemos observar que a região Sudeste possui o maior número de vagas autorizadas, seguida pelas regiões Nordeste e Sul. Isso pode refletir a maior densidade populacional e o número de instituições de ensino nas regiões mencionadas.")

pdf.add_page()

pdf.titulo_base("Gráfico 2: Modalidades de Ensino por Região (EAD vs Presencial)")

pdf.paragrafo("Este gráfico apresenta a distribuição das modalidades de ensino (Educação a Distância - EAD, e Presencial) em cada região do Brasil. Ele ajuda a entender a predominância de uma modalidade em cada região.")
pdf.imagem("Gráfico_modalidade.png", 30, 80, 150)
pdf.ln(120)

pdf.paragrafo("Observando o gráfico, podemos ver que a modalidade de ensino a distância (EAD) é mais predominante em algumas regiões, como o Nordeste, enquanto outras regiões, como o Sul, mantêm uma proporção mais equilibrada entre EAD e presencial.")

pdf.add_page()

pdf.titulo_base("Gráfico 3: Vagas Autorizadas por Curso (Primeiros 10 Cursos)")

pdf.paragrafo("O gráfico a seguir mostra a quantidade de vagas autorizadas para os 10 primeiros cursos, conforme ordenado no banco de dados. Ele permite a visualização de quais cursos possuem mais vagas disponíveis para os alunos.")
pdf.imagem("Gráfico_vagascurso.png", 30, 80, 150)
pdf.ln(120)

pdf.paragrafo("A análise deste gráfico revela que cursos como Engenharia e Ciências da Computação possuem uma quantidade expressiva de vagas, refletindo a demanda crescente nessas áreas. Por outro lado, alguns cursos relacionados a humanidades e ciências sociais têm menos vagas disponíveis.")

pdf.add_page()

pdf.titulo_base("Gráfico 4: Carga Horária Total por Instituição (Primeiras 10 Instituições)")

pdf.paragrafo("Este gráfico exibe a carga horária total dos cursos oferecidos por cada uma das 10 primeiras instituições. A carga horária é um indicador importante da estrutura curricular e da duração dos cursos oferecidos.")
pdf.imagem("Gráfico_cargahoraria.png", 30, 80, 150)
pdf.ln(120)

pdf.paragrafo("Podemos observar que algumas instituições concentram uma carga horária mais extensa, indicando programas de graduação mais robustos e exigentes. Isso pode influenciar na escolha dos alunos, dependendo de suas preferências de tempo de estudo.")

pdf.add_page()

pdf.titulo_base("Conclusão")

pdf.paragrafo("Este relatório apresentou uma visão geral sobre a distribuição de vagas e modalidades de ensino nas diferentes regiões do Brasil, além de uma análise da carga horária e vagas autorizadas por curso e instituição. Com base nas análises, é possível identificar tendências e oportunidades de aprimoramento nas políticas educacionais, bem como entender o cenário atual do ensino superior no país.")

pdf.output("relatorio_graficos_cursos.pdf")
