# Waveshare, M5Stack and NodeMCU review / 2026.10.3

**3 new records, 6 enriched records, 11 added references and 10 external terminal-purpose rows.** First Edition / 2026 is unchanged. This is a digital collection snapshot.

## Your ESP32-C5 boards

Both [ESP32-C5-Pico](https://valleytech-black-wire-guide.pages.dev/?board=waveshare-esp32-esp32-c5-pico) and [ESP32-C5-MINI-KIT](https://valleytech-black-wire-guide.pages.dev/?board=waveshare-esp32-esp32-c5-mini-kit) already had two physical pinout images. The current manufacturer pinout images were fetched again and match the saved SHA-256 hashes. Original board schematics are now saved too. Search includes the manufacturer's M, U and UM antenna/header variants and the common “ESP32-C5 Mini” name. Match the exact PCB and antenna/header variant before wiring.

All nine products in the current [Waveshare C5 documentation category](https://docs.waveshare.com/ESP32-C5) are tracked. This means catalog coverage, not nine independently approved complete physical pinouts.

## Added and expanded references

- **Waveshare ESP32-S3-LR1121-OLED-1.54:** new record with an original partial physical pinout of the two exposed headers and a three-page board schematic. HF/LF and EN/non-EN variants remain explicit. LR_IO7 and LR_IO8 are radio signals, not ESP32 GPIO7/GPIO8.
- **Waveshare ESP32-S3-RS485-WLED:** new record with a numbered hardware/terminal overview, manufacturer specifications and ten sourced external terminal-purpose rows. A complete physical pinout and saved board schematic remain missing. GPIO2′ and GPIO16′ output 5 V after level shifting; GPIO3/GPIO4 use 3.3 V logic. LED power output follows the external input voltage.
- **M5Stack Base PLC-M12 v1.1:** separate revision record, original four-page hardware guide and an uncropped render of its RS485/M5-Bus function page. This is an older revision identified during the review, not a new product launch.
- **M5Stack ToughC5 and Unit 8Servos2-I2C:** a labeled hardware overview and rear connector-label image respectively, alongside the existing schematics. The ToughC5 overview is not counted as a pinout. The servo-unit image covers only the connectors it labels and must not be used for the Chain variant.
- **NodeMCU DevKit 0.9 and 1.0:** original two-page instruction/pin-definition PDFs pinned to the official hardware repositories. These are ESP8266 boards. No new official NodeMCU hardware release was established by this pass.

The eleven attachments comprise **2 partial physical pinout images, 6 original PDFs, 2 supporting label images and 1 function sheet**. Original source bytes, hashes, model scope and rights notes are retained.

## Discovery scope and remaining gaps

The [Waveshare discovery inventory](../catalog/waveshare-discovery-2026.10.3.json) compares 156 top-level ESP32/RP2040/RP2350 documentation pages from a 1,829-URL sitemap. Seventeen unmatched pages were category/tutorial pages; the two remaining hardware records are added above. This migrated documentation tree is not proof of a complete manufacturer inventory.

The [M5Stack release history](https://docs.m5stack.com/en/history) was checked through its latest listed October 9 releases, including ToughC5, Chain Switch and Chain MIC, which were already tracked. Product-index comparison produced older revision/alias leads that still need individual review; these are recorded rather than silently treated as new models. TriviaPOD was excluded because its manufacturer comparison lists no expansion interface. Several M5Stack downloads timed out and are not counted as saved references.

An unrelated TTGO-TAudio schematic inside the Waveshare radio's bundled software dependencies was excluded. Generic product photos and packaging shots were also excluded. [Exact intake, rechecked hashes, exclusions and pending leads](../catalog/vendor-intake-2026.10.3.json).

No complete worldwide inventory or independent all-connector electrical approval is claimed. Manufacturer artwork retains its original rights; attribution does not establish permission to republish or print it. The existing rights and coverage audits remain authoritative.

## App and publication

App **0.16.0** uses this snapshot and adds a small, optional Patreon support card and footer link. It loads no Patreon widget or tracker. The browser deployment, desktop package validation, GitHub wiki and local copies are separate publication steps; see the app's release notes for their actual status and platform limits. The book draft is unchanged.
