# TOA_Douglas
# Caminho: Catálogo > Biblioteca de scripts > TOA_Douglas
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

import clr
clr.AddReference("Newtonsoft.Json")
clr.AddReference("System.Net.Http")
clr.AddReference("Supravizio.Custom")
clr.AddReference("System.Data")

from System import *
from System.Text import *
from System.Net.Http import *
from System.Net.Http.Headers import *
from Newtonsoft.Json.Linq import *


# ========================= CONFIG =========================
TOA_BASE_URL = "https://cobratecnologia.fs.ocs.oraclecloud.com/rest/ofscCore/v1"
TOA_USER = "***MASCARADO***"
TOA_PASSWORD = "***MASCARADO***"
TOA_TIMEOUT = TimeSpan(0, 0, 15, 0, 0)
TOA_DEBUG_SALVAR_JSON_CRU = False
LOG_MAX = 2000

POLITICA_TOA_MAIS_90_DIAS = "MANTER"
TOA_ACTIVITY_TYPES_IGNORAR = ("ALMOCO", "LUNCH", "BREAK", "PAUSA")



def to_str(x):
    try:
        if x is None:
            return ""
        s = x.ToString()
        if s is None:
            return ""
        return s
    except:
        try:
            s = str(x)
            if s is None:
                return ""
            return s
        except:
            return ""


def is_null_or_empty(v):
    return to_str(v).strip() == ""


def to_int_safe(v, default=0):
    try:
        if v is None:
            return default
        s = to_str(v).strip()
        if s == "":
            return default
        return Convert.ToInt32(s)
    except:
        try:
            return int(str(v))
        except:
            return default


def to_decimal_safe(v, default=0.0):
    try:
        if v is None:
            return Convert.ToDecimal(default)
        s = to_str(v).strip().replace(',', '.')
        if s == "":
            return Convert.ToDecimal(default)
        return Convert.ToDecimal(s)
    except:
        try:
            return Convert.ToDecimal(default)
        except:
            return default


def safe_row_str(row, col):
    try:
        return to_str(row[col]).strip()
    except:
        return ""


def safe_row_int(row, col, default=0):
    try:
        return to_int_safe(row[col], default)
    except:
        return default


def ParseDateSafe(s):
    if not s:
        return None
    formatos = [
        "dd-MM-yyyy", "dd/MM/yyyy", "yyyy-MM-dd", "yyyy/MM/dd",
        "yyyy-MM-ddTHH:mm:ss", "yyyy-MM-ddTHH:mm:ssZ",
        "yyyy-MM-ddTHH:mm:ss.fff", "yyyy-MM-ddTHH:mm:ss.fffZ",
        "yyyy-MM-dd HH:mm:ss", "dd/MM/yyyy HH:mm:ss", "dd-MM-yyyy HH:mm:ss"
    ]
    txt = to_str(s).strip()
    if txt == "":
        return None
    for f in formatos:
        try:
            return DateTime.ParseExact(txt, f, None)
        except:
            pass
    try:
        return DateTime.Parse(txt)
    except:
        return None


def to_list(value):
    if value is None:
        return []
    try:
        if isinstance(value, str):
            return []
    except:
        pass
    try:
        if hasattr(value, "Rows"):
            return list(value.Rows)
    except:
        pass
    try:
        if hasattr(value, "ContainsKey"):
            return [value]
        if isinstance(value, dict):
            return [value]
    except:
        pass
    try:
        if isinstance(value, JArray):
            return [x for x in value]
    except:
        pass
    try:
        return list(value)
    except:
        return []


def get_prop(obj, keys, default=None):
    if obj is None:
        return default
    for k in keys:
        try:
            if isinstance(obj, JObject):
                tok = obj.GetValue(k)
                if tok is not None:
                    return tok
        except:
            pass
        try:
            val = obj[k]
            if val is not None:
                return val
        except:
            pass
    return default


def periodo_para_dias_uteis_no_mes(di, df, ano_, mes_):
    s = set()
    if di is None or df is None:
        return s
    ini_mes = DateTime(ano_, mes_, 1)
    fim_mes = DateTime(ano_, mes_, DateTime.DaysInMonth(ano_, mes_))
    ini = di if di > ini_mes else ini_mes
    fim = df if df < fim_mes else fim_mes
    if ini > fim:
        return s
    d = ini.Date
    while d <= fim.Date:
        if d.DayOfWeek != DayOfWeek.Saturday and d.DayOfWeek != DayOfWeek.Sunday:
            s.add(d.Date)
        d = d.AddDays(1)
    return s


def set_to_sorted_dates(date_set):
    arr = list(date_set)
    arr.sort()
    return arr


def set_to_sorted_str_list(date_set):
    arr = []
    try:
        datas = list(date_set)
        datas.sort()
        for d in datas:
            try:
                arr.append(d.ToString("dd/MM/yyyy"))
            except:
                arr.append(to_str(d))
    except:
        pass
    return arr


def chunk_text_lines(lines, max_len):
    parts = []
    current = ""
    for line in lines:
        candidate = current + line + "\n"
        if len(candidate) > max_len and current != "":
            parts.append(current.rstrip())
            current = line + "\n"
        else:
            current = candidate
    if current.strip() != "":
        parts.append(current.rstrip())
    return parts

# ========================= PEOPLESOFT =========================
def consulta_ausencias_peoplesoft(matricula, ano, mes):
    dataFormatada = (DateTime(ano, mes, 1)).ToString('dd-MM-yyyy')
    raw = None
    try:
        raw = consultaAusencias(matricula, dataFormatada)
    except:
        try:
            raw = peopleSoft.consultaAusencias(matricula, dataFormatada)
        except Exception as ex:
            raise Exception("Falha ao consultar PeopleSoft (ausências): " + to_str(ex))
    return to_list(raw)

# ========================= TOA ROUTES =========================
def monta_url_routes(matricula, data_yyyy_mm_dd):
    base = to_str(TOA_BASE_URL).strip()
    if base == "":
        raise Exception("TOA_BASE_URL não foi preenchida.")
    if not base.endswith("/"):
        base += "/"
    m = to_str(matricula).strip()
    if m == "":
        raise Exception("Matrícula vazia para consulta no TOA routes.")
    dt = to_str(data_yyyy_mm_dd).strip()
    if dt == "":
        raise Exception("Data vazia para consulta no TOA routes.")
    return base + "resources/" + m + "/routes/" + dt


def http_get_json_basic(url, user, password):
    u = to_str(user).strip()
    p = to_str(password).strip()
    if is_null_or_empty(url):
        raise Exception("URL do TOA vazia.")
    if u == "":
        raise Exception("TOA_USER não foi preenchido.")
    if p == "":
        raise Exception("TOA_PASSWORD não foi preenchido.")

    c = HttpClient()
    auth_raw = u + ":" + p
    auth_bytes = Encoding.ASCII.GetBytes(auth_raw)
    auth_b64 = Convert.ToBase64String(auth_bytes)

    c.DefaultRequestHeaders.Authorization = AuthenticationHeaderValue("Basic", auth_b64)
    c.Timeout = TOA_TIMEOUT
    c.DefaultRequestHeaders.Accept.Clear()
    c.DefaultRequestHeaders.Accept.Add(MediaTypeWithQualityHeaderValue("application/json"))

    response = c.GetAsync(url)
    response.Wait()

    if response is None or response.Result is None:
        raise Exception("Resposta HTTP do TOA veio nula.")

    if not response.Result.IsSuccessStatusCode:
        body_async = response.Result.Content.ReadAsStringAsync()
        body_async.Wait()
        body = body_async.Result
        raise Exception("Erro HTTP TOA: " + to_str(response.Result.StatusCode) + " | URL: " + url + " | BODY: " + to_str(body))

    resultAsync = response.Result.Content.ReadAsStringAsync()
    resultAsync.Wait()
    result = resultAsync.Result
    if is_null_or_empty(result):
        raise Exception("TOA retornou body vazio.")

    try:
        return JObject.Parse(result), result
    except:
        try:
            return JArray.Parse(result), result
        except:
            raise Exception("Resposta TOA não está em JSON válido: " + to_str(result))


def item_rota_conta_como_demanda(item):
    if item is None:
        return False
    record_type = to_str(get_prop(item, ["recordType"], "")).strip().upper()
    activity_type = to_str(get_prop(item, ["activityType"], "")).strip().upper()
    if record_type != "REGULAR":
        return False
    if activity_type in TOA_ACTIVITY_TYPES_IGNORAR:
        return False
    return True


def consulta_rota_toa(matricula, data_dt):
    data_str = data_dt.ToString("yyyy-MM-dd")
    url = monta_url_routes(matricula, data_str)
    json_root, json_raw = http_get_json_basic(url, TOA_USER, TOA_PASSWORD)

    total_results = to_int_safe(get_prop(json_root, ["totalResults"], 0), 0)
    itens = to_list(get_prop(json_root, ["items"], []))

    demandas = []
    for item in itens:
        try:
            if item_rota_conta_como_demanda(item):
                demandas.append(item)
        except:
            pass

    detalhes = []
    for d in demandas:
        try:
            atividade = to_str(get_prop(d, ["activityType"], ""))
            status = to_str(get_prop(d, ["status"], ""))
            appt = to_str(get_prop(d, ["apptNumber"], ""))
            detalhes.append("{0} ({1}) {2}".format(atividade, status, appt))
        except:
            pass

    return {
        "data": data_str,
        "totalResults": total_results,
        "totalDemandasElegiveis": len(demandas),
        "teveDemanda": len(demandas) > 0,
        "detalhes": detalhes,
        "jsonRaw": json_raw
    }

# ========================= FERIADOS TABELA =========================
def consulta_feriados_tabela(base, uf, ano, mes):
    base_SV_formatada = base[3:] if base and len(base) > 3 else base
    primeiroDia = DateTime(ano, mes, 1)
    proximoMes = primeiroDia.AddMonths(1)
    d1_lit = primeiroDia.ToString("yyyy-MM-dd")
    d2_lit = proximoMes.ToString("yyyy-MM-dd")
    cidade_sql = to_str(base_SV_formatada).replace("'", "''")
    uf_sql = to_str(uf).replace("'", "''")

    fer_tr = DB.ExecuteDataTable(
        "SELECT fer.DT_FERIADO, fer.UF, fer.CIDADE, fer.TIPO, fer.SEMANA "
        "FROM tb_feriados_municipais fer "
        "WHERE ( (fer.CIDADE = '" + cidade_sql + "' AND fer.UF = '" + uf_sql + "') "
        " OR (fer.TIPO = 'Nacional' OR (fer.UF = 'BR' AND UPPER(fer.CIDADE) IN ('TODOS','TODAS'))) ) "
        " AND fer.DT_FERIADO >= DATE '" + d1_lit + "' "
        " AND fer.DT_FERIADO < DATE '" + d2_lit + "' "
        " AND TO_CHAR(fer.DT_FERIADO, 'DY', 'NLS_DATE_LANGUAGE=ENGLISH') NOT IN ('SAT','SUN') "
        "ORDER BY fer.DT_FERIADO"
    )

    feriados_set = set()
    feriados_municipais_log = []
    feriados_nacionais_log = []

    try:
        for d in fer_tr.Rows:
            try:
                dt_fer = d["DT_FERIADO"]
                if dt_fer is None:
                    continue
                try:
                    dt = dt_fer.Date
                    data_fmt = dt.ToString("dd/MM/yyyy")
                except:
                    data_fmt = to_str(dt_fer)
                    dt = ParseDateSafe(data_fmt)
                if dt is None:
                    continue
                feriados_set.add(dt.Date)

                tipo_fer = to_str(d["TIPO"]).strip().upper()
                uf_fer = to_str(d["UF"]).strip().upper()
                cid_fer = to_str(d["CIDADE"]).strip()
                if tipo_fer == "NACIONAL" or (uf_fer == "BR" and cid_fer.upper() in ("TODOS", "TODAS")):
                    feriados_nacionais_log.append(data_fmt)
                else:
                    feriados_municipais_log.append("{0} - {1}/{2}".format(data_fmt, cid_fer, uf_fer))
            except:
                pass
    except:
        pass

    return feriados_set, feriados_municipais_log, feriados_nacionais_log
