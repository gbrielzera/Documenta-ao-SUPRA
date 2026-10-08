# Extrai as assinaturas públicas da API de scripts a partir das DLLs do Supravizio Client.
# Lê somente metadados (ReflectionOnly): não executa nem descompila código.
#
# Uso (Windows PowerShell 5.1):
#   powershell -ExecutionPolicy Bypass -File tools\extrair_api.ps1
#   powershell -ExecutionPolicy Bypass -File tools\extrair_api.ps1 -Bin "C:\caminho\Supravizio Client\Bin"
# Saída: catalogo\api\_api.json  (depois rode: python -X utf8 tools\api.py)
param(
  [string]$Bin = (Join-Path (Split-Path $PSScriptRoot -Parent) "Supravizio Client3\Bin"),
  [string]$Saida = (Join-Path (Split-Path $PSScriptRoot -Parent) "catalogo\api\_api.json")
)

$resolver = [System.ResolveEventHandler]{ param($s, $e)
  $n = (New-Object System.Reflection.AssemblyName($e.Name)).Name
  $p = Join-Path $Bin ($n + ".dll")
  if (Test-Path $p) { return [System.Reflection.Assembly]::ReflectionOnlyLoadFrom($p) }
  try { return [System.Reflection.Assembly]::ReflectionOnlyLoad($e.Name) } catch { return $null }
}
[System.AppDomain]::CurrentDomain.add_ReflectionOnlyAssemblyResolve($resolver)

function TN($t) {
  if ($null -eq $t) { return "?" }
  try {
    if ($t.IsGenericType) {
      return ($t.Name -replace '`\d+', '') + "<" + (($t.GetGenericArguments() | ForEach-Object { TN $_ }) -join ", ") + ">"
    }
    if ($t.IsArray) { return (TN $t.GetElementType()) + "[]" }
    return $t.Name
  } catch { return "?" }
}

# DLL -> filtro de tipos. As *.custom são a API exposta aos scripts (todos os tipos públicos);
# das demais só interessam os objetos globais de script e os contextos de cada tipo de script.
$extras = '^(Utils|DB|AD|OpenLDAP|PowerShell|ControleFormulario|FormularioRegistro|FormularioTarefa|ListaAtores|CriticaValidacao|CriticaValidacaoList|TipoCritica|TemplateMensagem|SessionObjectProxy|SessionProxyList|NomeCampo)$'
$alvos = [ordered]@{
  "supravizio.custom.dll" = '.'
  "services.custom.dll"   = '.'
  "core.dll"              = $extras
  "services.dll"          = "$extras|ScriptContext$"
  "supravizio.dll"        = "$extras|ScriptContext$"
}
$flags = [System.Reflection.BindingFlags]"Public,Instance,Static,DeclaredOnly"
$res = New-Object System.Collections.ArrayList
$versoes = [ordered]@{}

foreach ($d in $alvos.Keys) {
  $a = [System.Reflection.Assembly]::ReflectionOnlyLoadFrom((Join-Path $Bin $d))
  $versoes[$d] = $a.GetName().Version.ToString()
  try { $types = $a.GetTypes() }
  catch [System.Reflection.ReflectionTypeLoadException] { $types = $_.Exception.Types | Where-Object { $_ } }
  foreach ($t in ($types | Where-Object { $_.IsPublic -and $_.Name -match $alvos[$d] })) {
    $o = [ordered]@{
      dll = $d; ns = $t.Namespace; nome = $t.Name; base = ""
      tipo = $(if ($t.IsEnum) { "enum" } elseif ($t.IsInterface) { "interface" } else { "class" })
      props = @(); metodos = @(); valores = @()
    }
    try { $o.base = TN $t.BaseType } catch {}
    try {
      if ($t.IsEnum) {
        $o.valores = @($t.GetFields() | Where-Object { $_.IsLiteral } | ForEach-Object { $_.Name })
      } else {
        $o.props = @($t.GetProperties($flags) | ForEach-Object {
          $g = $_.GetGetMethod(); $s = $_.GetSetMethod()
          $idx = @($_.GetIndexParameters() | ForEach-Object { (TN $_.ParameterType) + " " + $_.Name }) -join ", "
          "{0}{1} {2}{3} {{{4}{5}}}" -f $(if (($g -and $g.IsStatic) -or ($s -and $s.IsStatic)) { "static " } else { "" }),
            (TN $_.PropertyType), $_.Name, $(if ($idx) { "[$idx]" } else { "" }),
            $(if ($g) { "get;" } else { "" }), $(if ($s) { "set;" } else { "" })
        })
        $o.metodos = @($t.GetMethods($flags) | Where-Object { -not $_.IsSpecialName } | ForEach-Object {
          $ps = @($_.GetParameters() | ForEach-Object { (TN $_.ParameterType) + " " + $_.Name }) -join ", "
          "{0}{1} {2}({3})" -f $(if ($_.IsStatic) { "static " } else { "" }), (TN $_.ReturnType), $_.Name, $ps
        })
      }
    } catch {}
    [void]$res.Add($o)
  }
}

New-Item -ItemType Directory -Force (Split-Path $Saida -Parent) | Out-Null
$json = [ordered]@{ versoes = $versoes; tipos = $res } | ConvertTo-Json -Depth 5
[System.IO.File]::WriteAllText($Saida, $json, (New-Object System.Text.UTF8Encoding($false)))
"{0} tipos em {1}" -f $res.Count, $Saida
$versoes.GetEnumerator() | ForEach-Object { "  {0} v{1}" -f $_.Key, $_.Value }
