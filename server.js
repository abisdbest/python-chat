const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// In-memory storage for chat messages
const chatMessages = [];

app.use(bodyParser.json());

// Serve HTML page for testing
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Endpoint to handle incoming chat messages
app.post('/chat', (req, res) => {
  const { name, message } = req.body;

  if (!name || !message) {
    return res.status(400).json({ error: 'Name and message are required.' });
  }

  const chatEntry = { name, message, timestamp: new Date() };
  chatMessages.push(chatEntry);

  res.status(201).json(chatEntry);
});

// Endpoint to retrieve all chat messages
app.get('/chat', (req, res) => {
  res.json(chatMessages);
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
