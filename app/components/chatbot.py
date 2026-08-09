"""
===========================================================
Project     : NextHire AI
File        : chatbot.py
Author      : Santosh Kolagani

Purpose:
    True Floating, Resizable & Adjustable AI Chatbot Overlay Widget.
    Renders at the bottom-right corner of the browser viewport without pushing
    or modifying page layout. Pre-trained on all NextHire AI features.
===========================================================
"""

import streamlit as st
import streamlit.components.v1 as components
from app.config.settings import get_api_key


def render_floating_chatbot():
    """Renders 100% Floating, Resizable & Adjustable AI Chatbot Overlay Component."""
    api_key = get_api_key()

    # Self-Contained Floating HTML/CSS/JS Chatbot Widget (Position: Fixed Bottom-Right)
    chatbot_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        * {{
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }}
        body {{
            margin: 0;
            padding: 0;
            background: transparent;
            overflow: hidden;
        }}
        
        /* Floating Launcher Icon (Bottom-Right) */
        #nxt-bot-launcher {{
            position: fixed;
            bottom: 12px;
            right: 12px;
            background: linear-gradient(135deg, #2563EB 0%, #0284C7 100%);
            color: #FFFFFF;
            border: 2px solid #38BDF8;
            border-radius: 30px;
            padding: 12px 22px;
            font-weight: 700;
            font-size: 15px;
            cursor: pointer;
            box-shadow: 0 10px 25px rgba(2, 132, 199, 0.45);
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 999999;
        }}
        #nxt-bot-launcher:hover {{
            transform: translateY(-3px) scale(1.03);
            box-shadow: 0 15px 30px rgba(56, 189, 248, 0.6);
        }}
        .pulse-dot {{
            width: 9px;
            height: 9px;
            background-color: #22C55E;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 10px #22C55E;
        }}

        /* Floating Resizable Chat Window */
        #nxt-chat-modal {{
            display: none;
            position: fixed;
            bottom: 75px;
            right: 12px;
            width: 380px;
            height: 520px;
            min-width: 300px;
            min-height: 380px;
            max-width: 92vw;
            max-height: 85vh;
            resize: both;
            overflow: hidden;
            background: #0F172A;
            border: 2px solid #38BDF8;
            border-radius: 20px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.6);
            flex-direction: column;
            z-index: 999999;
            backdrop-filter: blur(12px);
        }}
        #nxt-chat-modal.open {{
            display: flex;
        }}

        /* Header Bar */
        .chat-header {{
            background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
            border-bottom: 1.5px solid #334155;
            padding: 14px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: move;
        }}
        .chat-title {{
            display: flex;
            align-items: center;
            gap: 10px;
            color: #F8FAFC;
            font-weight: 800;
            font-size: 15px;
        }}
        .chat-sub {{
            color: #38BDF8;
            font-size: 11px;
            font-weight: 600;
            display: block;
        }}
        .header-actions {{
            display: flex;
            gap: 8px;
        }}
        .btn-icon {{
            background: #1E293B;
            border: 1px solid #334155;
            color: #94A3B8;
            border-radius: 8px;
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 13px;
            transition: all 0.2s;
        }}
        .btn-icon:hover {{
            background: #EF4444;
            color: #FFFFFF;
            border-color: #EF4444;
        }}

        /* Chat Body & History */
        .chat-body {{
            flex: 1;
            padding: 16px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
            background: #090D16;
        }}
        .msg {{
            max-width: 85%;
            padding: 12px 16px;
            border-radius: 14px;
            font-size: 13.5px;
            line-height: 1.5;
            word-wrap: break-word;
        }}
        .msg-bot {{
            background: #1E293B;
            color: #F1F5F9;
            border: 1px solid #334155;
            align-self: flex-start;
            border-bottom-left-radius: 4px;
        }}
        .msg-user {{
            background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
            color: #FFFFFF;
            align-self: flex-end;
            border-bottom-right-radius: 4px;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }}

        /* Quick Suggestions */
        .suggestions {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            padding: 8px 14px;
            background: #0F172A;
            border-top: 1px solid #1E293B;
        }}
        .chip {{
            background: #1E293B;
            border: 1px solid #38BDF8;
            color: #38BDF8;
            padding: 5px 10px;
            border-radius: 12px;
            font-size: 11.5px;
            font-weight: 600;
            white-space: nowrap;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .chip:hover {{
            background: #38BDF8;
            color: #0F172A;
        }}

        /* Footer Input Form */
        .chat-footer {{
            padding: 12px 14px;
            background: #0F172A;
            border-top: 1px solid #1E293B;
            display: flex;
            gap: 8px;
        }}
        .chat-input {{
            flex: 1;
            background: #1E293B;
            border: 1.5px solid #334155;
            color: #F8FAFC;
            padding: 10px 14px;
            border-radius: 12px;
            font-size: 13px;
            outline: none;
        }}
        .chat-input:focus {{
            border-color: #38BDF8;
        }}
        .btn-send {{
            background: #2563EB;
            color: white;
            border: none;
            padding: 0 16px;
            border-radius: 12px;
            font-weight: 700;
            cursor: pointer;
            transition: background 0.2s;
        }}
        .btn-send:hover {{
            background: #1D4ED8;
        }}
    </style>
    </head>
    <body>

    <!-- Floating Trigger Launcher -->
    <div id="nxt-bot-launcher" onclick="toggleChat()">
        <span class="pulse-dot"></span>
        <span>🤖 NextHire AI Help</span>
    </div>

    <!-- Floating Resizable Chat Window -->
    <div id="nxt-chat-modal">
        <div class="chat-header">
            <div class="chat-title">
                <span style="font-size: 20px;">🤖</span>
                <div>
                    <div>NextHire AI Assistant</div>
                    <span class="chat-sub">Online • Fully Trained • Resizable Window</span>
                </div>
            </div>
            <div class="header-actions">
                <button class="btn-icon" onclick="toggleChat()" title="Close Window">✕</button>
            </div>
        </div>

        <div class="chat-body" id="chat-body">
            <div class="msg msg-bot">
                👋 <b>Greetings! I am NextHire AI Assistant.</b><br>
                Ask me anything about creating resumes, ATS scoring, our 50 templates, developer info, or platform features!
            </div>
        </div>

        <!-- Quick Question Chips -->
        <div class="suggestions">
            <div class="chip" onclick="quickAsk('Who developed NextHire AI?')">👨‍💻 Developer</div>
            <div class="chip" onclick="quickAsk('Tell me about the 50 templates')">🎨 50 Templates</div>
            <div class="chip" onclick="quickAsk('How does ATS scoring work?')">📊 ATS Score</div>
            <div class="chip" onclick="quickAsk('Is NextHire AI free?')">🔒 100% Free</div>
        </div>

        <div class="chat-footer">
            <input type="text" id="chat-input" class="chat-input" placeholder="Type your question here..." onkeypress="handleKey(event)">
            <button class="btn-send" onclick="sendMsg()">Send</button>
        </div>
    </div>

    <script>
        const API_KEY = "{api_key}";

        function toggleChat() {{
            const modal = document.getElementById("nxt-chat-modal");
            modal.classList.toggle("open");
            if (modal.classList.contains("open")) {{
                document.getElementById("chat-input").focus();
            }}
        }}

        function handleKey(e) {{
            if (e.key === "Enter") {{
                sendMsg();
            }}
        }}

        function quickAsk(text) {{
            document.getElementById("chat-input").value = text;
            sendMsg();
        }}

        function appendMessage(text, isUser) {{
            const body = document.getElementById("chat-body");
            const div = document.createElement("div");
            div.className = "msg " + (isUser ? "msg-user" : "msg-bot");
            div.innerHTML = text.replace(/\\n/g, "<br>").replace(/\\*\\*(.*?)\\*\\*/g, "<b>$1</b>");
            body.appendChild(div);
            body.scrollTop = body.scrollHeight;
        }}

        function getFallbackAnswer(q) {{
            q = q.toLowerCase();
            if (q.includes("who built") || q.includes("developer") || q.includes("author") || q.includes("santosh") || q.includes("creator")) {{
                return "🚀 <b>NextHire AI</b> was developed and engineered by <b>Santosh Kumar Kolagani</b>! It provides publication-ready 4K ATS vector PDF resumes and AI career strategy tools.";
            }}
            if (q.includes("free") || q.includes("cost") || q.includes("price") || q.includes("paid")) {{
                return "🎉 <b>NextHire AI is 100% FREE!</b> All 50 signature resume templates, ATS score checks, AI bullet polishing, and vector PDF exports are completely free without hidden fees.";
            }}
            if (q.includes("template") || q.includes("design") || q.includes("font") || q.includes("style")) {{
                return "🎨 <b>NextHire AI Features 50 Classified Signature Templates:</b><br>• ATS Friendly (20)<br>• Modern Professional (10)<br>• Tech & Developer (5)<br>• Creative & Design (5)<br>• Executive & Senior (5)<br>• Academic & Research (5)<br>Supports Helvetica, Times, Courier, Georgia, Trebuchet MS & Palatino fonts!";
            }}
            if (q.includes("ats") || q.includes("score") || q.includes("match") || q.includes("keyword")) {{
                return "📊 <b>ATS Score Dashboard Features:</b><br>• Calculates 0-100% match score against target job postings.<br>• Identifies missing critical technical & soft skills.<br>• Analyzes keyword density and formatting compliance.";
            }}
            if (q.includes("target") || q.includes("custom") || q.includes("company") || q.includes("google")) {{
                return "🎯 <b>Target Personalization Mode:</b><br>Allows you to tailor your resume for specific job titles (e.g. Senior Software Engineer) and companies (e.g. Google, Microsoft, Deloitte) with AI keyword extraction!";
            }}
            if (q.includes("download") || q.includes("pdf") || q.includes("export")) {{
                return "📥 <b>Exporting PDF Resumes:</b><br>Navigate to the 'Resume Final Preview' or 'Export PDF Resume' screen to download a 4K resolution vector PDF generated via ReportLab.";
            }}
            return "🤖 <b>NextHire AI Assistant Guide:</b><br>Thank you for asking! NextHire AI offers 50 classified resume templates, 1-click PDF vector downloads, AI bullet point polishing, and an ATS score engine. Explore the sidebar options or pick a template from the Template Gallery to begin!";
        }}

        async function sendMsg() {{
            const input = document.getElementById("chat-input");
            const text = input.value.trim();
            if (!text) return;

            appendMessage(text, true);
            input.value = "";

            if (API_KEY && API_KEY.length > 10) {{
                try {{
                    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${{API_KEY}}`;
                    const sysPrompt = "You are NextHire AI Assistant, developed by Santosh Kumar Kolagani. NextHire AI is a free, private AI career platform with 50 resume templates, ATS scoring, target company personalization, and 4K ReportLab vector PDF export. Be helpful, professional, and NEVER say 'I don't know'. Give detailed guidance on NextHire AI.";
                    
                    const res = await fetch(url, {{
                        method: "POST",
                        headers: {{ "Content-Type": "application/json" }},
                        body: JSON.stringify({{
                            contents: [{{
                                parts: [{{ text: sysPrompt + "\\n\\nUser question: " + text }}]
                            }}]
                        }})
                    }});

                    const data = await res.json();
                    if (data.candidates && data.candidates[0].content.parts[0].text) {{
                        const reply = data.candidates[0].content.parts[0].text;
                        appendMessage(reply, false);
                        return;
                    }}
                }} catch (e) {{
                    console.log("Gemini API error, using intelligent fallback", e);
                }}
            }}

            const reply = getFallbackAnswer(text);
            setTimeout(() => appendMessage(reply, false), 300);
        }}
    </script>
    </body>
    </html>
    """

    # Inject pure floating web component (Height 620px, viewport width 100%)
    components.html(chatbot_html, height=620, scrolling=False)
