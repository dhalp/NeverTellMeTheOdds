var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/mydb";

MongoClient.connect(url, function(err, db) {
        if (err) throw err;
        var dbo = db.db("mydb");
        var NLWest = [
                { name: "Rockies", Location: "Colorado"},
                { name: "Diamondbacks", Location: "Arizona"},
                { name: "Dodgers", Location: "Los Angeles"},
                { name: "Giants", Location: "San Francisco"},
                { name: "Padres", Location: "San Diego"}
        ];
        dbo.collection("BaseballTeams").insertMany(NLWest, function(err, res) {
                if (err) throw err;
                console.log(res);
                db.close();
        });
});
