const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/test', {useNewUrlParser: true, useUnifiedTopology: true});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  // we're connected!
  console.log("We are connected");
});

const potholeSchema = new mongoose.Schema({
    name: String,
    location:{
        l_lattiude: String,
        l_longitud: String
    },
    firstIncident: Date,
    lastIncident: Date,
    totalIncidents: Number
  });

  const adminSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String
  });


  const pothole = mongoose.model('ChaleBache', potholeSchema);
  const potholeAdmins = mongoose.model('ChaleBacheAdminds', adminSchema);

  const first = new pothole({ name:'Maria',
                            location:{l_lattiude:'av juarez', l_longitud:' 861'},
                            firstIncident:'2021-04-01', 
                            lastIncident:'2021-04-08',
                            totalIncidents:20 });

    const firstAdmin = new potholeAdmins({ name:'Javier',
                            email:'javier@gmail.com',
                            password:'123456' });


function registerPothole( nombre,  latitud, longitud, firstI, lastIn, totalInc){

    const first = new pothole({ name:nombre,
                            location:{l_lattiude:latitud, l_longitud:longitud},
                            firstIncident:firstI, 
                            lastIncident:lastIn,
                            totalIncidents:totalInc });
    first.save(function (err, first) {
        if (err) return console.error(err);
        });
}


function registerAdmin(nameA, emailA, passwordA){
    const firstAdmin = new potholeAdmins({ name:nameA,
                            email:emailA,
                            password:passwordA });
    firstAdmin.save(function (err, firstAdmin) {
        if (err) return console.error(err);
        });
}


registerPothole('Javi', 'av lopes','97897', '2021-04-01', '2021-04-02', 30);
registerAdmin('Guido','guido@gmail.com','123456');
registerAdmin('Javi','javi@gmail.com','1234567');


function checkDataAdmins(){
    potholeAdmins.find(function (err, admins) {
        if (err) return console.error(err);
      })
}

function checkDataPotholes(){
    pothole.find(function (err, poth) {
        if (err) return console.error(err);
        console.log(poth);
      })
}

checkDataAdmins();
checkDataPotholes();


// DELETE OF DATABASE
// pothole.deleteMany({}, function (err) {
//     if(err) console.log(err);
//     console.log("Successful deletion");
//   });

// potholeAdmins.deleteMany({}, function (err) {
//     if(err) console.log(err);
//     console.log("Successful deletion");
//   });