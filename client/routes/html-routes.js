const mysql = require('mysql');

const connection = mysql.createConnection ({
  host: 'localhost',
  user: 'root',
  password: 'myjs123',
  database: 'reactdb'
});


module.exports = function(app) {
  app.get('/', function(req, res) {
    connection.connect(function(err) {
      if (err) throw err;
      connection.query("SELECT * FROM users", function (err, result) {
        (err)?res.send(err):res.json({users: result});
      });
    });
  });
};
