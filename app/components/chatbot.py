"""
===========================================================
Project     : NextHire AI
File        : chatbot.py
Author      : Santosh Kolagani

Purpose:
    Parent-Injected 100% Floating, Draggable & Resizable AI Chatbot Overlay Widget.
    Attached directly to the top-level browser viewport body so users can
    use the website simultaneously while positioning and sizing the chatbot anywhere.
===========================================================
"""

import streamlit as st
import streamlit.components.v1 as components
from app.config.settings import get_api_key


def render_floating_chatbot():
    """Injects parent-body floating, draggable & resizable AI Chatbot overlay widget."""
    api_key = get_api_key()

    # JS/HTML injected directly into parent document body (0px Streamlit DOM space)
    chatbot_injector_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    </head>
    <body>
    <script>
    (function() {{
        try {{
            const pDoc = window.parent.document;

            // Remove existing container if re-rendering
            let oldHost = pDoc.getElementById("nxt-chatbot-overlay-root");
            if (oldHost) {{
                oldHost.remove();
            }}

            // Create detached top-level root container in parent document
            const root = pDoc.createElement("div");
            root.id = "nxt-chatbot-overlay-root";
            pDoc.body.appendChild(root);

            // Inject styles and markup into parent document body
            root.innerHTML = `
                <style>
                    #nxt-bot-fab {{
                        position: fixed;
                        bottom: 22px;
                        right: 22px;
                        background: linear-gradient(135deg, #2563EB 0%, #0284C7 100%);
                        color: #FFFFFF;
                        border: 2px solid #38BDF8;
                        border-radius: 30px;
                        padding: 12px 22px;
                        font-weight: 700;
                        font-size: 14px;
                        cursor: pointer;
                        box-shadow: 0 12px 30px rgba(2, 132, 199, 0.5);
                        display: flex;
                        align-items: center;
                        gap: 10px;
                        z-index: 999999999;
                        transition: transform 0.2s, box-shadow 0.2s;
                        font-family: system-ui, -apple-system, sans-serif;
                    }}
                    #nxt-bot-fab:hover {{
                        transform: translateY(-3px) scale(1.03);
                        box-shadow: 0 16px 36px rgba(56, 189, 248, 0.7);
                    }}
                    .nxt-dot {{
                        width: 9px;
                        height: 9px;
                        background: #22C55E;
                        border-radius: 50%;
                        display: inline-block;
                        box-shadow: 0 0 10px #22C55E;
                    }}

                    #nxt-chat-dialog {{
                        display: none;
                        position: fixed;
                        bottom: 80px;
                        right: 22px;
                        width: 390px;
                        height: 530px;
                        min-width: 320px;
                        min-height: 380px;
                        max-width: 92vw;
                        max-height: 85vh;
                        resize: both;
                        overflow: hidden;
                        background: #0F172A;
                        border: 2px solid #38BDF8;
                        border-radius: 20px;
                        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.75);
                        z-index: 999999999;
                        flex-direction: column;
                        font-family: system-ui, -apple-system, sans-serif;
                    }}
                    #nxt-chat-dialog.is-open {{
                        display: flex;
                    }}

                    .nxt-dialog-hdr {{
                        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
                        border-bottom: 1.5px solid #334155;
                        padding: 12px 16px;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        cursor: move;
                        user-select: none;
                    }}
                    .nxt-dialog-title {{
                        display: flex;
                        align-items: center;
                        gap: 10px;
                        color: #F8FAFC;
                        font-weight: 800;
                        font-size: 15px;
                    }}
                    .nxt-dialog-sub {{
                        color: #38BDF8;
                        font-size: 11px;
                        font-weight: 600;
                    }}
                    .nxt-hdr-btns {{
                        display: flex;
                        gap: 6px;
                    }}
                    .nxt-btn-close {{
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
                        font-size: 14px;
                    }}
                    .nxt-btn-close:hover {{
                        background: #EF4444;
                        color: white;
                    }}

                    .nxt-dialog-body {{
                        flex: 1;
                        padding: 14px;
                        overflow-y: auto;
                        display: flex;
                        flex-direction: column;
                        gap: 10px;
                        background: #090D16;
                    }}
                    .nxt-msg {{
                        max-width: 86%;
                        padding: 10px 14px;
                        border-radius: 14px;
                        font-size: 13px;
                        line-height: 1.5;
                        word-wrap: break-word;
                    }}
                    .nxt-msg-bot {{
                        background: #1E293B;
                        color: #F1F5F9;
                        border: 1px solid #334155;
                        align-self: flex-start;
                        border-bottom-left-radius: 3px;
                    }}
                    .nxt-msg-user {{
                        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
                        color: #FFFFFF;
                        align-self: flex-end;
                        border-bottom-right-radius: 3px;
                    }}

                    .nxt-chips-bar {{
                        display: flex;
                        gap: 6px;
                        overflow-x: auto;
                        padding: 8px 12px;
                        background: #0F172A;
                        border-top: 1px solid #1E293B;
                    }}
                    .nxt-chip {{
                        background: #1E293B;
                        border: 1px solid #38BDF8;
                        color: #38BDF8;
                        padding: 4px 10px;
                        border-radius: 12px;
                        font-size: 11px;
                        font-weight: 600;
                        white-space: nowrap;
                        cursor: pointer;
                    }}
                    .nxt-chip:hover {{
                        background: #38BDF8;
                        color: #0F172A;
                    }}

                    .nxt-dialog-ftr {{
                        padding: 10px 12px;
                        background: #0F172A;
                        border-top: 1px solid #1E293B;
                        display: flex;
                        gap: 8px;
                    }}
                    .nxt-in {{
                        flex: 1;
                        background: #1E293B;
                        border: 1.5px solid #334155;
                        color: #F8FAFC;
                        padding: 8px 12px;
                        border-radius: 10px;
                        font-size: 13px;
                        outline: none;
                    }}
                    .nxt-in:focus {{
                        border-color: #38BDF8;
                    }}
                    .nxt-send-btn {{
                        background: #2563EB;
                        color: white;
                        border: none;
                        padding: 0 14px;
                        border-radius: 10px;
                        font-weight: 700;
                        cursor: pointer;
                    }}
                </style>

                <!-- Floating Trigger Button -->
                <div id="nxt-bot-fab">
                    <span class="nxt-dot"></span>
                    <span>🤖 NextHire AI Assistant</span>
                </div>

                <!-- Floating Draggable & Resizable Dialog -->
                <div id="nxt-chat-dialog">
                    <div class="nxt-dialog-hdr" id="nxt-drag-hdr">
                        <div class="nxt-dialog-title">
                            <span style="font-size: 18px;">🤖</span>
                            <div>
                                <div>NextHire AI Assistant</div>
                                <span class="nxt-dialog-sub">✋ Drag Header to Move • Corner to Resize</span>
                            </div>
                        </div>
                        <div class="nxt-hdr-btns">
                            <button class="nxt-btn-close" id="nxt-close-btn">✕</button>
                        </div>
                    </div>

                    <div class="nxt-dialog-body" id="nxt-msg-body">
                        <div class="nxt-msg nxt-msg-bot">
                            👋 <b>Greetings! I am NextHire AI Assistant.</b><br>
                            I am here to guide you while you work! Ask me anything about building resumes, ATS scoring, 50 templates, or target company tailoring.
                        </div>
                    </div>

                    <div class="nxt-chips-bar">
                        <div class="nxt-chip" id="chip-1">👨‍💻 Developer</div>
                        <div class="nxt-chip" id="chip-2">🎨 50 Templates</div>
                        <div class="nxt-chip" id="chip-3">📊 ATS Score</div>
                        <div class="nxt-chip" id="chip-4">🔒 100% Free</div>
                    </div>

                    <div class="nxt-dialog-ftr">
                        <input type="text" id="nxt-input-text" class="nxt-in" placeholder="Ask a question about NextHire AI...">
                        <button id="nxt-send-trigger" class="nxt-send-btn">Send</button>
                    </div>
                </div>
            `;

            // Logic Wire Up inside Parent Document
            const fab = pDoc.getElementById("nxt-bot-fab");
            const dialog = pDoc.getElementById("nxt-chat-dialog");
            const closeBtn = pDoc.getElementById("nxt-close-btn");
            const inputTxt = pDoc.getElementById("nxt-input-text");
            const sendBtn = pDoc.getElementById("nxt-send-trigger");
            const msgBody = pDoc.getElementById("nxt-msg-body");
            const dragHdr = pDoc.getElementById("nxt-drag-hdr");

            fab.onclick = function() {{
                dialog.classList.toggle("is-open");
                if (dialog.classList.contains("is-open")) {{
                    inputTxt.focus();
                }}
            }};

            closeBtn.onclick = function() {{
                dialog.classList.remove("is-open");
            }};

            function appendMsg(text, isUser) {{
                const msg = pDoc.createElement("div");
                msg.className = "nxt-msg " + (isUser ? "nxt-msg-user" : "nxt-msg-bot");
                msg.innerHTML = text.replace(/\\n/g, "<br>").replace(/\\*\\*(.*?)\\*\\*/g, "<b>$1</b>");
                msgBody.appendChild(msg);
                msgBody.scrollTop = msgBody.scrollHeight;
            }}

            function getAnswer(q) {{
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
                return "🤖 <b>NextHire AI Assistant Guide:</b><br>Thank you for asking! NextHire AI offers 50 classified resume templates, 1-click PDF vector downloads, AI bullet point polishing, and an ATS score engine. Feel free to ask more questions while you build your resume!";
            }}

            async function handleSend() {{
                const val = inputTxt.value.trim();
                if (!val) return;
                appendMsg(val, true);
                inputTxt.value = "";

                const apiKey = "{api_key}";
                if (apiKey && apiKey.length > 10) {{
                    try {{
                        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${{apiKey}}`;
                        const sysPrompt = "You are NextHire AI Assistant, developed by Santosh Kumar Kolagani. NextHire AI is a free, private AI career platform with 50 templates, ATS scoring, target company personalization, and 4K vector PDF export. Be helpful and NEVER say 'I don't know'. Give concise guidance.";

                        const res = await fetch(url, {{
                            method: "POST",
                            headers: {{ "Content-Type": "application/json" }},
                            body: JSON.stringify({{ contents: [{{ parts: [{{ text: sysPrompt + "\\n\\nUser question: " + val }}] }}] }})
                        }});
                        const data = await res.json();
                        if (data.candidates && data.candidates[0].content.parts[0].text) {{
                            appendMsg(data.candidates[0].content.parts[0].text, false);
                            return;
                        }}
                    }} catch(e) {{
                        console.log("Gemini API fallback triggered", e);
                    }}
                }}

                setTimeout(function() {{
                    appendMsg(getAnswer(val), false);
                }}, 250);
            }}

            sendBtn.onclick = handleSend;
            inputTxt.onkeypress = function(e) {{
                if (e.key === "Enter") handleSend();
            }};

            pDoc.getElementById("chip-1").onclick = function() {{ inputTxt.value = "Who developed NextHire AI?"; handleSend(); }};
            pDoc.getElementById("chip-2").onclick = function() {{ inputTxt.value = "Tell me about the 50 templates"; handleSend(); }};
            pDoc.getElementById("chip-3").onclick = function() {{ inputTxt.value = "How does ATS scoring work?"; handleSend(); }};
            pDoc.getElementById("chip-4").onclick = function() {{ inputTxt.value = "Is NextHire AI free?"; handleSend(); }};

            // Draggable Header Handler
            (function makeDraggable() {{
                let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
                dragHdr.onmousedown = function(e) {{
                    e = e || window.event;
                    e.preventDefault();
                    pos3 = e.clientX;
                    pos4 = e.clientY;
                    pDoc.onmouseup = function() {{
                        pDoc.onmouseup = null;
                        pDoc.onmousemove = null;
                    }};
                    pDoc.onmousemove = function(e) {{
                        e = e || window.event;
                        e.preventDefault();
                        pos1 = pos3 - e.clientX;
                        pos2 = pos4 - e.clientY;
                        pos3 = e.clientX;
                        pos4 = e.clientY;
                        dialog.style.top = (dialog.offsetTop - pos2) + "px";
                        dialog.style.left = (dialog.offsetLeft - pos1) + "px";
                        dialog.style.bottom = "auto";
                        dialog.style.right = "auto";
                    }};
                }};
            }})();

        }} catch(err) {{
            console.log("Chatbot injector error:", err);
        }}
    }})();
    </script>
    </body>
    </html>
    """

    # Inject script with 0px Streamlit DOM space occupied
    components.html(chatbot_injector_html, height=0, width=0)
