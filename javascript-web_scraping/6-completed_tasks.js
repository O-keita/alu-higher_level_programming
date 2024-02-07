#!/usr/bin/node

const request = require('request');

const computeCompletedTasks = (apiUrl) => {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`Error making request: ${error}`);
      process.exit(1);
    }

    if (response.statusCode !== 200) {
      console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
      process.exit(1);
    }

    try {
      const todos = JSON.parse(body);

      const userTasks = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          const userId = todo.userId;
          userTasks[userId] = (userTasks[userId] || 0) + 1;
        }
      });

      // Print users with completed tasks
      Object.entries(userTasks).forEach(([userId, completedTasks]) => {
        console.log(`{${userId}: ${completedTasks}}`);
      });
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError.message}`);
      process.exit(1);
    }
  });
};

if (require.main === module) {
  if (process.argv.length !== 3) {
    console.error('Usage: ./computeCompletedTasks.js <API_URL>');
    process.exit(1);
  }

  const apiUrl = process.argv[2];
  computeCompletedTasks(apiUrl);
}
