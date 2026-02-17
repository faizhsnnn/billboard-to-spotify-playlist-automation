# Billboard to Spotify Playlist Automation

## Overview

This project automates the creation of a Spotify playlist based on historical Billboard Hot 100 rankings.

Given a specific date, the script:

1. Scrapes Billboard’s Hot 100 chart.
2. Extracts song titles.
3. Authenticates with the Spotify Web API.
4. Searches for each track.
5. Creates a private Spotify playlist.
6. Populates it with the matched tracks.

Built as part of #90DaysOfCode, this project demonstrates multi-service integration, authentication handling, and structured automation workflows.

---

## Technologies Used

- Python
- requests
- BeautifulSoup (bs4)
- spotipy (Spotify API wrapper)
- OAuth 2.0 authentication

---

## Key Concepts Demonstrated

- Web scraping with custom headers
- HTML parsing and structured extraction
- OAuth-based authentication
- API search queries with filtering
- Playlist creation via REST API
- Error handling for missing results
- Automated multi-step workflow orchestration

---

## Installation

Install dependencies:

```
pip install requests beautifulsoup4 spotipy
```

---

# Spotify Setup

Create an app at ```https://developer.spotify.com/dashboard```

Add Redirect URI:
```http://127.0.0.1:8888/callback```

Set environment variables:
```
export SPOTIPY_CLIENT_ID="your_client_id"
export SPOTIPY_CLIENT_SECRET="your_client_secret"
```

(On Windows PowerShell)
```
setx SPOTIPY_CLIENT_ID "your_client_id"
setx SPOTIPY_CLIENT_SECRET "your_client_secret"
```

---
# Project Structure
```
billboard-to-spotify-playlist-automation/
│
├── main.py
│   └── Complete scraping + playlist automation logic
│
├── token.txt
│   └── Spotify OAuth cache (auto-generated)
│
└── README.md
```

---
# How It Works

User inputs a date in YYYY-MM-DD format.

Billboard Hot 100 page is scraped.

Song titles are extracted.

Spotify OAuth authentication is triggered.

Songs are searched and matched.

A private playlist is created.

Tracks are added automatically.

Why This Project Matters

This project demonstrates:

Real-world API integrations

Secure OAuth authentication flow

Service-to-service automation

Data transformation across platforms

Backend orchestration logic

It reflects practical backend automation beyond isolated scripts.

---

# Author

Faiz Hasan

Python Automation & Backend Developer
