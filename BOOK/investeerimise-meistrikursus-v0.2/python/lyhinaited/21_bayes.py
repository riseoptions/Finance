# Bayesi uuendus
p_hea,p_pos_hea,p_pos_halb=.10,.80,.20
p_pos=p_hea*p_pos_hea+(1-p_hea)*p_pos_halb
posterior=p_hea*p_pos_hea/p_pos
print(f"P(hea | positiivne test): {posterior:.4%}")
