# NM-RF-HAT: two different host connection arrangements

Contributor: JimGat (@jimgat).

## NM-CYD-C5 — direct FPC plus UART

Contributor: JimGat (@jimgat). Contributor-supplied assembly photograph and report: the two host-to-HAT connections shown are the direct expansion FPC and additional UART lead. No SD-slot adapter is required for this C5 arrangement. The external GPS receiver and its separate leads are optional expansion, not extra required host-to-HAT connections. This photograph does not establish connector contact order, FPC contact-side orientation, supply limits, or a continuity/functional test. Match the actual board revision.

The contributor supplied the photograph directly for inclusion. The published candidate is a privacy-cleaned derivative, not the private original. Only EXIF Artist @jimgat is retained; camera/GPS/time metadata is removed. A visible factory identifier/data-matrix strip is privacy-masked; connectors and cable routing are unchanged.

Candidate SHA-256: `6947148b05ed8a636acda0ee492c40bcd0502f4635c55b37677aa00b2f1c8106`.

Original photograph by JimGat (@jimgat); contributor authorized inclusion and metadata stripping/editing. No blanket Creative Commons or book-print permission is inferred; confirm intended licensing before public submission.

## Classic CYD — SD-slot adapter

CLASSIC CYD ONLY: manufacturer connection illustration shows ESP32-2432S028 / Classic CYD connected to NM-RF-HAT using the TF/microSD-slot SPI adapter plus separate signal/UART leads. This is NOT the NM-CYD-C5 connection arrangement. Do not copy this SD-slot adapter recipe onto the direct-FPC C5. The external GPS and battery paths drawn are accessory options, not blanket requirements. Original source labels are preserved, not independently transcribed or electrically certified.

Source: https://www.nmminer.com/wp-content/uploads/2026/02/connection-1024x712.png

Original SHA-256: `79cf43f8115e8639715bb3644f26b8c1fd2aac7bb0411883452f49758b78b367`. The transparent original PNG is retained byte-for-byte; convenience screen previews use a white background for legible source labels.

NMTech / NMminer manufacturer illustration; original downloaded bytes retained unchanged. Reuse, redistribution and print rights not established; public submission requires permissions review.

## Evidence limits

Assembly-photo evidence is not a new physical pin-number map or electrical acceptance test. Unknown PCB revisions, cable contact-side orientation, power routing/limits and untested interfaces remain unqualified. No firmware flashing or RF operation was performed.
