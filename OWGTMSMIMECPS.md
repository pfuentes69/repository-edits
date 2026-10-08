---
title: |
 ![](./media/image1.png)






 OISTE/WISeKey Global Trust Model S/MIME and Client Certificates CP/CPS
author:
 - OISTE Policy Approval Authority
subtitle: Version 5.0
date: December 15, 2026 (TO BE CONFIRMED)
copyright: |
 Copyright 2026 OISTE Foundation. 
 This work is licensed under the Creative Commons Attribution 4.0 International license.
geometry: "left=3cm,right=2cm,top=2cm,bottom=2cm"
output: pdf_document
header-includes: |
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyfoot[CE,CO]{OWGTM S/MIME CP/CPS - OISTE Foundation}
  \fancyfoot[LE,RO]{\thepage}
toc: true
include-before: |
  \newpage
---

\newpage

# 1. INTRODUCTION

This document is the combined Certificate Policy (CP) and Certification Practice Statement (CPS) that governs the issuance and management of S/MIME, client authentication and document signing certificates ("Personal Certificates") by the Certification Authorities of the OISTE/WISeKey Global Trust Model (OWGTM from now on).

## 1.1 Overview

<!-- common:begin 1.1-entities -->
The main two legal entities involved in the control and operation of the OISTE/WISeKey Global Trust Model are:

- OISTE Foundation. The International Organization for Secure Electronic Transactions ("IOSET" or "OISTE"), a Swiss non-profit foundation established in 1998, and recognized with a "Special Consultative Status" by the United Nations. The OISTE Foundation maintains a Policy Approval Authority (PAA) that drafts, approves and revises the policies to which WISeKey is bound to comply with under its operator contract. The PAA is composed of members of the community to which OISTE provides its Certification Authority Services, resulting in a virtuous cycle for trust management.
- WISeKey. WISeKey is referenced in this document as the short name for the entities "WISeKey International Holding Ltd.", "WISeKey SA" or other members of the WISeKey Holding that are mandated by OISTE to host and operate the Root Certification Authorities and the technical infrastructures required to maintain the PKI at the appropriate operational level. WISeKey also operates as a "Subordinate Certification Authority" under the OISTE Roots, according to practices disclosed in this document.

The OISTE/WISeKey Global Trust Model (OWGTM) has been designed and is operated in accordance with the broad strategic direction of international PKI (Public Key Infrastructure) standards, and is intended to serve as a common Trust Model for Certification Authorities that comply with OISTE requirements.

The OISTE Foundation, under Swiss law, cannot belong to any individual or company. It is subject to annual supervision by the Swiss Federal Government and audited annually by independent auditors. Such supervision and audit require the foundation to pursue the objectives that have been set out for it, which includes the promotion of security in electronic communications worldwide.

This document is structured in accordance with RFC 3647, published by the Internet Engineering Task Force (IETF). It contains every section and subsection of the RFC 3647 outline. The words "No stipulation" mean that this document imposes no requirement for the topic of that section, and are followed by a short reason.
<!-- common:end 1.1-entities -->

**Scope of this document**

This CP/CPS applies to:

- the Root CA Certificates, Subordinate CA Certificates and Cross-Certificates listed in [Appendix B](#appendix-b-ca-hierarchies) as governed by this document;
- all Subscriber Certificates issued by those CAs: S/MIME Certificates (containing the `id-kp-emailProtection` Extended Key Usage), and certificates for client authentication and document signing; and
- the OCSP Responder Certificates of those CAs.

TLS server certificates are governed by the "OISTE/WISeKey Global Trust Model TLS CP/CPS" (OID 2.16.756.5.14.9.1). The OISTE WISeKey Global Root GB CA is governed by both documents, each for its own branch of the hierarchy, as identified in [Appendix B](#appendix-b-ca-hierarchies).

In this version, this document also covers the client authentication and document signing certificates issued by the CAs of [Appendix B](#appendix-b-ca-hierarchies). These use cases may be moved to a separate CP/CPS in a future version.

From its effective date (section 1.2), this document and the OWGTM TLS CP/CPS together supersede the OISTE/WISeKey Global Trust Model CP/CPS version 4.2 (OID 2.16.756.5.14.7.1). Certificates issued before that date remain subject to the version in force when they were issued, as stated in [section 9.10.3](#9103-effect-of-termination-and-survival).

**Organization of this document**

1. Introduction – This section. Introduces the OWGTM and this document.
2. Publication and Repository Responsibilities – Describes the publication of this document and of certificate information.
3. Identification and Authentication – Discloses the rules for subscriber naming and the required identity and mailbox validation practices.
4. Certificate Life-Cycle Operational Requirements – Describes the different phases in the life-cycle of certificates and their requirements.
5. Facility, Management and Operational Controls – Describes the physical, procedural and personnel controls enforced in the OWGTM.
6. Technical Security Controls – Discloses the technical security controls adopted in the OWGTM.
7. Certificate, CRL and OCSP Profiles – Describes the technical details of the certificates, CRLs and OCSP responses issued under this document.
8. Compliance Audit and Other Assessments – Discloses the audit policies followed in the OWGTM.
9. Other Business and Legal Matters – Describes the commercial, legal and contractual aspects of the services covered by this document.

**ADHERENCE TO ROOT PROGRAMS AND OTHER INDUSTRY POLICIES:**

This CP/CPS adheres to the latest published version of the following requirements:

- CA/Browser Forum "Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates" (S/MIME Baseline Requirements);
- CA/Browser Forum "Network and Certificate System Security Requirements" (NCSSR);
- Common CA Database (CCADB) Policy;
- Chrome Root Program Policy;
- Mozilla Root Store Policy;
- Apple Root Program Policy;
- Microsoft Trusted Root Program Requirements; and
- Adobe Approved Trust List (AATL) Technical Requirements, for the certificates identified as qualifying for the AATL (see [section 7.1.6](#716-certificate-policy-object-identifier)).

In particular, OISTE and WISeKey state their adherence to the latest published version of the Chrome Root Program Policy and of the CCADB Policy.

**APPLICABILITY NOTICE:** If any inconsistency exists between this document and the normative provisions of an applicable industry guideline or standard ("Applicable Requirements"), then the Applicable Requirements take precedence over this CP/CPS.

## 1.2 Document name and identification

| Name | OISTE/WISeKey Global Trust Model S/MIME and Client Certificates Certificate Policy/Certification Practice Statement (S/MIME CP/CPS) |
| --- | --- |
| Version | 5.0 |
| OID | 2.16.756.5.14.9.2 |
| Effective date | 2026-12-15 **TO BE CONFIRMED** |
| Location | https://github.com/OISTE/repository (file `OWGTMSMIMECPS.md`), linked from https://oiste.org/repository and https://wisekey.com/repository |
| Authoritative format | The Markdown file `OWGTMSMIMECPS.md` published in the OISTE GitHub repository is the authoritative version of this document. The PDF rendering is provided for convenience only. |
| Supersedes | OISTE/WISeKey Global Trust Model CP/CPS version 4.2 (OID 2.16.756.5.14.7.1), for the certificates within the scope of this document |

The OID of this document is stable and does not carry the version number. Each version is identified by the version number stated in this section and in [Appendix E](#appendix-e-version-history).

## 1.3 PKI participants

The following sections describe the different participant types in the OWGTM.

### 1.3.1 Certification authorities

OISTE and WISeKey own and operate the Root and Subordinate Certification Authorities (CAs) that deliver certification services under this CP/CPS. [Appendix B](#appendix-b-ca-hierarchies) identifies each CA certificate within the scope of this document, with its SHA-256 fingerprint, issuer, Extended Key Usages and status.

All Subordinate CAs within the scope of this document are hosted and operated by WISeKey. There are no Externally-Operated Subordinate CAs within the scope of this document.

Time-stamping services are governed by the CertifyID Time-Stamping Policy (see [section 6.8](#68-time-stamping)) and are not in the scope of this document.

### 1.3.2 Registration authorities

<!-- common:begin 1.3.2-general -->
The Registration Authorities (RA) are the physical or legal persons responsible for the identification of the entities requesting a certificate (referred as "applicants" when the request is in process and "subscribers" for those in possession of a certificate). The OWGTM delegates to Registration Authorities the responsibility of verifying the information provided by the applicant within a certificate request, ensuring that the request and the process used to deliver the certificate to the subscriber meet the requirements of this CP/CPS.

The Registration Authorities in the OWGTM are directly supervised by the CA and follow an accreditation process imposed by the CA in order to ensure that all security and operational procedures related to the certificate life-cycle are strictly enforced. Within the OWGTM environment there exist locations named "OWGTM Registration Points", which are the physical or virtual locations where a Registration Authority operates. These Registration Points are operated by "Registration Authority Officers", who are authorized persons responsible for verifying the identity and veracity of a certificate request for an end entity and the delivery of the certificate once issued by the Certification Authority.

The responsibilities of Registration Authorities operating under the OWGTM are:

- Check the identity and circumstances needed to verify that a certificate request is valid according to the type of certificate requested.
- Inform the applicant, before the issuance of the certificate, about the terms and conditions related to the certificate and its usage.
- Verify that the information contained in a certificate is exact and complete according to the requirements of this CP/CPS.
- Ensure that the subscriber is in possession of the private key associated to the certificate to be issued.

OWGTM may delegate identity vetting and application intake to accredited RAs under written contracts requiring adherence to this CP/CPS, audit rights and security controls. OWGTM maintains oversight of each RA and audits it at least annually, as described in [section 8.7](#87-self-audits).
<!-- common:end 1.3.2-general -->

The verification of mailbox authorization or control (section 3.2.2.2) and the processing of CAA records (section 4.2.2) are always performed by WISeKey and are never delegated to an RA, an Enterprise RA or a Delegated Third Party.

**Enterprise RAs.** OWGTM may designate an organization as an Enterprise RA, to verify certificate requests for Sponsor-validated and Organization-validated certificates for its own organization, within the domains whose control has been validated by WISeKey (see [section 3.2.2.2](#3222-validation-of-mailbox-authorization-or-control)). The Enterprise RA may not authorize the issuance of certificates for other organizations or for Mailbox Addresses outside its validated domains. The obligations of each Enterprise RA are documented in a contract, and its compliance is monitored and audited at least annually (see [section 8.7](#87-self-audits)).

### 1.3.3 Subscribers

<!-- common:begin 1.3.3 -->
In the OWGTM two different end-user roles are defined. Depending on the status of the certificate request, these roles are named "Applicant" and "Subscriber".

- An applicant is a natural or legal person that requests a certificate on their own behalf or on behalf of a third party. The applicant needs to prove their identity and ability to request a certificate. An applicant acting on behalf of a third party or legal person is requested to prove the empowerment for such representation, as required by law.
- A subscriber is the natural or legal person whose identity is linked to the private key and included in a digital certificate. In general, a subscriber is considered the "owner" of a certificate. The subscriber of a certificate is responsible for the custody of its private key and for not communicating it in any way to any other person.

This document details the particular community of subscribers to whom each type of certificate is aimed and what identification and other security requirements must be fulfilled.
<!-- common:end 1.3.3 -->

### 1.3.4 Relying parties

<!-- common:begin 1.3.4 -->
All natural and legal persons and other entities that trust the certificates issued by certification authorities operating under the OWGTM are considered to be "relying parties". Relying parties do not need to be subscribers of an OWGTM certificate, but are requested to accept the "CertifyID Relying Party Agreement", available at https://oiste.org/repository.
<!-- common:end 1.3.4 -->

### 1.3.5 Other participants

<!-- common:begin 1.3.5 -->
No stipulation. This document does not define other participants.
<!-- common:end 1.3.5 -->

## 1.4 Certificate usage

In the OWGTM, the type of a certificate is determined by the combination of its "Key Usage" and "Extended Key Usage" extensions and its certificate policy identifiers (see [section 7.1.6](#716-certificate-policy-object-identifier)).

### 1.4.1 Appropriate certificate uses

#### 1.4.1.1 Trust Purposes and Extended Key Usages

This CP/CPS is scoped to the following Trust Purposes, as defined in Appendix A of the Apple Root Program Policy:

| Trust Purpose | Required EKU(s) | Applicable requirements |
| --- | --- | --- |
| Secure Email | `id-kp-emailProtection` (1.3.6.1.5.5.7.3.4) | S/MIME Baseline Requirements |
| Legacy S/MIME | `id-kp-emailProtection` (1.3.6.1.5.5.7.3.4) and `id-kp-clientAuth` (1.3.6.1.5.5.7.3.2) | S/MIME Baseline Requirements |

In this version, this document also covers the following uses, which are not Trust Purposes of the Apple Root Program and are only issued by the legacy multi-purpose Subordinate CAs identified below:

| Use | EKU(s) | Applicable requirements |
| --- | --- | --- |
| Client authentication | `id-kp-clientAuth` (1.3.6.1.5.5.7.3.2), without `id-kp-emailProtection` | This CP/CPS; WebTrust for CAs |
| Document signing | Microsoft Document Signing (1.3.6.1.4.1.311.10.3.12), or the AATL policy identifiers of [section 7.1.6](#716-certificate-policy-object-identifier) | This CP/CPS; Adobe AATL Technical Requirements; WebTrust for CAs |
| Smart card logon | Microsoft Smart Card Logon (1.3.6.1.4.1.311.20.2.2) **TO BE CONFIRMED** (whether subscriber certificates use it) | This CP/CPS; WebTrust for CAs |

The CAs within the scope of this document serve the following Trust Purposes:

| CA certificate | EKUs in the CA certificate | Trust Purpose |
| --- | --- | --- |
| WISeKey CertifyID Client RSA CA 1, WISeKey CertifyID Client ECC CA 1 | `id-kp-emailProtection`, `id-kp-clientAuth` | Legacy S/MIME |
| Cross-Certificates issued by OISTE WISeKey Global Root GB CA to OISTE Client Root RSA G1 and OISTE Client Root ECC G1 | `id-kp-emailProtection`, `id-kp-clientAuth` | Legacy S/MIME |
| WISeKey CertifyID Personal GB CA 4 | `id-kp-emailProtection`, `id-kp-clientAuth` | Legacy S/MIME |
| WISeKey CertifyID Personal GB CA 3 | `id-kp-emailProtection`, `id-kp-clientAuth`, Microsoft Smart Card Logon, Microsoft Document Signing | Multi-purpose Subordinate CA signed before 2026-08-01 (Legacy S/MIME, client authentication, document signing) |
| WISeKey CertifyID Advanced Services CA 4 | No EKU extension | Multi-purpose Subordinate CA signed before 2026-08-01 |

The following rules apply to the Extended Key Usages:

- Every S/MIME Certificate contains `id-kp-emailProtection` and at least one Mailbox Address in the `subjectAltName` extension. Effective 2027-02-01, every certificate containing `id-kp-emailProtection` contains at least one `rfc822Name`.
- Until 2027-06-30, S/MIME Certificates may contain the other EKUs allowed by the S/MIME Baseline Requirements. Effective 2027-07-01, S/MIME Subordinate CA Certificates and S/MIME Certificates contain only `id-kp-emailProtection` and, optionally, `id-kp-clientAuth`.
- Subordinate CA Certificates signed on or after 2026-08-01 contain an Extended Key Usage extension, do not contain `anyExtendedKeyUsage`, and serve a single Trust Purpose.
- Every Subordinate CA Certificate and Subscriber Certificate issued under the OISTE Client Root RSA G1 and OISTE Client Root ECC G1 hierarchies contains `id-kp-emailProtection`. Certificates without `id-kp-emailProtection` (client authentication or document signing only) are only issued by the legacy multi-purpose Subordinate CAs. **TO BE CONFIRMED**
- The `id-kp-serverAuth`, `id-kp-codeSigning`, `id-kp-timeStamping` and `anyExtendedKeyUsage` EKUs are never present in the certificates issued under this CP/CPS.

#### 1.4.1.2 Certificate types

| Certificate type | Description | Permitted uses |
| --- | --- | --- |
| Root, Subordinate and Cross-Certified CA Certificate | Infrastructure certificate of the CAs listed in Appendix B | Certificate Signing, CRL Signing |
| OCSP Responder Certificate | Infrastructure certificate of the Online Certificate Status Protocol responders of the CAs listed in Appendix B | OCSP Response Signature |
| Standard (Basic) Personal Certificate | Low assurance personal certificate used by natural persons to authenticate and encrypt documents and transactions. Only the e-mail address is verified and included in the certificate.<br>**When used for e-mail protection, it is equivalent to the "Mailbox-validated" profile of the S/MIME Baseline Requirements.** | Digital Signature, Encryption, Client Authentication and e-mail Protection |
| Advanced Personal Certificate | High assurance personal certificate with software keys, used by natural persons to authenticate and encrypt documents and transactions. Personal identity attributes are validated and included in the certificate. Remote verification is allowed as described in section 3.2.3.<br>**When used for e-mail protection, it is equivalent to the "Individual-validated" profile of the S/MIME Baseline Requirements.** | Digital Signature, Encryption, Client Authentication and e-mail Protection |
| Qualified Personal Certificate | High assurance personal certificate with software or hardware keys, used by natural persons to authenticate and encrypt documents and transactions. Valid for advanced signatures of PDF documents. Personal identity attributes are validated and included in the certificate. Remote verification is allowed as described in section 3.2.3.<br>**When used for e-mail protection, it is equivalent to the "Individual-validated" profile of the S/MIME Baseline Requirements.** | Digital Signature, Encryption, Non-Repudiation, Client Authentication, Document Signing and e-mail Protection |
| Advanced Professional Certificate | High assurance personal certificate with software keys, used by natural persons to authenticate and encrypt documents and transactions. Personal identity and organization attributes are validated and included in the certificate. Remote verification is allowed as described in section 3.2.3.<br>**When used for e-mail protection, it is equivalent to the "Sponsor-validated" profile of the S/MIME Baseline Requirements.** | Digital Signature, Encryption, Client Authentication and e-mail Protection |
| Qualified Professional Certificate | High assurance personal certificate with software or hardware keys, used by natural persons to authenticate and encrypt documents and transactions. Valid for advanced signatures of PDF documents. Personal identity and organization attributes are validated and included in the certificate. Remote verification is allowed as described in section 3.2.3.<br>**When used for e-mail protection, it is equivalent to the "Sponsor-validated" profile of the S/MIME Baseline Requirements.** | Digital Signature, Encryption, Non-Repudiation, Client Authentication, Document Signing and e-mail Protection |
| Advanced Corporate Certificate | High assurance corporate certificate with software keys, used by legal persons to authenticate and encrypt documents and transactions. Organization attributes are validated and included in the certificate. Remote verification is allowed as described in section 3.2.3.<br>**When used for e-mail protection, it is equivalent to the "Organization-validated" profile of the S/MIME Baseline Requirements.** | Digital Signature, Encryption, Client Authentication and e-mail Protection |
| Qualified Corporate Certificate | High assurance corporate certificate with software or hardware keys, used by legal persons to authenticate and encrypt documents and transactions. Valid for advanced signatures of PDF documents. Organization attributes are validated and included in the certificate. Remote verification is allowed as described in section 3.2.3.<br>**When used for e-mail protection, it is equivalent to the "Organization-validated" profile of the S/MIME Baseline Requirements.** | Digital Signature, Encryption, Non-Repudiation, Client Authentication, Document Signing and e-mail Protection |

The "Document Signing" use of the Qualified certificates is subject to the EKU rules of [section 1.4.1.1](#1411-trust-purposes-and-extended-key-usages): effective 2027-07-01, an S/MIME Certificate does not include a document signing EKU.

### 1.4.2 Prohibited certificate uses

Any usage that is not explicitly stated in [section 1.4.1](#141-appropriate-certificate-uses) is prohibited. In particular:

- Certificates issued under this CP/CPS are not used as TLS server certificates, for code signing or for time-stamping.
- OWGTM does not issue Code Signing Certificates.
- Device certificates are not issued under this CP/CPS. Device certificates for IoT ecosystems are governed by the corresponding ecosystem CP/CPS.

## 1.5 Policy administration

<!-- common:begin 1.5 -->
This section describes how this document is administered. The same practices apply to all the CP/CPS documents of the OWGTM.

### 1.5.1 Organization administering the document

This document is administered by the OWGTM Policy Approval Authority (referred from now as PAA).

The PAA has a series of distinct functions but does not operate as a separate legal Entity. It is managed and organized in accordance with a process that draws on expertise within the OISTE Foundation and WISeKey. The PAA has been established to develop, review and approve the practices, policies and procedures for the entire Trust Model, subject to guidelines established by the members and advisors of the OISTE Foundation and WISeKey.

### 1.5.2 Contact person

- **Name:** OISTE Foundation - OWGTM Policy Approval Authority
- **E-mail address:** cps@oiste.org, cps@wisekey.com
- **Address:** Avenue Louis-Casaï 58 - 1216 Cointrin - Switzerland

**Certificate Problem Reports.** Subscribers, Relying Parties, Application Software Suppliers and other third parties report suspected Private Key Compromise, Certificate misuse, Certificate mis-issuance, or other types of fraud, compromise, misuse, inappropriate conduct, or any other matter related to Certificates by sending an e-mail message to **cps@wisekey.com**. This channel is available 24x7. Reports of Key Compromise include the evidence described in [section 4.9.12](#4912-special-requirements-re-key-compromise). The same instructions are published at https://wisekey.com/repository. The handling of Certificate Problem Reports is described in [section 4.9.5](#495-time-within-which-ca-must-process-the-revocation-request).

Subscribers request the revocation of their own certificates as described in [section 4.9.3](#493-procedure-for-revocation-request).

### 1.5.3 Person determining CPS suitability for the policy

The competent entity which determines the compliance and suitability of the OWGTM CP/CPS documents is the OWGTM PAA.

### 1.5.4 CPS approval procedures

The OWGTM PAA defines and executes the procedures related to the approval of this CP/CPS and its subsequent amendments. Amendments produce a new version of the document, which is published in the OWGTM Policy Repository (see [section 2.1](#21-repositories)) before its effective date.

The approval of a major version requires a meeting of the PAA and an approval memo signed by at least two members of the PAA. A minor version requires the approval of one member of the PAA.

This CP/CPS is reviewed and a new version is published at least once every 365 days (see [section 2.3](#23-time-or-frequency-of-publication)). In the case of a versioning conflict, the version published in the Policy Repository prevails.

The OWGTM maintains one CP/CPS per use case. Provisions common to these documents are kept identical in all of them, and the documents are reviewed and released on the same date.

Once any document of the Trust Model is updated, the CAs perform a technical assessment to identify any impact on, or configuration change required in, the platforms, and complete the required changes before the effective date of the new version.

The version history of this document is included in [Appendix E](#appendix-e-version-history).
<!-- common:end 1.5 -->

## 1.6 Definitions and acronyms

<!-- common:begin 1.6 -->
Definitions and acronyms are included in [Appendix A](#appendix-a-glossary).
<!-- common:end 1.6 -->

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES

## 2.1 Repositories

<!-- common:begin 2.1 -->
The repositories of the OWGTM are:

- The Policy Repository, for the disclosure of the CP/CPS documents and related information. The authoritative Markdown versions are published at https://github.com/OISTE/repository, and the documents are linked from https://oiste.org/repository and https://wisekey.com/repository. Superseded versions remain available in the same repository.
- The certificate status repositories. The CA certificates and the Certificate Revocation Lists (CRL) are published at the URLs included in the CRL Distribution Points and Authority Information Access extensions of the certificates issued under the OISTE Root CAs. The URLs of all CRLs are disclosed in the CCADB as required by the CCADB Policy.
- The public certificate repositories described in [section 2.2](#22-publication-of-certification-information).
<!-- common:end 2.1 -->

## 2.2 Publication of certification information

<!-- common:begin 2.2 -->
The OWGTM is responsible for the publication of information regarding its practices, its certificates and the current status of certificates.

The repositories containing public information in the OWGTM are managed by the operator of the Issuing CAs and are available 24 hours a day, seven days a week. In the case of an interruption due to "force majeure", the service is re-established in accordance with the Business Continuity Plan (see [section 5.7.4](#574-business-continuity-capabilities-after-a-disaster)).
<!-- common:end 2.2 -->

### 2.2.1 Statement on Compliance with CA/Browser Forum requirements

The CAs governed by this CP/CPS conform to the current version of the Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates published at <https://www.cabforum.org>. In the event of any inconsistency between this document and those Requirements, those Requirements take precedence over this document.

The CA infrastructure, Certificate Systems, Network Boundary Controls and Security Support Systems of the OWGTM are operated in accordance with the current version of the CA/Browser Forum Network and Certificate System Security Requirements published at <https://www.cabforum.org>.

## 2.3 Time or frequency of publication

<!-- common:begin 2.3 -->
This CP/CPS is reviewed and updated at least once every 365 days. Each review results in an increment of the version number and a dated entry in Appendix E, even if no other change is made to the document. A new version is published in the Policy Repository before its effective date.

Issued certificates are published as described in [section 4.4.2](#442-publication-of-the-certificate-by-the-ca).

Revocation information is published in the Certificate Revocation Lists (CRL) according to [section 4.9.7](#497-crl-issuance-frequency).
<!-- common:end 2.3 -->

## 2.4 Access controls on repositories

<!-- common:begin 2.4 -->
The OWGTM makes its repositories publicly available in a read-only manner, without registration or other access restrictions. Only authorized personnel in Trusted Roles can modify the content of the repositories.
<!-- common:end 2.4 -->

# 3. IDENTIFICATION AND AUTHENTICATION

<!-- common:begin 3-intro -->
The OWGTM mandates the fulfillment of a set of minimum controls that ensure the authenticity of the data included in certificates. These controls are enforced during the full life-cycle of certificates, certificate requests and related documents.
<!-- common:end 3-intro -->

## 3.1 Naming

This section describes the elements regarding the naming and identification of the subscribers of OWGTM certificates.

### 3.1.1 Types of names

Every certificate contains a Distinguished Name (DN) conforming to ITU-T X.500 in the `subject` field, composed as described in [section 7.1.4](#714-name-forms) and in the profiles of [Appendix D](#appendix-d-certificate-profiles).

S/MIME Certificates identify the Mailbox Addresses of the subscriber as `rfc822Name` or `otherName` of type `id-on-SmtpUTF8Mailbox` entries in the `subjectAltName` extension. When the `subject:emailAddress` attribute is present, it contains one of the Mailbox Addresses of the `subjectAltName` extension.

### 3.1.2 Need for names to be meaningful

<!-- common:begin 3.1.2 -->
All Distinguished Names are meaningful, and the identification attributes associated to the subscriber are in a human-readable form.
<!-- common:end 3.1.2 -->

### 3.1.3 Anonymity or pseudonymity of subscribers

Anonymous certificates are not issued. The use of pseudonymity is controlled by the applicable regulations.

For S/MIME Certificates, OWGTM permits the use of Pseudonyms only in `Sponsor-validated` certificates issued through an authorized Enterprise RA, where the associated Subject has been verified in accordance with [section 3.2.3](#323-authentication-of-individual-identity). In such cases, if present, the `subject:pseudonym` attribute contains an identifier selected by the Enterprise RA which uniquely identifies the Subject of the certificate within the Organization included in the `subject:organizationName` attribute, and its use and validity are restricted to the context of that Enterprise. Pseudonyms are not used in `Individual-validated` certificates.

Pseudonym certificates are not anonymous. OWGTM and its Enterprise RAs treat the Individual identity information relating to a Pseudonym as private information, in accordance with [section 9.4.2](#942-information-treated-as-private).

### 3.1.4 Rules for interpreting various name forms

<!-- common:begin 3.1.4 -->
The rules used in the OWGTM to interpret the distinguished names of certificates are those of RFC 4514 and ITU-T X.520.
<!-- common:end 3.1.4 -->

### 3.1.5 Uniqueness of names

<!-- common:begin 3.1.5 -->
OWGTM requires the uniqueness of the Subject Distinguished Names of the CA certificates issued by the Roots, except for re-issuances, renewals and Cross-Certificates of the same CA, which keep a byte-for-byte identical Subject Distinguished Name (see [section 7.1.4](#714-name-forms)).

The uniqueness of the Subject Distinguished Names of Subscriber Certificates is not enforced.
<!-- common:end 3.1.5 -->

### 3.1.6 Recognition, authentication, and role of trademarks

<!-- common:begin 3.1.6 -->
The inclusion of a name in a certificate does not imply any right over that name, neither for the OWGTM nor for the applicant or the subscriber. The OWGTM reserves the right to refuse a certificate request, or to revoke an existing certificate, if a conflict is detected over the ownership of a name.

The OWGTM does not intermediate in, nor resolve, conflicts regarding the ownership of names or trademarks.
<!-- common:end 3.1.6 -->

## 3.2 Initial identity validation

OWGTM performs "face to face" identity validation of the organizations requesting a Subordinate CA certificate from the Roots. The stipulations related to Subscriber Certificates are defined in the following sections. Every CA governed by this CP/CPS validates the information included in S/MIME Certificates in accordance with the S/MIME Baseline Requirements.

The information sources used for organization validation (the registration agencies and Reliable Data Sources) are published at https://wisekey.com/repository, as required by Section 3.2.3.3 of the S/MIME Baseline Requirements.

<!-- common:begin 3.2-rds -->
Before relying on a third-party data source as a "Reliable Data Source" for identity or DBA/organization validation, OWGTM evaluates and approves it. The evaluation covers: (a) provenance and authority (whether it is a recognized government or registered business registry); (b) accuracy (currency and update frequency); (c) resistance to alteration or falsification (controls on write access, and cryptographic protections if applicable); (d) availability; and (e) whether the validation process can independently corroborate results from the source. The outcome of the evaluation and the authorization to use the source are recorded and versioned. The list of sources is reviewed at least once a year and whenever a source changes its characteristics.
<!-- common:end 3.2-rds -->

**Correspondence with the S/MIME Baseline Requirements.** This document follows the RFC 3647 outline. The S/MIME Baseline Requirements insert a section "Validation of mailbox authorization or control" as section 3.2.2, which shifts the numbering of the following subsections. The correspondence is: S/MIME BR 3.2.2 is described in section 3.2.2.2 of this document; S/MIME BR 3.2.3 (organization identity) in section 3.2.2.1; S/MIME BR 3.2.4 (individual identity) in section 3.2.3; S/MIME BR 3.2.5 (non-verified information) in section 3.2.4; and S/MIME BR 3.2.6 (validation of authority) in section 3.2.5. See also [Appendix F](#appendix-f-compliance-cross-reference).

### 3.2.1 Method to prove possession of private key

If the key pair is generated by the applicant or subscriber, a demonstration of the possession of the private key associated to the public key is requested. The accepted means are a Certificate Signing Request (CSR) signed with the private key, or any other method accepted by OWGTM that proves possession of the private key.

If, when allowed by this CP/CPS, the key pair is generated by the CA or the RA, OWGTM applies the procedures of [section 6.1.2](#612-private-key-delivery-to-subscriber) to transfer the private key securely to the subscriber.

### 3.2.2 Authentication of organization identity

<!-- common:begin 3.2.2-subca -->
Before issuing a certificate for a Subordinate Certification Authority, OWGTM requires the execution of a legally binding agreement between the organization and the OISTE Foundation, which includes the appropriate validation of the organization identity and of the signatories of the agreement.
<!-- common:end 3.2.2-subca -->

#### 3.2.2.1 Organization identity validation

If the Subject Distinguished Name of a certificate is to include the name or address of an organization (Sponsor-validated and Organization-validated certificates), the RA verifies the identity and address of the organization and that the address is the Applicant's address of existence or operation, in accordance with Section 3.2.3 of the S/MIME Baseline Requirements.

The RA verifies the identity and address of the Applicant using documentation provided by, or through communication with, at least one of the following:

- A government agency in the jurisdiction of the Applicant's legal creation, existence, or recognition;
- A third-party database that is periodically updated and considered a Reliable Data Source, evaluated as described in the [introduction of section 3.2](#32-initial-identity-validation);
- A site visit by OWGTM or a third party who is acting as an agent for OWGTM; or
- An Attestation Letter.

Acceptable documentation includes:

- Articles of incorporation;
- Government-issued business registration certificate;
- Recent financial or statutory document.

The RA performs an out-of-band verification, such as a telephone call or an e-mail to a known domain address, when the documentation does not by itself establish the identity of the Applicant.

OWGTM may verify the address of the Applicant (but not the identity of the Applicant) using a utility bill, bank statement, credit card statement, government-issued tax document, or other reliable form of identification.

When the Applicant is a Legal Entity, and in accordance with Section 3.2.3.2.1 of the S/MIME Baseline Requirements, the verification of its full legal name and address includes the following additional checks:

- When verification relies on documentation provided by, or communication with, a government agency in the jurisdiction of the Legal Entity's creation, existence, or recognition, or on an Attestation, OWGTM verifies that the status of the Applicant is not designated by labels such as "ceased", "inactive", "invalid", "not current", or the equivalent.
- When a Legal Entity Identifier (LEI) data reference is used, OWGTM verifies that the RegistrationStatus is ISSUED and the EntityStatus is ACTIVE, and only allows the use of an LEI if the ValidationSources entry is FULLY_CORROBORATED. An LEI is not used if the ValidationSources entry is PARTIALLY_CORROBORATED, PENDING, or ENTITY_SUPPLIED_ONLY.

Any DBA or assumed name included in a certificate is validated using a Reliable Data Source, an Attestation Letter, or a reliable form of identification, in accordance with this section.

| Certificate type | Organization validation |
| --- | --- |
| Standard Personal Certificate<br>Advanced Personal Certificate<br>Qualified Personal Certificate | Not applicable: organization information does not appear in these certificates. |
| Advanced Professional Certificate<br>Qualified Professional Certificate<br>Advanced Corporate Certificate<br>Qualified Corporate Certificate | The Registration Authority verifies that the organization exists and that the certificate applicant is authorized to enroll for a certificate on behalf of the organization, by means of the authorization of a representative of the same organization (see [section 3.2.5](#325-validation-of-authority)). |

<!-- common:begin 3.2.2.1-inspection -->
In all cases, OWGTM validation practices include the inspection of any documentary evidence or other documents relied upon for alteration or falsification prior to accepting the document as proof of identity or entitlement. Inspection procedures include:

1. verification of the document issuer and issuance date against an authoritative source where available;
2. comparison of document details (name, address, identifiers) against other corroborating sources;
3. visual and electronic checks for signs of alteration (e.g., inconsistent fonts, metadata anomalies, checksum or hash verification for electronic documents); and
4. recording the inspection outcome in the validation record.

Deviations or suspected falsifications are escalated and handled per the procedures in [section 8.5](#85-actions-taken-as-a-result-of-deficiency).
<!-- common:end 3.2.2.1-inspection -->

#### 3.2.2.2 Validation of mailbox authorization or control

**General principles**

- OWGTM verifies that the Applicant controls the e-mail accounts associated with all Mailbox Fields referenced in the certificate, or has been authorized by the e-mail account holder to act on the account holder's behalf.
- OWGTM does not delegate the verification of mailbox authorization or control.
- OWGTM maintains a record of which validation method, including the relevant version number of the TLS Baseline Requirements or S/MIME Baseline Requirements, was used to validate every domain and every e-mail address in issued certificates.

**Validating authority over mailbox via domain**

OWGTM may confirm that the Applicant has been authorized by the e-mail account holder to act on the account holder's behalf by verifying the Applicant's control over the domain portion of the Mailbox Address to be used in the certificate. This method is used to entitle an Enterprise RA to issue certificates for the authorized domains. For the purposes of domain validation, the Applicant includes the Applicant's Parent Company, Subsidiary Company or Affiliate.

To perform this verification, OWGTM uses only the following methods of Section 3.2.2.4 of the TLS Baseline Requirements, as required by Section 3.2.2.1 of the S/MIME Baseline Requirements:

| Method | TLS BR section | Description |
| --- | --- | --- |
| Email to a Constructed Address | 3.2.2.4.4 | WISeKey sends an e-mail to "admin", "administrator", "webmaster", "hostmaster" or "postmaster", followed by "@" and the Authorization Domain Name, including a Random Value and a method to confirm its reception. Since 2026-03-15 this method is not used for new validations; effective 2028-03-15, WISeKey neither uses this method nor relies on validations previously performed with it. |
| DNS Change | 3.2.2.4.7 | WISeKey provides a Random Value that the Applicant places in a DNS TXT, CNAME or CAA record of the Authorization Domain Name. |
| Email to DNS CAA Contact | 3.2.2.4.13 | WISeKey retrieves the Domain Contact from the DNS CAA records and sends an e-mail including a Random Value and a method to confirm its reception. Since 2026-03-15 this method is not used for new validations; effective 2028-03-15, WISeKey neither uses this method nor relies on validations previously performed with it. |
| Email to DNS TXT Contact | 3.2.2.4.14 | WISeKey retrieves the Domain Contact from the DNS TXT record and sends an e-mail including a Random Value and a method to confirm its reception. Since 2026-03-15 this method is not used for new validations; effective 2028-03-15, WISeKey neither uses this method nor relies on validations previously performed with it. |
| Agreed-Upon Change to Website v2 | 3.2.2.4.18 | WISeKey provides a Random Value that the Applicant places in a file at the path `/.well-known/pki-validation/` of the domain. The platform retrieves the file over HTTP or HTTPS, requires a 2xx HTTP status code, and verifies that the Random Value appears in the file content. |
| Agreed-Upon Change to Website - ACME | 3.2.2.4.19 | WISeKey validates the domain using the ACME "http-01" challenge defined in Section 8.3 of RFC 8555. |

For these methods, Random Values are unique for each request and remain valid for no more than 30 days from their creation; the Authorization Domain Name is derived as specified for the method in the TLS Baseline Requirements; and Multi-Perspective Issuance Corroboration is performed as described in [section 3.2.2.3](#3223-multi-perspective-issuance-corroboration).

**Validating control over mailbox via email**

Unless the domain portion of the Mailbox Address has been validated for the Applicant as described above, OWGTM confirms the Applicant's control over each Mailbox Address to be included in a certificate by sending a Random Value by e-mail to that Mailbox Address and then receiving a confirming response that uses the Random Value, entered by the user in the OWGTM mailbox validation service, in accordance with Section 3.2.2.2 of the S/MIME Baseline Requirements:

- Each Mailbox Address is confirmed using a unique Random Value, which is sent only to the Mailbox Address being validated and is not shared in any other way.
- The Random Value is unique in each e-mail, and remains valid for use in a confirming response for no more than 24 hours from its creation.
- The Random Value is reset upon each e-mail sent to a Mailbox Address, and upon its first use if it is intended for additional use as an authentication factor.

OWGTM does not use the methods of Sections 3.2.2.3 (operator of the associated mail servers) and 3.2.2.4 (ACME for S/MIME) of the S/MIME Baseline Requirements.

#### 3.2.2.3 Multi-Perspective Issuance Corroboration

When the domain portion of a Mailbox Address is validated using a method of the TLS Baseline Requirements, and for the processing of CAA records, OWGTM implements Multi-Perspective Issuance Corroboration (MPIC) in accordance with Section 3.2.2.9 of the TLS Baseline Requirements, as required by Section 4.2.2.2 of the S/MIME Baseline Requirements: the Primary Network Perspective performs the initial validation, and the CA obtains corroborating observations from at least the number of remote Network Perspectives mandated by the TLS Baseline Requirements (four (4) since 2026-06-15, and five (5) effective 2026-12-15), in the service regions of at least two (2) distinct Regional Internet Registries. If the quorum of the TLS Baseline Requirements is not achieved, the certificate is not issued. The MPIC records are retained as part of the validation record.

<!-- common:begin 3.2.2.9-infra -->
The infrastructure supporting the MPIC systems uses network hardening mechanisms to mitigate BGP routing incidents affecting the Internet connectivity of the Network Perspectives, and is hosted in ISO/IEC 27001 certified facilities, or facilities certified or reported under an equivalent independently audited security framework. The MPIC systems are included in the vulnerability assessment and patch management applied to the rest of the PKI systems.
<!-- common:end 3.2.2.9-infra -->

### 3.2.3 Authentication of individual identity

The identity of individuals (S/MIME Baseline Requirements Section 3.2.4) is verified using the practices of [section 3.2.2.1](#3221-organization-identity-validation), with the following acceptable identity documents:

- Government-issued passport;
- National identity card or driving license;
- Other government-issued ID with photograph.

The RA may require additional evidence, such as:

- Video-based identity proofing;
- A notarized document;
- An external eID verification, when available.

The list of the accepted identity document types, of the accepted eIDs and their attributes, and of the accepted mobile driving licence (mDL) issuing jurisdictions and versions, if any, is published at https://wisekey.com/repository. **TO BE CONFIRMED**

**Collection of Individual identity attributes.** In accordance with Section 3.2.4.1 of the S/MIME Baseline Requirements, Individual identity attributes are collected through one or more of the following methods:

- submission by the Applicant during the certificate enrolment process, subject to the verification practices of this section;
- collection by a Validation Specialist appointed by OWGTM, or by an authorized Enterprise RA, from government-issued identity documents presented in a face-to-face or remote (e.g., video-based) verification session;
- retrieval from a well-maintained database of identity data created on the basis of face-to-face or remote verification using official identity documents;
- collection from records maintained by an authorized Enterprise RA for Subjects within its own Organization; or
- external eID verification means, when available.

Any Individual identity attribute collected through these methods and included in a certificate is verified as described in this section.

| Certificate type | Validation policy |
| --- | --- |
| Standard Personal Certificate | **ID data verified**: only the e-mail address.<br>**Method of verification**:<ul><li>When the Extended Key Usage for e-mail protection is set: e-mail challenge-response proving control of the mailbox (see [section 3.2.2.2](#3222-validation-of-mailbox-authorization-or-control)).</li><li>Pre-authorization of the full domain by the organization to which the user belongs, using the domain validation methods of [section 3.2.2.2](#3222-validation-of-mailbox-authorization-or-control).</li></ul>**Entities authorized to verify**:<ul><li>Validation Specialist appointed by OWGTM.</li><li>Authorized Enterprise Registration Authority entitled to issue certificates for pre-authorized Organizations and a validated set of domains.</li></ul> |
| Advanced Personal Certificate<br>Qualified Personal Certificate<br>Advanced Professional Certificate<br>Qualified Professional Certificate | **ID data verified**: the e-mail address, verified as for the Standard Personal Certificate, and the personal identity data (such as name, date of birth, nationality, telephone number). Any name or identity attribute included in the certificate is verified.<br>**Method of verification**: verification of official identity documents, face-to-face or remote, or a well-maintained database of identity data created on the basis of face-to-face or remote verification using official identity documents.<br>**Entities authorized to verify**:<ul><li>Validation Specialist appointed by OWGTM.</li><li>Authorized Enterprise Registration Authority entitled to issue certificates for pre-authorized Organizations and a validated set of domains.</li></ul> |
| Advanced Corporate Certificate<br>Qualified Corporate Certificate | The e-mail address is verified as for the Standard Personal Certificate. Individual identity information is not included in these certificates; the organization is validated as described in [section 3.2.2.1](#3221-organization-identity-validation). |

**Note**: Certificates containing an OID of the Adobe AATL (see [section 7.1.6](#716-certificate-policy-object-identifier)) are validated according to the rules for Qualified certificates.

### 3.2.4 Non-verified subscriber information

All the attributes included in a certificate that are subject to the S/MIME Baseline Requirements or to Root Program requirements are validated as described in this section 3.2.

### 3.2.5 Validation of authority

Validation of authority is performed in accordance with the S/MIME Baseline Requirements (Section 3.2.6). It determines whether a person has the rights, entitlements or permissions to act on behalf of an organization to obtain a certificate.

For any certificate containing Subject Identity Information of an organization, OWGTM uses a Reliable Method of Communication to verify the authorization of the Applicant Representative to submit the certificate request, such as determining the relationship of the person sending the request with the Applicant's main business offices, corporate offices, human resources offices or information technology offices.

For certificates requested through an Enterprise RA, the authorization of the Enterprise RA to request certificates on behalf of its organization is established in the contract with the Enterprise RA.

<!-- common:begin 3.2.5-common -->
OWGTM requires that any person participating in any operating process related to certificate generation or status modification is explicitly authorized, and that the authority is verified through a Reliable Method of Communication.

OWGTM allows an Applicant to specify the individuals who may request certificates, by providing web interfaces in which the Applicant maintains the list of authorized accounts.
<!-- common:end 3.2.5-common -->

### 3.2.6 Criteria for interoperation

<!-- common:begin 3.2.6 -->
A Certification Authority that wishes to interoperate with the OWGTM undergoes an internal accreditation process to verify its compliance with the applicable OWGTM CP/CPS. If this accreditation process is successful, an Issuing CA under the OWGTM is created that adheres to the applicable CP/CPS and is authorized to issue certain certificate types.

All Cross-Certificates that identify an OWGTM CA as the Subject are disclosed in the CCADB.
<!-- common:end 3.2.6 -->

## 3.3 Identification and authentication for re-key requests

<!-- common:begin 3.3-intro -->
This section describes the identification and authentication procedures for re-key requests. Unless otherwise specified, the same rules apply to "re-key" (a new certificate for an existing subscriber, using a new key pair) and to "renewal" (a new certificate for an existing subscriber, using the same key pair).
<!-- common:end 3.3-intro -->

### 3.3.1 Identification and authentication for routine re-key

The subscriber requests a routine re-key by authenticating to the certificate management portal through which the certificate was obtained (WISeID portal, Universal Registration Authority or Managed PKI interface) with one of these methods:

- Username and password;
- A valid digital certificate linked to the user account.

Validated information is reused only within the periods of [section 4.2.1](#421-performing-identification-and-authentication-functions). When a reuse period has expired, the information is validated again as for an initial request.

### 3.3.2 Identification and authentication for re-key after revocation

<!-- common:begin 3.3.2 -->
The OWGTM does not support the re-key of certificates after revocation. The subscriber applies for a new certificate by using the same procedures as for the initial issuance.
<!-- common:end 3.3.2 -->

## 3.4 Identification and authentication for revocation request

<!-- common:begin 3.4 -->
Revocation requests are authenticated with the same means used for the initial registration. The preferred method is an authentication based on a digital certificate owned by the subscriber or by an authorized party; passwords may be accepted as an alternative. A CA may allow the subscriber to set, during enrolment, a password that can be used in remote revocation requests, using an on-line procedure communicated to the subscriber when the certificate is issued.

Certificate Problem Reports from third parties are handled as described in [section 4.9.3](#493-procedure-for-revocation-request).
<!-- common:end 3.4 -->

# 4. CERTIFICATE LIFE-CYCLE OPERATIONAL REQUIREMENTS

The stipulations of this section apply to all the certificates within the scope of this document, unless otherwise specified. The CAs governed by this CP/CPS apply the requirements of the S/MIME Baseline Requirements to S/MIME Certificates.

## 4.1 Certificate Application

<!-- common:begin 4.1 -->
Before issuing a new certificate for a Subordinate Certification Authority, OWGTM requires the execution of a legally binding agreement between the affiliated organization and the OISTE Foundation, which includes the appropriate validation of the organization identity and of the signatories of the agreement. Additionally, for each Subordinate CA, a "CA Naming Request" signed by an authorized representative of the affiliate is required.

For subscriber certificates, the Registration Authorities operating under the OWGTM determine whether the type of the requested certificate is adequate for the applicant, in conformity with this CP/CPS, and therefore whether to proceed with the certificate application. The certificate application process includes the acceptance of the Subscriber Agreement, by means of a handwritten signature or another legally enforceable mechanism (see [section 9.6.3](#963-subscriber-representations-and-warranties)), as the first step of the certificate issuance process.

### 4.1.1 Who can submit a certificate application

A certificate application can be submitted by the subject of the certificate or by an authorized representative of the subject.
<!-- common:end 4.1 -->

### 4.1.2 Enrollment process and responsibilities

WISeKey ensures that the identity of each Applicant is verified in accordance with this CP/CPS prior to the issuance of a certificate. Applicants are responsible for submitting sufficient information and documentation for the CA or the RA to perform the required verification.

All Applicants complete the enrolment process, which may include:

- Submitting a certificate application through the certificate management portals (WISeID portal, Universal Registration Authority or Managed PKI interface), including the identity information to be validated, and accepting the Subscriber Agreement presented during the request.
- Optionally, submitting a Certificate Signing Request (CSR) that demonstrates possession of the Private Key corresponding to the Public Key to be included in the certificate. When no CSR is submitted, the key pair is generated as described in [section 6.1.1.3](#6113-subscriber-key-pair-generation).
- Protecting the integrity and confidentiality of the Private Key.

For all received requests, the authorized Validation Specialist performs the identity validation tasks defined in [section 3.2](#32-initial-identity-validation). The validation of domain names and mailboxes is automated through the certificate management portals, and is never delegated. The validation of organization information may be automated using official interfaces of Reliable Data Sources.

The enrolment process identifies suspicious requests through automated checks against lists of high-risk domain names and against previously rejected requests marked as suspicious, and subjects them to additional verification before approval.

## 4.2 Certificate application processing

This section describes the procedures for processing certificate applications.

### 4.2.1 Performing identification and authentication functions

<!-- common:begin 4.2.1-ra -->
Before an OISTE Root issues a certificate for a Subordinate Certification Authority, two authorized representatives of the PAA verify the CA Naming Application and the right of the applicant to operate a Subordinate CA under the OISTE Root.

The identification and authentication functions are delegated to the Registration Authorities operating under the OWGTM. An authorized Registration Authority Officer performs these functions. This role can be assumed by:

- An accredited person that, on behalf of a Registration Authority, personally executes the identification and authentication functions.
- An accredited software application that performs the identification and authentication functions for automated certification procedures, in accordance with [section 3.2](#32-initial-identity-validation).
<!-- common:end 4.2.1-ra -->

The Issuing CA or RA performs the following steps:

1. The verifications stipulated in [section 3.2](#32-initial-identity-validation).
2. The retrieval and processing of the CAA records for the domain portion of each Mailbox Address included in the certificate, as described in [section 4.2.2.1](#4221-caa-record-processing).
3. A check of the certificate details against the list of previously revoked certificates and rejected certificate requests, to identify suspicious certificate requests (see [section 4.1.2](#412-enrollment-process-and-responsibilities)).

The Issuing CA issues a certificate only after successfully completing these steps.

**Information reuse.** When performing the validations of [section 3.2](#32-initial-identity-validation), OWGTM may reuse completed validations and supporting evidence within the following periods, counted back from the date of issuance, in accordance with Section 4.2.1 of the S/MIME Baseline Requirements:

| Validation | Maximum reuse period |
| --- | --- |
| Authority over a mailbox via domain (section 3.2.2.2) | 398 days |
| Control over a mailbox via e-mail (section 3.2.2.2) | 30 days |
| Organization identity (section 3.2.2.1) | 825 days |
| Validation of authority (section 3.2.5) | 825 days, unless the contract with the Applicant specifies a different term |
| Individual identity (section 3.2.3) | 825 days |

A prior validation is not reused if any data or document used in it was obtained more than the maximum reuse period before the issuance of the certificate.

### 4.2.2 Approval or rejection of certificate applications

<!-- common:begin 4.2.2 -->
The approval of a certificate application results from the successful execution of the certificate issuance procedures defined in [section 4.3](#43-certificate-issuance).

The rejection of a certificate application results in a notification sent to the applicant and is recorded for further reference.
<!-- common:end 4.2.2 -->

#### 4.2.2.1 CAA record processing

Prior to issuing a certificate that includes a Mailbox Address, OWGTM retrieves and processes the CAA records for the domain portion of each Mailbox Address (each `rfc822Name` or `id-on-SmtpUTF8Mailbox` entry of the `subjectAltName` extension, and any subject Mailbox Field), in accordance with Section 4 of RFC 9495 and Section 4.2.2.1 of the S/MIME Baseline Requirements:

- OWGTM processes the `issuemail` property tag as specified in RFC 9495. Additional property tags are supported only if they do not conflict with or supersede the authorizations to issue S/MIME Certificates of the `issuemail` property tag.
- OWGTM does not issue a certificate if a CAA record contains an unrecognized property tag with the critical flag set.
- The Issuer Domain Names that OWGTM recognizes in CAA `issuemail` records as permitting it to issue are: `wisekey.com`, `hightrusted.com`, `certifyid.com` and `oiste.org`.
- If the CA issues a certificate after evaluating the CAA records, the issuance occurs within the TTL of the CAA record, or within 8 hours, whichever is greater. Otherwise, the CAA records are evaluated again before issuance.
- CAA lookups performed by remote Network Perspectives follow the corroboration rules of [section 3.2.2.3](#3223-multi-perspective-issuance-corroboration).
- A CAA lookup failure is treated as permission to issue only if the failure occurs outside the CA's infrastructure, the lookup has been retried at least once, and the domain's zone is confirmed to be "Insecure" as defined in RFC 4035, Section 4.3.
- The platforms log all actions taken in the processing of CAA records. Potential issuances prevented by a CAA record are documented, and a report is sent to the contact in the CAA `iodef` record, if present, using the `mailto:` or `https:` URL schemes.

#### 4.2.2.2 DNSSEC validation

OWGTM performs DNSSEC validation back to the IANA DNSSEC root trust anchor on all DNS queries associated with the validation of the domain portion of Mailbox Addresses and with CAA record lookups performed by the Primary Network Perspective, in accordance with Section 4.2.2.1.1 of the S/MIME Baseline Requirements and Section 4.2.2.2 of the TLS Baseline Requirements. The validating resolvers implement RFC 4035 Section 5, support NSEC3 (RFC 5155) and the SHA-2 algorithms (RFC 4509, RFC 5702), and handle the security concerns of RFC 6840 Section 4. DNSSEC validation is never disabled by local policy, and DNSSEC validation errors (e.g., SERVFAIL) are never treated as permission to issue.

### 4.2.3 Time to process certificate applications

<!-- common:begin 4.2.3 -->
No stipulation. There is no time limit to complete the processing of an application; the reuse limits of section 4.2.1 apply.
<!-- common:end 4.2.3 -->

## 4.3 Certificate issuance

<!-- common:begin 4.3 -->
A certificate request is forwarded to a Certification Authority for issuance only after the Registration Authority confirms the correctness of the information contained in the request. The validity of the information contained in a certificate is re-verified when the certificate is renewed or re-keyed, within the reuse periods of section 4.2.1.

### 4.3.1 CA actions during certificate issuance

A Certification Authority of the OWGTM issues a certificate only after verifying that the signing request is authorized and genuine, as stipulated in this document.

#### 4.3.1.1 Linting practices

Each to-be-signed certificate is checked by a Linting process for technical conformity with the applicable profile and requirements prior to signing. A Linting error generates an alert and prevents the issuance of the certificate. Linting warnings generate alerts that are reviewed to assess their impact, but do not necessarily prevent issuance.

Linting is also applied to the certificates sampled in the self-audits of [section 8.7](#87-self-audits).
<!-- common:end 4.3 -->

<!-- common:begin 4.3.2-4.8 -->
### 4.3.2 Notification to subscriber by the CA of issuance of certificate

For CA Certificates, OWGTM notifies the authorized representative of the CA.

For subscriber certificates, WISeKey sends the notifications to the e-mail address specified in the application process.

## 4.4 Certificate acceptance

Certificate acceptance is the final step of the certificate issuance process. After acceptance, the subscriber is entitled to use the certificate.

### 4.4.1 Conduct constituting certificate acceptance

For CA Certificates, the CA representative acknowledges the reception of the certificate, verifying that the key fingerprint matches the request. Installing the CA Certificate in the CA server constitutes tacit acceptance.

A subscriber certificate is accepted when the subscriber or its representative performs one or more of the following:

- Accepts the Subscriber Agreement, which includes the terms and conditions associated with this CP/CPS; or
- Downloads or installs the certificate; or
- Does not expressly refuse the certificate after the issuance notification has been sent.

### 4.4.2 Publication of the certificate by the CA

CA Certificates are published in the repositories of [section 2.1](#21-repositories) and disclosed in the CCADB. Subscriber certificates are made available to the subscriber through the certificate management portal and, where applicable, published as described in this CP/CPS.

### 4.4.3 Notification of certificate issuance by the CA to other entities

The CA notifies the issuance of a certificate only to the Registration Authority from which it received the request. The RA notifies the subscriber as stipulated in [section 4.3.2](#432-notification-to-subscriber-by-the-ca-of-issuance-of-certificate).

## 4.5 Key pair and certificate usage

The certificates issued by the OWGTM are used to provide authenticity, integrity, confidentiality and non-repudiation in electronic transactions and other computerized functions, within the uses permitted for each certificate type.

### 4.5.1 Subscriber private key and certificate usage

For CA Certificates, the private key may only be used in accordance with the CP/CPS applicable to the CA, subject to approval by the OWGTM PAA.

The uses allowed for the private key associated to each certificate type are those listed in [section 1.4](#14-certificate-usage).

### 4.5.2 Relying party public key and certificate usage

Relying parties access and use the public keys and certificates issued under the OWGTM as stipulated in this CP/CPS and in the "Relying Party Agreement", published at https://oiste.org/repository.

## 4.6 Certificate renewal

Certificate renewal is the issuance of a new certificate to a subscriber that keeps the key pair of the original certificate. Certificate renewal may not be offered for all certificate types.

### 4.6.1 Circumstance for certificate renewal

For CA Certificates, renewal is allowed for these purposes:

- Extend the validity period.
- Modify the name constraints, Extended Key Usages or other non-identity extensions, within the limits of the requirements applicable to the CA.

For subscriber certificates, renewal is allowed to extend the validity period, subject to the reuse periods of [section 4.2.1](#421-performing-identification-and-authentication-functions).

### 4.6.2 Who may request renewal

The certificate renewal can be requested by the same entities allowed to request the initial issuance of the certificate.

### 4.6.3 Processing certificate renewal requests

Certificate renewal requests are processed according to the same rules as the initial issuance.

### 4.6.4 Notification of new certificate issuance to subscriber

The notification of the issuance of a renewed certificate occurs as described in [section 4.3.2](#432-notification-to-subscriber-by-the-ca-of-issuance-of-certificate).

### 4.6.5 Conduct constituting acceptance of a renewal certificate

As stipulated in [section 4.4.1](#441-conduct-constituting-certificate-acceptance).

### 4.6.6 Publication of the renewal certificate by the CA

As stipulated in [section 4.4.2](#442-publication-of-the-certificate-by-the-ca).

### 4.6.7 Notification of certificate issuance by the CA to other entities

As stipulated in [section 4.4.3](#443-notification-of-certificate-issuance-by-the-ca-to-other-entities).

## 4.7 Certificate re-key

Certificate re-key is the issuance of a new certificate to a subscriber that generates a new key pair. Re-key is supported for all certificate types.

### 4.7.1 Circumstance for certificate re-key

Any certificate that is not revoked can be re-keyed.

### 4.7.2 Who may request certification of a new public key

The re-key can be requested by the same entities allowed to request the initial issuance of the certificate.

### 4.7.3 Processing certificate re-keying requests

Certificate re-key requests are processed according to the same rules as the initial issuance.

### 4.7.4 Notification of new certificate issuance to subscriber

As stipulated in [section 4.3.2](#432-notification-to-subscriber-by-the-ca-of-issuance-of-certificate).

### 4.7.5 Conduct constituting acceptance of a re-keyed certificate

As stipulated in [section 4.4.1](#441-conduct-constituting-certificate-acceptance).

### 4.7.6 Publication of the re-keyed certificate by the CA

As stipulated in [section 4.4.2](#442-publication-of-the-certificate-by-the-ca).

### 4.7.7 Notification of certificate issuance by the CA to other entities

As stipulated in [section 4.4.3](#443-notification-of-certificate-issuance-by-the-ca-to-other-entities).

## 4.8 Certificate modification

The OWGTM does not allow the modification of certificates during their validity period. If the information contained in a certificate ceases to be valid, the certificate is revoked and a new certificate is issued.

### 4.8.1 Circumstance for certificate modification

No stipulation. Certificate modification is not supported.

### 4.8.2 Who may request certificate modification

No stipulation. Certificate modification is not supported.

### 4.8.3 Processing certificate modification requests

No stipulation. Certificate modification is not supported.

### 4.8.4 Notification of new certificate issuance to subscriber

No stipulation. Certificate modification is not supported.

### 4.8.5 Conduct constituting acceptance of modified certificate

No stipulation. Certificate modification is not supported.

### 4.8.6 Publication of the modified certificate by the CA

No stipulation. Certificate modification is not supported.

### 4.8.7 Notification of certificate issuance by the CA to other entities

No stipulation. Certificate modification is not supported.
<!-- common:end 4.3.2-4.8 -->

## 4.9 Certificate revocation and suspension

<!-- common:begin 4.9-intro -->
All Certification Authorities operating under the OWGTM revoke any certificate that compromises the Trust Model, and maintain the means to do so.

The OWGTM maintains a comprehensive and actionable plan for mass revocation events, performs annual testing of the plan, and incorporates lessons learned into it (see [section 5.7.1.2](#5712-mass-revocation-plans)).

Suspension of certificates is not supported.

### 4.9.1 Circumstances for revocation

All subscribers of certificates issued under a CA governed by this CP/CPS are bound by the stipulations of this section.
<!-- common:end 4.9-intro -->

#### 4.9.1.1 Reasons for Revoking a Subscriber Certificate

A Certification Authority governed by this CP/CPS revokes a certificate within 24 hours if one or more of the following occurs:

1. The Subscriber requests in writing that the CA revoke the Certificate;
2. The Subscriber notifies the CA that the original Certificate Request was not authorized and does not retroactively grant authorization;
3. The CA obtains evidence that the Subscriber's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise;
4. The CA is made aware of a demonstrated or proven method that can easily compute the Subscriber's Private Key based on the Public Key in the Certificate (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>);
5. The CA obtains evidence that the validation of domain authorization or mailbox control for any Mailbox Address in the Certificate should not be relied upon.

The CA revokes a certificate, where possible within 24 hours and in any case within 5 days, if one or more of the following occurs:

6. The Certificate no longer complies with the requirements of [section 6.1.5](#615-key-sizes) and [section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
7. The CA obtains evidence that the Certificate was misused;
8. The CA is made aware that a Subscriber has violated one or more of its material obligations under the Subscriber Agreement or Terms of Use;
9. The CA is made aware of any circumstance indicating that use of an email address or Fully-Qualified Domain Name in the Certificate is no longer legally permitted (e.g., a court or arbitrator has revoked the right to use an email address or Domain Name, a relevant licensing or services agreement between the Subscriber has terminated, or the account holder has failed to maintain the active status of the email address or Domain Name);
10. The CA is made aware of a material change in the information contained in the Certificate;
11. The CA is made aware that the Certificate was not issued in accordance with the S/MIME Baseline Requirements or this CP/CPS;
12. The CA determines or is made aware that any of the information appearing in the Certificate is inaccurate;
13. The CA's right to issue Certificates under the S/MIME Baseline Requirements expires or is revoked or terminated, unless the CA has made arrangements to continue maintaining the CRL/OCSP Repository;
14. Revocation is required by this CP/CPS; or
15. The CA is made aware of a demonstrated or proven method that exposes the Subscriber's Private Key to compromise or if there is clear evidence that the specific method used to generate the Private Key was flawed.

The same reasons and time frames apply to the client authentication and document signing certificates within the scope of this document.

<!-- common:begin 4.9.1.2-4.9.2 -->
#### 4.9.1.2 Reasons for Revoking a Subordinate CA Certificate

The Issuing CA revokes a Subordinate CA Certificate within seven (7) days if one or more of the following occurs:

1. The Subordinate CA requests revocation in writing;
2. The Subordinate CA notifies the Issuing CA that the original certificate request was not authorized and does not retroactively grant authorization;
3. The Issuing CA obtains evidence that the Subordinate CA's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise or no longer complies with the requirements of [section 6.1.5](#615-key-sizes) and [section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
4. The Issuing CA obtains evidence that the Certificate was misused;
5. The Issuing CA is made aware that the Certificate was not issued in accordance with, or that the Subordinate CA has not complied with, this CP/CPS or the applicable CA/Browser Forum requirements;
6. The Issuing CA determines that any of the information appearing in the Certificate is inaccurate or misleading;
7. The Issuing CA or Subordinate CA ceases operations for any reason and has not made arrangements for another CA to provide revocation support for the Certificate;
8. The Issuing CA's or Subordinate CA's right to issue Certificates expires or is revoked or terminated, unless the Issuing CA has made arrangements to continue maintaining the CRL/OCSP Repository;
9. Revocation is required by this CP/CPS; or
10. Revocation is required by the OISTE Foundation.

### 4.9.2 Who can request revocation

The subscriber, the RA or the Issuing CA can initiate revocation. Additionally, Subscribers, Relying Parties, Application Software Suppliers and other third parties may submit Certificate Problem Reports informing the Issuing CA of reasonable cause to revoke a certificate, such as fraud, misuse or compromise. A Certificate Problem Report identifies the entity reporting it and the reason for the request.
<!-- common:end 4.9.1.2-4.9.2 -->

### 4.9.3 Procedure for revocation request

Subscribers request the revocation of their own certificates through the certificate management portal through which the certificate was obtained (WISeID portal, Universal Registration Authority or Managed PKI interface). The portal allows the subscriber to select the revocation reason options described in [section 7.2.2](#722-crl-and-crl-entry-extensions); the default option is that no revocation reason is provided. The contact and procedure information is also published at https://wisekey.com/repository and in the Subscriber Agreement.

<!-- common:begin 4.9.3-common -->
Suspected Private Key Compromise, certificate misuse, certificate mis-issuance and other types of fraud, compromise, misuse or inappropriate conduct are reported as described in [section 1.5.2](#152-contact-person), by e-mail to cps@wisekey.com. WISeKey maintains a continuous 24x7 ability to accept and respond to revocation requests and Certificate Problem Reports.

Subscribers seeking general support contact WISeKey at support@wisekey.com.

Revocation requests are accepted and processed without delay in the case of:

- Remote requests sent by e-mail or through a web page or service, authenticated as described in [section 3.4](#34-identification-and-authentication-for-revocation-request);
- Face-to-face requests addressed to an official Registration Authority representative, when the identity of the requestor is proved by the same means as used for certificate registration;
- Revocation requests sent by an official Registration or Certification Authority representative operating in the OWGTM.

### 4.9.4 Revocation request grace period

No stipulation. There is no grace period: the revocation process starts upon the receipt of a request by an authorized party.

### 4.9.5 Time within which CA must process the revocation request

Within 24 hours after receiving a Certificate Problem Report, OWGTM investigates the facts and circumstances related to the report and provides a preliminary report on its findings to both the Subscriber and the entity that filed the report.

After reviewing the facts and circumstances, OWGTM works with the Subscriber and with any entity reporting the problem to establish whether the certificate will be revoked and, if so, the date of revocation. The period from the receipt of the Certificate Problem Report to the published revocation does not exceed the time frames of [section 4.9.1](#491-circumstances-for-revocation). The date selected considers the nature of the problem (scope, context, severity, magnitude, risk of harm), the consequences of revocation for Subscribers and Relying Parties, the number of reports received about the certificate or Subscriber, the entity making the report, and the relevant legislation.

Revocation requests from the Subscriber are processed within the time frames of [section 4.9.1](#491-circumstances-for-revocation).

### 4.9.6 Revocation checking requirement for relying parties

Relying parties check the status of the certificates on which they rely, at each signature verification and authentication, by consulting the most recent CRL of the CA that issued the certificate or, when available, the OCSP service of that CA.

The locations of these services are included in the certificates, in the CRL Distribution Points and Authority Information Access extensions.
<!-- common:end 4.9.3-common -->

### 4.9.7 CRL issuance frequency

CRLs are published at publicly accessible HTTP URLs.

For the status of Subscriber Certificates, the Issuing CAs update and reissue their CRLs at least once every seven (7) days, with a `nextUpdate` value no more than ten (10) days after the `thisUpdate` value, and publish a new CRL within twenty-four (24) hours after recording a certificate as revoked.

For the status of Subordinate CA Certificates, the Root CAs and the other CAs that issue CA Certificates update and reissue their CRLs at least once every twelve (12) months and within twenty-four (24) hours after revoking a Subordinate CA Certificate, with a `nextUpdate` value no more than twelve (12) months after the `thisUpdate` value.

Each CA continues issuing CRLs until either all Subordinate CA Certificates containing the same Subject Public Key are expired or revoked, or the corresponding Private Key is destroyed.

<!-- common:begin 4.9.8 -->
### 4.9.8 Maximum latency for CRLs

CRLs are published to their distribution points immediately after their generation, and in any case within the time frames of section 4.9.7.
<!-- common:end 4.9.8 -->

### 4.9.9 On-line revocation/status checking availability

The Issuing CAs may provide an OCSP service, which is available 24x7 for the certificates that include an Authority Information Access extension with an `id-ad-ocsp` accessMethod. OCSP responses conform to RFC 6960 and/or RFC 5019, and are signed either by the CA that issued the certificate whose status is checked, or by an OCSP Responder whose certificate is signed by that CA and contains the `id-kp-OCSPSigning` EKU and the `id-pkix-ocsp-nocheck` extension (see [Appendix D](#appendix-d-certificate-profiles)).

### 4.9.10 On-line revocation checking requirements

When OCSP is provided, and in accordance with Section 4.9.10 of the S/MIME Baseline Requirements:

- OCSP responders support the HTTP GET method described in RFC 6960 and/or RFC 5019.
- For the status of Subscriber Certificates, OCSP responses have a validity interval of at least eight (8) hours and at most ten (10) days. For responses with a validity interval of less than sixteen (16) hours, the information is updated before one-half of the validity period before the `nextUpdate`. For responses with a validity interval of sixteen (16) hours or more, the information is updated at least eight (8) hours before the `nextUpdate` and no later than four (4) days after the `thisUpdate`.
- For the status of Subordinate CA Certificates, the information is updated at least every twelve (12) months and within 24 hours after revoking a Subordinate CA Certificate.
- The responder does not respond with a "good" status for a certificate serial number that is unused.

Relying parties check the status of certificates as stipulated in [section 4.9.6](#496-revocation-checking-requirement-for-relying-parties).

<!-- common:begin 4.9.11-4.9.16 -->
### 4.9.11 Other forms of revocation advertisements available

No stipulation. OWGTM does not provide other forms of revocation advertisement.

### 4.9.12 Special requirements re key compromise

Any party detecting a key compromise at any level of the OWGTM reports it immediately as described in [section 1.5.2](#152-contact-person).

The following methods are accepted to demonstrate a Private Key Compromise:

- Submission of a text file signed with the compromised Private Key;
- Submission of a custom Certificate Signing Request (CSR) signed with the compromised Private Key; or
- Submission of the Private Key itself, or of a link to the location where it is publicly disclosed.

When a Key Compromise is demonstrated, OWGTM revokes all the certificates containing the compromised Public Key and rejects future certificate requests containing that Public Key (see [section 6.1.1.3](#6113-subscriber-key-pair-generation)). When the CA, rather than the Subscriber, revokes a certificate for Key Compromise, the keyCompromise CRLReason is used only when the Key Compromise has been demonstrated by one of the methods above or the CA has otherwise obtained evidence of the Key Compromise.

### 4.9.13 Circumstances for suspension

Suspension is not allowed for any certificate issued under this CP/CPS.

### 4.9.14 Who can request suspension

No stipulation. Suspension is not supported.

### 4.9.15 Procedure for suspension request

No stipulation. Suspension is not supported.

### 4.9.16 Limits on suspension period

No stipulation. Suspension is not supported.

## 4.10 Certificate status services

Every CA operating in the OWGTM provides a highly available and reliable service for checking the status of the certificates it has issued.

### 4.10.1 Operational characteristics

Certificate status services are accessible through HTTP servers operated by the OWGTM Certification Authorities, by downloading Certificate Revocation Lists or, when available, by sending requests to the OCSP responders. The URLs of these services are included in the certificates.

Revocation entries on a CRL or OCSP response are not removed until after the expiry date of the revoked certificate.

### 4.10.2 Service availability

The certificate status services are available 24x7.

### 4.10.3 Optional features

No stipulation. No optional features are provided.

## 4.11 End of subscription

"End of subscription" occurs after the expiration or revocation of a certificate. It is specific to that certificate and does not affect any other certificate that the subscriber may hold within the OWGTM.
<!-- common:end 4.9.11-4.9.16 -->

## 4.12 Key escrow and recovery

Key escrow may be provided for the Private Keys of Personal Certificates, under the conditions of section 4.12.1.

### 4.12.1 Key escrow and recovery policy and practices

A CA providing key escrow services for Personal Certificates:

- Notifies Subscribers that their Private Keys are escrowed;
- Protects escrowed keys from unauthorized disclosure;
- Protects any authentication mechanisms that could be used to recover escrowed Private Keys;
- Releases an escrowed key only after making or receiving (as applicable) a properly authorized request for recovery; and
- Complies with any legal obligations to disclose or keep confidential escrowed keys, escrowed key related information, or the facts concerning any key recovery request or process.

### 4.12.2 Session key encapsulation and recovery policy and practices

No stipulation. Session key encapsulation and recovery is not supported.

# 5. FACILITY, MANAGEMENT, AND OPERATIONAL CONTROLS

<!-- common:begin 5.0-5.2.1 -->
This section describes the non-technical security controls used by the participants involved in the issuance, publication and management of keys and certificates within the OWGTM. These controls are a fundamental basis to provide trust to subscribers and relying parties, and the OWGTM establishes and maintains the means to ensure and demonstrate that they are enforced.

These controls are audited internally and externally by accredited bodies. The audit reports are published in the OWGTM repository (https://oiste.org/repository) and disclosed in the CCADB.

The OWGTM may allow third parties to host and operate some components of its infrastructure. In such a case, the third party is required to meet the controls stipulated in this section, and an audit verifies that these controls are effective. In particular:

- The OISTE Foundation delegates the hosting and operation of the Root CAs and their hierarchies (and the related certificate publication and verification services) to WISeKey.
- The Issuing CAs (and the related certificate publication and verification services) are hosted and operated by WISeKey, except for technically-constrained CAs, which may be hosted by their owners. Other delegations or outsourcing are only permitted after a security assessment and a formal authorization.
- Registration Authorities and Registration Points are appointed by WISeKey. Registration Authorities do not delegate their operations to other parties without the approval and direct supervision of WISeKey.

OWGTM's CA Infrastructure, Certificate Systems, Network Boundary Controls and Security Support Systems are managed in accordance with the latest version of the CA/Browser Forum Network and Certificate System Security Requirements (NCSSR) and with the controls described in this CP/CPS.

## 5.1 Physical controls

This section describes the physical controls on facilities housing OWGTM components.

### 5.1.1 Site location and construction

The OWGTM information systems are located in secure datacenters under surveillance 24 hours a day, 7 days a week. These datacenters are built so that the relevant critical physical risks are managed.

OWGTM secure datacenters and all copies (online and offline) of the Root and Subordinate CA private keys are located in Switzerland.

### 5.1.2 Physical access

The OWGTM secure datacenter implements nested security perimeters. Access from an outer to an inner perimeter requires additional security and authorization controls, including biometric door access, video surveillance and intrusion detection systems.

### 5.1.3 Power and air conditioning

The OWGTM secure datacenter implements power and air conditioning systems dimensioned for the operating needs, protected by Uninterruptible Power Supply units (UPS) and backup power generators.

### 5.1.4 Water exposures

The facilities are located in a place where natural flooding risks are controlled, and they are equipped with flooding sensors and alarms.

### 5.1.5 Fire prevention and protection

The facilities implement fire detection, prevention and protection controls.

### 5.1.6 Media storage

Media containing sensitive information are stored in fireproof containers and high-security safes, depending on the media type and the classification of the information they contain.

These containers and safes are located in redundant places, to eliminate the risks of using a single location (i.e. in the case of fire or water damage).

Access to these storage locations is restricted to authorized persons and regulated by security procedures.

### 5.1.7 Waste disposal

Optical, magnetic or electronic media and paper containing information generated during OWGTM operations are disposed of following established procedures, including demagnetization and/or destruction, depending on the media type.

### 5.1.8 Off-site backup

OWGTM makes backup copies of all information needed to bring a secondary datacenter to operational status in the event of a disaster that prevents the main datacenter from maintaining an adequate service level.

A remote backup copy is made periodically and stored so that dual access control is required to restore it.

All key backups are stored on HSM devices meeting FIPS 140-2 or FIPS 140-3 Level 3 criteria.

## 5.2 Procedural controls

The information systems and services of the OWGTM are operated following a set of predefined procedures that are enforced by the OWGTM and verified through periodic audits.

The detailed information related to these controls is classified as "CONFIDENTIAL"; this document discloses a summary. The detailed information is only disclosed to the accredited auditors responsible for reviewing OWGTM components and operations.

### 5.2.1 Trusted roles

The OWGTM establishes and enforces a security policy to control all operations performed at any level of the Trust Model, including the identification and control of the persons performing those operations. These persons hold "Trusted Roles", which include:

- Certification Authority Administrator
- Certification Authority Operator
- Registration Authority Administrator
- Registration Authority Operator with vetting attributions (also named Validation Agent or Validation Specialist)
- Registration Authority Operator without vetting attributions
- Systems Administrator
- Security Administrator
- Policy Approval Authority Member

The responsibilities, privileges and access of each Trusted Role are documented. Any account capable of authenticating to or accessing CA Infrastructure or Network Boundary Controls is reviewed at least every three (3) months.

Each Trusted Role is assigned responsibilities, privileges and access in a manner consistent with:

- the Principle of Least Privilege; and
- the Principle of Separation of Duties.

Persons seeking to become Trusted Persons by obtaining a Trusted Role successfully complete the screening requirements of [section 5.3](#53-personnel-controls).
<!-- common:end 5.0-5.2.1 -->

### 5.2.2 Number of persons required per task

<!-- common:begin 5.2.2 -->
Root and Subordinate CA key generation, activation, backup and recovery, and access to the areas hosting Root CA Systems, require the presence of at least two persons in Trusted Roles (Multi-Party Control).
<!-- common:end 5.2.2 -->

<!-- common:begin 5.2.3-5.6 -->
### 5.2.3 Identification and authentication for each role

All persons assuming a Trusted Role follow an authorization process that entitles them to access the information and systems required for their role.

Physical access control for all authorized persons accessing OWGTM systems and services is enforced using two-factor authentication that includes biometrics. Logical access to the CA Infrastructure and Network Boundary Controls requires Multi-Factor Authentication, as stipulated in [section 6.5.1](#651-specific-computer-security-technical-requirements).

Access to CA Infrastructure and Network Boundary Controls is disabled within twenty-four (24) hours of the termination of an individual's employment or contracting relationship, and authentication credentials are changed or revoked whenever the associated authorizations are changed or revoked.

### 5.2.4 Roles requiring separation of duties

Individuals are specifically designated to one or more of the roles defined in [section 5.2.1](#521-trusted-roles). OWGTM enforces the separation of roles whenever it is required to avoid conflicts of interest or a weakening of the security level.

## 5.3 Personnel controls

Personnel holding one of the roles defined in [section 5.2.1](#521-trusted-roles) are required to fulfil the "OWGTM Trusted Professional Policy", summarized in the following sections.

### 5.3.1 Qualifications, experience, and clearance requirements

Personnel acting directly or indirectly for the OWGTM possess the required qualification and/or proven experience in certification service provision environments. All involved personnel act according to the OWGTM Security Policy and possess:

- Knowledge and training (according to the role assigned to the person) in Public Key Infrastructures.
- Knowledge and training (according to the role) in Information Systems Security.
- Knowledge and training specific for the responsibilities assigned.

### 5.3.2 Background check procedures

The Human Resources Department conducts verification checks on permanent staff at the time of job application, and ensures that all personnel with access to sensitive information are trustworthy and understand their responsibilities. These checks include at least:

- Availability and verification of satisfactory references;
- Confirmation of claimed academic and professional qualifications;
- Identity checks of a passport or similar document.

### 5.3.3 Training requirements

Personnel directly involved in the OWGTM, including the Registration Authorities, follow an internal training plan adapted to their assigned attributions. This training covers the CA/Browser Forum requirements applicable to the certificate types they handle.

OWGTM defines the role of Validation Specialist for personnel who perform identity, domain and mailbox validations. Before performing Validation Specialist duties, the CA documents that each Validation Specialist:

- has completed CA-provided training covering the applicable CA/Browser Forum requirements, the CP/CPS procedures, the CA's validation tools, and the handling of suspicious requests;
- has passed the CA's validation examination with a passing score defined by the CA; and
- is formally authorized in writing to perform validations.

OWGTM maintains training and examination records for each Validation Specialist, including the training content version, date completed, exam results and authorization records. Validation Specialists receive refresher training at least annually and whenever the applicable requirements or internal procedures are updated. OWGTM retains training and personnel qualification records for the duration of employment plus 3 years.

### 5.3.4 Retraining frequency and requirements

Retraining sessions are performed at least annually, and for all involved personnel in the case of environmental, technology or operational changes. Changes in practices and policies are communicated to all involved personnel.

### 5.3.5 Job rotation frequency and sequence

No stipulation. Job rotation is not required.

### 5.3.6 Sanctions for unauthorized actions

Any action that, intentionally or unintentionally, contravenes this CP/CPS is considered an unauthorized action, and the OWGTM undertakes the necessary disciplinary actions.

Upon detection of an unauthorized action, the OWGTM initiates an investigation. During the investigation, the involved persons are prevented from accessing OWGTM systems and information.

Disciplinary actions are taken after the investigation determines the severity and intent of the action.

### 5.3.7 Independent contractor requirements

External contractors agree to the Information Security policies of the OWGTM. Temporary staff not already covered by an existing confidentiality agreement sign a Non-Disclosure Agreement before being granted access to information resources.

Contractors assigned to a role meet the same training requirements as WISeKey employees assigned to the same role.

The agreement is reviewed when there are changes to employment terms or contracts.

### 5.3.8 Documentation supplied to personnel

All personnel incorporated within the OWGTM have access, as required for their role, to the following information:

- Certificate Policies and Certification Practice Statements
- Privacy Policy
- Security Policy
- Organization chart and assigned functions and responsibilities
- Operational procedures
- Incident response procedures
- Applicable standards and requirements (e.g., CA/Browser Forum or Root Program requirements)

## 5.4 Audit logging procedures

This section describes the event logging and audit systems implemented to maintain a secure environment in the OWGTM.

### 5.4.1 Types of events recorded

OWGTM PKI systems record at least the following events:

1. CA certificate and key lifecycle events, including:
   1. Key generation, backup, storage, recovery, archival, and destruction;
   2. Certificate requests, renewal, and re-key requests, and revocation;
   3. Approval and rejection of certificate requests;
   4. Cryptographic device lifecycle management events;
   5. Generation of Certificate Revocation Lists;
   6. Signing of OCSP Responses (as described in [section 4.9](#49-certificate-revocation-and-suspension) and [section 4.10](#410-certificate-status-services)); and
   7. Introduction of new Certificate Profiles and retirement of existing Certificate Profiles.
2. Subscriber Certificate lifecycle management events, including:
   1. Certificate requests, renewal, and re-key requests, and revocation;
   2. All verification activities stipulated in the applicable CA/Browser Forum requirements and in this CP/CPS, recording at a minimum: the information that was validated (e.g., the applied-for FQDN, Mailbox Address or organization name); the Authorization Domain Name used, where different from the applied-for FQDN; and the validation method used, denoted by the applicable Baseline Requirements section number or registered ACME validation method label;
   3. Approval and rejection of certificate requests;
   4. Issuance of Certificates;
   5. Generation of Certificate Revocation Lists;
   6. Signing of OCSP Responses (as described in [section 4.9](#49-certificate-revocation-and-suspension) and [section 4.10](#410-certificate-status-services));
   7. Multi-Perspective Issuance Corroboration attempts from each Network Perspective, recording at a minimum: an identifier that uniquely identifies the Network Perspective used; the attempted domain name; and the result of the attempt (e.g., "domain validation pass/fail", "CAA permission/prohibition"); and
   8. Multi-Perspective Issuance Corroboration quorum results for each attempted domain name represented in a certificate request (i.e., "3/4", meaning that three (3) out of four (4) attempted Network Perspectives corroborated the determinations made by the Primary Network Perspective).
3. Security events, including:
   1. Successful and unsuccessful PKI system access attempts;
   2. PKI and security system actions performed;
   3. Security profile changes;
   4. Installation, update and removal of software on a Certificate System;
   5. System crashes, hardware failures, and other anomalies;
   6. Relevant router and firewall activities (as described in [section 5.4.1.1](#5411-router-and-firewall-activities-logs)); and
   7. Entries to and exits from the CA facility.

Log records include at least the following elements:

- Date and time of the event;
- Identity of the person making the journal record (when applicable); and
- Description of the event.

#### 5.4.1.1 Router and firewall activities logs

The logging of router and firewall activities includes at least:

- Successful and unsuccessful login attempts to routers and firewalls;
- All administrative actions performed on routers and firewalls, including configuration changes, firmware updates, and access control modifications;
- All changes made to firewall rules, including additions, modifications, and deletions; and
- All system events and errors, including hardware failures, software crashes, and system restarts.

### 5.4.2 Frequency of processing log

Audit logs of the CA Infrastructure and Network Boundary Controls are processed continuously through automated mechanisms under the control of personnel in Trusted Roles, capable of identifying possible Critical Security Events and unauthorized modifications of the infrastructure. Alerts are delivered to Trusted Role personnel through multiple mechanisms and/or communication channels, and an initial response to any alert commences within twenty-four (24) hours of its generation; alerts identified as legitimate Critical Security Events are handled under the Incident Response Plan (see [section 5.7.1](#571-incident-and-compromise-handling-procedures)). The integrity of the logging processes is monitored through continuous automated monitoring or, at a minimum, through a review performed at least once every thirty-one (31) days.

For systems that are kept offline, such as the Root CA systems, the system audit logs are reviewed at each activation of the system. The physical access records and surveillance of the Root CA environment remain subject to the monitoring described above.

### 5.4.3 Retention period for audit log

OWGTM and each Delegated Third Party retain, for at least two (2) years:

1. CA certificate and key lifecycle management event records (as listed in item 1 of [section 5.4.1](#541-types-of-events-recorded)) after the later occurrence of:
   - the destruction of the CA Private Key; or
   - the revocation or expiration of the final CA Certificate in that set of Certificates that have an X.509v3 basicConstraints extension with the cA field set to true and which share a common Public Key corresponding to the CA Private Key;
2. Subscriber Certificate lifecycle management event records (as listed in item 2 of [section 5.4.1](#541-types-of-events-recorded)) after the expiration of the Subscriber Certificate;
3. Security event records (as listed in item 3 of [section 5.4.1](#541-types-of-events-recorded)) after the event occurred.

### 5.4.4 Protection of audit log

Audit logs, whether in production or archived, are protected from modification, substitution, or unauthorized destruction. Archived audit records are stored in fireproof cabinets accessible only to authorized persons.

An audit record can only be destroyed after the signed authorization of the OWGTM auditor and of the OWGTM Information Security Manager. A trace of the destroyed materials is kept for future reference.

### 5.4.5 Audit log backup procedures

The audit logs are backed up using incremental and remote procedures.

### 5.4.6 Audit collection system (internal vs. external)

The audit log collection system of the OWGTM is a combination of automatic and manual processes, executed by the operating systems, the software applications and the personnel operating these systems.

### 5.4.7 Notification to event-causing subject

No stipulation. The subjects that cause an event are not notified.

### 5.4.8 Vulnerability assessments

OWGTM maintains a documented vulnerability management program covering all Certificate Systems, Security Support Systems and Network Boundary Controls. Detected vulnerabilities are reviewed, responded to and remediated within the timeframes stated in [section 6.7](#67-network-security-controls), or alternatively closed through a documented determination that they do not impact the security posture of the CA, with exceptions risk-assessed and recorded. Patch cycles are executed at least monthly, and annual third-party penetration tests complement the internal assessment activities.

OWGTM reviews the activity logs to assess vulnerabilities at least quarterly. In-depth assessments are performed yearly, including the conformance to the disaster recovery plans. If an assessment cannot be performed or is delayed, the OWGTM informs the involved parties and keeps a record of the event and its cause.

OWGTM performs an annual Risk Assessment that:

1. identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management processes;
2. assesses the likelihood and potential damage caused by these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management processes; and
3. assesses the adequacy of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

Penetration Tests, at least annually and after significant infrastructure or application changes, and quarterly Vulnerability Scans are conducted by a team with the skills, tools, proficiency, code of ethics, and independence necessary to provide a reliable Vulnerability Scan or Penetration Test.

The results of these analyses identify the tasks necessary to correct the detected vulnerabilities.

## 5.5 Records archival

This section includes the stipulations regarding record archival and retention.

### 5.5.1 Types of records archived

The information and events archived are:

- Information generated (at the CA and the RA) during the life cycle of all OWGTM certificates;
- Contracts and agreements;
- Audit logs stipulated in [section 5.4](#54-audit-logging-procedures).

### 5.5.2 Retention period for archive

Archived records are retained for at least two (2) years after the expiration of the certificates they relate to, or for the period required by the applicable CA/Browser Forum requirements, whichever is greater.

### 5.5.3 Protection of archive

Access to archived materials is restricted to authorized persons, and controls to ensure the archive integrity are enforced.

### 5.5.4 Archive backup procedures

Backup copies are made daily. The main copy is kept in the principal OWGTM facility, inside a secured zone. Copies are stored off-site periodically.

### 5.5.5 Requirements for time-stamping of records

Archived records include the date and time of their creation. These time stamps need not be cryptographic.

### 5.5.6 Archive collection system (internal or external)

Archive collection is an internal task of the OWGTM that is not outsourced to third parties.

The only exception are the authorized Registration Authority points, which may archive the information collected during the certificate life-cycle. In such case, this information is kept securely, accessible only to authorized persons, and made available to any internal or external auditor mandated by OWGTM.

### 5.5.7 Procedures to obtain and verify archive information

Only authorized personnel obtain access to the physical media containing archives, backups and other recorded information.

Integrity checks are performed automatically when the archive includes a digital signature.

## 5.6 Key changeover

OWGTM requires the creation of new keys for a CA that renews its certificate. Only in exceptional cases a CA Creation Ceremony may be repeated with the same keys created in a Hardware Security Module during a previous ceremony, in order to amend an error in the process.

The validity period of a new certificate for an entity is constrained to the validity of the keys of the Certification Authority issuing it.
<!-- common:end 5.2.3-5.6 -->

<!-- common:begin 5.7 -->
## 5.7 Compromise and disaster recovery

If OWGTM systems and services are not available for a period greater than 12 hours, the Continuity Plan is activated. The Continuity Plan ensures that the critical services (as stated in [section 5.7.4](#574-business-continuity-capabilities-after-a-disaster)) are available in less than 72 hours after the plan is activated.

The following sections summarize the specific situations and the stipulated reaction in the OWGTM. The detailed Continuity Plan is a confidential document.

### 5.7.1 Incident and compromise handling procedures

The Certification and Registration Authorities operating under the OWGTM enforce the controls necessary to ensure and demonstrate that the incident and compromise handling procedures are effective. Involved personnel are trained in their roles and responsibilities.

In the event of a detected or suspected compromise of the CA Infrastructure, OWGTM's incident response procedures comply with the NCSSR requirements for alerting, response time, root-cause analysis, containment and remediation.

**Incident reporting.** OWGTM discloses incidents (failures to comply with this CP/CPS, with the CA/Browser Forum requirements or with the Root Program requirements, including audit findings) in Mozilla's Bugzilla, following the format and timelines of the CCADB Incident Reporting Guidelines and the requirements of the Root Programs.

#### 5.7.1.1 Incident Response and Disaster Recovery Plans

OWGTM documents an Incident Response Plan and a Disaster Recovery Plan.

OWGTM documents business continuity and disaster recovery procedures designed to notify and reasonably protect Application Software Suppliers, Subscribers, and Relying Parties in the event of a disaster, security compromise, or business failure. OWGTM makes its business continuity plan and security plans available to its auditors upon request, and tests, reviews and updates these procedures annually.

The business continuity plan includes:

1. The conditions for activating the plan;
2. Emergency procedures;
3. Fallback procedures;
4. Resumption procedures;
5. A maintenance schedule for the plan;
6. Awareness and education requirements;
7. The responsibilities of the individuals;
8. Recovery time objective (RTO);
9. Regular testing of contingency plans;
10. The CA's plan to maintain or restore the CA's business operations in a timely manner following interruption to or failure of critical business processes;
11. A requirement to store critical cryptographic materials (i.e., secure cryptographic device and activation materials) at an alternate location;
12. What constitutes an acceptable system outage and recovery time;
13. How frequently backup copies of essential business information and software are taken;
14. The distance of recovery facilities to the CA's main site; and
15. Procedures for securing its facility to the extent possible during the period of time following a disaster and prior to restoring a secure environment either at the original or a remote site.

**Compromise notification.** In the event of a key compromise (Root CA, Subordinate CA or Subscriber key), the CA:

1. Revokes the affected certificates within the time frames of [section 4.9.1](#491-circumstances-for-revocation).
2. Notifies the relevant stakeholders (subscribers, RAs, relying parties with a registered relationship) according to defined procedures.
3. Reports to the Root Store Operators, according to their requirements.
4. Retains forensic evidence (logs, access records) for the investigation.

**Post-incident review.** After any incident, the CA conducts a post-incident review, documents lessons learned, updates the incident response plan and remediates root causes.

#### 5.7.1.2 Mass Revocation Plans

OWGTM maintains a comprehensive and actionable plan for mass revocation events, performs annual testing of the mass revocation plan, and incorporates lessons learned into the plan in order to continually improve its preparedness for mass revocation events. The plan ensures a rapid, consistent and reliable response to large-scale certificate revocation events, and is tested, reviewed and updated at least annually. The plan is not public, and is made available to the auditors upon request.

The mass revocation provisions include:

1. Activation criteria – specific, objective, and measurable thresholds at which the mass revocation plan is triggered, based on the CA's risk profile, issuance volumes, and operational capabilities;
2. Customer contact information – how subscriber and customer contact details are stored, maintained, and kept up to date;
3. Automation points – processes that are automated or could be automated, and those processes that require manual intervention;
4. Targets and timelines – for incident triage, revocation initiation, certificate replacement, and post-event review;
5. Subscriber notification methods – mechanisms for notifying impacted Subscribers;
6. Role assignments – roles and responsibilities of personnel responsible for initiating, coordinating, and executing the plan;
7. Training and education – training, awareness, and readiness activities for personnel responsible for, or supporting, the plan;
8. Plan testing – annual operational testing to assess readiness and demonstrate implementation feasibility, using one or more of tabletop exercises, simulations, parallel testing, or controlled test environments that do not involve the revocation of active Subscriber Certificates; and
9. Post-test analysis and update schedule – how lessons learned from testing or live incidents are incorporated into the plan, and how often it is reviewed and updated.
<!-- common:end 5.7 -->

The Subscriber Agreement informs Subscribers about the revocation time frames of [section 4.9.1](#491-circumstances-for-revocation) and requires their timely cooperation in the replacement of certificates that must be revoked.

<!-- common:begin 5.7.2-5.8 -->
### 5.7.2 Computing resources, software, and/or data are corrupted

If the hardware or software resources are altered or suspected to have been altered, the OWGTM stops normal operations until a secure environment is established. In parallel, an audit is conducted to identify the cause and the actions necessary to avoid a recurrence.

If certificates are issued during the period of uncertainty and there is a risk that they are compromised, those certificates are revoked and the subscribers are notified of the need to obtain new certificates.

### 5.7.3 Entity private key compromise procedures

If a CA private key of the OWGTM is compromised, in addition to the stipulations of [section 5.7.2](#572-computing-resources-software-andor-data-are-corrupted), the subordinate entities depending on the compromised private key are notified and the necessary actions are undertaken.

All certificates issued by entities subordinated to the compromised key between the time of the key's compromise and the revocation of its certificate are revoked, and the involved parties are notified as stipulated in this CP/CPS. Additional steps are taken to re-issue the necessary certificates.

### 5.7.4 Business continuity capabilities after a disaster

In the event of a disaster (independently of its nature) that affects OWGTM's main facilities and the services provided from them, the OWGTM Service Continuity Plan is activated, ensuring that the services identified as "Critical" are available in less than 72 hours after the activation of the plan. The other services are restored within the time objectives defined in the Service Continuity Plan according to their criticality.

## 5.8 CA or RA termination

The causes that could imply the termination of a Certification or Registration Authority operating under the OWGTM are:

- Private Key Compromise;
- A political or judicial decision;
- A contract termination after a breach of the corresponding terms and conditions.

If a Certification Authority under the OWGTM terminates its activities, the minimum actions to be executed are:

- Immediately after the termination decision, notify all certificate subscribers and the Root Store Operators (through the CCADB);
- Revoke all certificates issued by the CA;
- Inform all relying parties that have a registered direct relationship with that Certification Authority about the termination of the certificate service. This also terminates the accreditation granted to the Certification Authority to operate under the OWGTM;
- Publish a public notice of the termination in the repository of the affected CA, and undertake other public communications as deemed necessary to inform the wider relying party community.

The termination of an OWGTM Root Certification Authority implies the termination of the entire hierarchy dependent on that Root CA.
<!-- common:end 5.7.2-5.8 -->

# 6. TECHNICAL SECURITY CONTROLS

<!-- common:begin 6-6.1.1.2 -->
This section describes the technical security controls of the Certification Authorities operating under the OWGTM. These controls are fundamental to provide trust to subscribers and relying parties, and the OWGTM has established the means to ensure and demonstrate that they are enforced. These controls are audited internally and externally by accredited bodies.

## 6.1 Key pair generation and installation

Key pairs are generated under the necessary security levels, in secure physical facilities and under adequate personnel control.

### 6.1.1 Key pair generation

#### 6.1.1.1 CA Key Pair Generation

The key pairs of the Certification Authorities operating in the OWGTM are generated and installed under a procedure compliant with the applicable requirements:

- The Root CA key generation ceremony is witnessed by an external Qualified Auditor, who issues a report on the ceremony.
- The Subordinate CA key generation ceremonies are performed under the direct supervision of internal auditors from WISeKey.
- CA ceremonies are executed by designated personnel in Trusted Roles, under Multi-Party Control.
- A pre-defined script is followed during the ceremony.
- During the ceremony, an audit trail is recorded that is sufficient to prove that the ceremony was executed as planned and without any security risk.
- After the ceremony, a Ceremony Report is generated and archived.

All CA key pairs are generated within, and their private keys are protected by, Hardware Security Modules (HSM) meeting the standards specified in [section 6.2.1](#621-cryptographic-module-standards-and-controls). CA HSM administrative access requires split knowledge and multi-person authentication.

The key pairs of the Subordinate CAs are generated within the HSMs that operate them, or within HSMs of the same standard from which they are transferred under the controls of [section 6.2.6](#626-private-key-transfer-into-or-from-a-cryptographic-module). **TO BE CONFIRMED** (version 4.2 allowed the key pairs of Policy and Issuing CAs to be "generated in escrowable form" and imported into the HSMs; confirm that this practice is no longer used.)

#### 6.1.1.2 RA Key Pair Generation

No stipulation. RA key pairs are subject to the controls of the RA credentials described in [section 5.2.3](#523-identification-and-authentication-for-each-role).
<!-- common:end 6-6.1.1.2 -->

#### 6.1.1.3 Subscriber Key Pair Generation

<!-- common:begin 6.1.1.3 -->
OWGTM rejects a certificate request if one or more of the following conditions are met:

1. The Key Pair does not meet the requirements of [section 6.1.5](#615-key-sizes) and/or [section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
2. There is clear evidence that the specific method used to generate the Private Key was flawed;
3. The CA is aware of a demonstrated or proven method that exposes the Applicant's Private Key to compromise;
4. The CA has previously been notified that the Applicant's Private Key has suffered a Key Compromise, using the procedures of [section 4.9.3](#493-procedure-for-revocation-request) and [section 4.9.12](#4912-special-requirements-re-key-compromise);
5. The Public Key corresponds to an industry-demonstrated weak Private Key. At least the following precautions are implemented:
   1. In the case of the Debian weak keys vulnerability (https://wiki.debian.org/SSLkeys), the CA rejects all keys found at https://github.com/cabforum/Debian-weak-keys/ for each key type (e.g., RSA, ECDSA) and size listed in the repository. For all other keys meeting the requirements of [section 6.1.5](#615-key-sizes), with the exception of RSA key sizes greater than 8192 bits, the CA rejects Debian weak keys.
   2. In the case of the ROCA vulnerability, the CA rejects keys identified by the tools available at https://github.com/crocs-muni/roca or equivalent.
   3. In the case of the Close Primes vulnerability (https://fermatattack.secvuln.info/), the CA rejects weak keys which can be factored within 100 rounds using Fermat's factorization method.
<!-- common:end 6.1.1.3 -->

The key pair of a Personal Certificate is generated by the Subscriber or, when allowed for the certificate type, by the CA or the RA on behalf of the Subscriber. A key pair generated by the CA or the RA meets the requirements of [section 6.1.5](#615-key-sizes) and [section 6.1.6](#616-public-key-parameters-generation-and-quality-checking), and is delivered as described in [section 6.1.2](#612-private-key-delivery-to-subscriber).

### 6.1.2 Private key delivery to subscriber

The private keys of CA certificates are never delivered or handled outside the HSMs of [section 6.2.1](#621-cryptographic-module-standards-and-controls).

If the certificate type allows the generation of the private key by the CA or the Registration Authority, the private key is delivered in a password-protected encrypted software file, in a smart card or in another accepted crypto-token.

When OWGTM or a Registration Authority generates the key pair on behalf of the Subscriber, the private key is delivered either in hardware with an activation method equivalent to at least 128 bits of encryption, or encrypted using an algorithm and key size providing at least 112 bits of encryption strength (e.g., a PKCS#12 file using an approved key-wrapping algorithm), in accordance with Section 6.1.2 of the S/MIME Baseline Requirements. The activation data or password is delivered through a channel separate from the protected key, and Subscriber private keys are never stored in clear text. Any private key generated for a digital signature use is deleted by the CA or RA once its transfer to the Subscriber is effective, unless it is escrowed as described in [section 4.12](#412-key-escrow-and-recovery).

If OWGTM or any of its RAs becomes aware that a Subscriber's Private Key has been communicated to an unauthorized person or to an organization not affiliated with the Subscriber, OWGTM revokes all certificates that include the Public Key corresponding to the communicated Private Key.

<!-- common:begin 6.1.3-6.1.4 -->
### 6.1.3 Public key delivery to certificate issuer

Public keys generated by, or for, the end entities are sent to the Certification Authority through secure channels, as part of a certificate request in an accepted format, such as PKCS#10 or the ACME protocol.

### 6.1.4 CA public key delivery to relying parties

The certificates of all Certification Authorities operating under the OWGTM are published in the repositories of [section 2.1](#21-repositories) and disclosed in the CCADB.

Trusted Root Certificates can be obtained directly from the root stores of the main browsers and operating systems.
<!-- common:end 6.1.3-6.1.4 -->

### 6.1.5 Key sizes

The OWGTM uses the following keys and algorithms for the CAs and the Subscriber Certificates within the scope of this document, in accordance with Section 6.1.5 of the S/MIME Baseline Requirements:

- RSA keys with a modulus of at least 2048 bits, divisible by 8. The keys of CA Certificates (Root, Subordinate and Cross-Certificates) signed on or after 2026-09-15 have a modulus of at least 4096 bits.
- ECDSA keys on the NIST P-256 or P-384 curves. NIST P-521 keys are not used in the hierarchies governed by this document.

Effective 2027-09-15, no S/MIME Certificate is issued by a CA whose RSA key has a modulus of less than 3072 bits. The Subordinate CAs affected by this rule are WISeKey CertifyID Personal GB CA 3, WISeKey CertifyID Personal GB CA 4 and WISeKey CertifyID Advanced Services CA 4 (see [Appendix B](#appendix-b-ca-hierarchies)).

Certificates and CRLs are signed using sha256WithRSAEncryption, sha384WithRSAEncryption or sha512WithRSAEncryption, or using ECDSA with SHA-256 (P-256 signing keys) or SHA-384 (P-384 signing keys). Effective 2026-09-15, no certificate or CRL within the scope of the S/MIME Baseline Requirements is signed using a signature algorithm that incorporates SHA-1, and no unexpired Subordinate CA Certificate within that scope whose signature incorporates SHA-1 remains unrevoked. Subordinate CA Certificates outside the scope of the S/MIME Baseline Requirements and of the corresponding audits are not subject to this revocation provision.

<!-- common:begin 6.1.6-6.1.7 -->
### 6.1.6 Public key parameters generation and quality checking

The algorithms used in the OWGTM for key generation are RSA and ECDSA.

RSA: OWGTM confirms that the value of the public exponent is an odd number equal to 3 or more. Additionally, the public exponent SHOULD be in the range between 2^16 + 1 and 2^256 - 1. The modulus SHOULD also have the following characteristics: an odd number, not the power of a prime, and have no factors smaller than 752. [Source: Section 5.3.3, NIST SP 800-89]

ECDSA: OWGTM SHOULD confirm the validity of all keys using either the ECC Full Public Key Validation Routine or the ECC Partial Public Key Validation Routine. [Source: Sections 5.6.2.3.2 and 5.6.2.3.3, respectively, of NIST SP 800-56A: Revision 2]

### 6.1.7 Key usage purposes (as per X.509 v3 key usage field)

The key usage of CA certificates is restricted to digital signature, CRL signing and certificate signing.

Private keys corresponding to Root Certificates are not used to sign certificates except in the following cases:

- Self-signed certificates to represent the Root CA itself;
- Certificates for Subordinate CAs and Cross-Certificates;
- Certificates for infrastructure purposes (administrative role certificates, internal CA operational device certificates); and
- Certificates for OCSP Response verification.

All subscriber certificates issued in the OWGTM contain the "Key Usage" and "Extended Key Usage" extensions, as defined in the profiles of [Appendix D](#appendix-d-certificate-profiles).

## 6.2 Private Key Protection and Cryptographic Module Engineering Controls

The OWGTM has established controls to ensure that the risks derived from a private key compromise are managed and kept under reasonable levels. These controls are different for the CA keys and for the subscriber keys.

### 6.2.1 Cryptographic module standards and controls

The Certification Authorities of the OWGTM use Hardware Security Modules validated to FIPS 140-2 Level 3 or FIPS 140-3 Level 3, or evaluated against an appropriate Common Criteria Protection Profile or Security Target at EAL 4 or higher. Other PKI components use cryptographic modules validated at least to FIPS 140-2 or FIPS 140-3 Level 2.

### 6.2.2 Private key (n out of m) multi-person control

The private keys of the Certification Authorities are always under multi-person control. The activation data needed to enable a Certification Authority is shared so that at least two authorized persons are needed to perform any sensitive operation on a Certification Authority, except where the unattended operational restart of Issuing CAs is enabled.

Private keys of end entities are under the sole control of the subscriber or of its authorized representative.
<!-- common:end 6.1.6-6.1.7 -->

### 6.2.3 Private key escrow

Private key escrow is only provided for the Private Keys of Personal Certificates, as described in [section 4.12](#412-key-escrow-and-recovery). The private keys of the Certification Authorities are not escrowed.

### 6.2.4 Private key backup

<!-- common:begin 6.2.4-ca -->
Backup copies of the CA private keys of all Certification Authorities under the OWGTM are kept for routine recovery and disaster recovery purposes. Such keys are always stored in encrypted form within hardware cryptographic modules and associated key storage devices that meet the requirements of [section 6.2.1](#621-cryptographic-module-standards-and-controls).
<!-- common:end 6.2.4-ca -->

Backup copies of the Private Keys of Personal Certificates are only kept when key escrow is provided, as described in [section 4.12](#412-key-escrow-and-recovery).

<!-- common:begin 6.2.5-6.3.1 -->
### 6.2.5 Private key archival

The CA does not provide key archival services to subscribers. The private keys of expired or revoked CAs may be archived by leaving them in the HSM or its backup until their destruction.

### 6.2.6 Private key transfer into or from a cryptographic module

The key pairs of the Certification Authorities operating under the OWGTM are operated in Hardware Security Modules as defined in [section 6.2.1](#621-cryptographic-module-standards-and-controls). Private keys can be transferred between such modules, in encrypted form and under Multi-Party Control, for backup and recovery operations.

### 6.2.7 Private key storage on cryptographic module

All CA Private Keys are stored on a cryptographic module that has been evaluated to at least FIPS 140-2 Level 3, FIPS 140-3 Level 3, or an appropriate Common Criteria Protection Profile or Security Target, EAL 4 (or higher), which includes requirements to protect the Private Key and other assets against known threats.

### 6.2.8 Method of activating private key

The private key of a Certification Authority is activated by initiating the PKI software and activating the HSM where the key is stored. This process requires at least dual-person control, except for Issuing CAs where automatic key activation in case of system failure or restart is enabled.

The activation of subscriber private keys is stipulated in [section 6.4](#64-activation-data).

### 6.2.9 Method of deactivating private key

The private key of a Certification Authority is deactivated by shutting down the associated server, by terminating the PKI software, or by extracting or shutting down the HSM that contains the key. This task can be done by a Systems Administrator and, when planned, is notified to and authorized by the person responsible for the CA.

RA or end-user private keys stored in hardware are deactivated by removing the secure device (smart card or other accepted crypto-token) from the workstation where it is used.

End-user private keys not stored in hardware are deactivated by shutting down the device where the private key is stored. The subscriber takes all reasonable measures to avoid the unauthorized use of the device.

### 6.2.10 Method of destroying private key

The procedure to destroy a private key is initiated in the following cases:

- The private key is no longer used and its destruction is mandated;
- The token or HSM containing the key has deteriorated to an extent that prevents its normal usage;
- A lost or stolen token is found, and the keys it contained are suspected to be compromised.

A private key can be destroyed by the key owner or by its legal representative. In such cases the corresponding certificate is revoked. The procedure used to destroy the private key depends on the container holding it. The private keys of CAs are destroyed under dual control, and the destruction is recorded.

### 6.2.11 Cryptographic Module Rating

No stipulation additional to [section 6.2.1](#621-cryptographic-module-standards-and-controls).

## 6.3 Other aspects of key pair management

This section includes additional stipulations regarding key pair management.

### 6.3.1 Public key archival

The public keys of the OWGTM are archived for a period of 7 years after the expiry or revocation of the corresponding certificate.
<!-- common:end 6.2.5-6.3.1 -->

### 6.3.2 Certificate operational periods and key pair usage periods

The operational period of a certificate starts at its issuance and ends with its expiration or revocation. The validity period of a certificate is limited by the validity of the issuing Certification Authority.

| Certificate type | Validity period |
| --- | --- |
| OISTE WISeKey Global Root GA CA | 32 years |
| Other Root CAs within the scope of this document | 25 years |
| Subordinate CA Certificates and Cross-Certificates | Up to the remaining lifetime of the issuing Root CA. Subordinate CA Certificates signed on or after the effective date of this document have a validity period of at most five (5) years, with a target of three (3) years. **TO BE CONFIRMED** |
| S/MIME Certificates (Mailbox-, Individual-, Sponsor- and Organization-validated, Multipurpose generation) | At most 825 days |
| Client authentication and document signing certificates without the `id-kp-emailProtection` EKU | At most 825 days **TO BE CONFIRMED** |

For the purpose of calculations, a day is measured as 86,400 seconds, and any amount of time greater than this, including fractional seconds and leap seconds, represents an additional day.

When key escrow is supported in accordance with [section 4.12](#412-key-escrow-and-recovery), the CA may retain Subscriber Private Keys past the validity period of the certificate.

The commitments regarding the retirement of the Root CAs within the scope of this document are stated in [Appendix B](#appendix-b-ca-hierarchies).

## 6.4 Activation data

<!-- common:begin 6.4-ca -->
This section stipulates the management of the data necessary to activate the private keys.

### 6.4.1 Activation data generation and installation

The activation data of the Certification Authorities is generated and stored in cryptographic tokens and/or smart cards, which are only used by authorized persons and require a password or PIN to enable the activation process.

Activations requiring multi-person control are enforced by splitting the activation data across several tokens.
<!-- common:end 6.4-ca -->

End-entity activation data is only stipulated for hardware-based private keys. In particular:

- The private keys of RA certificates and of Qualified Certificates, when protected in a hardware device, require a password or PIN of eight or more characters to activate the hardware device where the key is stored.
- The private keys of Standard Personal Certificates can be generated and installed without a password, although this is discouraged.

The private keys of other certificate types are generated after the subscriber has been authenticated in the system where the keys are created, for example with a password to access the RA user interface.

<!-- common:begin 6.4.2-6.8 -->
### 6.4.2 Activation data protection

Only the authorized persons know the password or PIN that activates the private keys. In the case of end entities, only the subscriber is entitled to know this information.

In all cases, the owner of the activation data safeguards its secrecy.

### 6.4.3 Other aspects of activation data

No stipulation. No other aspects of activation data are regulated.

## 6.5 Computer security controls

The details of the computer security controls are classified and therefore not made public. The documents describing them are only available to authorized personnel involved in OWGTM operations, and are disclosed to accredited external parties for audit purposes.

The Certification and Registration Authorities operating under the OWGTM meet these security controls, and their compliance is verified by audits.

OWGTM implements access controls, monitoring, logging, alerting, change management, vulnerability management and operational security in accordance with the latest version of the NCSSR, and retains evidence of compliance with its requirements.

### 6.5.1 Specific computer security technical requirements

OWGTM enforces procedures and technical measures to effectively control security risks, including:

- Maintaining Root CA Systems Air-Gapped — physically and logically separated, disconnected and isolated from all other systems — within a Physically Secure Environment and on physically separate networks from all other CA Infrastructure;
- Authentication of each authorized individual through unique, individually attributable credentials, technical measures minimizing the susceptibility to repeated authentication attempts (e.g., account lockout and rate limiting), and Multi-Factor Authentication for all accounts capable of authenticating to or accessing the CA Infrastructure and Network Boundary Controls; a possession-based cryptographic key is relied upon as an authentication factor only when stored in a device resistant to key extraction;
- Granting administration access to Certificate Systems only to persons acting in Trusted Roles, who are accountable for the Certificate System's security;
- Removing or disabling all accounts, applications, services, protocols, and ports that are not used in operations;
- Continuous improvement of administration and operating procedures;
- Physical isolation of confidential systems;
- Antivirus and anti-malware detection systems;
- Internal security reviews, performed at least annually. **TO BE CONFIRMED**

Workstations are configured to prevent continued access after a set period of inactivity, for example by automatically logging off active users.

### 6.5.2 Computer security rating

No stipulation. No specific computer security rating is required.

## 6.6 Life cycle technical controls

### 6.6.1 System development controls

Systems are developed using the WISeKey KeySteps Methodology, which ensures security and quality by setting policies and operational and technical procedures controlling the building of the PKI components in all the phases of a project.

The authenticity and integrity of critical software components are checked before they are enabled in a production environment, by using code signing or other acceptable methods.

OWGTM monitors for updated versions of any third-party Linting software used in the CA service, and plans its update no later than three (3) months after the release of an update. When appropriate, after updating the Linting software, OWGTM performs Linting on the corpus of its unexpired, unrevoked Subscriber Certificates.

### 6.6.2 Security management controls

OWGTM maintains a documented information security management framework aligned with the ISO/IEC 27001 principles and with the NCSSR. Security policies and procedures are approved by management, reviewed at least annually, and enforced for all personnel acting in Trusted Roles.

### 6.6.3 Life cycle security controls

OWGTM establishes and maintains a change management process that is aligned with the NCSSR and is:

1. documented comprehensively;
2. authoritative for:
   - all personnel in Trusted Roles;
   - management of Network Boundary Controls; and
   - management of CA Infrastructure;
3. reviewed annually;
4. updated as needed; and
5. approved:
   - with each update;
   - prior to going into effect; and
   - by personnel in applicable Trusted Roles.

## 6.7 Network security controls

The OWGTM enforces effective controls to minimize the risks related to network security. OWGTM infrastructures are protected in accordance with the latest version of the NCSSR.

These protections include:

- Vulnerability scans;
- Effective network segmentation through firewall systems and other controls;
- Detection and prevention measures to guard against viruses and malicious software;
- Monitoring controls for health and any abnormal activity;
- System security patch management;
- Management of logical access permissions in accordance with a formal procedure;
- Multi-Factor Authentication;
- Monitoring of the configuration of access permissions;
- Regular training of personnel in Trusted Roles.

Vulnerability scans covering the Certificate Systems, Security Support Systems and Network Boundary Controls are performed at least quarterly. Independent penetration tests are performed by external parties at least annually. The following timeframes, established in accordance with the Risk Assessment described in [section 5.4.8](#548-vulnerability-assessments), are the timeframes for responding to and remediating vulnerabilities that the NCSSR requires to be documented in this section. Vulnerabilities are reviewed, responded to and remediated within these timeframes, or alternatively closed by documenting the rationale why they do not impact the security posture of the CA:

- Critical severity vulnerabilities are addressed within 96 hours;
- High severity vulnerabilities are addressed within 10 days;
- Medium or lower severity vulnerabilities are addressed within 60 days.

Exceptions are documented, assessed for risk, and recorded.

The Root CA systems are offline systems, physically disconnected from any computer network. All communication of sensitive information is protected using encryption and digital signature techniques.

When allowed, remote connections enabling Privileged Access to the CA Infrastructure comply with the NCSSR requirements for remote access: they (i) originate from a Workstation owned and controlled by the CA; (ii) use a temporary, non-persistent encrypted channel; (iii) require Multi-Factor Authentication; and (iv) are mediated by an asset acting as a Network Boundary Control located within the CA's network.

The detailed information about these controls is classified and only made available to external auditors after the appropriate authorization process.

## 6.8 Time-stamping

The OWGTM publishes a Time-Stamping Policy (CertifyID TSP) that regulates the operation of Time-Stamping Authorities according to RFC 3161. This service is provided by WISeKey as the main operator and by other authorized entities adhering to the TSP. More information on time-stamping services is published at https://oiste.org/repository.

The time and date information of other data, such as certificates and CRLs, is not cryptographic.
<!-- common:end 6.4.2-6.8 -->

# 7. CERTIFICATE, CRL, AND OCSP PROFILES

<!-- common:begin 7-intro -->
All certificates issued under the OWGTM comply with:

- ITU-T Recommendation X.509: Information Technology - Open Systems Interconnection - The Directory: Public-key and attribute certificate frameworks; and
- RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile.
<!-- common:end 7-intro -->

## 7.1 Certificate profile

The certificate profiles of the CAs, OCSP Responders and Subscriber Certificates within the scope of this document are described in [Appendix D](#appendix-d-certificate-profiles). The profiles of S/MIME Certificates comply with Section 7.1 of the S/MIME Baseline Requirements. The profiles effectively used are always aligned with the version of these requirements in force at the moment of issuance.

### 7.1.1 Version number(s)

<!-- common:begin 7.1.1 -->
All certificates in the OWGTM conform to X.509 Version 3.
<!-- common:end 7.1.1 -->

### 7.1.2 Certificate extensions

The extensions of each certificate type are specified in [Appendix D](#appendix-d-certificate-profiles). In particular:

- **Subordinate CA Certificates.** Every Subordinate CA Certificate created after 2019-01-01 contains an Extended Key Usage extension. Subordinate CA Certificates used to issue S/MIME Certificates contain `id-kp-emailProtection` and may contain `id-kp-clientAuth`; the values `id-kp-serverAuth`, `id-kp-codeSigning`, `id-kp-timeStamping` and `anyExtendedKeyUsage` are never present. Other values may be present only in Subordinate CA Certificates signed before 2026-08-01 (see [section 1.4.1.1](#1411-trust-purposes-and-extended-key-usages)).
- **Cross-Certificates.** Cross-Certificates issued to the Root CAs of the OWGTM S/MIME hierarchies (OISTE Client Root RSA G1 and OISTE Client Root ECC G1) by a multi-purpose Root CA contain only the values `id-kp-emailProtection`, or `id-kp-emailProtection` and `id-kp-clientAuth`, and never `anyExtendedKeyUsage`, as required by Section 7.1.2.2 of the S/MIME Baseline Requirements and Section 6.3 of the CCADB Policy.
- **Subscriber Certificates.** The Key Usage and Extended Key Usage of S/MIME Certificates follow Section 7.1.2.3 of the S/MIME Baseline Requirements and the rules of [section 1.4.1.1](#1411-trust-purposes-and-extended-key-usages).
- **Serial numbers.** The serial number of every certificate is a non-sequential, positive number greater than zero that contains at least 64 bits of output from a CSPRNG, and is not longer than 20 octets.

### 7.1.3 Algorithm object identifiers

The following algorithm object identifiers are used in the certificates within the scope of this document:

| Use | Algorithms |
| --- | --- |
| Subject public key | `rsaEncryption` (RSA keys of [section 6.1.5](#615-key-sizes)); `id-ecPublicKey` with `secp256r1` or `secp384r1` |
| Signature | `sha256WithRSAEncryption`, `sha384WithRSAEncryption`, `sha512WithRSAEncryption`; `ecdsa-with-SHA256` (P-256 signing keys), `ecdsa-with-SHA384` (P-384 signing keys) |

The `sha1WithRSAEncryption` algorithm is not used to sign any certificate or CRL within the scope of the S/MIME Baseline Requirements. The self-signature of the OISTE WISeKey Global Root GA CA, created in 2005, uses `sha1WithRSAEncryption`.

### 7.1.4 Name forms

<!-- common:begin 7.1.4 -->
For CA certificates, the Subject Distinguished Name, by combining adequate values of the commonName, organizationalUnitName, organizationName and countryName attributes, uniquely identifies the CA and distinguishes it from the other CAs of the Trust Model.

For every valid Certification Path (as defined by RFC 5280, Section 6):

- for each Certificate in the Certification Path, the encoded content of the Issuer Distinguished Name field of a Certificate is byte-for-byte identical with the encoded form of the Subject Distinguished Name field of the Issuing CA Certificate; and
- for each CA Certificate in the Certification Path, the encoded content of the Subject Distinguished Name field of a Certificate is byte-for-byte identical among all Certificates whose Subject Distinguished Names can be compared as equal according to RFC 5280, Section 7.1, including expired and revoked Certificates.
<!-- common:end 7.1.4 -->

The Subject Distinguished Name of S/MIME Certificates contains only the attributes listed for each profile in [Appendix D](#appendix-d-certificate-profiles), validated as described in [section 3.2](#32-initial-identity-validation) and encoded as required by Section 7.1.4 of the S/MIME Baseline Requirements. If the `subject:commonName` attribute contains a Pseudonym, the `subject:givenName` and `subject:surname` attributes are not present; if it contains a Personal Name, the `subject:pseudonym` attribute is not present.

### 7.1.5 Name constraints

OWGTM requires that any Subordinate CA capable of issuing certificates containing the `id-kp-emailProtection` EKU that is not operated by WISeKey be technically constrained, as defined in Section 7.1.5 of the S/MIME Baseline Requirements, to a set of pre-agreed Mailbox Address domains (`rfc822Name` permitted subtrees). If such a CA is not technically constrained, it is included in the scope of the external audits of [section 8](#8-compliance-audit-and-other-assessments) against the S/MIME Baseline Requirements. At the effective date of this document, no such CA exists.

Domain name restrictions are also applied in the Managed PKI interface, which only allows an Enterprise RA to request certificates for Mailbox Addresses within its validated domains.

### 7.1.6 Certificate policy object identifier

The object identifiers used in the certificates within the scope of this document are listed in [Appendix C](#appendix-c-oid-inventory).

Every S/MIME Certificate contains exactly one of the reserved CA/Browser Forum S/MIME policy identifiers of the Multipurpose generation listed in [Appendix C](#appendix-c-oid-inventory), according to its validation type. The CAs governed by this CP/CPS represent that all certificates containing a policy identifier indicating compliance with the S/MIME Baseline Requirements are issued and managed in accordance with those Requirements.

The certificates that qualify for the Adobe Approved Trust List (AATL) are identified by the OWGTM AATL policy identifiers listed in [Appendix C](#appendix-c-oid-inventory), as required by the AATL Technical Requirements. **TO BE CONFIRMED** (which identifiers are asserted in current certificates, and which OWGTM CAs are included in the AATL)

<!-- common:begin 7.1.7-7.1.9 -->
### 7.1.7 Usage of Policy Constraints extension

The Subordinate CAs are constrained to comply with the CA/Browser Forum and Root Program requirements applicable to them. Issuing CAs cannot issue their own Subordinate CAs (path length constraint of zero) and are restricted in the key usages allowed in end-entity certificates. The correctness of this information is verified during the Key Generation Ceremony of the CA. The Policy Constraints extension is not used.

### 7.1.8 Policy qualifiers syntax and semantics

Unless disallowed by the applicable requirements, certificates may contain the `id-qt-cps` policy qualifier with the HTTP or HTTPS URL of the OWGTM repository.

### 7.1.9 Processing semantics for the critical Certificate Policies extension

The Certificate Policies extension is not marked critical. It identifies the policy under which the certificate was issued; software applications that require a specific certificate type check this extension to verify the suitability of the certificate for the intended purpose.

## 7.2 CRL profile

The CRLs generated under the OWGTM comply with RFC 5280.

### 7.2.1 Version number(s)

The CRLs of the OWGTM conform to X.509 Version 2.
<!-- common:end 7.1.7-7.1.9 -->

### 7.2.2 CRL and CRL entry extensions

The CRLs of the CAs within the scope of this document contain the following extensions:

| Extension | Presence | Critical | Content |
| --- | --- | --- | --- |
| `authorityKeyIdentifier` | Mandatory | No | Key identifier of the issuing CA |
| `CRLNumber` | Mandatory | No | An INTEGER greater than or equal to zero (0) and less than 2^159, conveying a strictly increasing sequence |
| `IssuingDistributionPoint` | Only in partitioned CRLs | Yes | Identifies the partition |

Each revoked certificate entry contains the `serialNumber` and the `revocationDate` and, when applicable, a non-critical `reasonCode` entry extension, in accordance with Section 7.2.2 of the S/MIME Baseline Requirements. The CRL entries of Root CA and Subordinate CA Certificates, including Cross-Certificates, always contain a `reasonCode`. When the reason for revocation is unspecified, the `reasonCode` extension is omitted. OWGTM uses the following reasons:

| RFC 5280 reasonCode | Value | Use |
| --- | --- | --- |
| unspecified | 0 | Represented by the omission of the reasonCode. It is not used for CA Certificates. |
| keyCompromise | 1 | It is known or suspected that the Subscriber's Private Key has been compromised. |
| affiliationChanged | 3 | The Subject's name or other Subject Identity Information in the certificate has changed (e.g., the Subscriber has left the Organization named in the certificate), and there is no cause to suspect that the Private Key has been compromised. |
| superseded | 4 | The certificate is replaced because the Subscriber requested a new certificate, because the validation of mailbox authorization or control should not be relied upon, or because the certificate was revoked for compliance reasons. |
| cessationOfOperation | 5 | The Subscriber no longer uses, or no longer controls, the Mailbox Address or the Domain Name in the certificate, before the expiration of the certificate. |
| privilegeWithdrawn | 9 | There has been a subscriber-side infraction that has not resulted in keyCompromise, such as the provision of misleading information in the certificate request or the breach of material obligations under the Subscriber Agreement. |

The certificateHold reason (6) is never used.

The Subscriber Agreement informs Subscribers about these revocation reasons and when to choose each of them. The revocation tools of the certificate management portals allow the Subscriber to select the reasons keyCompromise, affiliationChanged, superseded and cessationOfOperation, or no reason; the default option is that no revocation reason is provided. The privilegeWithdrawn reason is not offered to the Subscriber, because its use is determined by the CA.

## 7.3 OCSP profile

When provided, the OCSP responses of the CAs within the scope of this document conform to RFC 6960 and/or RFC 5019. The OCSP Responder certificates follow the profile of [Appendix D](#appendix-d-certificate-profiles). The CRLReason of a revoked certificate in an OCSP response is one of the values permitted for CRLs in [section 7.2.2](#722-crl-and-crl-entry-extensions) and matches the reason in the CRL.

### 7.3.1 Version number(s)

OCSP responses use Version 1 of the OCSP protocol defined in RFC 6960.

### 7.3.2 OCSP extensions

OCSP responses may include the nonce extension when it is present in the request, in accordance with RFC 8954.

# 8. COMPLIANCE AUDIT AND OTHER ASSESSMENTS

OWGTM monitors and ensures compliance with legal, security and industry requirements at all levels of the Trust Model, through internal and external audits. The external audits of the CAs within the scope of this document are performed as required by the S/MIME Baseline Requirements and the Root Programs.

<!-- common:begin 8-intro -->
OWGTM carries out internal and external audits, risk assessments, system inventories and reviews of its CA Infrastructure, Network Boundary Controls and Certificate Systems in alignment with the NCSSR, and retains the records of these activities.
<!-- common:end 8-intro -->

## 8.1 Frequency or circumstances of assessment

<!-- common:begin 8.1 -->
All Certification Authorities and the Registration Authorities depending on them are assessed under the programs of [section 8.4](#84-topics-covered-by-assessment) at least once every 365 days. The external audits are period-of-time audits whose audit periods are contiguous, with no gap, from the generation of each CA key until the key is destroyed or ceases to be trusted, and each audit period does not exceed one year.

In addition, OWGTM performs the quarterly self-audits of [section 8.7](#87-self-audits).
<!-- common:end 8.1 -->

<!-- common:begin 8.2-8.3 -->
## 8.2 Identity/qualifications of assessor

An auditor or assessor is selected when an audit or assessment is required. Any company or professional contracted as auditor or assessor fulfils these requirements:

- Adequate and accredited capability and experience to perform the required services (PKI audit, security assessment, etc.). For external audits, the auditor is a Qualified Auditor licensed to perform WebTrust audits.
- In the case of external audits, independence from the OWGTM at an organizational level.

## 8.3 Assessor's relationship to assessed entity

The OWGTM audit policy does not allow any kind of legal, organizational or other relationship with the external auditor that would result in a conflict of interests.
<!-- common:end 8.2-8.3 -->

## 8.4 Topics covered by assessment

The Root CAs and the Subordinate CAs within the scope of this document, owned or operated by OISTE or WISeKey, are audited annually against:

- WebTrust Principles and Criteria for Certification Authorities;
- WebTrust Principles and Criteria for Certification Authorities – S/MIME; and
- WebTrust Principles and Criteria for Certification Authorities – Network Security.

The Subordinate CAs that issue client authentication or document signing certificates are within the scope of the WebTrust Principles and Criteria for Certification Authorities audit. The versions of the criteria used are those required by the Root Programs for the audit period.

Registration Authorities, Enterprise RAs and Delegated Third Parties are assessed as described in [section 8.7](#87-self-audits).

<!-- common:begin 8.5-8.6 -->
## 8.5 Actions taken as a result of deficiency

If a deficiency is identified, the OWGTM adopts, and is responsible for, all necessary corrective measures.

In the case of a severe deficiency affecting the reliable operation of a Certification or Registration Authority, the OWGTM may temporarily suspend the activities of the affected systems or services until the deficiency is solved.

Deficiencies that constitute incidents, including audit findings, are publicly disclosed in Mozilla's Bugzilla as described in [section 5.7.1](#571-incident-and-compromise-handling-procedures), and managed until their resolution.

## 8.6 Communication of results

The results of each assessment are reported in:

- A detailed report, which covers all the topics of the assessment program in detail. The detailed report is private and only available to the following parties:
  - The Certification Authority owner;
  - The OWGTM Policy Approval Authority;
  - The Root Programs, upon request.
- An audit statement, which includes the formal opinion of the auditor, the topics covered, the CAs in scope, and the policy documents (with their version numbers) on which the audit was based. The audit statement is public: it is published in the OWGTM repository and submitted to the CCADB within the timeframe required by the CCADB Policy (currently 92 days after the end of the audit period).
<!-- common:end 8.5-8.6 -->

For audit periods starting on or after 2027-07-01, OWGTM also obtains a Detailed Controls Report from its auditor, and provides it to the Root Programs that require it.

## 8.7 Self-Audits

During the period in which a CA issues certificates, OWGTM monitors adherence to this CP/CPS and to the S/MIME Baseline Requirements by performing self-audits at least quarterly, against a randomly selected sample including a minimum of the greater of thirty (30) certificates or three percent (3%) of the certificates issued by the CA during the period commencing immediately after the previous self-audit sample was taken. The self-audit includes the Linting of the selected certificates, independently of the Linting performed at issuance.

OWGTM additionally performs the annual self-assessments required by the Root Programs and the CCADB, and submits them to the CCADB.

The results are retained and provided to the auditors upon request.

OWGTM does not delegate the verification of mailbox authorization or control. If a Delegated Third Party is allowed to perform other validation functions, OWGTM obtains an audit report, issued under the audit schemes of [section 8.4](#84-topics-covered-by-assessment), that provides an opinion whether the Delegated Third Party's performance complies with either the Delegated Third Party's practice statement or this CP/CPS. If the opinion is that the Delegated Third Party does not comply, the CA does not allow the Delegated Third Party to continue performing delegated functions.

In accordance with Section 8.8 of the S/MIME Baseline Requirements, OWGTM documents the obligations of each Enterprise RA and Delegated Third Party in a contract, and monitors and audits internally their adherence to those obligations and to this CP/CPS at least annually.

# 9. OTHER BUSINESS AND LEGAL MATTERS

<!-- common:begin 9.0-9.5 -->
This section includes the stipulations for business and legal matters and has contractual value for all the PKI participants.

## 9.1 Fees

The fees applicable to the certification services covered by this CP/CPS may vary according to specific agreements with the participants in the service. The detailed information on fees is made available to the subscribers and other affected parties before they use the services.

### 9.1.1 Certificate issuance or renewal fees

The issuance of certificates in the OWGTM is a commercial service subject to fees. The fees depend on the certificate type and project, and are agreed before the service is made available to subscribers.

### 9.1.2 Certificate access fees

No stipulation. OWGTM does not charge fees for access to the certificate information published in its repositories.

### 9.1.3 Revocation or status information access fees

No stipulation. OWGTM does not charge fees for access to revocation or status information.

### 9.1.4 Fees for other services

The operators of Issuing CAs in the OWGTM can set fees for the commercial services provided to parties participating in the Trust Model, including:

- Managed PKI Services;
- CA Signing Services;
- CA Hosting and operation services.

### 9.1.5 Refund policy

The refund policy applicable to the commercial services provided by WISeKey is included in the Subscriber Agreement and/or in the general Terms and Conditions communicated to the end user when providing the service. Other refund policies may be established, and in such cases are communicated to all affected parties.

## 9.2 Financial responsibility

The OWGTM has established controls to ensure that the different levels of financial responsibility are met by the different participants, according to their impact on the Trust Model.

### 9.2.1 Insurance coverage

For the Root CAs, the Issuing CAs and the certification services provided directly by WISeKey, an Errors and Omissions insurance policy is maintained that covers the liability expressed in [section 9.8](#98-limitations-of-liability).

For affiliates and corporate customers acting as Certification or Registration Authorities, the contractual terms agreed among the parties allocate the responsibilities of each party and transfer the requirement for appropriate insurance for the transferred liabilities.

### 9.2.2 Other assets

No stipulation. No other assets are allocated to financial responsibility.

### 9.2.3 Insurance or warranty coverage for end-entities

The maximum liability per subscriber certificate issued under the OWGTM is established in the applicable Subscriber Agreement published by the Issuing CA.

## 9.3 Confidentiality of business information

In general, an Issuing CA under the OWGTM does not disclose the confidential information of a subscriber, or use that information for any purpose, except:

- To its staff requiring the information for the purposes of this CP/CPS or for the delivery of the services;
- With the explicit consent of the subscriber;
- If required to do so by law or by an applicable agreement.

### 9.3.1 Scope of confidential information

All Issuing CAs under the OWGTM keep the following types of information confidential, and maintain reasonable controls to prevent the exposure of such records to non-trusted personnel:

- All private keys;
- Any activation data used to access private keys or to gain access to the CA system;
- Any business continuity, incident response, contingency, and disaster recovery plans;
- Any other security practices, measures, mechanisms, plans, or procedures used to protect the confidentiality, integrity or availability of information;
- Any information held by the Issuing CA as private information in accordance with [section 9.4](#94-privacy-of-personal-information);
- Any transactional, audit log and archive record identified in [section 5.4](#54-audit-logging-procedures) or [section 5.5](#55-records-archival), including certificate application records and the documentation submitted in support of certificate applications, whether successful or rejected;
- Transaction records, financial audit records and external or internal audit trail records and any audit reports (with the exception of the public audit statements described in [section 8.6](#86-communication-of-results));
- All information classified explicitly as "PRIVATE", "CONFIDENTIAL" or "STRICTLY CONFIDENTIAL" when generated or exchanged among the involved parties.

### 9.3.2 Information not within the scope of confidential information

The following information is deemed non-confidential:

- All information contained in the issued certificates and Certificate Revocation Lists (CRLs), including all information that can be derived from them;
- All information classified expressly as "PUBLIC".

### 9.3.3 Responsibility to protect confidential information

The OWGTM Issuing CAs are responsible for the protection of the confidential information generated or communicated during all operations. Delegated parties, such as the entities managing Registration Authorities, are responsible for protecting the confidential information that they generate or store.

Subscribers are responsible for protecting their own private keys and all the activation information (i.e. passwords or PINs) needed to access or use them.

## 9.4 Privacy of personal information

The Issuing CAs operating in the OWGTM publish their Privacy Policy and communicate it to the subscribers. This policy complies with the applicable requirements for international commercial services, and in particular with the applicable CA/Browser Forum requirements and the European General Data Protection Regulation (GDPR).

In general, the CAs act as "Data Controllers", and the RAs and other parties involved in certificate management act as "Data Processors" or, in certain cases, "Joint Controllers".

### 9.4.1 Privacy plan

WISeKey publishes its Privacy Policy and related materials at https://www.wisekey.com/repository.

### 9.4.2 Information treated as private

Personal information about an individual that is not publicly available in the contents of a certificate or CRL is considered private.

### 9.4.3 Information not deemed private

The provisions of [section 9.3.2](#932-information-not-within-the-scope-of-confidential-information) apply to personal information.

### 9.4.4 Responsibility to protect private information

The OWGTM ensures compliance with the legal obligations of the Certification Authorities, Registration Authorities and other entities operating under the OWGTM. Each of these participants is responsible for protecting the private information provided by subscribers or other participants in the issuance and maintenance of certificates.

### 9.4.5 Notice and consent to use private information

The Issuing CAs and the other parties interacting with subscribers obtain the subscriber's consent to the use of its personal information for the provision of the certification service.

This consent is given by the explicit acceptance of the Subscriber Agreement or Terms and Conditions during the certificate request process.

### 9.4.6 Disclosure pursuant to judicial or administrative process

The participants in the OWGTM disclose personal information if required by a judicial or administrative process, upon presentation of the appropriate orders in accordance with the laws of the country where the Certification Authority operates.

### 9.4.7 Other information disclosure circumstances

No stipulation. No other disclosure circumstances are defined.

## 9.5 Intellectual property rights

All intellectual property rights, including those on the certificates and CRLs issued by the OWGTM Root CAs, the Object Identifiers and the OWGTM CP/CPS documents, are owned by the OISTE Foundation.

The private and public keys are the property of their respective owners.

Any commercial or protected trademark included in the Distinguished Name of a certificate is the responsibility of the subscriber.

## 9.6 Representations and warranties

This section includes general stipulations. The Subscriber, Relying Party and other agreements distributed among the parties may include specific terms.
<!-- common:end 9.0-9.5 -->

### 9.6.1 CA representations and warranties

By issuing a certificate, the CA makes the certificate warranties listed herein to the following Certificate Beneficiaries:

1. The Subscriber that is a party to the Subscriber Agreement or Terms of Use for the certificate;
2. All Application Software Suppliers with whom the Root CA has entered into a contract for inclusion of its Root CA Certificate in software distributed by such Application Software Supplier; and
3. All Relying Parties who reasonably rely on a Valid Certificate.

The CA represents and warrants to the Certificate Beneficiaries that, during the period when the certificate is valid, the CA has complied with the S/MIME Baseline Requirements and this CP/CPS in issuing and managing the certificate. These warranties specifically include:

1. **Right to Use Mailbox Address**: that, at the time of issuance, the CA implemented a procedure for verifying that the Applicant either had the right to use, or had control of, the Mailbox Addresses listed in the certificate's `subject` field and `subjectAltName` extension (or was delegated such right or control by someone who had such right to use or control), followed the procedure when issuing the certificate, and accurately described the procedure in this CP/CPS;
2. **Authorization for Certificate**: that, at the time of issuance, the CA implemented a procedure for verifying that the Subject authorized the issuance of the certificate and that the Applicant Representative is authorized to request the certificate on behalf of the Subject, followed the procedure, and accurately described it in this CP/CPS;
3. **Accuracy of Information**: that, at the time of issuance, the CA implemented a procedure for verifying the accuracy of all of the information contained in the certificate (with the exception of the `subject:serialNumber` attribute), followed the procedure, and accurately described it in this CP/CPS;
4. **Identity of Applicant**: that, if the certificate contains Subject Identity Information, the CA implemented a procedure to verify the identity of the Applicant in accordance with [section 3.2](#32-initial-identity-validation), followed the procedure, and accurately described it in this CP/CPS;
5. **Subscriber Agreement**: that, if the CA and the Subscriber are not Affiliated, the Subscriber and the CA are parties to a legally valid and enforceable Subscriber Agreement that satisfies the S/MIME Baseline Requirements, or, if the CA and the Subscriber are the same entity or are Affiliated, the Applicant Representative acknowledged the Terms of Use;
6. **Status**: that the CA maintains a 24x7 publicly-accessible repository with current information regarding the status (valid or revoked) of all unexpired certificates; and
7. **Revocation**: that the CA will revoke the certificate for any of the reasons specified in [section 4.9.1](#491-circumstances-for-revocation).

The Root CA is responsible for the performance and warranties of its Subordinate CAs, for their compliance with the S/MIME Baseline Requirements, and for all liabilities and indemnification obligations of the Subordinate CAs under those requirements, as if the Root CA were the Subordinate CA issuing the certificates.

In addition, the OWGTM Root CAs:

- Establish a chain of trust through their self-signed certificates;
- Sign the Subordinate CA certificates issued under the OWGTM hierarchies;
- Ensure that all relevant information concerning a certificate is recorded (electronically or otherwise) for the periods of [section 5.5](#55-records-archival), in particular to provide evidence for the purposes of legal proceedings; and
- Use trustworthy systems, procedures and human resources in performing their services.

All CAs in the OWGTM manage their keys in accordance with [section 6.2](#62-private-key-protection-and-cryptographic-module-engineering-controls), ensure the availability of a certificate repository and CRL, and revoke certificates when required.

### 9.6.2 RA representations and warranties

<!-- common:begin 9.6.2 -->
The Registration Authorities operating under the OWGTM warrant that:

- They operate according to the requirements of this CP/CPS;
- The certificates they approve meet all material requirements of this CP/CPS;
- No errors have been introduced in the certificate information by the entities approving the certificate application as a result of a failure when managing the application;
- There are no material misrepresentations of fact in the certificate attributable to the entities approving the application or issuing the certificate;
- Revocation services (when applicable) are available and a repository conforming with this CP/CPS in all material aspects is used.

Registration Authority commercial contracts and agreements may include additional warranties.
<!-- common:end 9.6.2 -->

### 9.6.3 Subscriber representations and warranties

Prior to the issuance of a certificate, the CA obtains, for the express benefit of the CA and the Certificate Beneficiaries, either the Applicant's agreement to the Subscriber Agreement with the CA, or the Applicant's acknowledgement of the Terms of Use.

OWGTM implements a process to ensure that each Subscriber Agreement or Terms of Use is legally enforceable against the Applicant. In either case, the agreement applies to the certificate to be issued pursuant to the certificate request. The CA may use an electronic or "click-through" agreement, provided that the CA has determined that such agreements are legally enforceable. A separate agreement may be used for each certificate request, or a single agreement may be used to cover multiple future certificate requests and the resulting certificates, so long as each certificate that the CA issues to the Applicant is clearly covered by that Subscriber Agreement or Terms of Use.

The Subscriber Agreement or Terms of Use contains provisions imposing on the Applicant itself (or made by the Applicant on behalf of its principal or agent under a subcontractor or hosting service relationship) the following obligations and warranties:

1. **Accuracy of Information**: to provide accurate and complete information at all times to the CA, both in the certificate request and as otherwise requested by the CA in connection with the issuance of the certificates;
2. **Protection of Private Key**: to take all reasonable measures to assure control of, keep confidential, and properly protect at all times the Private Key that corresponds to the Public Key included in the requested certificates (and any associated activation data or device, such as a password or token);
3. **Acceptance of Certificate**: to review and verify the certificate contents for accuracy;
4. **Use of Certificate**: to use the certificate only on the Mailbox Addresses listed in the certificate, and to use the certificate solely in compliance with all applicable laws and solely in accordance with the Subscriber Agreement or Terms of Use;
5. **Reporting and Revocation**: (i) to promptly request revocation of the certificate, and cease using it and its associated Private Key, if there is any actual or suspected misuse or compromise of the Subscriber's Private Key associated with the Public Key included in the certificate, and (ii) to promptly request revocation of the certificate, and cease using it, if any information in the certificate is or becomes incorrect or inaccurate;
6. **Termination of Use of Certificate**: to promptly cease all use of the Private Key corresponding to the Public Key included in the certificate upon revocation of that certificate for reasons of Key Compromise;
7. **Responsiveness**: to respond to the CA's instructions concerning Key Compromise or certificate misuse within the time period specified in the Subscriber Agreement;
8. **Acknowledgment and Acceptance**: to acknowledge and accept that the CA is entitled to revoke the certificate immediately if the Applicant violates the terms of the Subscriber Agreement or Terms of Use, or if revocation is required by this CP/CPS or by the S/MIME Baseline Requirements.

For client authentication and document signing certificates without a Mailbox Address, obligation 4 applies to the uses of the certificate stated in [section 1.4.1](#141-appropriate-certificate-uses). Each digital signature created with the Private Key is the digital signature of the Subscriber, and the Subscriber does not use the Private Key to sign certificates or CRLs.

The Subscriber Agreement may include additional warranties.

<!-- common:begin 9.6.4-9.7 -->
### 9.6.4 Relying party representations and warranties

Before relying on a certificate or a digital signature, relying parties:

- Validate the certificate and the digital signature, including the check of whether the certificate has been revoked or has expired;
- Ascertain and comply with the purposes for which the certificate was issued and any other limitations on reliance or use of the certificate that are specified in this CP/CPS.

If a relying party relies on a digital signature or certificate that it has not validated, it assumes all risks with regard to it (except those that would have arisen had the relying party validated the certificate), and is not entitled to any presumption that the digital signature is effective as the signature of the subscriber or that the certificate is valid.

Relying parties also comply with any other relevant obligations specified in this CP/CPS, including those imposed on the entity when it is acting as a subscriber.

Relying parties consider the certificate type. The final decision concerning whether or not to rely on a verified digital signature is exclusively that of the relying party.

The Relying Party Agreement may include additional warranties.

### 9.6.5 Representations and warranties of other participants

No stipulation. This document does not define other participants.

## 9.7 Disclaimers of warranties

Other disclaimers of warranties, if any, are included in the agreements presented to each PKI participant, or in other documents published by the Issuing CA.
<!-- common:end 9.6.4-9.7 -->

<!-- common:begin 9.8-9.16.2 -->
## 9.8 Limitations of liability

Liability limitations are regulated in the contractual agreements between the concerned parties. If applicable, they are specified in the Subscriber, Relying Party or other commercial agreements made among the participants.

Subject to the foregoing limitations, OWGTM's aggregate liability towards all end users, relying parties and any other entities that are not subordinate PKI entities, for the whole of the validity period of the certificates issued by the Root CA (unless revoked prior to their expiry), is CHF 5,000,000.00 (Five Million Swiss Francs), with a maximum aggregate liability per year of CHF 500,000.00 (Five Hundred Thousand Swiss Francs). The OISTE Foundation delegates this liability to WISeKey, as lead operator, according to a formal agreement executed between the parties, and WISeKey covers it through an appropriate "Errors and Omissions" insurance.

These limitations also apply to certificates that were not issued or managed in compliance with this CP/CPS or with the applicable CA/Browser Forum requirements, to the extent permitted by the applicable law. **TO BE CONFIRMED** (legal review)

## 9.9 Indemnities

Indemnities are regulated in the contractual agreements between the concerned parties. If applicable, they are specified in the Subscriber, Relying Party or other commercial agreements made among the participants.

In accordance with Section 9.9 of the applicable CA/Browser Forum Baseline Requirements, and notwithstanding any limitations on its liability to Subscribers and Relying Parties, OWGTM understands and acknowledges that the Application Software Suppliers that have agreed to distribute the OISTE Root CA Certificates do not assume any obligation or potential liability of the CA under those requirements, or that otherwise might exist because of the issuance or maintenance of certificates or reliance thereon by Relying Parties or others.

As OWGTM is not operated by a government entity, OWGTM defends, indemnifies, and holds harmless each Application Software Supplier for any and all claims, damages, and losses suffered by such Application Software Supplier related to a certificate issued by a CA operating under this CP/CPS, regardless of the cause of action or legal theory involved. This does not apply, however, to any claim, damage, or loss suffered by such Application Software Supplier related to a certificate issued by the CA where such claim, damage, or loss was directly caused by such Application Software Supplier's software displaying as not trustworthy a certificate that is still valid, or displaying as trustworthy: (1) a certificate that has expired, or (2) a certificate that has been revoked (but only in cases where the revocation status is currently available from the CA online, and the software either failed to check such status or ignored an indication of revoked status).

## 9.10 Term and termination

This section refers to the validity periods related to this document.

### 9.10.1 Term

This document becomes effective on the effective date stated in [section 1.2](#12-document-name-and-identification), once published in the OWGTM repository.

### 9.10.2 Termination

This document (in its current version) is valid until replaced by a new version.

### 9.10.3 Effect of termination and survival

The certificates issued during the validity period of a version of this document are bound to the clauses of that version until their expiration.

The termination of the CP/CPS is without prejudice to the responsibility to protect confidential and personal information.

## 9.11 Individual notices and communications with participants

Notices to subscribers are sent to the postal or e-mail address of the subscriber included in its registration information, or to another address that the subscriber has specified to the sender. Reasonable measures are taken to ensure the reception of the notices.

## 9.12 Amendments

The OWGTM can unilaterally amend this document, by adhering to the following procedure:

- The modification is justified under legal and technical considerations.
- A modification of this document does not contradict the other OWGTM CP/CPS documents in their common provisions (see [section 1.5.4](#154-cps-approval-procedures)).
- There is a modification procedure and change management for these amendments.
- The implications of the amendments for the participants are notified as described in [section 9.12.2](#9122-notification-mechanism-and-period).

### 9.12.1 Procedure for amendment

The entity with the authority to make and approve any change in this CP/CPS is the Policy Approval Authority (PAA, described in [section 1.5](#15-policy-administration)), which reviews the change request, assesses whether the change is required, and approves the changes.

A change can only be made to the approved documents once approval has been granted by the PAA.

When the PAA decides to modify this CP/CPS, a new version of the document is generated. The version of the document is controlled with two numbers separated by a period. The first number (major version) is incremented if the new version could affect the acceptance of the certificates by the users. The second number (minor version) is incremented if the amendment does not affect the certificate acceptance criteria. The OID of the document does not change between versions (see [section 1.2](#12-document-name-and-identification)).

Once a new version of the document is approved, the procedures of [section 9.12.2](#9122-notification-mechanism-and-period) are executed.

### 9.12.2 Notification mechanism and period

Any modification of this document is published in the OWGTM repository (https://oiste.org/repository) before its effective date, and the affected participants are directly notified when necessary.

Participants are not directly notified of minor version changes.

In the case of a major version change, the OWGTM may notify the affected participants with a digitally signed electronic message.

### 9.12.3 Circumstances under which OID must be changed

The OID of this CP/CPS is not modified by new versions of the document. A new OID is assigned only to a new document with a different scope.

## 9.13 Dispute resolution provisions

As agreed between the parties by the acceptance of the Subscriber and/or Relying Party agreements. If no prior agreement on the dispute resolution mechanism was made, the general rules of law apply.

## 9.14 Governing law

This CP/CPS and the operations of the OWGTM are governed by the laws of Geneva, Switzerland.

## 9.15 Compliance with applicable law

All related parties comply with all applicable Swiss laws, rules, regulations, ordinances, and directives, and all provisions required thereby to be included in this CP/CPS are hereby incorporated herein by reference.

Applicable national laws can affect parties operating Certification Authorities in different jurisdictions.

## 9.16 Miscellaneous provisions

This section includes miscellaneous contractual and legal clauses.

### 9.16.1 Entire agreement

All provisions of this CP/CPS apply to all Certification and Registration Authorities operating under it and to their subscribers.

Agreements or supplementary agreements by word of mouth are not allowed.

### 9.16.2 Assignment

Parties to this CP/CPS may not assign any of their rights or obligations under this CP/CPS or applicable agreements without the written consent of WISeKey.
<!-- common:end 9.8-9.16.2 -->

### 9.16.3 Severability

Should individual provisions of this CP/CPS prove to be ineffective or incomplete, this is without prejudice to the effectiveness of all other provisions. The ineffective provision is replaced by an effective provision deemed as most closely reflecting the sense and purpose of the ineffective provision. In the case of incomplete provisions, the amendment is agreed as deemed to correspond to what would have reasonably been agreed upon in line with the sense and purposes of this CP/CPS, had the matter been considered beforehand.

If a law in any jurisdiction where OWGTM operates or issues certificates conflicts with the S/MIME Baseline Requirements, OWGTM may modify its internal processes only to the minimum extent necessary to comply with that law. Prior to issuing any certificate under such a modified process, OWGTM publishes in this section 9.16.3:

- a detailed reference to the law (statute, regulation or order, jurisdiction and date);
- a description of the specific requirement(s) affected; and
- the precise modification(s) implemented by the CA.

Prior to issuing any certificate under the modified requirement, OWGTM also notifies the CA/Browser Forum of the relevant information newly added to this CP/CPS by sending a message to public@cabforum.org and receiving confirmation that it has been posted to the Public Mailing List and is indexed in the Public Mail Archives available at <https://cabforum.org/pipermail/public/> (or such other e-mail addresses and links as the Forum may designate), so that the CA/Browser Forum may consider possible revisions to the requirements accordingly.

Any modification to OWGTM practice enabled under this section is discontinued if and when the law no longer applies, or the requirements are modified to make it possible to comply with both them and the law simultaneously. An appropriate change in practice, modification to this CP/CPS and notice to the CA/Browser Forum, as outlined above, are made within 90 days.

OWGTM retains the documentation supporting the legal determination and notifies the applicable Root Programs and auditors as required by those programs.

At the effective date of this document, no such modification applies.

<!-- common:begin 9.16.4-9.17 -->
### 9.16.4 Enforcement (attorneys' fees and waiver of rights)

No stipulation. No specific provisions on attorneys' fees or waiver of rights are made.

### 9.16.5 Force Majeure

Force majeure clauses, if any, are included in the Subscriber Agreement.

## 9.17 Other provisions

No stipulation. No other provisions are made.
<!-- common:end 9.16.4-9.17 -->

# Appendix A: Glossary

## Acronyms

| Acronym | Description |
| --- | --- |
| AATL | Adobe Approved Trust List |
| CA | Certificate Authority or Certification Authority |
| CAA | Certification Authority Authorization |
| CA/B Forum | CA/Browser Forum |
| CCADB | Common CA Database |
| CP | Certificate Policy |
| CPS | Certification Practice Statement |
| CRL | Certificate Revocation List |
| CSPRNG | Cryptographically Secure Pseudo-Random Number Generator |
| CSR | Certificate Signing Request |
| DBA | Doing Business As (also known as "Trading As") |
| DNS | Domain Name System |
| DNSSEC | Domain Name System Security Extensions |
| EKU | Extended Key Usage |
| eID | Electronic Identification |
| FIPS | (US Government) Federal Information Processing Standard |
| FQDN | Fully-Qualified Domain Name |
| HSM | Hardware Security Module |
| HTTP | Hypertext Transfer Protocol |
| IANA | Internet Assigned Numbers Authority |
| IETF | Internet Engineering Task Force |
| ITU | International Telecommunication Union |
| LEI | Legal Entity Identifier |
| mDL | Mobile Driving Licence |
| MPIC | Multi-Perspective Issuance Corroboration |
| NCSSR | CA/Browser Forum Network and Certificate System Security Requirements |
| NIST | National Institute of Standards and Technology |
| OCSP | Online Certificate Status Protocol |
| OID | Object Identifier |
| PAA | Policy Approval Authority |
| PKI | Public Key Infrastructure |
| RA | Registration Authority |
| RFC | Request for Comments (at IETF.org) |
| S/MIME | Secure MIME (Multipurpose Internet Mail Extensions) |
| SAN | Subject Alternative Name |
| SHA | Secure Hash Algorithm |
| TSA | Time-Stamping Authority |
| TTL | Time To Live |
| URA | Universal Registration Authority |
| UTC | Coordinated Universal Time |
| X.509 | The ITU-T standard for Certificates and their corresponding authentication framework |

## Definitions

Terms not defined in this appendix have the meaning given to them in the S/MIME Baseline Requirements and the NCSSR.

| Definition | Description |
| --- | --- |
| Applicant | An entity applying for a Certificate. |
| Applicant Representative | A natural person employed by, or an authorized agent of, the Applicant, who submits or approves a certificate request on behalf of the Applicant. |
| Application Software Supplier | A supplier of software that displays or uses certificates and incorporates Root Certificates. |
| Attestation Letter | A letter attesting that Subject Information is correct, written by an accountant, lawyer, government official, or other reliable third party customarily relied upon for such information. |
| Certification Authority Authorization (CAA) | A DNS resource record that allows a domain owner to specify which Certification Authorities are authorized to issue certificates for the domain; its use for Mailbox Addresses is specified in RFC 9495. |
| Certificate | An electronic document, conformant to X.509v3, digitally signed by a Certification Authority, that binds a Public Key to an identity. |
| Certificate Beneficiaries | The parties to which the CA makes the warranties of [section 9.6.1](#961-ca-representations-and-warranties). |
| Certificate Problem Report | A complaint of suspected Key Compromise, certificate misuse, or other types of fraud, compromise, misuse, or inappropriate conduct related to certificates. |
| Cross-Certificate | A certificate that is used to establish a trust relationship between two Root CAs. |
| Delegated Third Party | A natural person or legal entity that is not the CA and that operates any part of a Certificate System. |
| Enterprise RA | An employee or agent of an organization unaffiliated with the CA who authorizes the issuance of certificates to that organization or its Affiliates. |
| Issuing CA | Any CA issuing subscriber certificates under this CP/CPS. |
| Key Compromise | A Private Key is said to be compromised if its value has been disclosed to an unauthorized person, or an unauthorized person has had access to it. |
| Key Pair | A Private Key and its associated Public Key. |
| Legal Entity | An association, corporation, partnership, proprietorship, trust, government entity or other entity with legal standing in a country's legal system. |
| Linting | A process in which the content of digitally signed data such as a Certificate or a tbsCertificate (as described in RFC 5280, Section 4.1.1.1) is checked for conformance with the profiles and requirements defined in the applicable requirements. |
| Mailbox Address | An e-mail address as specified in Section 4.1.2 of RFC 5321 and amended by Section 3.2 of RFC 6532, with no additional padding or structure. |
| Mailbox Field | In Subscriber Certificates, an `rfc822Name` or `otherName` of type `id-on-SmtpUTF8Mailbox` in the `subjectAltName` extension, or the `subject:emailAddress` attribute. |
| Mailbox-validated, Organization-validated, Sponsor-validated, Individual-validated | The S/MIME Certificate types defined in the S/MIME Baseline Requirements. |
| OCSP Responder | An online software application operated under the authority of the OWGTM for processing certificate status requests. |
| Personal Certificate | A certificate issued under this CP/CPS to a natural or legal person, for e-mail protection, client authentication and/or document signing (see [section 1.4.1.2](#1412-certificate-types)). |
| Private Key | The key of a Key Pair that is kept secret by the holder of the Key Pair, and that is used to create digital signatures and/or to decrypt electronic records or files that were encrypted with the corresponding Public Key. |
| Pseudonym | A fictitious name used in the Subject of a certificate instead of the Personal Name of the Individual, as defined in the S/MIME Baseline Requirements. |
| Public Key | The key of a Key Pair that may be publicly disclosed by the holder of the corresponding Private Key and that is used by a Relying Party to verify digital signatures created with the holder's corresponding Private Key and/or to encrypt messages so that they can be decrypted only with the holder's corresponding Private Key. |
| Random Value | A value specified by the CA to the Applicant that exhibits at least 112 bits of entropy. |
| Relying Party | An entity that relies upon the information contained within a Certificate. |
| Relying Party Agreement | An agreement which is read and accepted by the Relying Party prior to validating, relying on or using a Certificate. |
| S/MIME Baseline Requirements | The CA/Browser Forum "Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates". |
| S/MIME Certificate | A certificate containing the `id-kp-emailProtection` EKU and at least one Mailbox Address in the `subjectAltName` extension. |
| Subject Identity Information | Information that identifies the Certificate Subject. |
| Subscriber | The entity identified as the subject in the Certificate, which is bound by a Subscriber Agreement or Terms of Use. |
| Subscriber Agreement | An agreement that governs the issuance and use of a Certificate that the Applicant reads and accepts before receiving a Certificate. |
| TLS Baseline Requirements | The CA/Browser Forum "Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates", whose domain validation methods are used in this CP/CPS for the domain portion of Mailbox Addresses. |
| Validation Specialist | A person who performs the information verification duties of this CP/CPS (also named Validation Agent). |
| WebTrust | The current version of the WebTrust Program for Certification Authorities of CPA Canada. |

<!-- common:begin ncssr-definitions -->
## Network security definitions

The following terms are used as defined in the CA/Browser Forum Network and Certificate System Security Requirements (NCSSR):

| Term | Definition (summary of the NCSSR definition) |
| --- | --- |
| Air-Gapped | Physically and logically separated, disconnected, and isolated from all other Systems. |
| CA Infrastructure | Collectively, the Certificate Systems, Root CA Systems (Air-Gapped and otherwise) and Security Support Systems used by the CA or a Delegated Third Party. |
| Certificate System | A system used by a CA or Delegated Third Party to store, access, process, or manage data or provide services related to identity validation, identity authentication, account registration, certificate application, certificate approval, certificate issuance, certificate revocation, generation and signing of authoritative certificate status, or key escrow. |
| Critical Security Event | An event, set of circumstances, or anomalous activity that could lead to a circumvention of CA Infrastructure security controls, or a compromise of CA Infrastructure integrity or operational continuity. |
| Multi-Factor Authentication | An authentication mechanism consisting of two or more independent categories of credentials (something the user knows, has, or is). |
| Multi-Party Control | An access control mechanism which requires two or more separate, authorized users to successfully authenticate with their own unique credentials prior to access being granted. |
| Network Boundary Control | Components that manage and control network traffic flow to, from, and within CA Infrastructure. |
| Physically Secure Environment | A controlled and protected physical space protected by security controls addressing the topics of Section 4.5.1 of RFC 3647, and operated in accordance with the Risk Assessments of the CA. |
| Principle of Least Privilege | The principle that users, devices, and software should only have the minimum necessary access and privileges to complete their functions. |
| Principle of Separation of Duties | The principle that tasks are divided among multiple individuals such that no single person has complete control over sensitive operations. |
| Privileged Access | Access to CA Infrastructure or Network Boundary Controls that provides capabilities or permissions enabling administration, configuration, management, or operation of such systems. |
| Risk Assessment | A formal process that identifies foreseeable threats to the CA Infrastructure, assesses their likelihood and potential damage, and assesses the sufficiency of the controls in place to counter them. |
| Root CA System | A system used to generate a Key Pair whose Private Key is or will be a Root CA Private Key, to store a Root CA Private Key, or to create digital signatures using a Root CA Private Key. |
| Security Support System | The systems supporting the security of CA Infrastructure, performing functions such as authentication, audit logging, audit log reduction and analysis, vulnerability scanning, and physical, host-based and network-based intrusion detection. |
| Trusted Role | An individual employee or contractor of a CA or Delegated Third Party who has authorized access to any Certificate System or Root CA System. |
| Workstation | A device (e.g., a phone, tablet, desktop or laptop computer) connected to the same network as CA Infrastructure and/or a Network Boundary Control, and capable of Privileged Access. |
<!-- common:end ncssr-definitions -->

# Appendix B: CA Hierarchies

This appendix identifies every CA certificate within the scope of this document. The OISTE WISeKey Global Root GB CA is also within the scope of the OWGTM TLS CP/CPS, which governs its TLS branch.

## Root CA certificates

| Root CA (Subject) | Status under this document |
| --- | --- |
| CN=OISTE Client Root RSA G1, O=OISTE Foundation, C=CH | Active. Valid until 2048-05-24. |
| CN=OISTE Client Root ECC G1, O=OISTE Foundation, C=CH | Active. Valid until 2048-05-24. |
| CN=OISTE WISeKey Global Root GB CA, OU=OISTE Foundation Endorsed, O=WISeKey, C=CH | Legacy. The Subordinate CAs directly under this Root cease issuing S/MIME Certificates on 2026-12-31 **TO BE CONFIRMED**. This Root remains the issuer of the Cross-Certificates to the OISTE Client Roots. OISTE has requested that the email trust of this Root be maintained in the Mozilla root store until 2029-04-31 **TO BE CONFIRMED**. |
| CN=OISTE WISeKey Global Root GA CA, OU=OISTE Foundation Endorsed, OU=Copyright (c) 2005, O=WISeKey, C=CH | Legacy. Issuance status **TO BE CONFIRMED**. The Mozilla root store distrusts S/MIME certificates issued by hierarchies with key material created before 2006 after 2028-04-15. |

## Subordinate CA certificates and Cross-Certificates

| Subject | Issuer | EKU | Status |
| --- | --- | --- | --- |
| CN=WISeKey CertifyID Client RSA CA 1, O=WISeKey, C=CH | OISTE Client Root RSA G1 | emailProtection, clientAuth | Active |
| CN=WISeKey CertifyID Client ECC CA 1, O=WISeKey, C=CH | OISTE Client Root ECC G1 | emailProtection, clientAuth | Active |
| CN=OISTE Client Root RSA G1, O=OISTE Foundation, C=CH (Cross-Certificate) | OISTE WISeKey Global Root GB CA | emailProtection, clientAuth | Active |
| CN=OISTE Client Root ECC G1, O=OISTE Foundation, C=CH (Cross-Certificate) | OISTE WISeKey Global Root GB CA | emailProtection, clientAuth | Active |
| CN=WISeKey CertifyID Personal GB CA 3, O=WISeKey, C=CH | OISTE WISeKey Global Root GB CA | emailProtection, clientAuth, Microsoft Smart Card Logon, Microsoft Document Signing | Active; S/MIME issuance ceases on 2026-12-31 **TO BE CONFIRMED**. RSA 2048 key: no S/MIME issuance after 2027-09-15 in any case. |
| CN=WISeKey CertifyID Personal GB CA 4, O=WISeKey, C=CH | OISTE WISeKey Global Root GB CA | emailProtection, clientAuth | Active; S/MIME issuance ceases on 2026-12-31 **TO BE CONFIRMED**. RSA 2048 key: no S/MIME issuance after 2027-09-15 in any case. |
| CN=WISeKey CertifyID Advanced Services CA 4, OU=International, OU=Copyright (c) 2016 WISeKey SA, O=WISeKey, C=CH | OISTE WISeKey Global Root GA CA | No EKU extension | **TO BE CONFIRMED**. RSA 2048 key: no S/MIME issuance after 2027-09-15 in any case. |

## SHA-256 fingerprints

| CA certificate | SHA-256 fingerprint |
| ---------------------- | ------------------------------------------------------------------------------ |
| OISTE Client Root RSA G1 | `D02A0F994A868C66395F2E7A880DF509BD0C29C96DE16015A0FD501EDA4F96A9` |
| OISTE Client Root ECC G1 | `D9A32485A8CCA85539CEF12FFFFF711378A17851D73DA2732AB4302D763BD62B` |
| OISTE WISeKey Global Root GB CA | `6B9C08E86EB0F767CFAD65CD98B62149E5494A67F5845E7BD1ED019F27B86BD6` |
| OISTE WISeKey Global Root GA CA | `41C923866AB4CAD6B7AD578081582E020797A6CBDF4FFF78CE8396B38937D7F5` |
| WISeKey CertifyID Client RSA CA 1 | `41F8755AEE782FF08D8EBB579ABC33C93E9E5613FC146F86A86E012860B54ADA` |
| WISeKey CertifyID Client ECC CA 1 | `1F5233119B894DB95B4A3737397366457B566308CF8E30C4D2935EA7049013D0` |
| OISTE Client Root RSA G1 (Cross-Certificate) | `DF426697B907906C2C777BF74EE63A408F8D9ECF57C01D687755A3C931464AF5` |
| OISTE Client Root ECC G1 (Cross-Certificate) | `1D857BFC6F90496DA7E50AB350A5AE31CB96F9A2C8E0DA5B283DEBB7223CF3EA` |
| WISeKey CertifyID Personal GB CA 3 | `E5937790AA6915755C9A532B10C9610A07C9877C7C60E1B819A294207A3786F5` |
| WISeKey CertifyID Personal GB CA 4 | `8D45BF32C041A7EE46325F06AE604FAF7142DD99373DDB1EB74C70488A56FFB8` |
| WISeKey CertifyID Advanced Services CA 4 | `41144BD4174C3152E1CA526F77D9F9CE89DEBC4EBA6C778F815C21164B5101D3` |

All the CAs of this appendix are audited as described in [section 8.4](#84-topics-covered-by-assessment).

# Appendix C: OID Inventory

OWGTM defines the following OID schema to identify its policy documents and the certificate policies of the certificates within the scope of this document.

PUBLIC-ARCH = 2.16.756.5.14

PUBLIC-ARCH.4 – OISTE Certificate Policy Identifiers (legacy, used in certificates issued under previous policy documents)

- 4.3.2.1.1 – CertifyID Advanced Individual Secure Mail
- 4.3.2.1.2 – CertifyID Advanced Individual Digital Signature
- 4.3.2.1.3 – CertifyID Advanced Corporate Digital Signature
- 4.4.2.1.1 – CertifyID Qualified Individual
- 4.4.2.1.2 – CertifyID Qualified Corporate
- 4.4.2.1.3 – CertifyID Qualified Individual for Adobe
- 4.4.2.1.4 – CertifyID Qualified Corporate for Adobe

PUBLIC-ARCH.7 – OISTE Certificate Policy Identifiers

- 7.1 – Root CP
- 7.2 – Policy CA CP
- 7.3 – Issuing CA CP
- 7.4 – End Entity CP
  - 7.4.0 – CertifyID URA Admin Certificate
  - 7.4.1 – CertifyID Personal Standard Certificate
  - 7.4.2 – CertifyID Personal Advanced Certificate
  - 7.4.3 – CertifyID Corporate Advanced Certificate
  - 7.4.4 – CertifyID Personal Qualified Certificate
  - 7.4.5 – CertifyID Corporate Qualified Certificate
  - 7.4.9 – CertifyID Code Signing Certificate (withdrawn: OWGTM does not issue Code Signing Certificates)
  - 7.4.10 – CertifyID EV Code Signing Certificate (withdrawn: OWGTM does not issue Code Signing Certificates)
- 7.6 – Time Stamp Policy CP
- 7.7 – OCSP Service

PUBLIC-ARCH.8 – Policy qualifiers for special purposes

- 8.1 – Vendor specific OID
  - 8.1.1 – Qualifier for Adobe PDF (AATL)
- 8.2 – Device certificates (not issued under this CP/CPS; used in the ecosystem CP/CPS documents)

PUBLIC-ARCH.9 – OWGTM policy documents

- 9.1 – OWGTM TLS CP/CPS
- 9.2 – OWGTM S/MIME and Client Certificates CP/CPS (this document)
- 9.3 – reserved
- 9.4 – reserved

The identifier 2.16.756.5.14.7.1 identified the combined OWGTM CP/CPS up to version 4.2. It keeps its meaning as the Root CP identifier.

**CA/Browser Forum reserved policy identifiers used in the certificates within the scope of this document:**

| OID | Certificate type |
| --- | --- |
| 2.23.140.1.5.1.2 | Mailbox-validated, Multipurpose generation |
| 2.23.140.1.5.2.2 | Organization-validated, Multipurpose generation |
| 2.23.140.1.5.3.2 | Sponsor-validated, Multipurpose generation |
| 2.23.140.1.5.4.2 | Individual-validated, Multipurpose generation |

The Legacy generation policy identifiers (2.23.140.1.5.x.1) are not used since 2025-07-15.

# Appendix D: Certificate Profiles

This appendix describes the certificate profiles issued by the CAs within the scope of this document, including all mandatory and optional extensions, based on the S/MIME Baseline Requirements. The profiles effectively used are always aligned with the version of these requirements in force at the moment of issuance.

In all cases, the serial numbers of new certificates contain at least 64 bits of output from a CSPRNG.

## Infrastructure Certificates

### Cross-Certified Subordinate CA

| Attribute | Content | Example Value | Notes |
| --- | --- | --- | --- |
| **Version** | v3 | v3 | **Mandatory** |
| **Serial Number** | Unique value assigned by the issuing Root CA | 33:00:00:... | **Mandatory** |
| **Signature Algorithm** | sha256/384/512WithRSAEncryption, ecdsa-with-SHA256/384 | sha256WithRSAEncryption | **Mandatory** |
| **Issuer** | Name of the Root CA performing the cross-certification | C=CH, O=WISeKey, OU=OISTE Foundation Endorsed, CN=OISTE WISeKey Global Root GB CA | **Mandatory** |
| **Validity Period** | Determined by the issuing Root CA | 2026-02-25 → 2039-12-01 | **Mandatory**; does not exceed the validity of the issuing Root CA |
| **Subject** | Byte-for-byte identical to the Subject of the cross-certified Root CA | C=CH, O=OISTE Foundation, CN=OISTE Client Root RSA G1 | **Mandatory** |
| **Public Key Algorithm / Size** | Public key of the cross-certified Root CA | RSA 4096 | **Mandatory** |
| **Basic Constraints (critical)** | CA:TRUE | CA:TRUE | **Mandatory** |
| **Key Usage (critical)** | Certificate Sign, CRL Sign, Digital Signature (optional) | Certificate Sign, CRL Sign | **Mandatory** |
| **Extended Key Usage (EKU)** | E-mail Protection; TLS Web Client Authentication (optional). `anyExtendedKeyUsage` is never present. | E-mail Protection, TLS Web Client Authentication | **Mandatory** (S/MIME BR Section 7.1.2.2; CCADB Policy Section 6.3) |
| **Subject Key Identifier (SKI)** | keyid:… | keyid:5F:1B:C5:... | **Mandatory** |
| **Authority Key Identifier (AKI)** | keyid:… | keyid:35:0F:C8:... | **Mandatory** |
| **CRL Distribution Points (CRL DP)** | URI of the CRL of the issuing Root CA | http://public.wisekey.com/ca.crl | **Mandatory** |
| **Authority Info Access (AIA)** | CA Issuers URI; OCSP URI (optional) | CA Issuers: http://public.wisekey.com/ca.crt | **Mandatory** |
| **Certificate Policies** | `anyPolicy`, or the reserved CA/Browser Forum S/MIME identifiers of the certificate types issued in the subject hierarchy | anyPolicy | **Mandatory** |

### Issuing CA Certificates

| Attribute | Content | Example Value | Notes |
| --- | --- | --- | --- |
| **Version** | v3 | v3 | **Mandatory** |
| **Serial Number** | Unique value assigned by the Root CA | 33:00:00:... | **Mandatory** |
| **Signature Algorithm** | sha256/384/512WithRSAEncryption, ecdsa-with-SHA256/384 | sha384WithRSAEncryption | **Mandatory** |
| **Issuer** | Root CA Subject Name | C=CH, O=OISTE Foundation, CN=OISTE Client Root RSA G1 | **Mandatory** |
| **Validity Period** | See [section 6.3.2](#632-certificate-operational-periods-and-key-pair-usage-periods) | 2024-02-20 → 2039-02-16 | **Mandatory** |
| **Subject** | Issuing CA identity | C=CH, O=WISeKey, CN=WISeKey CertifyID Client RSA CA 1 | **Mandatory** |
| **Public Key Algorithm / Size** | RSA 4096 (RSA 2048 or 3072 only in CA certificates signed before 2026-09-15), EC P-256/P-384 | RSA 4096 | **Mandatory** |
| **Basic Constraints (critical)** | CA:TRUE, pathlen:0 | CA:TRUE, pathlen:0 | **Mandatory** |
| **Key Usage (critical)** | Certificate Sign, CRL Sign, Digital Signature (optional) | Certificate Sign, CRL Sign | **Mandatory** |
| **Extended Key Usage (EKU)** | E-mail Protection; TLS Web Client Authentication (optional). Other values only in CA certificates signed before 2026-08-01. | E-mail Protection, TLS Web Client Authentication | **Mandatory** |
| **Subject Key Identifier (SKI)** | keyid:… | keyid:5F:1B:C5:... | **Mandatory** |
| **Authority Key Identifier (AKI)** | keyid:… | keyid:35:0F:C8:... | **Mandatory** |
| **CRL Distribution Points (CRL DP)** | URI:… | http://public.wisekey.com/ca.crl | **Mandatory** |
| **Authority Info Access (AIA)** | CA Issuers URI, OCSP URI (optional) | CA Issuers: http://public.wisekey.com/ca.crt | **Mandatory** |
| **Certificate Policies** | `anyPolicy` (affiliated CA), or the reserved CA/Browser Forum S/MIME identifiers of the certificate types issued by the CA | anyPolicy | **Mandatory** |

### OCSP Responder Certificates

| Attribute | Content | Example Value | Notes |
| --- | --- | --- | --- |
| **Version** | v3 | v3 | **Mandatory** |
| **Serial Number** | Unique value assigned by the issuing CA | 35:16:6B:... | **Mandatory** |
| **Signature Algorithm** | sha256/384WithRSAEncryption, ecdsa-with-SHA256/384 | sha256WithRSAEncryption | **Mandatory** |
| **Issuer** | Issuing CA Subject Name | C=CH, O=WISeKey, CN=WISeKey CertifyID Client RSA CA 1 | **Mandatory** |
| **Validity Period** | Up to 1 year | 2026-05-29 → 2027-05-29 | **Mandatory** |
| **Subject** | OCSP responder identity | C=CH, O=WISeKey, CN=WISeKey CertifyID Client RSA CA 1 OCSP | **Mandatory** |
| **Public Key Algorithm / Size** | RSA 2048/3072/4096, EC P-256/P-384 | RSA 2048 | **Mandatory** |
| **Basic Constraints (critical)** | CA:FALSE | CA:FALSE | **Optional** |
| **Key Usage (critical)** | Digital Signature | Digital Signature | **Mandatory** |
| **Extended Key Usage (EKU)** | OCSP Signing (id-kp-OCSPSigning) only | OCSP Signing | **Mandatory** |
| **OCSP No Check** | Present (non-critical) | OCSP No Check | **Mandatory** |
| **Subject Key Identifier (SKI)** | keyid:… | keyid:5F:DE:F0:... | **Optional** |
| **Authority Key Identifier (AKI)** | keyid:… | keyid:5F:... | **Mandatory** |
| **Authority Info Access (AIA)** | — | *Not present* | **Optional** |
| **CRL Distribution Points** | — | *Not present* | **Optional** |
| **Certificate Policies** | — | *Not present* | **Optional** |

## S/MIME Certificate Profiles

When the certificate includes the usage for e-mail protection, the commercial names of the Personal Certificates correspond to the S/MIME Certificate types of the S/MIME Baseline Requirements as indicated in this table:

| Commercial names | S/MIME Baseline Requirements type |
| --- | --- |
| Standard Certificate<br>Basic Certificate | Mailbox-validated |
| Advanced Personal Certificate<br>Qualified Personal Certificate | Individual-validated |
| Advanced Professional Certificate<br>Qualified Professional Certificate | Sponsor-validated |
| Advanced Corporate Certificate<br>Qualified Corporate Certificate | Organization-validated |

The S/MIME Certificates issued by OWGTM follow the "Multipurpose" profiles of the S/MIME Baseline Requirements. Each S/MIME Certificate includes exactly one reserved CA/Browser Forum policy identifier, according to its profile: 2.23.140.1.5.1.2 (Mailbox-validated multipurpose), 2.23.140.1.5.4.2 (Individual-validated multipurpose), 2.23.140.1.5.3.2 (Sponsor-validated multipurpose) and 2.23.140.1.5.2.2 (Organization-validated multipurpose). Legacy generation policy identifiers (2.23.140.1.5.x.1) are not used since 2025-07-15.

### S/MIME Certificates Validity Period Schedule

| Certificate Type | Maximum Validity |
| --- | --- |
| Mailbox-validated | 825 days |
| Individual-validated | 825 days |
| Sponsor-validated | 825 days |
| Organization-validated | 825 days |

### Mailbox-Validated Certificate Profile

| Attribute | Content | Example Value | Notes |
| --- | --- | --- | --- |
| Version | v3 | v3 | **Mandatory** |
| Serial Number | Unique value | 14:b4:... | **Mandatory** |
| Signature Algorithm | sha256/384WithRSAEncryption, ecdsa-with-SHA256/384 | sha256WithRSAEncryption | **Mandatory** |
| Issuer | Issuing CA Subject Name | C=CH, O=WISeKey, CN=WISeKey CertifyID Client RSA CA 1 | **Mandatory** |
| Validity Period | See the schedule above | Not Before: Oct 30 2025 16:10:52 GMT <br> Not After: Oct 30 2027 16:10:51 GMT | **Mandatory**; at most 825 days |
| Subject | CN, emailAddress (or other combinations and fields allowed by the S/MIME Baseline Requirements) | CN=john.smith@example.com, emailAddress=john.smith@example.com | **Mandatory** |
| Public Key Algorithm / Size | RSA 2048/3072/4096, P-256/P-384 | RSA 2048 | **Mandatory** |
| Basic Constraints (critical) | CA:FALSE | CA:FALSE | **Optional** |
| Key Usage (critical) | RSA: a valid combination of Digital Signature, nonRepudiation, Key Encipherment and/or Data Encipherment (Data Encipherment only together with Key Encipherment).<br>ECDSA: a valid combination of Digital Signature, nonRepudiation and/or Key Agreement (encipherOnly/decipherOnly only together with Key Agreement).<br>No other bits are set. | Digital Signature | **Mandatory** |
| Extended Key Usage | E-mail Protection (mandatory); TLS Web Client Authentication and other values allowed by the S/MIME Baseline Requirements (optional); id-kp-serverAuth, id-kp-codeSigning, id-kp-timeStamping and anyExtendedKeyUsage are never present.<br>Effective 2027-07-01: only E-mail Protection and, optionally, TLS Web Client Authentication | E-mail Protection | **Mandatory** |
| Subject Alternative Name (SAN) | rfc822Name (at least one; mandatory from 2027-02-01) | email:john.smith@example.com | **Mandatory** |
| Certificate Policies | 2.23.140.1.5.1.2 (exactly one reserved CA/Browser Forum policy identifier); CPS URI and other OIDs as allowed by the S/MIME Baseline Requirements (optional) | 2.23.140.1.5.1.2 | **Mandatory** |
| Authority Key Identifier (AKI) | keyid:... | keyid:DB:68:... | **Mandatory** |
| Subject Key Identifier (SKI) | keyid:... | keyid:0C:D1... | **Optional** |
| Authority Info Access (AIA) | CA Issuers URI, OCSP URI (optional) | CA Issuers: http://public.wisekey.com/ca.crt | **Mandatory** |
| CRL Distribution Points (CRL DP) | URI:... | http://public.wisekey.com/ca.crl | **Mandatory** |

### Individual-Validated Certificate Profile

| Attribute | Content | Example Value | Notes |
| --- | --- | --- | --- |
| Version | v3 | v3 | **Mandatory** |
| Serial Number | Unique value | 14:b4:... | **Mandatory** |
| Signature Algorithm | sha256/384WithRSAEncryption, ecdsa-with-SHA256/384 | sha256WithRSAEncryption | **Mandatory** |
| Issuer | Issuing CA Subject Name | C=CH, O=WISeKey, CN=WISeKey CertifyID Client RSA CA 1 | **Mandatory** |
| Validity Period | See the schedule above | Not Before: Oct 30 2025 16:10:52 GMT <br> Not After: Oct 30 2027 16:10:51 GMT | **Mandatory**; at most 825 days |
| Subject | C, ST, L, SN, GN, CN, emailAddress (or other combinations and fields allowed by the S/MIME Baseline Requirements) | C=CH, L=Geneve, SN=Smith, GN=John, CN=john.smith@example.com, emailAddress=john.smith@example.com | **Mandatory**; Pseudonyms are not used in Individual-validated certificates (see [section 3.1.3](#313-anonymity-or-pseudonymity-of-subscribers)) |
| Public Key Algorithm / Size | RSA 2048/3072/4096, P-256/P-384 | RSA 2048 | **Mandatory** |
| Basic Constraints (critical) | CA:FALSE | CA:FALSE | **Optional** |
| Key Usage (critical) | As for the Mailbox-validated profile | Digital Signature | **Mandatory** |
| Extended Key Usage | As for the Mailbox-validated profile | E-mail Protection | **Mandatory** |
| Subject Alternative Name (SAN) | rfc822Name (at least one; mandatory from 2027-02-01) | email:john.smith@example.com | **Mandatory** |
| Certificate Policies | 2.23.140.1.5.4.2 (exactly one reserved CA/Browser Forum policy identifier); CPS URI and other OIDs as allowed by the S/MIME Baseline Requirements (optional) | 2.23.140.1.5.4.2 | **Mandatory** |
| Authority Key Identifier (AKI) | keyid:... | keyid:DB:68:... | **Mandatory** |
| Subject Key Identifier (SKI) | keyid:... | keyid:0C:D1... | **Optional** |
| Authority Info Access (AIA) | CA Issuers URI, OCSP URI (optional) | CA Issuers: http://public.wisekey.com/ca.crt | **Mandatory** |
| CRL Distribution Points (CRL DP) | URI:... | http://public.wisekey.com/ca.crl | **Mandatory** |

### Sponsor-Validated Certificate Profile

| Attribute | Content | Example Value | Notes |
| --- | --- | --- | --- |
| Version | v3 | v3 | **Mandatory** |
| Serial Number | Unique value | 14:b4:... | **Mandatory** |
| Signature Algorithm | sha256/384WithRSAEncryption, ecdsa-with-SHA256/384 | sha256WithRSAEncryption | **Mandatory** |
| Issuer | Issuing CA Subject Name | C=CH, O=WISeKey, CN=WISeKey CertifyID Client RSA CA 1 | **Mandatory** |
| Validity Period | See the schedule above | Not Before: Oct 30 2025 16:10:52 GMT <br> Not After: Oct 30 2027 16:10:51 GMT | **Mandatory**; at most 825 days |
| Subject | C, ST, L, OU, O, organizationIdentifier, SN, GN, pseudonym, CN, emailAddress (or other combinations and fields allowed by the S/MIME Baseline Requirements) | C=CH, ST=Geneve, O=WISeKey SA, organizationIdentifier=NTRCH-CHE-101.022.134, SN=Smith, GN=John, CN=john.smith@example.com, emailAddress=john.smith@example.com | **Mandatory**; if the subject:commonName contains a Pseudonym, the subject:givenName and subject:surname attributes are not present, and the Pseudonym in the commonName matches the subject:pseudonym attribute when that attribute is present; if the subject:commonName contains a Personal Name, the subject:pseudonym attribute is not present (see [section 3.1.3](#313-anonymity-or-pseudonymity-of-subscribers)) |
| Public Key Algorithm / Size | RSA 2048/3072/4096, P-256/P-384 | RSA 2048 | **Mandatory** |
| Basic Constraints (critical) | CA:FALSE | CA:FALSE | **Optional** |
| Key Usage (critical) | As for the Mailbox-validated profile | Digital Signature | **Mandatory** |
| Extended Key Usage | As for the Mailbox-validated profile | E-mail Protection | **Mandatory** |
| Subject Alternative Name (SAN) | rfc822Name (at least one; mandatory from 2027-02-01) | email:john.smith@example.com | **Mandatory** |
| Certificate Policies | 2.23.140.1.5.3.2 (exactly one reserved CA/Browser Forum policy identifier); CPS URI and other OIDs as allowed by the S/MIME Baseline Requirements (optional) | 2.23.140.1.5.3.2 | **Mandatory** |
| Authority Key Identifier (AKI) | keyid:... | keyid:DB:68:... | **Mandatory** |
| Subject Key Identifier (SKI) | keyid:... | keyid:0C:D1... | **Optional** |
| Authority Info Access (AIA) | CA Issuers URI, OCSP URI (optional) | CA Issuers: http://public.wisekey.com/ca.crt | **Mandatory** |
| CRL Distribution Points (CRL DP) | URI:... | http://public.wisekey.com/ca.crl | **Mandatory** |

### Organization-Validated Certificate Profile

| Attribute | Content | Example Value | Notes |
| --- | --- | --- | --- |
| Version | v3 | v3 | **Mandatory** |
| Serial Number | Unique value | 14:b4:... | **Mandatory** |
| Signature Algorithm | sha256/384WithRSAEncryption, ecdsa-with-SHA256/384 | sha256WithRSAEncryption | **Mandatory** |
| Issuer | Issuing CA Subject Name | C=CH, O=WISeKey, CN=WISeKey CertifyID Client RSA CA 1 | **Mandatory** |
| Validity Period | See the schedule above | Not Before: Oct 30 2025 16:10:52 GMT <br> Not After: Oct 30 2027 16:10:51 GMT | **Mandatory**; at most 825 days |
| Subject | C, ST, L, OU, O, organizationIdentifier, CN, emailAddress (or other combinations and fields allowed by the S/MIME Baseline Requirements) | C=CH, ST=Geneve, O=WISeKey SA, organizationIdentifier=NTRCH-CHE-101.022.134, CN=WISeKey SA, emailAddress=info@example.com | **Mandatory** |
| Public Key Algorithm / Size | RSA 2048/3072/4096, P-256/P-384 | RSA 2048 | **Mandatory** |
| Basic Constraints (critical) | CA:FALSE | CA:FALSE | **Optional** |
| Key Usage (critical) | As for the Mailbox-validated profile | Digital Signature | **Mandatory** |
| Extended Key Usage | As for the Mailbox-validated profile | E-mail Protection | **Mandatory** |
| Subject Alternative Name (SAN) | rfc822Name (at least one; mandatory from 2027-02-01) | email:info@example.com | **Mandatory** |
| Certificate Policies | 2.23.140.1.5.2.2 (exactly one reserved CA/Browser Forum policy identifier); CPS URI and other OIDs as allowed by the S/MIME Baseline Requirements (optional) | 2.23.140.1.5.2.2 | **Mandatory** |
| Authority Key Identifier (AKI) | keyid:... | keyid:DB:68:... | **Mandatory** |
| Subject Key Identifier (SKI) | keyid:... | keyid:0C:D1... | **Optional** |
| Authority Info Access (AIA) | CA Issuers URI, OCSP URI (optional) | CA Issuers: http://public.wisekey.com/ca.crt | **Mandatory** |
| CRL Distribution Points (CRL DP) | URI:... | http://public.wisekey.com/ca.crl | **Mandatory** |

## Client Authentication and Document Signing Certificate Profiles

OWGTM issues Personal Certificates that do not include the `id-kp-emailProtection` EKU, typically intended for:

- **Client authentication**: certificates used mainly for TLS client authentication.
- **Document signing**: certificates used for the digital signature of documents (e.g., Adobe PDF documents).

These certificates use the profiles of the S/MIME Certificates above, without the `id-kp-emailProtection` EKU and without the reserved CA/Browser Forum S/MIME policy identifiers, and with the following differences:

| Attribute | Content |
| --- | --- |
| Extended Key Usage | Client authentication: TLS Web Client Authentication (and, when used, Microsoft Smart Card Logon). Document signing: Microsoft Document Signing (1.3.6.1.4.1.311.10.3.12) and/or the policy identifiers that identify AATL-qualifying certificates. `id-kp-serverAuth`, `id-kp-codeSigning`, `id-kp-timeStamping` and `anyExtendedKeyUsage` are never present. |
| Certificate Policies | The OWGTM policy identifier of the certificate type (Appendix C) and, for AATL-qualifying certificates, the AATL policy identifier. |
| Subject Alternative Name | Optional. When present, it only contains values validated as described in [section 3.2](#32-initial-identity-validation). |
| Issuing CAs | Only the Subordinate CAs whose EKUs allow these uses (see [section 1.4.1.1](#1411-trust-purposes-and-extended-key-usages)). |

These certificates are subject to the requirements of the Root under which they are issued. **TO BE CONFIRMED** (profile details of the client authentication and document signing certificates currently issued)

# Appendix E: Version history

## OWGTM S/MIME and Client Certificates CP/CPS (this document)

| **VERSION** | **DATE** | **MODIFICATION** | **AUTHOR** |
| --- | --- | --- | --- |
| 5.0 | 2026-12-15 **TO BE CONFIRMED** | Split of the OWGTM CP/CPS v4.2: this document governs the S/MIME, client authentication and document signing certificates, and the OWGTM TLS CP/CPS governs the TLS server certificates. New document OID 2.16.756.5.14.9.2. Alignment with S/MIME BR v1.0.16, NCSSR v2.0.5, Mozilla Root Store Policy v3.1, Apple Root Program Policy v2.0, Microsoft Trusted Root Program Requirements v1.2, CCADB Policy v2.1 and the Adobe AATL Technical Requirements v2.0. Code Signing and Device certificates removed from the scope. | Pedro Fuentes |

## Combined OWGTM CP/CPS (predecessor of this document)

| **VERSION** | **DATE** | **MODIFICATION** | **AUTHOR** |
| --- | --- | --- | --- |
| 4.0 | 9/12/2024 | First consolidated CP/CPS | Pedro Fuentes |
| 4.0.1 | 13/1/2025 | Minor changes | Pedro Fuentes |
| 4.0.2 | 21/3/2025 | Minor changes | Pedro Fuentes |
| 4.0.3 | 27/6/2025 | Minor changes | Pedro Fuentes |
| 4.0.4 | DRAFT | Statement for Mass Revocation | Pedro Fuentes |
| 4.1 | 26/11/2025 | Wording improvements to address root program feedback | Pedro Fuentes |
| 4.1.1 | 17/2/2026 | Inclusion of new profile to allow cross-signing of CAs | Pedro Fuentes |
| 4.1.2 | 19/2/2026 | Typo in effective date | Pedro Fuentes |
| 4.1.3 | 26/2/2026 | Updated CA Hierarchies | Pedro Fuentes |
| 4.1.4 | 31/3/2026 | Corrected typo about key generation | Pedro Fuentes |
| 4.2 | 31/8/2026 | Wording improvements and alignment with CABF Baseline Requirements | Pedro Fuentes |

## Previous versions

Before the combined CP/CPS, the OISTE/WISeKey Trust Model published separate CP documents for each type of certificate and separate CPS documents for OISTE (covering the Root CAs) and WISeKey (covering the Subordinate CAs). The previous documents and their version history are available at https://oiste.org/repository and https://wisekey.com/repository, respectively.

# Appendix F: Compliance cross-reference

This appendix maps the main requirements applicable to the CAs within the scope of this document to the sections of this CP/CPS where the corresponding practices are described. The numbering of section 3.2 of the S/MIME Baseline Requirements differs from the RFC 3647 outline followed by this document; the correspondence is shown below.

| Requirement | Source | Section of this CP/CPS |
| --- | --- | --- |
| Publication of the CP/CPS, RFC 3647 structure, conformance clause | S/MIME BR 2.2 | 1.1, 2.2.1 |
| Review at least every 365 days, version increment and dated changelog | S/MIME BR 2.3; Mozilla RSP 3.3 | 1.5.4, 2.3, Appendix E |
| Certificate Problem Report instructions | S/MIME BR 1.5.2, 4.9.3 | 1.5.2 |
| Disclosure of the use of Pseudonyms | S/MIME BR 3.1.3 | 3.1.3 |
| Validation of mailbox authorization or control | S/MIME BR 3.2.2; Mozilla RSP 2.2 | 3.2.2.2 |
| Authentication of organization identity | S/MIME BR 3.2.3 | 3.2.2.1 |
| Disclosure of verification sources | S/MIME BR 3.2.3.3 | 3.2 |
| Authentication of individual identity; attribute collection | S/MIME BR 3.2.4, 3.2.4.1 | 3.2.3 |
| Non-verified subscriber information | S/MIME BR 3.2.5 | 3.2.4 |
| Validation of authority | S/MIME BR 3.2.6 | 3.2.5 |
| Criteria for interoperation; disclosure of Cross-Certificates | S/MIME BR 3.2.7 | 3.2.6 |
| Reliability of verification sources | S/MIME BR 3.2.8 | 3.2 |
| Data reuse periods | S/MIME BR 4.2.1 | 4.2.1 |
| CAA processing and Issuer Domain Names | S/MIME BR 4.2.2.1 | 4.2.2.1 |
| DNSSEC validation | S/MIME BR 4.2.2.1.1 | 4.2.2.2 |
| Multi-Perspective Issuance Corroboration | S/MIME BR 4.2.2.2 | 3.2.2.3, 5.4.1 |
| Linting | S/MIME BR 4.3.1 | 4.3.1.1, 6.6.1, 8.7 |
| Revocation reasons and time frames | S/MIME BR 4.9.1 | 4.9.1 |
| Revocation request procedure, Certificate Problem Reports | S/MIME BR 4.9.3, 4.9.5 | 4.9.3, 4.9.5 |
| CRL and OCSP | S/MIME BR 4.9.7–4.9.10, 7.2, 7.3 | 4.9.7–4.9.10, 7.2, 7.3 |
| Methods to demonstrate Key Compromise | Mozilla RSP 6 | 4.9.12 |
| Key escrow | S/MIME BR 4.12 | 4.12 |
| Incident reporting | CCADB Incident Reporting Guidelines; Microsoft 2.1.18 | 5.7.1, 8.5 |
| Trusted roles, account review, MFA, access removal | NCSSR | 5.2, 6.5.1 |
| Logging, log processing and alerting | NCSSR; S/MIME BR 5.4 | 5.4.1–5.4.3 |
| Vulnerability management and remediation timeframes | NCSSR | 5.4.8, 6.7 |
| Air-Gapped Root CA systems, remote access | NCSSR | 6.5.1, 6.7 |
| Change management | NCSSR | 6.6.3 |
| Weak key rejection | S/MIME BR 6.1.1.3 | 6.1.1.3 |
| Private key delivery | S/MIME BR 6.1.2 | 6.1.2 |
| Key sizes (RSA 4096 for CA certificates, RSA 3072 issuing CAs), SHA-1 sunset | S/MIME BR 6.1.5, 7.1.3 | 6.1.5, 7.1.3 |
| Subscriber certificate validity | S/MIME BR 6.3.2 | 6.3.2, Appendix D |
| Certificate profiles, EKUs, policy identifiers | S/MIME BR 7.1; Apple policy 1.3.1, 1.7, 2.3; Mozilla RSP 7.5.2 | 1.4.1, 7.1, Appendix C, Appendix D |
| Cross-Certificate EKUs | S/MIME BR 7.1.2.2; CCADB Policy 6.3 | 7.1.2, Appendix D |
| Name forms (byte-for-byte encoding), pseudonym rules | S/MIME BR 7.1.4 | 7.1.4, Appendix D |
| Audits and self-audits | S/MIME BR 8; Mozilla RSP 3.1; Apple policy 1.1; Microsoft 4.2; AATL G2 | 8.1–8.7 |
| Review of delegated parties and Enterprise RAs | S/MIME BR 8.8 | 8.7 |
| Privacy Policy location | S/MIME BR 9.4.1 | 9.4.1 |
| Certificate warranties and Certificate Beneficiaries | S/MIME BR 9.6.1 | 9.6.1 |
| Subscriber obligations | S/MIME BR 9.6.3 | 9.6.3 |
| Indemnification of Application Software Suppliers | S/MIME BR 9.9 | 9.9 |
| Conflict with law | S/MIME BR 9.16.3 | 9.16.3 |
| Adherence to the Chrome and CCADB policies | Chrome policy 1.1.3; CCADB Policy 4 | 1.1 |
| Trust Purpose and EKUs in section 1.4 | Apple policy 1.3.1 | 1.4.1.1 |
| Mapping of practices to root and intermediate certificates | Mozilla RSP 3.3 | 1.1, Appendix B |
| AATL: RFC 3647 CPS, policy identifiers, notification of changes | AATL Technical Requirements G6, G9, ICA1 | 1.1, 7.1.6, Appendix C |
