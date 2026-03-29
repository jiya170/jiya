# Development Proposal: Daikibo Telemetry Dashboard

## 1. Overview
This project provides a secure, internal dashboard for Daikibo to monitor the health of 36 machines across 4 global factories. It is designed to run exclusively on the company intranet for maximum security.

## 2. Scope
* **Single Page Layout:** View all 4 factories and their 9 machines at once.
* **Interactive Views:** Sections can be expanded to see a history of machine statuses.
* **Internal Sync:** Works with existing company login accounts (SSO).
* **Intranet Only:** No data leaves the private company network.

## 3. Development Estimate
| Phase | Task | Hours |
| :--- | :--- | :--- |
| **Build** | Coding the Dashboard & Logic | 100 |
| **Sync** | Connecting to Login Servers | 45 |
| **Check** | Security & Bug Testing | 35 |
| **Total** | | **180 Hours** |

## 4. Timeline
* **Week 1:** Setup & Security Login integration.
* **Week 2-3:** Building the visual dashboard.
* **Week 4:** Connecting live machine data.
* **Week 5:** Final testing and launch.

## 5. Support
We provide ongoing support for bug fixes and can add more factory locations in the future as the company grows.
