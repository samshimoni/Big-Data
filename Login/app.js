    const express = require('express')
    const bodyParser = require('body-parser')

    const app = express()
    const port = 3001


    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({extended: true}));

    //when we press /localhost:3001
    app.get('/', function(req, res) {
        console.log(__dirname)
        res.sendFile(__dirname + '/public/index.html');
    });

    //we we want to get to loclhost:3001/Welcome
    app.get('/Welcome', function(req, res) {
        console.log(__dirname)
        res.sendFile(__dirname + '/public/Welcome.html');
    });

    //post request to transfer the user to the menu page(in future)
    app.post('/', function(req, res) {
        console.log('post /')
        res.sendFile(__dirname + '/Welcome.html');
    });


    //when we press 'upload-to-HDFS'
    app.post('/Welcome', function(req, res){
        console.log('posted /')
        writeToHadoop(JSON.stringify(req.body));
        res.sendFile(__dirname + '/Welcome.html');
    })

    app.listen(port, () => console.log(`Example app listening on port ${port}!`))
    //Imports all css files and design (backgrounds)
     app.use(express.static('public'))


   //function that writes files to hadoop
    function writeToHadoop(input){
        var json = JSON.parse(input);
        var path= json['myPath'];

        var name= extract_file_name(path);

        var WebHDFS = require('webhdfs');
        var fs = require('fs');
        var hdfs = WebHDFS.createClient({port: 50070});

        var localFileStream = fs.createReadStream(path);
        var remoteFileStream = hdfs.createWriteStream(name);
        localFileStream.pipe(remoteFileStream);
        console.log("opening stream to HDFS")
        remoteFileStream.on('error', function onError (err) {
            console.log("it failed");
            console.log(err);
        });

        remoteFileStream.on('finish', function onFinish () {
            console.log("it is done!");
        });
    }

    //extract file name from path
    function extract_file_name(path) {
        var first= path.lastIndexOf("/");
        var last= path.lastIndexOf(".");
        var name=path.substring(first, last);
        return name;
    }
