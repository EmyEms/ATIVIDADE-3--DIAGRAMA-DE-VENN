# Função para representar a implicação lógica P → Q
def implica(p, q):
    return not p or q

# Função para gerar a tabela verdade
def gerar_tabela_verdade():
    # Cabeçalho da tabela
    print(f"{'P':<5}{'Q':<5}{'M':<5}{'P → Q':<10}{'P ∨ Q → R':<15}{'¬P → (M → R)':<15}{'R'}")
    
    # Todas as combinações possíveis de P, Q e M
    for p in [True, False]:
        for q in [True, False]:
            for m in [True, False]:
                # Avaliar proposições
                p_implies_q = implica(p, q)
                p_or_q = p or q
                m_implies_r = implica(m, p_or_q)
                not_p_implies_m_implies_r = implica(not p, m_implies_r)
                
                # Determinar R (se a festa é animada)
                if p:  # Se Ana vai à festa, Bruno também vai, e a festa é animada
                    r = p_or_q
                else:  # Se Ana não vai, depende de Bruno trazer música
                    r = not_p_implies_m_implies_r
                
                # Mostrar resultados da tabela verdade
                print(f"{p:<5}{q:<5}{m:<5}{p_implies_q:<10}{p_or_q:<15}{not_p_implies_m_implies_r:<15}{r}")

# Chamar a função para gerar a tabela verdade
gerar_tabela_verdade()
