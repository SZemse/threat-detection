# Threat Detection System

## Overview

This project demonstrates a simple **neurosymbolic cybersecurity pipeline** that analyzes network logs and detects attack patterns using **symbolic reasoning with PyReason**.

The system extracts security events from logs and applies reasoning rules to identify threats such as **privilege escalation, lateral movement, and brute-force attacks**.

## Pipeline

Network Logs → Event Extraction → PyReason-based Symbolic Reasoning → Threat Detection

## Components

* **network_logs.txt** – simulated network/security logs
* **event_extractor.py** – extracts structured events from logs
* **simple_reasoner.py** – rule-based threat detection using PyReason-inspired reasoning
* **pipeline.py** – runs the complete analysis pipeline

## Example Threat Rules

* `login_success + admin_access → privilege_escalation`
* `ssh_connection + multiple_hosts → lateral_movement`
* `failed_logins + port_scan → brute_force_attack`

## Running the Project

```
python src/pipeline.py
```

## Purpose

This prototype illustrates how **PyReason-style symbolic reasoning can be combined with log analysis to build interpretable cybersecurity threat detection systems.**
