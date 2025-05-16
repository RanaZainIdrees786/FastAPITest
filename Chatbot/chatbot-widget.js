(function () {
  // === CONFIG ===
  const BACKEND_URL = "http://127.0.0.1:8000/chat";

  // === STYLES ===
  const style = document.createElement("style");
  style.innerHTML = `
      #chat-icon {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: #007bff;
        color: white;
        font-size: 30px;
        text-align: center;
        line-height: 60px;
        cursor: pointer;
        z-index: 9999;
      }
  
      #chat-window {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: white;
        z-index: 9998;
        display: none;
        flex-direction: column;
        font-family: sans-serif;
        background-color: #212121;
      }
  
      #chat-header {
        // background: #007bff;
        color: white;
        padding: 10px;
        font-size: 18px;
      }
  
      #chat-messages {
        flex: 1;
        padding: 10px;
        overflow-y: auto;
      }

    .chat-msg.user-msg{
        margin: 30px;
        }
        
    .chat-msg.user-msg, .chat-msg.bot-msg{
        text-align: left;
        background-color: #303030;
        color: white;
        padding: 10px;
        border-radius: 8px;
        }
        
    .chat-msg {
        margin: 5px 0;
    }

    .chat-msg.bot-msg{
        margin: 30px;
    }
  
      .user-msg {
        text-align: right;
        }
        
        .bot-msg {
            text-align: left;
            
            }
            
            #chat-input {
                display: flex;
                border-top: 1px solid #ccc;
                }
      #chat-input::placeholder{
        color: #303030;
      }
  
      #chat-input input {
        flex: 1;
        padding: 10px;
        border: none;
        font-size: 16px;
      }
  
      #chat-input button {
        padding: 10px;
        background: #007bff;


        color: white;
        border: none;
        cursor: pointer;
      }
    `;
  document.head.appendChild(style);

  // === ICON ===
  const icon = document.createElement("div");
  icon.id = "chat-icon";
  icon.innerHTML = "💬";
  document.body.appendChild(icon);

  // === CHAT WINDOW ===
  const chat = document.createElement("div");
  chat.id = "chat-window";
  chat.innerHTML = `
      <div id="chat-header">ChatBot <span style="float:right;cursor:pointer;" id="chat-close">✖</span></div>
      <div id="chat-messages"></div>
      <div id="chat-input">
        <input type="text" id="chat-text" placeholder="What you want to know about AKTI..." />
        <button id="chat-send">Send</button>
      </div>
    `;
  document.body.appendChild(chat);

  // === EVENTS ===
  icon.onclick = () => {
    chat.style.display = "flex";
    icon.style.display = "none";
  };

  document.getElementById("chat-close").onclick = () => {
    chat.style.display = "none";
    icon.style.display = "block";
  };

  document.getElementById("chat-send").onclick = async () => {
    const input = document.getElementById("chat-text");
    const message = input.value.trim();
    if (!message) return;
    appendMessage(message, "user-msg");
    input.value = "";

    //
    try {
      const res = await fetch(
        BACKEND_URL + `?q=${encodeURIComponent(message)}`,
        {
          method: "GET",
          headers: { "Content-Type": "application/json" },
        }
      );
      const data = await res.json();
      appendMessage(data.reply || "No reply", "bot-msg");
    } catch (err) {
      appendMessage("Error reaching server.", "bot-msg");
    }
  };

  function appendMessage(text, cls) {
    const box = document.getElementById("chat-messages");
    const msg = document.createElement("div");
    msg.className = `chat-msg ${cls}`;
    msg.innerText = text;
    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
  }
})();
