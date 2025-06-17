const socket = new WebSocket("ws://localhost:8080/ws/stockstream");

    socket.onopen = () => {
      console.log("Connected to WebSocket server");
    };

    socket.onmessage = (event) => {
        console.log("📨 Message arrived!", event);
        try {
            const data = JSON.parse(event.data); // message expected as JSON
            console.log("Parsed Data:", data);
            
        } catch (e) {
            console.error("❌ JSON Parse error:", e, event.data);
        }
    };

    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    socket.onclose = (event) => {
      console.log("WebSocket connection closed:", event);
    };