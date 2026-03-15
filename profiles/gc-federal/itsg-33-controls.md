# ITSG-33 Application Security Controls Checklist

> **Profile:** Protected B / Medium Integrity / Medium Availability
> **Source:** [CCCS ITSG-33 Annex 3A](https://www.cyber.gc.ca/en/guidance/annex-3a-security-control-catalogue-itsg-33) and [Annex 4A Profile 1](https://www.cyber.gc.ca/en/guidance/annex-4a-profile-1-protected-b-medium-integrity-medium-availability-itsg-33)
> **Scope:** Application-level controls relevant to web application development
> **CDR Context:** These are the controls a CDR terry must implement when building tools for GC federal departments

This checklist extracts the ITSG-33 security controls that are **directly relevant to application developers** building web applications at the Protected B level. Infrastructure, physical, and organizational controls are excluded — those are the deploying department's responsibility.

**How to use this:** Every checkbox must be addressed. If a control doesn't apply to your specific tool, mark it N/A with a justification. Never leave a control unaddressed.

---

## AC — Access Control

### AC-2: Account Management
- [ ] Application supports creation, modification, disabling, and removal of user accounts
- [ ] Implement role-based access control (RBAC) — users get minimum privileges needed
- [ ] Provide administrative interface for account management
- [ ] Automatically disable accounts after department-defined period of inactivity (default: 90 days)
- [ ] Log all account management actions (create, modify, disable, delete, role changes)
- [ ] Support group/role membership management
- [ ] Notify administrators of account creation, modification, and termination

### AC-3: Access Enforcement
- [ ] Enforce approved authorization policies for every resource access
- [ ] Implement access control checks on both client and server side (server is authoritative)
- [ ] Deny by default — if no explicit permission exists, access is denied
- [ ] Enforce access control on all API endpoints, not just UI routes
- [ ] Prevent privilege escalation (horizontal and vertical)
- [ ] Validate that the authenticated user has permission for the requested action

### AC-4: Information Flow Enforcement
- [ ] Control information flow between application tiers (frontend → backend → database)
- [ ] Prevent unauthorized data export/download where applicable
- [ ] Implement data classification-aware access (if handling multiple classification levels)
- [ ] Control cross-domain/cross-origin requests (strict CORS policy)

### AC-5: Separation of Duties
- [ ] Separate administrative functions from regular user functions
- [ ] No single user should be able to both submit AND approve critical transactions
- [ ] Implement maker-checker patterns for sensitive operations where required

### AC-6: Least Privilege
- [ ] Users receive only the minimum access required for their role
- [ ] Application runs with minimum OS/database privileges
- [ ] Database connections use role-specific accounts (not superuser/root)
- [ ] Disable or restrict access to administrative functions for regular users

### AC-7: Unsuccessful Login Attempts
- [ ] Lock accounts after maximum 3 consecutive failed login attempts (Protected B requirement)
- [ ] Implement progressive delays or lockout periods
- [ ] Log all failed authentication attempts with timestamp and source
- [ ] Notify user and/or administrator of account lockout
- [ ] Require administrative action or time-based unlock to restore access

### AC-8: System Use Notification
- [ ] Display approved system use notification/banner before authentication
- [ ] Banner must include: authorized use only, monitoring notice, consent to monitoring
- [ ] User must acknowledge banner before proceeding
- [ ] Banner text in configuration (not hardcoded) — must be bilingual

### AC-9: Previous Logon Notification
- [ ] Display date/time of last successful login after authentication
- [ ] Display number of failed login attempts since last successful login

### AC-10: Concurrent Session Control
- [ ] Limit concurrent sessions per user (default: 3 for Protected B)
- [ ] Implement session tracking across application instances

### AC-11: Session Lock
- [ ] Lock session after 30 minutes of inactivity (Protected B requirement)
- [ ] Require re-authentication to unlock
- [ ] Conceal session content when locked

### AC-12: Session Termination
- [ ] Automatically terminate sessions after defined idle period
- [ ] Provide explicit logout functionality
- [ ] Invalidate session tokens on logout (server-side)
- [ ] Clear session data from client on logout

### AC-14: Permitted Actions Without Authentication
- [ ] Document any actions permitted without authentication
- [ ] Minimize unauthenticated functionality
- [ ] Never expose Protected B data to unauthenticated users

### AC-17: Remote Access
- [ ] All remote access via HTTPS (TLS 1.2 minimum, TLS 1.3 preferred)
- [ ] Authenticate all remote sessions
- [ ] Log all remote access attempts

### AC-22: Publicly Accessible Content
- [ ] Review and authorize all publicly accessible content
- [ ] Ensure no Protected B information is publicly accessible
- [ ] Implement processes to remove unauthorized public content

---

## AU — Audit and Accountability

### AU-2: Auditable Events
Log the following events at minimum:
- [ ] Successful and failed authentication attempts
- [ ] Account management actions (create, modify, delete, lock, unlock)
- [ ] Access control decisions (grants and denials)
- [ ] Data creation, modification, and deletion
- [ ] Administrative actions and configuration changes
- [ ] Application errors and exceptions
- [ ] Session start and end
- [ ] File/data export operations

### AU-3: Content of Audit Records
Every log entry must include:
- [ ] Timestamp (ISO 8601, UTC or with timezone)
- [ ] Event type/category
- [ ] User identity (authenticated user ID)
- [ ] Source (IP address, user agent where applicable)
- [ ] Outcome (success/failure)
- [ ] Affected resource/object
- [ ] Action performed
- [ ] **Never** log passwords, session tokens, or other secrets
- [ ] **Never** log full Protected B data values (log references, not content)

### AU-4: Audit Storage Capacity
- [ ] Allocate sufficient storage for audit logs
- [ ] Implement log rotation with configurable retention period
- [ ] Alert administrators when audit storage reaches 80% threshold

### AU-5: Response to Audit Processing Failures
- [ ] Application must not fail silently if audit logging fails
- [ ] Alert administrators on audit logging failures
- [ ] Consider failing closed (deny operations) if audit logging is unavailable

### AU-8: Time Stamps
- [ ] Use reliable, synchronized time source (NTP)
- [ ] Record timestamps with millisecond precision
- [ ] Use UTC or include timezone offset

### AU-9: Protection of Audit Information
- [ ] Audit logs must be write-once (application cannot modify or delete its own logs)
- [ ] Restrict access to audit logs to authorized administrators only
- [ ] Protect audit log integrity (append-only storage)

### AU-11: Audit Record Retention
- [ ] Retain audit records for minimum 2 years (Protected B standard)
- [ ] Support secure archival of old audit records

### AU-12: Audit Generation
- [ ] Generate audit records for all events identified in AU-2
- [ ] Audit generation must be always-on (not configurable to disable for security-relevant events)

---

## IA — Identification and Authentication

### IA-2: Organizational User Authentication
- [ ] Uniquely identify and authenticate all users before granting access
- [ ] Support multi-factor authentication (MFA) — **required for Protected B**
- [ ] Integrate with GC identity providers where possible (GCKey, SAML, OIDC)
- [ ] No shared accounts — every user has a unique identity

### IA-4: Identifier Management
- [ ] Ensure user identifiers are unique — never reuse identifiers
- [ ] Disable identifiers after defined period of inactivity
- [ ] Prevent use of known-compromised identifiers

### IA-5: Authenticator Management
- [ ] Enforce password complexity: minimum 12 characters, mix of character types
- [ ] Store passwords using strong one-way hashing (**bcrypt, scrypt, or Argon2** with unique salt per password)
- [ ] Never store plaintext passwords
- [ ] Enforce password history (prevent reuse of last 10 passwords)
- [ ] Support password change and reset functionality
- [ ] Protect authenticators in transit (TLS only)
- [ ] Implement secure password reset (token-based, time-limited, single-use)

### IA-6: Authenticator Feedback
- [ ] Obscure password input (mask characters)
- [ ] Generic error messages: "Invalid credentials" — not "User not found" or "Wrong password"

### IA-8: Non-Organizational User Authentication
- [ ] If external users access the system, authenticate them appropriately
- [ ] Support federated identity where applicable
- [ ] Apply same authentication strength requirements

### IA-11: Re-Authentication
- [ ] Require re-authentication for sensitive operations (changing security settings, accessing highly sensitive data)
- [ ] Implement session-based re-authentication without full logout

---

## SC — System and Communications Protection

### SC-2: Application Partitioning
- [ ] Separate user interface from application logic from data access (layered architecture)
- [ ] Separate administrative functionality from regular user functionality
- [ ] Use clear architectural boundaries (presentation → business logic → data layer)

### SC-4: Information in Shared Resources
- [ ] Prevent information leakage through shared resources
- [ ] Clear temporary files and buffers after use
- [ ] Do not expose server-side error details to users

### SC-5: Denial of Service Protection
- [ ] Implement rate limiting on authentication endpoints
- [ ] Implement rate limiting on API endpoints
- [ ] Set maximum request sizes
- [ ] Implement timeouts for all operations
- [ ] Use connection pooling for database connections

### SC-8: Transmission Confidentiality and Integrity
- [ ] All data in transit encrypted via TLS 1.2+ (TLS 1.3 preferred)
- [ ] Enforce HTTPS — redirect HTTP to HTTPS
- [ ] Set HSTS header (`Strict-Transport-Security: max-age=31536000; includeSubDomains`)
- [ ] Use secure cookies (`Secure`, `HttpOnly`, `SameSite` flags)
- [ ] Disable weak cipher suites

### SC-12: Cryptographic Key Management
- [ ] Use cryptographic modules validated under CMVP (FIPS 140-2/3) or approved by CCCS
- [ ] Manage encryption keys securely (never in source code)
- [ ] Support key rotation

### SC-13: Cryptographic Protection
Use only approved algorithms:
- [ ] **Hashing:** SHA-256 or stronger
- [ ] **Symmetric encryption:** AES-256
- [ ] **Password hashing:** bcrypt, scrypt, or Argon2
- [ ] **TLS:** 1.2 minimum with approved cipher suites
- [ ] No custom cryptography — use established libraries only
- [ ] No deprecated algorithms (MD5, SHA-1, DES, 3DES, RC4)

### SC-18: Mobile Code
- [ ] Restrict JavaScript to necessary functionality
- [ ] Implement Content Security Policy (CSP) headers
- [ ] Validate and sanitize all client-side inputs server-side

### SC-23: Session Authenticity
- [ ] Anti-CSRF tokens on all state-changing requests
- [ ] Validate session tokens server-side on every request
- [ ] Regenerate session ID after authentication
- [ ] Use cryptographically strong random session identifiers

### SC-28: Protection of Information at Rest
- [ ] Encrypt Protected B data at rest (AES-256)
- [ ] Use database-level or application-level encryption for sensitive fields
- [ ] Encryption keys stored separately from encrypted data

---

## SI — System and Information Integrity

### SI-2: Flaw Remediation
- [ ] Track and remediate security vulnerabilities in code and dependencies
- [ ] Run dependency vulnerability scanning (`pip-audit`, `npm audit`, `safety`)
- [ ] Patch timelines:
  - Critical: 48 hours
  - High: 7 days
  - Medium: 30 days
  - Low: 90 days

### SI-3: Malicious Code Protection (File Uploads)
- [ ] Scan uploaded files for malware (if application accepts uploads)
- [ ] Restrict file upload types to allowed list
- [ ] Store uploaded files outside the web root
- [ ] Never execute uploaded files

### SI-10: Information Input Validation
- [ ] Validate ALL input server-side (never trust client-side validation alone)
- [ ] Validate data type, length, range, and format
- [ ] Use allowlists over denylists
- [ ] Parameterize all database queries (prepared statements — **never concatenate user input into SQL**)
- [ ] Encode output to prevent XSS (HTML entity encoding, JavaScript encoding)
- [ ] Validate file paths to prevent path traversal
- [ ] Validate URLs to prevent SSRF
- [ ] Reject unexpected input fields (mass assignment protection)

### SI-11: Error Handling
- [ ] Display generic error messages to users — **never** expose stack traces, SQL errors, or system internals
- [ ] Log detailed error information server-side
- [ ] Custom error pages (400, 401, 403, 404, 500)
- [ ] Handle all exceptions — no unhandled exceptions in production
- [ ] Fail securely — when in doubt, deny access

### SI-12: Information Output Handling
- [ ] Validate and sanitize all output
- [ ] Set appropriate `Content-Type` headers
- [ ] Implement `Content-Disposition` headers for file downloads
- [ ] Log all exports of Protected B data

### SI-15: Information Output Filtering
- [ ] Remove unnecessary HTTP headers (`Server`, `X-Powered-By`, etc.)
- [ ] Do not expose internal system information in responses

---

## SA — System and Services Acquisition (Developer Controls)

### SA-3: System Development Lifecycle
- [ ] Follow a defined SDLC with security gates
- [ ] Integrate security into all phases of development
- [ ] Conduct security reviews at each milestone

### SA-8: Security Engineering Principles
- [ ] Defense in depth (multiple layers of security)
- [ ] Minimize attack surface
- [ ] Fail securely
- [ ] Apply least privilege
- [ ] Separate duties
- [ ] Keep security simple — complexity is the enemy

### SA-10: Developer Configuration Management
- [ ] Git version control for all source code
- [ ] Track and control all changes
- [ ] Document security-relevant configuration changes

### SA-11: Developer Security Testing
- [ ] Static Application Security Testing (SAST) — Bandit, Semgrep, or equivalent
- [ ] Dependency vulnerability scanning
- [ ] Dynamic testing where feasible
- [ ] Document and remediate all findings before release
- [ ] Security test cases included in test suite

### SA-15: Development Standards
- [ ] Use approved development tools and frameworks
- [ ] Follow OWASP secure coding standards
- [ ] Use linters and formatters for code quality

---

## CM — Configuration Management

### CM-6: Configuration Settings
- [ ] Define and document all security configuration settings
- [ ] Use environment variables for deployment-specific configuration
- [ ] **Never commit secrets to version control**
- [ ] Provide secure default configurations
- [ ] Document all configurable security parameters

### CM-7: Least Functionality
- [ ] Disable unnecessary features, ports, protocols, and services
- [ ] Remove development/debug endpoints before release
- [ ] Disable directory listing
- [ ] Remove default/sample pages and accounts

---

## HTTP Security Headers — Required for Every Application

| Header | Value | Purpose |
|--------|-------|---------|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | Force HTTPS |
| `X-Content-Type-Options` | `nosniff` | Prevent MIME sniffing |
| `X-Frame-Options` | `DENY` (or `SAMEORIGIN` if framing needed) | Prevent clickjacking |
| `Content-Security-Policy` | Restrictive policy for the application | Prevent XSS, injection |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Control referrer leakage |
| `Permissions-Policy` | Disable unnecessary browser features | Minimize attack surface |
| `Cache-Control` | `no-store` for pages with Protected B data | Prevent caching sensitive data |
| `Pragma` | `no-cache` for Protected B pages | Legacy cache prevention |

---

## CDR Implementation Notes

### For Mode 2 (Schema-Only) Builds

When building tools in Mode 2, you don't have real data to test with. Use these practices:

1. **Generate synthetic test data** that matches the schema structure but contains no real values. Use obviously fake data (e.g., "Jane TestUser", SIN "000-000-000", Department "TEST-001").
2. **Document every schema assumption** with `[SCHEMA-ASSUMPTION]` tags. The deploying department must verify these before connecting real data.
3. **Build data adapters as pluggable modules.** The adapter that connects to the real database is separate from the business logic — this is what the department configures during on-network deployment.
4. **Include a deployment guide** that walks the department through connecting real data sources.

### For Compliance Documentation

Every CDR tool submitted for GC deployment includes a `compliance/` directory:

```
compliance/
├── itsg-33-assessment.md    # Control-by-control assessment with code references
├── wcag-21-aa-audit.md      # Accessibility audit results
├── dependency-audit.md      # Third-party library analysis
├── sast-results.md          # Static analysis scan results
└── security-architecture.md # Architecture and threat model
```

This gives the department's SA&A team a head start. Most of the documentation work is already done.

---

## References

- [ITSG-33 Annex 3A — Security Control Catalogue](https://www.cyber.gc.ca/en/guidance/annex-3a-security-control-catalogue-itsg-33)
- [ITSG-33 Annex 4A — Profile 1 (PB/MI/MA)](https://www.cyber.gc.ca/en/guidance/annex-4a-profile-1-protected-b-medium-integrity-medium-availability-itsg-33)
- [ITSG-33 Suggested Security Controls Spreadsheet](https://www.cyber.gc.ca/en/guidance/suggested-security-controls-and-control-enhancements-itsg-33)
- [GC Cloud Guardrails](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32787)
- [OWASP Top 10 (2021)](https://owasp.org/www-project-top-ten/)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)

---

*This checklist covers application-level controls only. Infrastructure, physical security, personnel security, and organizational controls are the deploying department's responsibility.*
