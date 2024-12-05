<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temporary Chat Bot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
            margin: 0;
        }

        #chat-container {
            width: 100%;
            max-width: 400px;
            height: 600px;
            display: flex;
            justify-content: center;
            align-items: center;
            display: none; /* Hide chat initially */
        }

        #chat-box {
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            background-color: white;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            padding: 10px;
            border-radius: 10px;
        }

        #chat-log {
            flex: 1;
            overflow-y: auto;
            margin-bottom: 10px;
        }

        #user-input {
            width: 80%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        #send-btn {
            width: 15%;
            padding: 10px;
            border: none;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
            border-radius: 5px;
        }

        #send-btn:hover {
            background-color: #45a049;
        }

        .message {
            margin: 10px;
            padding: 10px;
            border-radius: 10px;
            max-width: 80%;
        }

        .user-message {
            background-color: #d4f1a7;
            align-self: flex-end;
        }

        .bot-message {
            background-color: #f1f1f1;
            align-self: flex-start;
        }

        #login-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        #login-container input {
            margin: 10px;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        #login-container button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        #login-container button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div id="login-container">
        <h2>Enter your ID to access the chat</h2>
        <input type="text" id="user-id" placeholder="Enter ID (user1 or admin)">
        <button id="login-btn">Login</button>
        <p id="error-message" style="color: red; display: none;">Invalid ID! Please enter 'user1' or 'admin'.</p>
    </div>

    <div id="chat-container">
        <div id="chat-box">
            <div id="chat-log">
                <!-- Messages will be appended here -->
            </div>
            <input type="text" id="user-input" placeholder="Type a message..." autofocus>
            <button id="send-btn">Send</button>
        </div>
    </div>

    <script>
        const validIds = ["user1", "admin"]; // The valid IDs
        let currentUser = "";

        document.getElementById('login-btn').addEventListener('click', function() {
            const enteredId = document.getElementById('user-id').value.trim();
            if (validIds.includes(enteredId)) {
                currentUser = enteredId;
                document.getElementById('login-container').style.display = 'none';
                document.getElementById('chat-container').style.display = 'flex';
            } else {
                document.getElementById('error-message').style.display = 'block';
            }
        });

        document.getElementById('send-btn').addEventListener('click', function() {
            const userInput = document.getElementById('user-input').value;
            
            if (userInput.trim() !== "") {
                addMessage(userInput, 'user');
                generateBotResponse(userInput);
                document.getElementById('user-input').value = ''; // Clear the input
            }
        });

        document.getElementById('user-input').addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                document.getElementById('send-btn').click();
            }
        });

        function addMessage(text, sender) {
            const chatLog = document.getElementById('chat-log');
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message');
            messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
            messageDiv.textContent = text;
            chatLog.appendChild(messageDiv);
            chatLog.scrollTop = chatLog.scrollHeight; // Scroll to the latest message
        }

        function generateBotResponse(userMessage) {
            let botResponse = "Sorry, I don't understand.";
            // Simple bot responses based on the user's message
            if (userMessage.toLowerCase().includes("hello")) {
                botResponse = "Hi! How can I help you?";
            } else if (userMessage.toLowerCase().includes("how are you")) {
                botResponse = "I'm just a bot, but I'm doing great!";
            } else if (userMessage.toLowerCase().includes("bye")) {
                botResponse = "Goodbye! Have a great day!";
            } else if (currentUser === "admin") {
                // Admin-specific response
                if (userMessage.toLowerCase().includes("admin")) {
                    botResponse = "Welcome, Admin! How can I assist you today?";
                }
            }
            
            setTimeout(() => {
                addMessage(botResponse, 'bot');
            }, 1000); // Simulate a delay for the bot's response
        }
    </script>
</body>
</html>
