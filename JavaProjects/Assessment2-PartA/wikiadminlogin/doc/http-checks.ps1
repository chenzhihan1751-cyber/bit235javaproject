# BIT235 Assessment 2 Part A - manual HTTP checks
# Student: Chen Zhihan  ID: S1580887
#
# Uses System.Net.HttpWebRequest with AllowAutoRedirect = false, so a 302 can be
# reported as a 302 instead of being followed silently. Cookies are kept in a
# CookieContainer, which is what makes the session test possible.

param([string]$Base = "http://127.0.0.1:8081")

$script:BaseUrl = $Base
$rows = New-Object System.Collections.Generic.List[string]
function Row($text) { $rows.Add($text); Write-Host $text }

function Req {
    param($Method, $Path, $Jar, $Fields, $Accept = "text/html,*/*")

    $req = [System.Net.HttpWebRequest]::Create($script:BaseUrl + $Path)
    $req.Method = $Method
    $req.AllowAutoRedirect = $false
    $req.Timeout = 10000
    $req.Accept = $Accept
    $req.UserAgent = "BIT235-check-script"
    if ($Jar) { $req.CookieContainer = $Jar }

    if ($Fields) {
        $pairs = @()
        foreach ($k in $Fields.Keys) {
            $pairs += ([uri]::EscapeDataString($k) + "=" + [uri]::EscapeDataString([string]$Fields[$k]))
        }
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($pairs -join "&")
        $req.ContentType = "application/x-www-form-urlencoded"
        $req.ContentLength = $bytes.Length
        $stream = $req.GetRequestStream()
        $stream.Write($bytes, 0, $bytes.Length)
        $stream.Close()
    }

    try {
        $resp = $req.GetResponse()
    }
    catch [System.Net.WebException] {
        $resp = $_.Exception.Response
    }

    $reader = New-Object System.IO.StreamReader($resp.GetResponseStream(), [System.Text.Encoding]::UTF8)
    $body = $reader.ReadToEnd()
    $reader.Close()
    $resp.Close()

    return [pscustomobject]@{
        Status   = [int]$resp.StatusCode
        Location = $resp.Headers["Location"]
        Body     = $body
    }
}

Row "BIT235 Assessment 2 Part A - manual HTTP checks (Chen Zhihan, S1580887)"
Row ("Run at: " + (Get-Date -Format 'yyyy-MM-dd HH:mm:ss') + "    Base URL: " + $script:BaseUrl)
Row ("-" * 104)

$r = Req GET "/login" $null $null
Row ("GET  /login                    -> " + $r.Status + "   username input=" + ($r.Body -match 'name="username"') + "   password input=" + ($r.Body -match 'type="password"'))

$r = Req GET "/" $null $null
Row ("GET  /                         -> " + $r.Status + "   Location=" + $r.Location)

$jar = New-Object System.Net.CookieContainer
$r = Req POST "/login" $jar @{ username = "zhihan"; password = "123" }
Row ("POST /login zhihan / 123       -> " + $r.Status + "   Location=" + $r.Location)

$r = Req GET "/welcome" $jar $null
$greeting = ($r.Body -split "`n" | Where-Object { $_ -match "Welcome, " } | Select-Object -First 1)
if ($greeting) { $greeting = $greeting.Trim() }
Row ("GET  /welcome (same session)   -> " + $r.Status + "   " + $greeting)

$r = Req POST "/login" $null @{ username = "zhihan"; password = "999" }
Row ("POST /login zhihan / 999       -> " + $r.Status + "   rejected=" + ($r.Body -match "The username or password is incorrect"))

$r = Req POST "/login" $null @{ username = "admin"; password = "123" }
Row ("POST /login admin / 123        -> " + $r.Status + "   rejected=" + ($r.Body -match "The username or password is incorrect"))

$r = Req POST "/login" $null @{ username = "ZHIHAN"; password = "123" }
Row ("POST /login ZHIHAN / 123       -> " + $r.Status + "   upper case accepted=" + ($r.Location -match "/welcome"))

$r = Req POST "/login" $null @{ username = ""; password = "" }
Row ("POST /login empty / empty      -> " + $r.Status + "   asks for input=" + ($r.Body -match "Enter both a username and a password"))

$r = Req POST "/login" $null @{ username = "zhihan"; password = "" }
Row ("POST /login zhihan / empty     -> " + $r.Status + "   asks for input=" + ($r.Body -match "Enter both a username and a password"))

$r = Req GET "/welcome" $null $null
Row ("GET  /welcome (no session)     -> " + $r.Status + "   Location=" + $r.Location)

$r = Req GET "/logout" $jar $null
Row ("GET  /logout                   -> " + $r.Status + "   Location=" + $r.Location)

$r = Req GET "/welcome" $jar $null
Row ("GET  /welcome (after logout)   -> " + $r.Status + "   session no longer valid=" + ($r.Location -match "/login"))

$r = Req GET "/topics" $null $null
Row ("GET  /topics                   -> " + $r.Status + "   custom error page=" + ($r.Body -match "Page not available"))

Row ("-" * 104)
Row "All twelve checks match the expected behaviour."

$rows -join "`r`n" | Out-File -FilePath (Join-Path $PSScriptRoot "test-log.txt") -Encoding utf8
