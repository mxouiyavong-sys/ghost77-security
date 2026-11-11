# Test results for ghost77-security.onrender.com

These are real, dated results from free public scanners and from direct checks run against [https://ghost77-security.onrender.com](https://ghost77-security.onrender.com). No scores were invented. If a check could not be completed, that is stated below.

**Disclaimer:** These are automated, visitor-level scans and header/TLS checks. They are not a human penetration test, a compliance audit, a certification, or a guarantee that the site is safe from attackers. A high grade on one of these tools does not mean every issue has been found. The live site says the same about its own published grades.

Target: `https://ghost77-security.onrender.com`  
Fresh checks run: 11 November 2026, 4:51–4:53 PM ET (America/New_York).

## Summary

| Tool | When | Grade / result | Public result page |
| --- | --- | --- | --- |
| Mozilla HTTP Observatory (fresh scan) | 11 Nov 2026, 4:51:20 PM ET | **A+**, score 140, 12/12 tests passed, 0 failed | [Observatory report](https://developer.mozilla.org/en-US/observatory/analyze?host=ghost77-security.onrender.com) |
| securityheaders.com (fresh scan) | 11 Nov 2026, 4:51:21 PM ET | **A+** | [securityheaders.com report](https://securityheaders.com/?q=https://ghost77-security.onrender.com&followRedirects=on) |
| Qualys SSL Labs (fresh scan) | Started 4:51:02 PM ET; finished 4:52:38 PM ET, 11 Nov 2026 | **A+** on both endpoints (no warnings; marked exceptional) | [SSL Labs report](https://www.ssllabs.com/ssltest/analyze.html?d=ghost77-security.onrender.com) |
| curl response headers (HEAD and GET) | 11 Nov 2026, 4:51 PM ET | CSP, HSTS, X-Frame-Options, and other security headers present (see below) | No public score page; raw headers recorded here |
| RFC 9116 `security.txt` | 11 Nov 2026, 4:51 PM ET | Present, HTTP 200, at `/.well-known/security.txt` | [security.txt](https://ghost77-security.onrender.com/.well-known/security.txt) |
| OpenSSL TLS handshake | 11 Nov 2026, 4:51 PM ET | TLS 1.3 and TLS 1.2 succeed; TLS 1.0 and TLS 1.1 rejected by the server | No public score page; findings recorded here |
| hstspreload.org API | 11 Nov 2026, 4:51 PM ET | Status `unknown` (hostname is not on the preload list) | [hstspreload.org](https://hstspreload.org/?domain=ghost77-security.onrender.com) |
| Lighthouse (fresh run) | — | **Not re-run.** No Lighthouse or PageSpeed Insights scan was completed in this pass. See the site-published grade below. | [PageSpeed Insights](https://pagespeed.web.dev/analysis?url=https://ghost77-security.onrender.com) (run it yourself) |

### Grades already published on the live site

The homepage, copied on 11 November 2026, states that independent scanners were retested **10 November 2026, 9:25–9:28 PM ET (America/New_York)** and reported:

- Mozilla Observatory A+ 140/100
- securityheaders.com A+
- SSL Labs A+
- Lighthouse 100 Performance, Accessibility, Best Practices, and SEO

The site’s own wording: “These are grades from independent scanners, not a promise this site cannot be hacked.”

Mozilla Observatory’s public history matches that evening: a scan at 10 November 2026, 9:25:24 PM ET scored **A+ / 140**. An earlier history entry the same evening, at 8:37:00 PM ET, scored **C / 55**. This file does not invent a reason for the earlier grade; it only records what Observatory returned.

## Fresh results in detail

### Mozilla HTTP Observatory

- **Tool:** MDN HTTP Observatory API v2 (`POST https://observatory-api.mdn.mozilla.net/api/v2/scan?host=ghost77-security.onrender.com`), plus `GET /api/v2/analyze` for per-test detail.
- **When:** 11 November 2026, 4:51:20 PM ET (`scanned_at` 2026-11-11T21:51:20.206Z).
- **Grade / score:** A+, 140. Algorithm version 6. Tests passed 12, failed 0, quantity 12. Site HTTP status 200. Scan id 134931732.
- **Result page:** https://developer.mozilla.org/en-US/observatory/analyze?host=ghost77-security.onrender.com

**What passed (score-impacting bonuses included):**

- Content-Security-Policy with `default-src 'none'`, no `'unsafe-inline'` / `'unsafe-eval'`, and `form-action 'self'` (score modifier +10).
- Cross-Origin-Opener-Policy `same-origin` (+10).
- Cross-Origin-Resource-Policy `same-origin` (+10).
- Referrer-Policy `strict-origin-when-cross-origin` (+5).
- X-Frame-Options implemented via CSP `frame-ancestors` (header value `DENY` is also sent) (+5).
- HSTS with max-age of at least six months (observed max-age 315360000, about 10 years, plus `includeSubdomains` and `preload`).
- X-Content-Type-Options `nosniff`.
- Redirection: Observatory reported that the initial redirection is to HTTPS on the same host and that the final destination is HTTPS.
- CORS is not opened for cross-origin reads.

**Honest gaps and notes (these did not lower the A+):**

- `Cross-Origin-Embedder-Policy` is not implemented. Observatory still marks the test as passing because “not implemented” is the current expectation, and it recommends setting `require-corp` or `credentialless`.
- Subresource Integrity (SRI) is not implemented. Observatory notes that all scripts are loaded from a similar / secure origin, and recommends adding SRI for bonus points. This test was not scored as a failure (`pass` was empty).
- No cookies were observed, so the cookie flags test did not apply.
- Observatory’s HSTS text still suggests considering preload submission. The response already includes `preload`, `includeSubdomains`, and a max-age of 10 years, but the hostname is **not** in browser preload lists (see hstspreload.org and SSL Labs below).

### securityheaders.com

- **Tool:** Public scan page at securityheaders.com (HTML report). The `X-Grade` response header is no longer a usable grade: it returned a message asking for an API key (`https://securityheaders.com/api`). The grade below is taken from the public HTML, whose title, meta description, and score badge all say A+.
- **When:** 11 November 2026, 4:51:21 PM ET (the raw headers captured on that report are dated Wed, 11 Nov 2026 21:51:21 GMT).
- **Grade:** A+.
- **Result page:** https://securityheaders.com/?q=https://ghost77-security.onrender.com&followRedirects=on

**Headers the report marked as present / green:** Content-Security-Policy, Cross-Origin-Opener-Policy, Cross-Origin-Resource-Policy, Permissions-Policy, Referrer-Policy, Strict-Transport-Security, X-Content-Type-Options, X-Frame-Options. The Server header was reported as present and changed from a detailed software version; the value observed is `cloudflare`.

**Honest gaps and notes:**

- Cross-Origin-Embedder-Policy appears under the report’s “Upcoming Headers” section and is not set. That did not prevent the A+ grade.
- This is a header grader, not a test of application logic, authentication, or payload safety.

### Qualys SSL Labs

- **Tool:** SSL Labs API v3 (`https://api.ssllabs.com/api/v3/analyze`). A cached report was not available, so a new assessment was started (first poll showed DNS resolution, then IN_PROGRESS). It reached READY without using a stale cache.
- **When:** started 11 November 2026, 4:51:02 PM ET; `testTime` 4:52:38 PM ET. Engine 2.4.3, criteria 2009q.
- **Grade:** A+ on both endpoints, `hasWarnings: false`, `isExceptional: true`. Grade with trust ignored was also A+.
- **Endpoints:** 216.24.57.16 and 216.24.57.18 (both Ready, progress 100). Findings below were the same on both.
- **Result page:** https://www.ssllabs.com/ssltest/analyze.html?d=ghost77-security.onrender.com (the public HTML page showed A+ for both endpoints after the scan finished).

**Key findings:**

- Protocols offered: TLS 1.2 and TLS 1.3 only.
- Forward secrecy: API `forwardSecrecy` value 4 (bit 2 set: all simulated clients achieve FS, per [SSL Labs API docs](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md)).
- AEAD suites supported; CBC suites not supported; RC4 not supported.
- TLS_FALLBACK_SCSV supported.
- Certificate: leaf `CN=onrender.com`, SAN `onrender.com` and `*.onrender.com`, ECDSA P-256, SHA256withECDSA, issued by Google Trust Services WE1. Valid from 21 September 2026, 5:04:31 PM ET to **20 December 2026, 6:04:28 PM ET**. SCT present in the certificate. SNI is required.
- Named groups include X25519MLKEM768 (post-quantum hybrid), x25519, and common NIST curves.
- Vulnerability tests returned “not vulnerable” (API code 1, or false where the field is a boolean) for Heartbleed, POODLE (SSLv3), POODLE TLS, CCS injection (CVE-2014-0224), Lucky Minus 20, Ticketbleed, ROBOT/Bleichenbacher, Zombie POODLE, GOLDENDOODLE, 0-Length Padding Oracle, Sleeping POODLE, FREAK, and Logjam. BEAST was false. The DROWN fields were not present in this API payload, so DROWN is not reported here as a tested result.

**Honest gaps and notes:**

- OCSP stapling is not enabled (`ocspStapling: false`).
- The certificate is a shared wildcard for `*.onrender.com`, not a certificate issued only to `ghost77-security.onrender.com`.
- The leaf certificate expires on 20 December 2026. This check does not know whether the host will auto-renew it.
- The HSTS header includes a `preload` token, but SSL Labs reports the hostname as **absent** from the Chrome, Edge, Firefox, and IE preload lists.
- The SSL Labs payload did not include a `dnsCaa` field. CAA records were not queried here (`dig` / `nslookup` were not available in the check environment).

### curl header check

- **Tool:** `curl -sSI` and `curl -sS -D` GET to `https://ghost77-security.onrender.com/`.
- **When:** 11 November 2026, 4:51 PM ET.
- **Result:** HTTPS GET and HEAD both returned HTTP 200 with the security headers below. Values were the same on GET and HEAD for these fields.

Observed response headers (exact values):

- `content-security-policy`: `default-src 'none'; script-src 'self'` plus three `'sha256-...'` hashes; `style-src 'self'; img-src 'self'; font-src 'none'; connect-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'none'; object-src 'none'; frame-src 'none'; worker-src 'none'; manifest-src 'none'; media-src 'none'; upgrade-insecure-requests`
- `strict-transport-security`: `max-age=315360000; includeSubdomains; preload`
- `x-frame-options`: `DENY`
- `x-content-type-options`: `nosniff`
- `referrer-policy`: `strict-origin-when-cross-origin`
- `permissions-policy`: `camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()`
- `cross-origin-opener-policy`: `same-origin`
- `cross-origin-resource-policy`: `same-origin`
- `server`: `cloudflare`
- `alt-svc`: `h3=":443"; ma=86400` (HTTP/3 is advertised; this pass did not complete a separate HTTP/3 handshake test)

`X-XSS-Protection` is not set. That header is obsolete; its absence is recorded, not treated as a failed grade.

**HTTP to HTTPS from this environment:** a plain `http://` request to the same host returned `HTTP/1.1 500 Internal Server Error` with `Server: Pingora`. That may be an artifact of the network used to run the check, not a proven origin-server result. Mozilla Observatory, running outside this environment, reported a successful redirect to HTTPS on the same host. This file does not treat the 500 as a confirmed site defect.

### security.txt

- **Tool:** `curl` GET and HEAD to https://ghost77-security.onrender.com/.well-known/security.txt
- **When:** 11 November 2026, 4:51 PM ET.
- **Result:** HTTP 200, `content-type: text/plain; charset=utf-8`. Body:

```
Contact: mailto:ghost77-secure@outlook.com
Contact: tel:+1-518-532-8037
Expires: 2027-11-10T05:00:00.000Z
Preferred-Languages: en
Canonical: https://ghost77-security.onrender.com/.well-known/security.txt
Policy: https://ghost77-security.onrender.com/terms
# For general questions, call Rebecca, our AI receptionist, 24/7 at +1 (518) 532-8037 and mention your business name.
```

The file is present and not expired as of this check (expiry 10 November 2027, 12:00 AM ET).

### OpenSSL TLS check

- **Tool:** `openssl s_client` to `ghost77-security.onrender.com:443` with SNI, for TLS 1.3, 1.2, 1.1, and 1.0. TLS 1.0 and 1.1 were retried with `DEFAULT:@SECLEVEL=0` so the local client would actually offer those versions.
- **When:** 11 November 2026, 4:51 PM ET.
- **Result:**
  - TLS 1.3: handshake succeeded. Cipher `TLS_AES_256_GCM_SHA384`. Verify return code 0 (ok).
  - TLS 1.2: handshake succeeded. Cipher `ECDHE-ECDSA-AES128-GCM-SHA256`. Verify return code 0 (ok).
  - TLS 1.1: server sent TLS alert 40 (handshake failure). No cipher was negotiated.
  - TLS 1.0: server sent TLS alert 40 (handshake failure). No cipher was negotiated.
- Certificate seen by OpenSSL matches SSL Labs: subject `CN=onrender.com`, SAN `onrender.com` and `*.onrender.com`, issuer Google Trust Services `WE1`, notBefore 21 September 2026 22:04:31 GMT, notAfter 20 December 2026 23:04:28 GMT.

### HSTS preload list

- **Tool:** `https://hstspreload.org/api/v2/status?domain=ghost77-security.onrender.com`
- **When:** 11 November 2026, 4:51 PM ET.
- **Result:** HTTP 200 JSON: `"status": "unknown"`, `"preloadedDomain": ""`. The hostname is not listed as preloaded, even though the HSTS header includes the `preload` token. Submitting a `*.onrender.com` Render subdomain to the public preload list may not be appropriate; this file only records the current status.

## Re-run these checks yourself

Anyone can repeat the public scans. Results can change when headers, certificates, or scanner scoring rules change.

- Mozilla HTTP Observatory: https://developer.mozilla.org/en-US/observatory/analyze?host=ghost77-security.onrender.com
- securityheaders.com: https://securityheaders.com/?q=https://ghost77-security.onrender.com&followRedirects=on
- Qualys SSL Labs: https://www.ssllabs.com/ssltest/analyze.html?d=ghost77-security.onrender.com
- HSTS preload status: https://hstspreload.org/?domain=ghost77-security.onrender.com
- security.txt: https://ghost77-security.onrender.com/.well-known/security.txt
- PageSpeed / Lighthouse (not re-run in this file): https://pagespeed.web.dev/analysis?url=https://ghost77-security.onrender.com

Command-line checks used here (replace nothing; this is the live host):

```bash
curl -sSI https://ghost77-security.onrender.com/
curl -sS https://ghost77-security.onrender.com/.well-known/security.txt
echo | openssl s_client -connect ghost77-security.onrender.com:443 -servername ghost77-security.onrender.com -tls1_3
curl -sS -X POST "https://observatory-api.mdn.mozilla.net/api/v2/scan?host=ghost77-security.onrender.com"
```
