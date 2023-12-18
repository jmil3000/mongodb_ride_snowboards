// 1: Select all the boards that have a "Park" use
db.Snowboards.find({ "use": "Park" });
// 2: Select all the boards that have a “151” length
db.Snowboards.find({ "availableLengths": "151" });
// 3: Select all the board that have “Medium” response and a “Powder” use
db.Snowboards.find({ "response": "Medium", "use": "Powder" });
// 4: Select all the board that have a “Twin Extra” camber
db.Snowboards.find({ "camber": "Twin Extra" });
// 5: Select all the boards that have a “Park” and an “All Mountain” use, as well as a “151” length
db.Snowboards.find({
"use": { $all: ["Park", "All Mountain"] },
"availableLengths": "151"
});