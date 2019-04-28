const express = require('express');

const PORT = process.env.PORT || 3001;

const app = express();

require('./routes/html-routes')(app);
app.listen(PORT, () => {
  console.log("App running on PORT " + PORT);

});
