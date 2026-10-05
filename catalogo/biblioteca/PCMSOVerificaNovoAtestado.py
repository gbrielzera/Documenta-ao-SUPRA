# PCMSOVerificaNovoAtestado
# Caminho: Catálogo > Biblioteca de scripts > PCMSOVerificaNovoAtestado
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def PCMSOVerificaNovoAtestado(matricula, idOcorrencia):
    
    valor = 0
     
    valor = DB.ExecuteScalar(" SELECT COUNT(a.emplid) FROM ps_gp_abs_event a, ps_GP_PIN b, PS_GP_ABS_RSN_LANG C, PS_GP_ABS_TAKE d, PS_GPBR_ABS_EV_AI e, ps_BBTS_APOSENTADO f, Pessoa g, cp_Pessoa h, Orgao i WHERE a.emplid = e.emplid AND a.pin_TAKE_num = e.pin_TAKE_num AND a.bgn_dt = e.bgn_dt AND a.end_dt = e.end_dt AND a.pin_TAKE_num = b.pin_num  AND a.pin_TAKE_num   = d.pin_num AND d.ABS_TYPE_OPTN = c.ABS_TYPE_OPTN AND A.ABSENCE_REASON = C.ABSENCE_REASON AND G.Id_Pessoa = H.Id_Pessoa  AND A.Emplid = h.matricula AND I.Id_Orgao = G.Id_Orgao AND c.country = 'BRA' AND c.language_cd = 'POR' AND a.emplid = f.emplid (+) AND b.pin_num IN ('220245', '220250') AND c.effdt = (SELECT MAX(cc.effdt) FROM PS_GP_ABS_RSN_LANG cc WHERE c.country = cc.country AND c.absence_reason = cc.absence_reason AND c.abs_type_optn = cc.abs_type_optn AND c.language_cd = cc.language_cd ) and A.END_DT > (Select  MAX(at.data_fim) From  Z_00143_PCMSO_ATESTADOS AT inner join Cpe_Saude_Ocupacional SO on at.Id_Ocorrencia = so.Id_Ocorrencia and So.Pcmso_Matricula = '" + matricula.ToString() + "' AND at.Id_Ocorrencia = '" + idOcorrencia.ToString() + "') AND H.Matricula = '" + matricula.ToString() + "' ORDER BY Last_Updt_Dt DESC ")
    
    if valor == 0:
        return "erro"
    else:
        return "ok"
